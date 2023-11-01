from django.shortcuts import render

# Create your views here.


def front_page(request):
    return render(request,"front_page.html")



def contact(request):
    return render(request,"contact.html")
