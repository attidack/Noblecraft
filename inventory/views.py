from django.shortcuts import render, get_object_or_404, reverse
from .models import Inventory_Log
from .forms import Inventoryform
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse



class UserAccessMixin(PermissionRequiredMixin):
    def has_permission(self):
        perms = self.get_permission_required()
        groups = self.request.user.groups.filter(name__in=perms).exists()
        return groups


class InventoryLog(LoginRequiredMixin, UserAccessMixin, ListView):
    login_url = '../login/'
    permission_required = ('admin', 'employee', 'manager', 'Owen-perms')
    template_name = 'inventories/inventory_log.html'

    def get(self, request, *args, **kwargs):
        queryset = Inventory_Log.objects.all()
        context = {
            "object_list": queryset.order_by('-pk')
        }
        return render(request, self.template_name, context)


class inventorycreateview(LoginRequiredMixin, UserAccessMixin, CreateView):
    login_url = '../login/'
    permission_required = ('admin', 'manager', 'Owen-perms')
    template_name = 'inventories/inventory_create.html'
    form_class = Inventoryform
    queryset = Inventory_Log.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


# Create your views here.
class inventorydetailview(LoginRequiredMixin, UserAccessMixin, DetailView):
    login_url = '../login/'
    permission_required = ('admin', 'employee', 'manager', 'Owen-perms')
    template_name = 'inventories/inventory_detail.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Inventory_Log, id=id_)


class inventoryupdateview(LoginRequiredMixin, UserAccessMixin, UpdateView):
    login_url = '../login/'
    permission_required = ('admin', 'manager', 'Owen-perms')
    template_name = 'inventories/inventory_create.html'
    form_class = Inventoryform
    queryset = Inventory_Log.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Inventory_Log, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)


class inventorydeleteview(LoginRequiredMixin, UserAccessMixin, DeleteView):
    login_url = '../login/'
    permission_required = ('admin', 'manager', 'Owen-perms')
    template_name = 'inventories/inventory_delete.html'


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Inventory_Log, id=id_)

    def get_success_url(self):
        return reverse('inventory:inventory-log')

