from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, 
                username=data.get("username"), 
                password=data.get("password")
            )

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated successfully.")
                else:
                    return HttpResponse("User account not active.")
            else:
                return HttpResponse("Invalid credentials.")
        else:
            form = LoginForm()

        context = {"form": form}

        return render(request, "account/login.html", context)


@login_required
def dashboard(request):
    context = {"section": "dashboard"}
    return render(request, "account/dashboard.html", context)
