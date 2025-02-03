from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def login_register(request):
    form_type = request.GET.get("form", "login")  # "login" por defecto
    return render(request, "log-regist.html", {"form_type": form_type})
