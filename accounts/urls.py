from django.conf.urls import url
from accounts import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.utils.decorators import method_decorator

app_name = "accounts"

urlpatterns = [
    url(r"^$",views.Dashboard.as_view(), name="dashboard"),
    url(r"^products/$",views.Products.as_view(), name="products"),
    path("customers/<str:id>/",views.Customers, name="customer"),
    url(r"^product_list/$", views.product_list, name="product_list"),
    url(r"^dashboard_list/$", views.dashboard_list, name="dashboard_list"),
    url(r"^order_list/$", views.orders_list, name="order_list"),
    url(r"^create_order/$", views.CreateOrder.as_view(), name="create_order"),
    url(r"^create_customers/$", views.CreateCustomers.as_view(), name="create_customers"),
    url(r"^register/$", views.CreateUser.as_view(), name="create_user"),
    url(r"^accounts/login/$", auth_views.LoginView.as_view(template_name="login.html",redirect_authenticated_user=True), name="login"),
    url(r"^logout/$", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    url(r"^update_orders/(?P<pk>\d+)/$",views.UpdateOrder.as_view(), name="update_orders"),
    url(r"^update_customers/(?P<pk>\d+)/$",views.UpdateCustomers.as_view(), name="update_customers"),
    url(r"^delete_orders/(?P<pk>\d+)/$",views.DeleteOrder.as_view(), name="delete_orders"),
    url(r"^delete_customer/(?P<pk>\d+)/$",views.DeleteCustomer.as_view(), name="delete_customer"),
    url(r"^user/$",views.UserView.as_view(), name="user_page"),
    url(r"^profile/$",views.UserProfile.as_view(), name="user_profile"),
]