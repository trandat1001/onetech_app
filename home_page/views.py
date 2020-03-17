from django.shortcuts import render, redirect
from home_page.models import Product, Category, Blog, Brand
from cart.forms import CartAddProductForm
from home_page.forms import ContactForm, RegisterForm, LoginForm
from random import randint
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
import django.contrib.auth as auth
from django.db.models import Q

# Create your views here.
def index(request):
    products = []
    weekDealProduct = Product.objects.filter(is_deal_week = 1)
    featureProduct = Product.objects.filter(is_feature = 1)
    saleProduct = Product.objects.filter(is_sale = 1)
    bestRateProduct = Product.objects.filter(is_best_rate = 1)
    categories = Category.objects.all()

    return render(request, "home_page/index.html", {
                                                        "products": products,
                                                        "weekDealProduct" : weekDealProduct,
                                                        "featureProduct": featureProduct,
                                                        "saleProduct": saleProduct,
                                                        "bestRateProduct": bestRateProduct,
                                                        "categories": categories
                                                    })

def contact(request):
    contactForm = ContactForm()
    registered = False

    if request.method == "POST":
        contactForm.setData(request.POST)

        if contactForm.is_valid():
            register = contactForm.save()
            register.save()
            registered = True
        else:
            print(contactForm.errors)

    return render(request, "home_page/contact.html", {"contactForm" : contactForm, 'registered': registered})

def productDetail(request, id):
    product = Product.objects.get(id = id)
    cartProductForm = CartAddProductForm()
    
    return render(request, "home_page/product_detail.html", {
                                                                "product": product,
                                                                "cartProductForm": cartProductForm
                                                            }
                  
                  )
    
def blog(request):
    blogs = Blog.objects.all().order_by('-create_date')
    
    return render(request, "home_page/blog.html", {"blogs": blogs})

def blogDetail(request, id):
    random3Blog = []
    blog = Blog.objects.get(id = id)
    allBlogs = Blog.objects.all().values()
    totalBlogItem = len(allBlogs)
    maxBlogIndex = totalBlogItem - 1
    # Get ramdom three blog from all available blogs
    random3Blog.append(allBlogs[randint(0, maxBlogIndex)])
    random3Blog.append(allBlogs[randint(0, maxBlogIndex)])
    random3Blog.append(allBlogs[randint(0, maxBlogIndex)])

    return render(request, "home_page/blog_detail.html",{"blog": blog, "random3Blog": random3Blog})

def shop(request, cat_id = 0, brand_id = 0):
    category = None
    brands = Brand.objects.all()
    search = request.GET.get('search')

    if (cat_id):
        category = Category.objects.get(id = cat_id)
    if (brand_id == 0 and cat_id != 0):
        products = Product.objects.filter(category = cat_id)
    elif (cat_id != 0 and brand_id != 0):
        products = Product.objects.filter(category = cat_id, band = brand_id)
    elif (search is not None):
        products = Product.objects.filter(name__contains = search)
    else:
        products = Product.objects.all()

    return render(request, "home_page/shop.html", {'products': products, 'cat': category, 'brands': brands, 'cat_id': cat_id, 'brand_id': brand_id})

def register(request):
    registerForm = RegisterForm()
    registered = False

    if request.method == "POST":
        registerForm.setData(request.POST)

        if registerForm.is_valid():
            try:
                validate_password(registerForm.data['password'])
            except exceptions.ValidationError as e:
                registerForm.add_error('password', list(e.messages))

                return render(request, "home_page/register.html", {"registerForm": registerForm})
            user = registerForm.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(registerForm.errors)

    return render(request, "home_page/register.html", {"registerForm": registerForm, 'registered': registered})

def login(request):
    loginForm = LoginForm()

    if request.method == "POST":
        loginForm.setData(request.POST)
        user = loginForm.authenticate()

        if user:
                auth.login(request, user)

                return redirect("/")

    return render(request, "home_page/login.html", {"loginForm": loginForm})

def logout(request):
    auth.logout(request)

    return redirect("/")