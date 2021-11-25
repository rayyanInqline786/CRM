from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.base import View
import json
from django.urls import reverse_lazy
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
# from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from accounts.models import Product,Customer,Order,Tag
from django.http import JsonResponse, HttpResponse, request
from . import forms
from itertools import chain
from accounts import forms
# from .decorators import admin_only
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator

# Create your views here.
    
# @method_decorator(admin_only,name="dispatch")
class Dashboard(LoginRequiredMixin,ListView):
    template_name = "dashboard.html"
    model = Order
    order = Order.objects.all()
    customer = Customer.objects.all()
    total_orders = order.count()
    order_delievered = order.filter(status="Delievered").count()
    order_pending = order.filter(status="Pending").count()
    redirect_field_name = None
    
    def get_queryset(self):
        query1 = Order.objects.all()
        query2 = Customer.objects.all()
        query_dict = {
            "orders":query1,
            "customers":query2
        }
        return query_dict
    def get_context_data(self, **kwargs):
        print("***********")
        print(self.get_queryset()['orders'])
        context = super().get_context_data(**kwargs)
        context["orders"]=self.get_queryset()['orders']
        context["customers"] = self.get_queryset()['customers']
        context["total_orders"]=self.get_queryset()['orders'].count()
        context["delivered"]=self.get_queryset()['orders'].filter(status="Delievered").count()
        context["pending"]=self.get_queryset()['orders'].filter(status="Pending").count()
        print(context)
        return context

class Products(LoginRequiredMixin,ListView):
    template_name="products.html"
    model = Product
    context_object_name = "products"
   
   
class UserView(LoginRequiredMixin,ListView):
    template_name="user.html"
    def get_queryset(self):
        user = self.request.user
        orders = user.customer.order_set.all()
        print(orders)
        return orders
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = self.get_queryset()
        context["total_orders"]=self.get_queryset().count()
        context["delivered"]=self.get_queryset().filter(status="Delievered").count()
        context["pending"]=self.get_queryset().filter(status="Pending").count()
        print(context)
        return context
    
class UserProfile(LoginRequiredMixin, View):
    model = Customer
    
    def get(self, request, *args, **kwargs):
        print(self.request.user.customer)
        profile_form = forms.CustomerForm(instance=self.request.user.customer)
        if self.request.user.DoesNotExist:
            profile_form = forms.CustomerForm()
        return render(self.request, 'user_profile.html', context = {"form":profile_form})
    
    def post(self, request, *args, **kwargs):
        form = forms.CustomerForm(self.request.POST, self.request.FILES, instance=self.request.user.customer)
        if form.is_valid():
            form.save()
            return redirect('accounts:user_profile')

@login_required
def Customers(request, id):
    customer = Customer.objects.get(id=id)
    order = customer.order_set.all()
    orders_count = order.count()
    context = {
        "customer":customer,
        "order":order,
        "order_count":orders_count
    }      
    return render(request,"customers.html", context)
        
        
class CreateOrder(LoginRequiredMixin,CreateView):
    template_name="order_form.html"
    model = Order
    form_class = forms.OrderForm
    success_url = reverse_lazy('accounts:dashboard')
    
    
class UpdateOrder(LoginRequiredMixin,UpdateView):
    template_name="order_form.html"
    model = Order
    form_class=forms.OrderForm
    success_url = reverse_lazy('accounts:dashboard')
    
class CreateCustomers(LoginRequiredMixin,CreateView):
    template_name="customer_form.html"
    model = Customer
    form_class = forms.CustomerForm
    success_url = reverse_lazy('accounts:dashboard')
    
    
class UpdateCustomers(LoginRequiredMixin,UpdateView):
    template_name="customer_form.html"
    model = Customer
    form_class = forms.CustomerForm
    success_url = reverse_lazy('accounts:dashboard')
    
class DeleteOrder(LoginRequiredMixin,DeleteView):
    model = Order
    success_url = reverse_lazy('accounts:dashboard')
    def get(self, *args, **kwargs):
        return self.post(request,*args, **kwargs)
    
class DeleteCustomer(LoginRequiredMixin,DeleteView):
    model = Customer
    success_url = reverse_lazy('accounts:dashboard')
    def get(self, *args, **kwargs):
        return self.post(request,*args, **kwargs)
    
class CreateUser(SuccessMessageMixin,CreateView):
    form_class=forms.CreateUser
    model = User
    template_name="register.html"
    # success_url = reverse_lazy('accounts:login')
    def get_success_url(self):
        g = Group.objects.get(name='customers') # assuming you have a group 'test' created already. check the auth_user_group table in your DB
        g.user_set.add(self.object)
        return reverse_lazy('accounts:login')
    def post(self, request, *args, **kwargs):
        Customer.objects.create(
            user = self.request.user,
            name = self.request.user.username
        )

@login_required
def product_list(request):
    '''
    return product list in json format
    '''
    # Grabs a QuerySet of dicts
    qs = Product.objects.all().values()

    # Convert the QuerySet to a List
    list_of_dicts = list(qs)
    
    # Convert List of Dicts to JSON
    data = json.dumps({"data":list_of_dicts}, default=str)
    return HttpResponse(data, content_type="application/json")

@login_required
def dashboard_list(request):
    order = Order.objects.values()
    customer = Customer.objects.values()
    total_orders = order.count()
    order_delievered = order.filter(status="Delievered").count()
    order_pending = order.filter(status="Pending").count()

    dashboard_items = {
        "order":order,
        "customer":customer,
        "total_orders":total_orders,
        "order_delievered":order_delievered,
        "order_pending":order_pending
    }

    data= list(order)
    return JsonResponse(data, safe=False)
   
def orders_list(request):
    '''
    return orders list in json format
    '''
    # Grabs a QuerySet of dicts
    qs = Order.objects.all().values()

    # Convert the QuerySet to a List
    list_of_dicts = list(qs)
    
    # Convert List of Dicts to JSON
    data = json.dumps({"data":list_of_dicts}, default=str)
    return HttpResponse(data, content_type="application/json")
