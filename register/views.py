from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.views import View
from django.http import HttpResponse


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, 'registration/register.html', {"form": form})


class LoginPage(LoginView):
    def get(self, request):
        if request.user.is_authenticated:
            if self.request.user.groups.filter('admin').exists:
                return redirect('dashboard/inventorydashboard/')
        context = {}
        return render(request, 'registration/login.html', context)


class AllowedUsers(View):
    def get(self, allowed_roles=[]):
        def decorator(view_func):
            def wrapper_func(request, *args, **kwargs):

                group = None
                if request.user.groups.exists():
                    group = request.user.groups.all()[0].name

                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse('You are not authorized to view this page')
            return wrapper_func
        return decorator


class AdminOnly(View):
    def get(self, view_func):
        def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group == 'employee':
                return redirect('production:production-start')

            else:
                return view_func(request, *args, **kwargs)

        return wrapper_function
