from django.shortcuts import render, get_object_or_404, reverse
from .models import Production_tracker, Pre_roll_1g_manuf, Preroll_half_manuf
from inventory.models import Inventory_Log
from .forms import Productionform
from django.views.generic import (
CreateView,
DetailView,
ListView,
UpdateView,
DeleteView
)
class productiontrackerview(ListView):
    template_name = 'productions/production_tracker.html'
    def get(self, request, *args, **kwargs):
        queryset = Production_tracker.objects.all()
        context = {
            "object_list": queryset
        }
        return render(request, self.template_name, context)


class productioncreateview(CreateView):
    template_name = 'productions/production_create.html'
    form_class = Productionform
    queryset = Production_tracker.objects.all()

    def form_valid(self, form):
        if form.cleaned_data.get('Task').finished_product == '1g_open_pre_roll':
            menu = Pre_roll_1g_manuf.objects.first()
            menu.pre_roll_amt = form.cleaned_data.get('Count') * menu.pre_roll_amt
            menu.cone_amt = form.cleaned_data.get('Count') * menu.cone_amt
            menu.canna_amount = form.cleaned_data.get('Count') * menu.canna_amount

            sgoprcone = Inventory_Log(
            Emp=form.cleaned_data.get('Employee'),
            Date=form.cleaned_data.get('End_time'),
            supply=menu.input1,
            supply_amt=menu.cone_amt * -1)
            sgoprcone.save()

            sgoprcanna = Inventory_Log(
            Emp=form.cleaned_data.get('Employee'),
            Date=form.cleaned_data.get('End_time'),
            supply=menu.input2,
            supply_amt=menu.canna_amount * -1)
            sgoprcanna.save()

        elif form.cleaned_data.get('Task').finished_product == 'halfg_open_pre_roll':
            menu = Preroll_half_manuf.objects.first()
            menu.pre_roll_amt = form.cleaned_data.get('Count') * menu.pre_roll_amt
            menu.cone_amt = form.cleaned_data.get('Count') * menu.cone_amt
            menu.canna_amount = form.cleaned_data.get('Count') * menu.canna_amount

            hgoprcone = Inventory_Log(
            Emp=form.cleaned_data.get('Employee'),
            Date=form.cleaned_data.get('End_time'),
            supply=menu.input1,
            supply_amt=menu.cone_amt * -1)
            hgoprcone.save()

            hgoprcanna = Inventory_Log(
            Emp=form.cleaned_data.get('Employee'),
            Date=form.cleaned_data.get('End_time'),
            supply=menu.input2,
            supply_amt=menu.canna_amount * -1)
            hgoprcanna.save()


        obj1 = Inventory_Log(
            Emp=form.cleaned_data.get('Employee'),
            Date=form.cleaned_data.get('End_time'),
            supply=form.cleaned_data.get('Task').finished_product,
            supply_amt=form.cleaned_data.get('Count'))

        obj1.save()
        return super(productioncreateview, self).form_valid(form)


class productiondetailview(DetailView):
    template_name = 'productions/production_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Production_tracker, id=id_)


class productionupdateview(UpdateView):
    template_name = 'productions/production_create.html'
    form_class = Productionform
    queryset = Production_tracker.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Production_tracker, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class productiondeleteview(DeleteView):
    template_name = 'productions/productions_delete.html'


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Production_tracker, id=id_)

    def get_success_url(self):
        return reverse('production:production-tracker')

