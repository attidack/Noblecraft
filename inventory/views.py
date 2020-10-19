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


class InventoryLog(ListView):
    template_name = 'inventories/inventory_log.html'

    def get(self, request, *args, **kwargs):
        queryset = Inventory_Log.objects.all()
        context = {
            "object_list": queryset
        }
        return render(request, self.template_name, context)


class inventorycreateview(CreateView):
    template_name = 'inventories/inventory_create.html'
    form_class = Inventoryform
    queryset = Inventory_Log.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


# Create your views here.
class inventorydetailview(DetailView):
    template_name = 'inventories/inventory_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Inventory_Log, id=id_)

class inventoryupdateview(UpdateView):
    template_name = 'inventories/inventory_create.html'
    form_class = Inventoryform
    queryset = Inventory_Log.objects.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Inventory_Log, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class inventorydeleteview(DeleteView):
    template_name = 'inventories/inventory_delete.html'


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Inventory_Log, id=id_)

    def get_success_url(self):
        return reverse('inventory:inventory-log')

