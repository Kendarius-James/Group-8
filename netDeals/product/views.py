import random # To get random products from the database
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Product
from django.db.models import Q
from django.http import JsonResponse
from .forms import AddToCartForm
from cart.cart import Cart
from django.http import HttpResponse
from .models import ProductReport
from .forms import ProductReportForm

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
            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

            messages.success(request, "The product was added to the cart.")

            return redirect('product:product', category_slug=category_slug, product_slug=product_slug)            
    
    else:
        form = AddToCartForm()

    similar_products = list(product.category.products.exclude(id=product.id))

    # If more than 4 similar products, then get 4 random products 
    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)
    report_form = ProductReportForm()
    context = {
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
    
    