from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings
from django import forms
from .models import Grade, Week
from .forms import AccountForm
# Create your views here.
def home_view(request):
    return render(request, "index.html", {})

@login_required
def account_view(response):
    weekNumber = Week.objects.get(id=1)
    Grades = Grade.objects.get(id=response.user.id)
    context = {
        'Grades':Grades,
        'weekNumber':weekNumber
    }
    return render(response, "account.html", context)


def registration_view(response):
    if response.method == "POST":
        form = AccountForm(response.POST or None)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = AccountForm()
    return render(response, "registration.html", {"form":form})

def test_view(response):
    weekNumber = Week.objects.get(id=1)
    context = {
        'weekNumber':weekNumber
    }
    return render(response, "test.html",context)