from django.http import HttpResponse
from django.shortcuts import redirect,render


# def admin_only(orig_func):
#     def wrapper_func(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name
#             print(group)
#         if group == "customers":
#             return redirect('accounts:user_page')
        
#         elif group == 'admin':
#             print("admin")
#             return orig_func(request, *args, **kwargs)
#     return wrapper_func