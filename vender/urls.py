from django.urls import path

from . import views

urlpatterns = [
    path('join_vender/',views.join_vender,name="join_vender"),
]
