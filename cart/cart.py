from django.conf import settings

from product.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        for item in self.cart.values():
            item['total_price'] = item['product'].price * item['quantity']

            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)
        product = Product.objects.get(pk=product_id)

        # Check if the product is available
        if product.quantity <= 0:
            return False

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'id': product_id}

        if update_quantity:
            new_quantity = self.cart[product_id]['quantity'] + int(quantity)
            if new_quantity <= product.quantity:
                self.cart[product_id]['quantity'] = new_quantity
            else:
                self.cart[product_id]['quantity'] = product.quantity

        self.save()
        return True

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        return sum(item['quantity'] * item['product'].price for item in self.cart.values())

        
