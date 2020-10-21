from django.shortcuts import render, get_object_or_404, reverse

from inventory.models import Inventory_Log
from .forms import Productionform, Productionformstart, Productionformend
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
    Production_tracker_start,
    Production_tracker_end

)
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

class productioncreateviewstart(CreateView):
    template_name = 'productions/production_start.html'
    form_class = Productionformstart
    queryset = Production_tracker_start.objects.all()

    def form_valid(self, form):
        obj1 = Production_tracker(
            user=form.cleaned_data.get('user'),
            Start_time=form.cleaned_data.get('Start_time'),
            Task=form.cleaned_data.get('Task'),
            UID=form.cleaned_data.get('UID'),
        )

        obj1.save()
        return super(productioncreateviewstart, self).form_valid(form)

class productioncreateviewend(CreateView):
    template_name = 'productions/production_end.html'
    form_class = Productionformend
    queryset = Production_tracker_end.objects.all()

    def form_valid(self, form):
        if form.cleaned_data.get('Task').finished_product == '1g_open_pre_roll':
            menu1gopr = Pre_roll_1g_manuf.objects.first()
            menu1gopr.cone_amt = form.cleaned_data.get('Count') * menu1gopr.cone_amt
            menu1gopr.canna_amount = form.cleaned_data.get('Count') * menu1gopr.canna_amount

            sgoprcone = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu1gopr.input1,
                supply_amt=menu1gopr.cone_amt * -1, )
            sgoprcone.save()

            sgoprcanna = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menu1gopr.input2,
                supply_amt=menu1gopr.canna_amount * -1,
                UID=form.cleaned_data.get('UID'))
            sgoprcanna.save()

        elif form.cleaned_data.get('Task').finished_product == 'halfg_open_pre_roll':
            menuhgopr = Preroll_half_manuf.objects.first()
            menuhgopr.cone_amt = form.cleaned_data.get('Count') * menuhgopr.cone_amt
            menuhgopr.canna_amount = form.cleaned_data.get('Count') * menuhgopr.canna_amount

            hgoprcone = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menuhgopr.input1,
                supply_amt=menuhgopr.cone_amt * -1)
            hgoprcone.save()

            hgoprcanna = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menuhgopr.input2,
                supply_amt=menuhgopr.canna_amount * -1,
                UID=form.cleaned_data.get('UID'))
            hgoprcanna.save()

        elif form.cleaned_data.get('Task').finished_product == 'halfg_pre_roll':
            menut = Twisting_Preroll_half_manuf.objects.first()
            menut.pre_roll_amt = form.cleaned_data.get('Count') * menut.pre_roll_amt
            menut.input1_amt = form.cleaned_data.get('Count') * menut.input1_amt

            twhgpr = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menut.input1,
                supply_amt=menut.input1_amt * -1)
            twhgpr.save()

        elif form.cleaned_data.get('Task').finished_product == '1g_pre_roll':
            menut1g = Twisting_Preroll_1g_manuf.objects.first()
            menut1g.input1_amt = form.cleaned_data.get('Count') * menut1g.input1_amt

            twgpr = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menut1g.input1,
                supply_amt=menut1g.input1_amt * -1,
                UID=form.cleaned_data.get('UID'))
            twgpr.save()

        elif form.cleaned_data.get('Task').finished_product == 'Unwrapped_box':
            menuuwbhg = Unwrapped_Box_manuf.objects.first()
            menuuwbhg.pre_roll_amt = form.cleaned_data.get('Count') * menuuwbhg.pre_roll_amt
            menuuwbhg.box_amt = form.cleaned_data.get('Count') * menuuwbhg.box_amt
            menuuwbhg.label_amount = form.cleaned_data.get('Count') * menuuwbhg.label_amount
            menuuwbhg.canna_sticker_amount = form.cleaned_data.get('Count') * menuuwbhg.canna_sticker_amount

            uwbprhg = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menuuwbhg.input1,
                supply_amt=menuuwbhg.pre_roll_amt * -1,
                UID=form.cleaned_data.get('UID'))
            uwbprhg.save()

            uwbb = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menuuwbhg.input2,
                supply_amt=menuuwbhg.box_amt * -1)
            uwbb.save()

            uwblbl = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menuuwbhg.input3,
                supply_amt=menuuwbhg.label_amount * -1)
            uwblbl.save()

            uwbcannalbl = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menuuwbhg.input4,
                supply_amt=menuuwbhg.label_amount * -1)
            uwbcannalbl.save()

        elif form.cleaned_data.get('Task').finished_product == 'Finished_Box':
            menufb = Finished_Box_manuf.objects.first()
            menufb.input1_amt = form.cleaned_data.get('Count') * menufb.input1_amt
            menufb.input2_amt = form.cleaned_data.get('Count') * menufb.input2_amt
            menufb.input3_amt = form.cleaned_data.get('Count') * menufb.input3_amt

            input1log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menufb.input1,
                supply_amt=menufb.input1_amt * -1,
                UID=form.cleaned_data.get('UID'))
            input1log.save()

            input2log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menufb.input2,
                supply_amt=menufb.input2_amt * -1)
            input2log.save()

            input3log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menufb.input3,
                supply_amt=menufb.input3_amt * -1)
            input3log.save()

        elif form.cleaned_data.get('Task').finished_product == 'Preroll_tube_2_half_grams':
            menupt2hg = Finished_Tube_2half_grams_manuf.objects.first()
            menupt2hg.input1_amt = form.cleaned_data.get('Count') * menupt2hg.input1_amt
            menupt2hg.input2_amt = form.cleaned_data.get('Count') * menupt2hg.input2_amt
            menupt2hg.input3_amt = form.cleaned_data.get('Count') * menupt2hg.input3_amt

            input1log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menupt2hg.input1,
                supply_amt=menupt2hg.input1_amt * -1,
                UID=form.cleaned_data.get('UID'))
            input1log.save()

            input2log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menupt2hg.input2,
                supply_amt=menupt2hg.input2_amt * -1)
            input2log.save()

            input3log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menupt2hg.input3,
                supply_amt=menupt2hg.input3_amt * -1)
            input3log.save()

        elif form.cleaned_data.get('Task').finished_product == 'Preroll_tube_1_gram':
            menupt1g = Finished_Tube_1_gram_manuf.objects.first()
            menupt1g.input1_amt = form.cleaned_data.get('Count') * menupt1g.input1_amt
            menupt1g.input2_amt = form.cleaned_data.get('Count') * menupt1g.input2_amt
            menupt1g.input3_amt = form.cleaned_data.get('Count') * menupt1g.input3_amt

            input1log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menupt1g.input1,
                supply_amt=menupt1g.input1_amt * -1,
                UID=form.cleaned_data.get('UID'))
            input1log.save()

            input2log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menupt1g.input2,
                supply_amt=menupt1g.input2_amt * -1)
            input2log.save()

            input3log = Inventory_Log(
                user_id=form.cleaned_data.get('user_id'),
                Date=form.cleaned_data.get('End_time'),
                supply=menupt1g.input3,
                supply_amt=menupt1g.input3_amt * -1)
            input3log.save()

        obj1 = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=form.cleaned_data.get('Task').finished_product,
            supply_amt=form.cleaned_data.get('Count'),
            UID=form.cleaned_data.get('UID')
        )
        obj1.save()

        obj2 = Production_tracker(
            user_id=form.cleaned_data.get('user_id'),
            End_time=form.cleaned_data.get('End_time'),
            Task=form.cleaned_data.get('Task'),
            UID=form.cleaned_data.get('UID'),
            Count=form.cleaned_data.get('Count')
            )

        obj2.save()
        return super(productioncreateviewend, self).form_valid(form)


