from home_page.models import Category
from cart.cart import Cart


def category(request):
    category = list(Category.objects.all())

    return {'category': category}


def cart(request):
    cart = Cart(request)

    return {'cart': cart}
