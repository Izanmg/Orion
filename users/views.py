from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import UserForm, LoginForm, UpdateForm, UpdatePassword

# Create your views here.

def index(request):
    return render(request,'index.html')


@login_required
def home(request):
    if request.method == "POST":
        print("=====")
        print(request.POST)
        print("UserID: ",request.user.id)
        
        if "old_password" in request.POST and "new_password1" in request.POST and "new_password2" in request.POST:

            form_password = UpdatePassword(user=request.user,data=request.POST)
        else:
            form_data = UpdateForm(request.POST, user=request.user)
        try:
            if form_data.is_valid():
                print("form_data.is_valid")
                if form_data.cleaned_data.get('username'):
                    user = request.user
                    user.username = form_data.cleaned_data.get('username')
                    user.save()
                elif form_data.cleaned_data.get('first_name'):
                    print("Modificando nombre")
                    user = request.user
                    user.first_name = form_data.cleaned_data.get('first_name')
                    user.save()
                elif form_data.cleaned_data.get('last_name'):
                    print("Modificando apellido")
                    user = request.user
                    user.last_name = form_data.cleaned_data.get('last_name')
                    user.save()
                elif form_data.cleaned_data.get('email'):
                    print("Modificando email")
                    user = request.user
                    user.email = form_data.cleaned_data.get('email')
                    user.save()
            else:
                print("Hay problemitas")
                print(form_data.errors)
                return render(request, "home.html",{"form":form_data})
            return redirect("home")
        except:    
            if form_password.is_valid():
                user = request.user
                user.set_password(form_password.cleaned_data.get("new_password2"))
                user.save()
                update_session_auth_hash(request,user)
            else:
                print("El formulario es invalido.")
                print(form_password.errors)
                return render(request, "home.html",{"form":form_password})

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

