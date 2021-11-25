from django.db.models import fields
from django.forms import ModelForm
from accounts import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrderForm(ModelForm):
    class Meta:
        model = models.Order
        fields = "__all__"
        
class CustomerForm(ModelForm):
    class Meta:
        model = models.Customer
        fields = "__all__"
        exclude = ["user"]
            
class CreateUser(UserCreationForm):
    
    class Meta():
        model = User
        fields = ["username","email","password1","password2"]
    