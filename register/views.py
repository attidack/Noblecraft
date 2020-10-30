from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



class UserAccessMixin(PermissionRequiredMixin):
    permission_denied_message = 'you do not have permission to view this page'
    def has_permission(self):
        perms = self.get_permission_required()
        groups = self.request.user.groups.filter(name__in=perms).exists()
        return groups


class Register(LoginRequiredMixin, UserAccessMixin, View):
    form_class = RegisterForm
    permission_required = ('admin', 'manager', 'Owen-perms')
    template_name = 'registration/register.html'
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="employee")
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            messages.success(request, 'account was created for  ' + username)
            return redirect('/register')

        context = {'form': form}
        return render(request, 'registration/register.html', context)


class LoginPage(LoginView):
    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'registration/login.html', context)


class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('login')


