from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import RegisterForm, LoginForm
from log.models import ActivityLog



def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()

        ActivityLog.log(
            user=user,
            action=ActivityLog.ActionType.REGISTER,
            request=request
        )

        return redirect("login")

    return render(request, "register.html", {"form": form})



def login_view(request):
    form = LoginForm(request, data=request.POST or None)

    if form.is_valid():
        user = form.get_user()
        login(request, user)

        return redirect("home")

    return render(request, "login.html", {"form": form})



def logout_view(request):
    logout(request)
    return redirect("home")


def home_view(request):
    return render(request, 'home.html')