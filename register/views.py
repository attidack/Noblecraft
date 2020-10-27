from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, 'registration/register.html', {"form":form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/home')
    context = {}
    return render(request, 'registration/login.html', context)