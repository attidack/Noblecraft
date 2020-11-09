from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView
from datetime import datetime, timedelta
from production.models import Production_tracker
from inventory.models import Inventory_Log, InventorySupplies, StorageLocation
from django.http import JsonResponse
# Create your views here.
from inventory.views import UserAccessMixin


class EmployeeDashboard(View):
    def get(self, request):
        now = datetime.now()
        context={
            'input_log_number': request.user.inventory_log_set.filter(Date__lte=now).count(),
            'queryset': Production_tracker.objects.filter(user_id=self.request.user).order_by('-pk')[:3],
            'object_list': Inventory_Log.objects.filter(user_id=self.request.user).order_by('-pk')[:10],
        }
        return render(request, 'employee_dashboard.html', context)


class InventoryDashboard(LoginRequiredMixin, UserAccessMixin, View):
    login_url = '../login/'
    permission_required = ('admin', 'employee', 'manager', 'Owen-perms')

    def get(self, request):
        supply_summery = InventorySupplies.objects.annotate(supply_amt_total=Sum('inventory_log__supply_amt'))
        context = {
            'object_list': supply_summery,

        }
        return render(request, 'inventory_dashboard.html', context)


class SupplyList(LoginRequiredMixin, UserAccessMixin, View):
    login_url = '../login/'
    permission_required = ('admin', 'employee', 'manager', 'Owen-perms')

    def get(self, request, supply_id):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        start_week = today - timedelta(today.weekday())
        end_week = start_week + timedelta(7)
        logs = Inventory_Log.objects.filter(supply__pk=supply_id)
        amount = logs.aggregate(Sum('supply_amt'))
        amount_day = logs.filter(Date__lte=tomorrow, Date__gte=today).aggregate(Sum('supply_amt'))
        amount_week = logs.filter(Date__lte=end_week, Date__gte=start_week).aggregate(Sum('supply_amt'))
        amount_month = logs.filter(Date__year=today.year, Date__month=today.month).aggregate(Sum('supply_amt'))
        amount_year = logs.filter(Date__year=today.year).aggregate(Sum('supply_amt'))
        live = logs.filter(storage_location=1).aggregate(Sum('supply_amt'))
        backstock = logs.filter(storage_location=2).aggregate(Sum('supply_amt'))

        context = {
            'object_list': logs.order_by('-pk'),
            'amount': amount,
            'amount_day': amount_day,
            'amount_week': amount_week,
            'amount_month': amount_month,
            'amount_year': amount_year,
            'live': live,
            'backstock': backstock,
        }

        return render(request, 'supply_log.html', context)





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

        return finalrep

class StatsView(TemplateView, InventorySummery):
    template_name = 'stats.html'
    def get_inventory_category_data(self, **kwargs):
        context = super().get_inventory_category_data(**kwargs)
        context['qs'] = InventorySummery
        return context