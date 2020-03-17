"""one_tech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from home_page import views

app_name = 'home-page'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('product-detail/<int:id>/',views.productDetail, name='product_detail'),
    path('blog', views.blog, name="blog"),
    path('blog-detail/<int:id>/', views.blogDetail, name="blog_detail"),
    path('shop/<int:cat_id>/<int:brand_id>/', views.shop, name="shop"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout")
]
