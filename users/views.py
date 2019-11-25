from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms


# Based Class
class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        # return 값은 suuccess_url 로 가기때문에 redirect가 필요하지 않음     
        return super().form_valid(form) 


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