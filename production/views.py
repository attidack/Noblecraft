from django.shortcuts import render, get_object_or_404, reverse
from datetime import datetime
from inventory.models import Inventory_Log
from .forms import Productionform, ProductionFormStart, ProductionFormEnd

from .models import (
    Production_tracker,
    Pre_roll_1g_manuf,
    Preroll_half_manuf,
    Twisting_Preroll_half_manuf,
    Twisting_Preroll_1g_manuf,
    Unwrapped_Box_manuf,
    Finished_Box_manuf,
    Finished_Tube_2half_grams_manuf,
    Finished_Tube_1_gram_manuf,


)
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



class ProductionTrackerView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = '../login/'
    permission_required = 'admin'
    template_name = 'productions/production_tracker.html'

    def get(self, request, *args, **kwargs):
        queryset = Production_tracker.objects.all()
        context = {
            "object_list": queryset
        }
        return render(request, self.template_name, context)


class ProductionCreateViewStart(LoginRequiredMixin, PermissionRequiredMixin,  CreateView):
    login_url = '../login/'
    permission_required = 'admin'
    template_name = 'productions/production_start.html'
    form_class = ProductionFormStart
    queryset = Production_tracker.objects.all()

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        form.instance.Start_time = datetime.now()
        return super(ProductionCreateViewStart, self).form_valid(form)

    def get_success_url(self):
        return reverse("production:production-end", kwargs={"id": self.object.id})


class ProductionEndView(LoginRequiredMixin, PermissionRequiredMixin,  UpdateView):
    login_url = '../login/'
    permission_required = 'admin'
    template_name = 'productions/production_end.html'
    form_class = ProductionFormEnd
    queryset = Production_tracker.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Production_tracker, id=id_)

    def form_valid(self, form):
        form.instance.End_time = datetime.now()
        if self.object.Task.finished_product == '1g_open_pre_roll':
            menu1 = Pre_roll_1g_manuf.objects.first()
            menu1.cone_amt = form.cleaned_data.get('Count') * menu1.cone_amt
            menu1.canna_amount = form.cleaned_data.get('Count') * menu1.canna_amount

            input1log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu1.input1,
                supply_amt=menu1.cone_amt * -1,)
            input1log.save()

            input2log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu1.input2,
                supply_amt=menu1.canna_amount * -1,
                UID=form.cleaned_data.get('UID'))
            input2log.save()

        elif self.object.Task.finished_product == 'halfg_open_pre_roll':
            menu2 = Preroll_half_manuf.objects.first()
            menu2.cone_amt = form.cleaned_data.get('Count') * menu2.cone_amt
            menu2.canna_amount = form.cleaned_data.get('Count') * menu2.canna_amount

            input1log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu2.input1,
                supply_amt=menu2.cone_amt * -1)
            input1log.save()

            input2log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu2.input2,
                supply_amt=menu2.canna_amount * -1,
                UID=form.cleaned_data.get('UID'))
            input2log.save()

        elif self.object.Task.finished_product == 'halfg_pre_roll':
            menu3 = Twisting_Preroll_half_manuf.objects.first()
            menu3.pre_roll_amt = form.cleaned_data.get('Count') * menu3.pre_roll_amt
            menu3.input1_amt = form.cleaned_data.get('Count') * menu3.input1_amt

            input1log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu3.input1,
                supply_amt=menu3.input1_amt * -1)
            input1log.save()

        elif self.object.Task.finished_product == '1g_pre_roll':
            menu4 = Twisting_Preroll_1g_manuf.objects.first()
            menu4.input1_amt = form.cleaned_data.get('Count') * menu4.input1_amt

            input1log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu4.input1,
                supply_amt=menu4.input1_amt * -1,
                UID=form.cleaned_data.get('UID'))
            input1log.save()

        elif self.object.Task.finished_product == 'Unwrapped_box':
            menu5 = Unwrapped_Box_manuf.objects.first()
            menu5.pre_roll_amt = form.cleaned_data.get('Count') * menu5.pre_roll_amt
            menu5.box_amt = form.cleaned_data.get('Count') * menu5.box_amt
            menu5.label_amount = form.cleaned_data.get('Count') * menu5.label_amount
            menu5.canna_sticker_amount = form.cleaned_data.get('Count') * menu5.canna_sticker_amount

            input1log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu5.input1,
                supply_amt=menu5.pre_roll_amt * -1,
                UID=form.cleaned_data.get('UID'))
            input1log.save()

            input2log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu5.input2,
                supply_amt=menu5.box_amt * -1)
            input2log.save()

            input3log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu5.input3,
                supply_amt=menu5.label_amount * -1)
            input3log.save()

            input4log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu5.input4,
                supply_amt=menu5.label_amount * -1)
            input4log.save()

        elif self.object.Task.finished_product == 'Finished_Box':
            menu6 = Finished_Box_manuf.objects.first()
            menu6.input1_amt = form.cleaned_data.get('Count') * menu6.input1_amt
            menu6.input2_amt = form.cleaned_data.get('Count') * menu6.input2_amt
            menu6.input3_amt = form.cleaned_data.get('Count') * menu6.input3_amt

            input1log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu6.input1,
                supply_amt=menu6.input1_amt * -1,
                UID=form.cleaned_data.get('UID'))
            input1log.save()

            input2log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu6.input2,
                supply_amt=menu6.input2_amt * -1)
            input2log.save()

            input3log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu6.input3,
                supply_amt=menu6.input3_amt * -1)
            input3log.save()

        elif self.object.Task.finished_product == 'Preroll_tube_2_half_grams':
            menu7 = Finished_Tube_2half_grams_manuf.objects.first()
            menu7.input1_amt = form.cleaned_data.get('Count') * menu7.input1_amt
            menu7.input2_amt = form.cleaned_data.get('Count') * menu7.input2_amt
            menu7.input3_amt = form.cleaned_data.get('Count') * menu7.input3_amt

            input1log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu7.input1,
                supply_amt=menu7.input1_amt * -1,
                UID=form.cleaned_data.get('UID'))
            input1log.save()

            input2log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu7.input2,
                supply_amt=menu7.input2_amt * -1)
            input2log.save()

            input3log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu7.input3,
                supply_amt=menu7.input3_amt * -1)
            input3log.save()

        elif self.object.Task.finished_product == 'Preroll_tube_1_gram':
            menu8 = Finished_Tube_1_gram_manuf.objects.first()
            menu8.input1_amt = form.cleaned_data.get('Count') * menu8.input1_amt
            menu8.input2_amt = form.cleaned_data.get('Count') * menu8.input2_amt
            menu8.input3_amt = form.cleaned_data.get('Count') * menu8.input3_amt

            input1log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu8.input1,
                supply_amt=menu8.input1_amt * -1,
                UID=form.cleaned_data.get('UID'))
            input1log.save()

            input2log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu8.input2,
                supply_amt=menu8.input2_amt * -1)
            input2log.save()

            input3log = Inventory_Log(
                user_id=self.request.user,
                Date=form.cleaned_data.get('End_time'),
                supply=menu8.input3,
                supply_amt=menu8.input3_amt * -1)
            input3log.save()

        obj1 = Inventory_Log(
            user_id=self.request.user,
            Date=form.cleaned_data.get('End_time'),
            supply=self.object.Task.finished_product,
            supply_amt=form.cleaned_data.get('Count'),
            UID=form.cleaned_data.get('UID')
        )

        obj1.save()
        return super().form_valid(form)