class productioncreateview(CreateView):
    template_name = 'productions/production_create.html'
    form_class = Productionform
    queryset = Production_tracker.objects.all()

    def form_valid(self, form):
        if form.cleaned_data.get('Task').finished_product == '1g_open_pre_roll':
            menu1gopr = Pre_roll_1g_manuf.objects.first()
            menu1gopr.cone_amt = form.cleaned_data.get('Count') * menu1gopr.cone_amt
            menu1gopr.canna_amount = form.cleaned_data.get('Count') * menu1gopr.canna_amount

            sgoprcone = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menu1gopr.input1,
            supply_amt=menu1gopr.cone_amt * -1,)
            sgoprcone.save()

            sgoprcanna = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menu1gopr.input2,
            supply_amt=menu1gopr.canna_amount * -1,
            UID=form.cleaned_data.get('UID'))
            sgoprcanna.save()

        elif form.cleaned_data.get('Task').finished_product == 'halfg_open_pre_roll':
            menuhgopr = Preroll_half_manuf.objects.first()
            menuhgopr.cone_amt = form.cleaned_data.get('Count') * menuhgopr.cone_amt
            menuhgopr.canna_amount = form.cleaned_data.get('Count') * menuhgopr.canna_amount

            hgoprcone = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menuhgopr.input1,
            supply_amt=menuhgopr.cone_amt * -1)
            hgoprcone.save()

            hgoprcanna = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menuhgopr.input2,
            supply_amt=menuhgopr.canna_amount * -1,
            UID=form.cleaned_data.get('UID'))
            hgoprcanna.save()

        elif form.cleaned_data.get('Task').finished_product == 'halfg_pre_roll':
            menut = Twisting_Preroll_half_manuf.objects.first()
            menut.pre_roll_amt = form.cleaned_data.get('Count') * menut.pre_roll_amt
            menut.input1_amt = form.cleaned_data.get('Count') * menut.input1_amt

            twhgpr = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menut.input1,
            supply_amt=menut.input1_amt * -1)
            twhgpr.save()

        elif form.cleaned_data.get('Task').finished_product == '1g_pre_roll':
            menut1g = Twisting_Preroll_1g_manuf.objects.first()
            menut1g.input1_amt = form.cleaned_data.get('Count') * menut1g.input1_amt

            twgpr = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menut1g.input1,
            supply_amt=menut1g.input1_amt * -1,
            UID=form.cleaned_data.get('UID'))
            twgpr.save()

        elif form.cleaned_data.get('Task').finished_product == 'Unwrapped_box':
            menuuwbhg = Unwrapped_Box_manuf.objects.first()
            menuuwbhg.pre_roll_amt = form.cleaned_data.get('Count') * menuuwbhg.pre_roll_amt
            menuuwbhg.box_amt = form.cleaned_data.get('Count') * menuuwbhg.box_amt
            menuuwbhg.label_amount = form.cleaned_data.get('Count') * menuuwbhg.label_amount
            menuuwbhg.canna_sticker_amount = form.cleaned_data.get('Count') * menuuwbhg.canna_sticker_amount

            uwbprhg = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menuuwbhg.input1,
            supply_amt=menuuwbhg.pre_roll_amt * -1,
            UID=form.cleaned_data.get('UID'))
            uwbprhg.save()

            uwbb = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menuuwbhg.input2,
            supply_amt=menuuwbhg.box_amt * -1)
            uwbb.save()

            uwblbl = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menuuwbhg.input3,
            supply_amt=menuuwbhg.label_amount * -1)
            uwblbl.save()

            uwbcannalbl = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menuuwbhg.input4,
            supply_amt=menuuwbhg.label_amount * -1)
            uwbcannalbl.save()

        elif form.cleaned_data.get('Task').finished_product == 'Finished_Box':
            menufb = Finished_Box_manuf.objects.first()
            menufb.input1_amt = form.cleaned_data.get('Count') * menufb.input1_amt
            menufb.input2_amt = form.cleaned_data.get('Count') * menufb.input2_amt
            menufb.input3_amt = form.cleaned_data.get('Count') * menufb.input3_amt

            input1log = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menufb.input1,
            supply_amt=menufb.input1_amt * -1,
            UID=form.cleaned_data.get('UID'))
            input1log.save()

            input2log = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menufb.input2,
            supply_amt=menufb.input2_amt * -1)
            input2log.save()

            input3log = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menufb.input3,
            supply_amt=menufb.input3_amt * -1)
            input3log.save()

        elif form.cleaned_data.get('Task').finished_product == 'Preroll_tube_2_half_grams':
            menupt2hg = Finished_Tube_2half_grams_manuf.objects.first()
            menupt2hg.input1_amt = form.cleaned_data.get('Count') * menupt2hg.input1_amt
            menupt2hg.input2_amt = form.cleaned_data.get('Count') * menupt2hg.input2_amt
            menupt2hg.input3_amt = form.cleaned_data.get('Count') * menupt2hg.input3_amt

            input1log = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menupt2hg.input1,
            supply_amt=menupt2hg.input1_amt * -1,
            UID=form.cleaned_data.get('UID'))
            input1log.save()

            input2log = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menupt2hg.input2,
            supply_amt=menupt2hg.input2_amt * -1)
            input2log.save()

            input3log = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menupt2hg.input3,
            supply_amt=menupt2hg.input3_amt * -1)
            input3log.save()

        elif form.cleaned_data.get('Task').finished_product == 'Preroll_tube_1_gram':
            menupt1g = Finished_Tube_1_gram_manuf.objects.first()
            menupt1g.input1_amt = form.cleaned_data.get('Count') * menupt1g.input1_amt
            menupt1g.input2_amt = form.cleaned_data.get('Count') * menupt1g.input2_amt
            menupt1g.input3_amt = form.cleaned_data.get('Count') * menupt1g.input3_amt

            input1log = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menupt1g.input1,
            supply_amt=menupt1g.input1_amt * -1,
            UID=form.cleaned_data.get('UID'))
            input1log.save()

            input2log = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menupt1g.input2,
            supply_amt=menupt1g.input2_amt * -1)
            input2log.save()

            input3log = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=menupt1g.input3,
            supply_amt=menupt1g.input3_amt * -1)
            input3log.save()

        obj1 = Inventory_Log(
            user_id=form.cleaned_data.get('user_id'),
            Date=form.cleaned_data.get('End_time'),
            supply=form.cleaned_data.get('Task').finished_product,
            supply_amt=form.cleaned_data.get('Count'),
            UID=form.cleaned_data.get('UID')
        )

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

