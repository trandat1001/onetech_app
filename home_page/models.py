from django.db import models
from email.policy import default
import datetime
from sympy.logic.boolalg import false

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 128, blank = False)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length = 128, blank = False)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    band = models.ForeignKey(Brand, on_delete=models.PROTECT)
    name = models.CharField(max_length = 128, blank = False)
    made_in = models.CharField(max_length = 64)
    description = models.TextField()
    price = models.FloatField()
    release_date = models.DateField()
    image = models.ImageField(upload_to = "images/", default = "")
    is_sale = models.BooleanField(default = False)
    is_feature = models.BooleanField(default = False)
    is_best_rate = models.BooleanField(default = False)
    is_deal_week = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length = 128, blank = False)
    content = models.TextField(blank = False)
    represent_image =  models.ImageField(upload_to = "images/", default = "")
    create_date = models.DateField(default = datetime.datetime.now())
    
    def __str__(self):
        return self.title
    
    
class Contact(models.Model):
    name = models.CharField(max_length = 64, blank = False)
    email = models.EmailField(max_length = 64, blank = False)
    phone_number = models.CharField(max_length = 32, blank = False)
    message = models.TextField(blank = False)
    create_date = models.DateField(default = datetime.datetime.now())

    def __str__(self):
        return self.name
    

        
