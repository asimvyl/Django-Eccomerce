from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm 
from .models import Vender

def join_vender(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            vender = Vender.objects.create(name=user.username, created_by=user)
            return redirect('front_page')
    else:
        form = CustomUserCreationForm()  
    return render(request, "join_vender.html", {"form": form})

@login_required
def vender_admin(request):
    # connected by model related name
    vender = request.user.vender
    
    return render(request,'vender_admin.html',{"vender":vender})