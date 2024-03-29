import random # To get random products from the database
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Product
from django.db.models import Q
from django.http import JsonResponse
from .forms import AddToCartForm
from accounts.models import CustomUser
from cart.cart import Cart
from django.http import HttpResponse
from .models import ProductReport, Rating
from .forms import ProductReportForm, RatingForm
#edit quantity feature
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from order.models import OrderItem
import json

# Create your views here.
def product(request, category_slug, product_slug):
    # Create instance of Cart class
    cart = Cart(request)

    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    # Check whether the AddToCart button is clicked or not
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            success = cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

            if success:
                messages.success(request, "Successfully added to cart.")
            else:
                messages.error(request, "Failed to add to cart. Item is not available.")
            

            return redirect('product:product', category_slug=category_slug, product_slug=product_slug)            
    
    else:
        form = AddToCartForm()

    similar_products = list(product.category.products.exclude(id=product.id))

    # If more than 4 similar products, then get 4 random products 
    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)
    report_form = ProductReportForm()
    rating_form = RatingForm()

    if request.user.is_authenticated:
        purchased = OrderItem.objects.filter(product=product, user=request.user).exists()
        rated = Rating.objects.filter(product = product, user = request.user).exists()
    else:
        purchased = False
        rated = False
    context = {
        'rated': rated,
        'CustomUser': CustomUser,
        'OrderItem': OrderItem,
        'purchased': purchased,
        'rating_form':rating_form,
        'product': product,
        'similar_products': similar_products,
        'form': form,
        'report_form': report_form,
    }

    return render(request, 'product/product.html', context)

#compare listings
def compare(request, product_id):
    product1 = get_object_or_404(Product, pk=product_id)
    product2_id = request.GET.get('product2')
    product2 = get_object_or_404(Product, pk=product2_id)
    context = {
        'product1': product1,
        'product2': product2,
    }
    return render(request, 'product/compare.html', context)

#remove compare listing item
def remove_compare(request, product_id):
    if 'product_to_compare' in request.session and int(request.session['product_to_compare']) == product_id:
        del request.session['product_to_compare']
    return redirect('product:compare', product_id=product_id)

#clear comparison
def clear_comparison(request):
    if 'product_to_compare' in request.session:
        del request.session['product_to_compare']
    return JsonResponse({'status': 'success'})

def get_product_name(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return HttpResponse(product.title)

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request,'product/category.html', {'category': category})


def search(request):
    query = request.GET.get('query', '') # second is default parameter which is empty
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'product/search.html', {'products':products, 'query': query})

def report_product(request, product_id):
    if request.method == 'POST':
        report_form = ProductReportForm(request.POST)
        if report_form.is_valid():
            report = report_form.save(commit=False)
            report.product = Product.objects.get(pk=product_id)
            report.listing_id = product_id  # Set the listing_id field value
            if request.user.is_authenticated:  # Check if the user is authenticated
                report.user = request.user
            report.save()
            product_instance = get_object_or_404(Product, pk=product_id)
            category_slug = product_instance.category.slug
            product_slug = product_instance.slug
            return redirect('product:product', category_slug=category_slug, product_slug=product_slug)
    else:
        report_form = ProductReportForm()
    return render(request, 'product/report_product.html', {'report_form': report_form, 'product_id': product_id}, content_type='text/html')
    
@login_required
def update_product(request, product_id):
    if request.method == "POST":
        data = json.loads(request.body)
        product = get_object_or_404(Product, id=product_id, seller=request.user.sellerprofile)
        product.price = data['price']
        product.quantity = data['quantity']
        product.description = data['description']
        try:
            product.save()
        except Exception as e:
            print(f"Error saving product: {e}")
            return JsonResponse({'status': 'error', 'message': 'Error saving product'})

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, seller=request.user.sellerprofile)
    
    try:
        product.delete()
    except Exception as e:
        print(f"Error deleting product: {e}")
        return JsonResponse({'status': 'error', 'message': 'Error deleting product'})

    return JsonResponse({'status': 'success'})
#
# def update_product(request, product_id):
#     if request.method == 'POST' and request.user.is_authenticated:
#         data = json.loads(request.body)
#         quantity = data.get('quantity')
#         price = data.get('price')

#         try:
#             product = Product.objects.get(id=product_id, seller=request.user)
#             product.quantity = quantity
#             product.price = price
#             product.save()

#             return JsonResponse({'status': 'success'})
#         except Product.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'Product not found'}, status=404)
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
@login_required
def submit_rating(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if the user has purchased the product
    if not OrderItem.objects.filter(product=product, user=request.user).exists():
        return JsonResponse({'status': 'error', 'message': "You can't rate a product you haven't purchased."})

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.product = product
            rating.save()
            return JsonResponse({'status': 'success', 'message': 'Rating submitted successfully.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form data.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})