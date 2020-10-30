from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from datetime import datetime, timedelta
from production.models import Production_tracker
from inventory.models import Inventory_Log
from django.http import JsonResponse
# Create your views here.


class EmployeeDashboard(View):
    def get(self, request):
        now = datetime.now()
        context={
            'input_log_number': request.user.inventory_log_set.filter(Date__lte=now).count(),
            'queryset': Production_tracker.objects.filter(user_id=self.request.user).order_by('-pk')[:3],
            'object_list': Inventory_Log.objects.filter(user_id=self.request.user).order_by('-pk')[:10],
        }
        return render(request, 'employee_dashboard.html', context)


class InventoryDashboard(View):
    def get(self, request):
        todays_date = datetime.now()
        inventory_supplies = Inventory_Log.objects.filter(Date__lte=todays_date)
        finalrep = {}

        def get_category(inventory_log):
            return inventory_log.supply

        category_list = list(set(map(get_category, inventory_supplies)))

        def get_inventory_category(supply):
            amount = 0
            filtered_by_category = inventory_supplies.filter(supply=supply)

            for item in filtered_by_category:
                amount += item.supply_amt or 0
            return amount

        for x in inventory_supplies:
            for y in category_list:
                finalrep[y] = get_inventory_category(y)
        context={
            'finalrep': finalrep,
            # 'finished_box': finished_box,
        }
        return render(request, 'inventory_dashboard.html', context)


# class OwenDashboard(View):
#     def get(self, request):
#         # queryset = Inventory_Log.objects.filter(supply='Finished_Box').aggregate(Sum('supply_amt'))
#     todays_date = datetime.now()
#     inventory_loc = Inventory_Log.supply
#     start_week = todays_date - timedelta(todays_date.weekday())
#     end_week = start_week + timedelta(7)
#     inventory_supplies_week = Inventory_Log.objects.filter(Date__range=[start_week, end_week],
#                                                       supply__in=(
#                                                           'Finished_Box',
#                                                           'Preroll_tube_2_half_grams',
#                                                           'Preroll_tube_1_gram'
#                                                       ))
#     inventory_supplies_month = Inventory_Log.objects.filter(Date__year=todays_date.year,
#                                                             Date__month=todays_date.month,
#                                                           supply__in=(
#                                                               'Finished_Box',
#                                                               'Preroll_tube_2_half_grams',
#                                                               'Preroll_tube_1_gram'
#                                                           ))
#     inventory_supplies_ytd = Inventory_Log.objects.filter(Date__year=todays_date.year,
#                                                       supply__in=(
#                                                           'Finished_Box',
#                                                           'Preroll_tube_2_half_grams',
#                                                           'Preroll_tube_1_gram'
#                                                       ))
#     inventory_supplies_total = Inventory_Log.objects.filter(supply__in=(
#                                                               'Finished_Box',
#                                                               'Preroll_tube_2_half_grams',
#                                                               'Preroll_tube_1_gram'
#                                                           ))
#     finalrepweek = {}
#     category_list = list(set(map(inventory_loc, inventory_supplies_week)))
#
#
#     def get_category(inventory_log):
#         return inventory_log.supply
#
#     def get_inventory_category(supply):
#         amount = 0
#         filtered_by_category = inventory_supplies_week.filter(supply=supply)
#
#         for item in filtered_by_category:
#             amount += item.supply_amt or 0
#         return amount
#
#     for x in inventory_supplies_week:
#         for y in category_list:
#             finalrepweek[y] = get_inventory_category(y)
#
#     finalrepmonth = {}
#
#     def get_category(inventory_log):
#         return inventory_log.supply
#
#     category_list = list(set(map(get_category, inventory_supplies_month)))
#
#     def get_inventory_category(supply):
#         amount = 0
#         filtered_by_category = inventory_supplies_month.filter(supply=supply)
#
#         for item in filtered_by_category:
#             amount += item.supply_amt or 0
#         return amount
#
#     for x in inventory_supplies_month:
#         for y in category_list:
#             finalrepmonth[y] = get_inventory_category(y)
#
#     finalrepytd = {}
#
#     def get_category(inventory_log):
#         return inventory_log.supply
#
#     category_list = list(set(map(get_category, inventory_supplies_ytd)))
#
#     def get_inventory_category(supply):
#         amount = 0
#         filtered_by_category = inventory_supplies_ytd.filter(supply=supply)
#
#         for item in filtered_by_category:
#             amount += item.supply_amt or 0
#         return amount
#
#     for x in inventory_supplies_ytd:
#         for y in category_list:
#             finalrepytd[y] = get_inventory_category(y)
#
#     finalrep = {}
#
#     def get_category(inventory_log):
#         return inventory_log.supply
#
#     category_list = list(set(map(get_category, inventory_supplies_total)))
#
#     def get_inventory_category(supply):
#         amount = 0
#         filtered_by_category = inventory_supplies_total.filter(supply=supply)
#
#         for item in filtered_by_category:
#             amount += item.supply_amt or 0
#         return amount
#
#     for x in inventory_supplies_total:
#         for y in category_list:
#             finalrep[y] = get_inventory_category(y)
#
#     context={
#         'finalrepweek': finalrepweek,
#         'finalrepmonth': finalrepmonth,
#         'finalrepytd': finalrepytd,
#         'finalrep': finalrep,
#
#     }
#         return render(request, 'owen_dashboard.html', context)


class InventorySummery(View):
    def get(self, request):
        todays_date = datetime.now()
        # six_months_ago = todays_date - timedelta(days=182)
        inventory_supplies = Inventory_Log.objects.filter(Date__lte=todays_date)
        # inventory_supplies = Inventory_Log.objects.filter(owner=request.user, Date__gte=six_months_ago, date__lte=todays_date)
        finalrep = {}

        def get_category(inventory_log):
            return inventory_log.supply

        category_list = list(set(map(get_category, inventory_supplies)))

        def get_inventory_category(supply):
            amount = 0
            filtered_by_category = inventory_supplies.filter(supply=supply)

            for item in filtered_by_category:
                amount += item.supply_amt or 0
            return amount

        for x in inventory_supplies:
            for y in category_list:
                finalrep[y] = get_inventory_category(y)

        return JsonResponse({'inventory_category_data': finalrep}, safe=False)

class StatsView(TemplateView, InventorySummery):
    template_name = 'stats.html'
    def get_inventory_category_data(self, **kwargs):
        context = super().get_inventory_category_data(**kwargs)
        context['qs'] = InventorySummery
        return context