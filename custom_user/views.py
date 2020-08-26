from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from custom_user.models import MyUser
from custom_user.forms import CustomUserForm, LoginForm
from custom.settings import AUTH_USER_MODEL


def index(request):
    data = MyUser.objects.all()
    return render(request, "index.html", {'data': data, "output": AUTH_USER_MODEL})

def signup_view(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(username=data.get("username"), password=data.get("password"), age=data.get("age"), display_name=data.get("display_name"), homepage=data.get("homepage"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))
        
    form = CustomUserForm()
    return render(request, "generic_form.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))




