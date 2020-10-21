from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(reposnce):
    if reposnce.method == "POST":
        form = RegisterForm(reposnce.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()
    return render(reposnce, 'register/register.html', {"form":form})