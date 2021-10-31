from django.shortcuts import render, redirect
from django.views import View
from account.forms import UserAuthForm, RegistrationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as django_logout
from account.services.account import get_user
from product.models import Basket
from account.models import User,UserProfile

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm
        return render(request, 'account/registration.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)

        email = form.data['email'].lower()
        password = form.data['password']
        password2 = form.data['password2']
        user = User.objects.filter(username=email)
        if user:
            error = "Пользователь существует"
        elif password !=password2:
            error = "Пароли не совпадают"
        else:
            User.objects.create_user(email, email, password)
            user = authenticate(request, username=email, password=password)
            UserProfile.objects.create(user=user, email=email)
            auth_login(request, user)
            Basket.objects.create(id_customer=get_user(request))
            return redirect("lending:index")
        return render(request, "account/registration.html", {'form': form, 'error': error})


class AuthView(View):
    def get(self, request):
        form = UserAuthForm
        return render(request, 'account/auth.html', {'form': form})

    def post(self, request):
        form = UserAuthForm(request.POST)

        email = form.data['email'].lower()
        password = form.data['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("lending:index")
        else:
            error = "Неверный логин или пароль! Повторите попытку."
        return render(request, "account/auth.html", {'form': form, 'error': error})


class LogoutView(View):
    def get(self, request):
        django_logout(request)
        return redirect("lending:index")