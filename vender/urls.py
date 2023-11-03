from django.urls import path

# to handle logout
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('join_vender/',views.join_vender,name="join_vender"),
    path('vender_admin/',views.vender_admin,name="vender_admin"),
    
    path('log_out/',auth_views.LogoutView.as_view(),name="log_out"),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name="login")
]
