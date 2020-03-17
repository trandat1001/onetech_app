from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from home_page.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.http import JsonResponse
from sympy.logic.boolalg import false


@require_POST
def cart_add(request, product_id):
	
	cart = Cart(request)  # create a new cart object passing it the request object 
	product = get_object_or_404(Product, id=product_id) 
	result = {
		"success": True,
		"total_item": 0,
		'total_item': 0,
		'error': ""
	}
	if 'price' not in request.POST:
		price=0
	else:
		price=request.POST['price']
	print("------------------------------",product.price)
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(product=product, price=product.price, quantity=int(cd['quantity']), update_quantity=cd['update'])
		result['total_item'] = len(cart)
		result['total_price'] = cart.get_total_price()
	else:
		result['error'] = form.errors()
		result['success'] = False
		
	return JsonResponse(result)


def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	return redirect('cart:cart_detail')


def cart_detail(request):
	print('------------------------------------')
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
		print(item['update_quantity_form'])
	return render(request, 'cart/detail.html', {'cart': cart})

def index(request):
	
	return render(request, "cart/index.html")
