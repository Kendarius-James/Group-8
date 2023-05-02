from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)
@register.filter(name='product_images')
def product_images(product):
    return [img for img in (product.image, product.image2, product.image3, product.image4) if img]