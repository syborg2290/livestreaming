# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from .tokens import account_activation_token
from django.http import HttpResponse
import json

from .models import User


def home(request):
    return render(request, 'home.html')


def loginUser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse(json.dumps({"message": "Success"}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"message": "inactive"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message": "invalid"}), content_type="application/json")
    return HttpResponse(json.dumps({"message": "denied"}), content_type="application/json")


def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        data = {'username': username, 'email': email,
                'password1': password1, 'password2': password2}
        if password1 == password2:
            form = SignUpForm(data=data)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = True
                user.is_staff = True
                user.is_superuser = False
                user.save()

                userAuth = authenticate(email=email, password=password1)
                if userAuth is not None:
                    if userAuth.is_active:
                        login(request, user)

                # current_site = get_current_site(request)
                # subject = "Activate your Account"
                # message = render_to_string(
                #     "account/registration/account_activation_email.html",
                #     {
                #         "user": user,
                #         "domain": current_site.domain,
                #         "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                #         "token": account_activation_token.make_token(user),
                #     },
                # )
                # user.email_user(subject=subject, message=message)

                return HttpResponse(json.dumps({"message": "Success"}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"message": form.errors}), content_type="application/json")
        else:
            form = SignUpForm()
    return HttpResponse(json.dumps({"message": "Denied"}), content_type="application/json")


# def account_activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, user.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return redirect('home:home')
#     else:
#         return render(request, 'components/panels/sub_panels/activation_invalid.html')
