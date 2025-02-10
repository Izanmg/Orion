from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm, LoginForm

# Create your views here.

def index(request):
    return render(request,'index.html')
@login_required
def home(request):
    return render(request,"home.html")

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username=username,password=password)
            login(request,user)
            return redirect("home")
        else:
            return render(request,"login.html",{"form":form})
    form = LoginForm()
    return render(request, "login.html",{"form": form})



def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)            
            login(request,user)
            return redirect("home")
        else:
            # Los errores se enviarán automáticamente a la plantilla
            return render(request, "register.html", {"form": form})

    form = UserForm()
    return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")