class ProductionCreateView(LoginRequiredMixin, PermissionRequiredMixin,  CreateView):
    login_url = '../login/'
    permission_required = 'admin'
    template_name = 'productions/production_create.html'
    form_class = Productionform
    queryset = Production_tracker.objects.all()

    def form_valid(self, form):
        if form.cleaned_data.get('Task').finished_product == '1g_open_pre_roll':
            menu1 = Pre_roll_1g_manuf.objects.first()
            menu1.cone_amt = form.cleaned_data.get('Count') * menu1.cone_amt
            menu1.canna_amount = form.cleaned_data.get('Count') * menu1.canna_amount

            input1log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu1.input1,
                supply_amt=menu1.cone_amt * -1,)
            input1log.save()

            input2log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu1.input2,
                supply_amt=menu1.canna_amount * -1,
                UID=form.cleaned_data.get('UID'))
            input2log.save()

        elif form.cleaned_data.get('Task').finished_product == 'halfg_open_pre_roll':
            menu2 = Preroll_half_manuf.objects.first()
            menu2.cone_amt = form.cleaned_data.get('Count') * menu2.cone_amt
            menu2.canna_amount = form.cleaned_data.get('Count') * menu2.canna_amount

            input1log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu2.input1,
                supply_amt=menu2.cone_amt * -1)
            input1log.save()

            input2log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu2.input2,
                supply_amt=menu2.canna_amount * -1,
                UID=form.cleaned_data.get('UID'))
            input2log.save()

        elif form.cleaned_data.get('Task').finished_product == 'halfg_pre_roll':
            menu3 = Twisting_Preroll_half_manuf.objects.first()
            menu3.pre_roll_amt = form.cleaned_data.get('Count') * menu3.pre_roll_amt
            menu3.input1_amt = form.cleaned_data.get('Count') * menu3.input1_amt

            input1log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu3.input1,
                supply_amt=menu3.input1_amt * -1)
            input1log.save()

        elif form.cleaned_data.get('Task').finished_product == '1g_pre_roll':
            menu4 = Twisting_Preroll_1g_manuf.objects.first()
            menu4.input1_amt = form.cleaned_data.get('Count') * menu4.input1_amt

            input1log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu4.input1,
                supply_amt=menu4.input1_amt * -1,
                UID=form.cleaned_data.get('UID'))
            input1log.save()

        elif form.cleaned_data.get('Task').finished_product == 'Unwrapped_box':
            menu5 = Unwrapped_Box_manuf.objects.first()
            menu5.pre_roll_amt = form.cleaned_data.get('Count') * menu5.pre_roll_amt
            menu5.box_amt = form.cleaned_data.get('Count') * menu5.box_amt
            menu5.label_amount = form.cleaned_data.get('Count') * menu5.label_amount
            menu5.canna_sticker_amount = form.cleaned_data.get('Count') * menu5.canna_sticker_amount

            input1log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu5.input1,
                supply_amt=menu5.pre_roll_amt * -1,
                UID=form.cleaned_data.get('UID'))
            input1log.save()

            input2log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu5.input2,
                supply_amt=menu5.box_amt * -1)
            input2log.save()

            input3log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu5.input3,
                supply_amt=menu5.label_amount * -1)
            input3log.save()

            input4log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu5.input4,
                supply_amt=menu5.label_amount * -1)
            input4log.save()

        elif form.cleaned_data.get('Task').finished_product == 'Finished_Box':
            menu6 = Finished_Box_manuf.objects.first()
            menu6.input1_amt = form.cleaned_data.get('Count') * menu6.input1_amt
            menu6.input2_amt = form.cleaned_data.get('Count') * menu6.input2_amt
            menu6.input3_amt = form.cleaned_data.get('Count') * menu6.input3_amt

            input1log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu6.input1,
                supply_amt=menu6.input1_amt * -1,
                UID=form.cleaned_data.get('UID'))
            input1log.save()

            input2log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu6.input2,
                supply_amt=menu6.input2_amt * -1)
            input2log.save()

            input3log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu6.input3,
                supply_amt=menu6.input3_amt * -1)
            input3log.save()

        elif form.cleaned_data.get('Task').finished_product == 'Preroll_tube_2_half_grams':
            menu7 = Finished_Tube_2half_grams_manuf.objects.first()
            menu7.input1_amt = form.cleaned_data.get('Count') * menu7.input1_amt
            menu7.input2_amt = form.cleaned_data.get('Count') * menu7.input2_amt
            menu7.input3_amt = form.cleaned_data.get('Count') * menu7.input3_amt

            input1log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu7.input1,
                supply_amt=menu7.input1_amt * -1,
                UID=form.cleaned_data.get('UID'))
            input1log.save()

            input2log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu7.input2,
                supply_amt=menu7.input2_amt * -1)
            input2log.save()

            input3log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu7.input3,
                supply_amt=menu7.input3_amt * -1)
            input3log.save()

        elif form.cleaned_data.get('Task').finished_product == 'Preroll_tube_1_gram':
            menu8 = Finished_Tube_1_gram_manuf.objects.first()
            menu8.input1_amt = form.cleaned_data.get('Count') * menu8.input1_amt
            menu8.input2_amt = form.cleaned_data.get('Count') * menu8.input2_amt
            menu8.input3_amt = form.cleaned_data.get('Count') * menu8.input3_amt

            input1log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu8.input1,
                supply_amt=menu8.input1_amt * -1,
                UID=form.cleaned_data.get('UID'))
            input1log.save()

            input2log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu8.input2,
                supply_amt=menu8.input2_amt * -1)
            input2log.save()

            input3log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu8.input3,
                supply_amt=menu8.input3_amt * -1)
            input3log.save()

        obj1 = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=form.cleaned_data.get('Task').finished_product,
            supply_amt=form.cleaned_data.get('Count'),
            UID=form.cleaned_data.get('UID')
        )

        obj1.save()
        return super(ProductionCreateView, self).form_valid(form)


class ProductionDetailView(LoginRequiredMixin, PermissionRequiredMixin,  DetailView):
    login_url = '../login/'
    permission_required = 'admin'
    template_name = 'productions/production_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Production_tracker, id=id_)


class ProductionUpdateView(LoginRequiredMixin, PermissionRequiredMixin,  UpdateView):
    login_url = '../login/'
    permission_required = 'admin'
    template_name = 'productions/production_create.html'
    form_class = Productionform
    queryset = Production_tracker.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Production_tracker, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ProductionDeleteView(LoginRequiredMixin, PermissionRequiredMixin,  DeleteView):
    login_url = '../login/'
    permission_required = 'admin'
    template_name = 'productions/productions_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Production_tracker, id=id_)

    def get_success_url(self):
        return reverse('production:production-tracker')
