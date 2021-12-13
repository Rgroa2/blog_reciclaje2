from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.views.generic import CreateView, TemplateView, LoginView, LogoutView

from .models import Profile

from .forms import SignUpForm

# Create your views here.

class Login(LoginView):
    template_name = 'profiles/login.html'

class SignUpView(CreateView):
    model = Profile
    form_class = SignUpForm
    
    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')
    
class Logout(LoginView):
    pass
    
class WelcomeView(TemplateView):
    template_name = 'profiles/welcome.html'
        