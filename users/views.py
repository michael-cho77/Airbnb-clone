from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms


# Based Class
class LoginView(View):

    def get(self, request):
        form = forms.LoginFrom()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginFrom(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


"""
Based function 
def login_view(request):
    if request.method == "GET"
        pass
    elif request.method == "POST    "
"""