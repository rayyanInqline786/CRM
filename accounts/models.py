from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=255, null=True)
    phone=models.CharField(max_length=255, null=True)
    email=models.EmailField(max_length=255, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(upload_to="profile_pic",default="banner1.png",null=True,blank=True)
    
    def __str__(self):
        return self.email
    
    
class Tag(models.Model):
    tag_name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.tag_name

class Product(models.Model):
    CATEGORY = (
        ("Indoor","Indoor"),
        ("Outdoor","Outdoor")
    )
    tags = models.ManyToManyField(Tag, null=False)
    name=models.CharField(max_length=255, null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200, null=True, choices=CATEGORY)
    description=models.CharField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ("Pending","Pending"),
        ("Out for delievery","Out for delievery"),
        ("Delieverd","Delievered")
    )
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    def __str__(self):
        return self.products.name