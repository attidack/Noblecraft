from django.db.models import Sum
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
            'queryset': Production_tracker.objects.filter(user_id=self.request.user).order_by('-pk'),
        }
        return render(request, 'employee_dashboard.html', context)


class InventoryDashboard(View):
    def get(self, request):
        # queryset = Inventory_Log.objects.filter(supply='Finished_Box')
        # finished_box = sum(Inventory_Log.supply_amt in queryset)
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
                amount += item.supply_amt
            return amount

        for x in inventory_supplies:
            for y in category_list:
                finalrep[y] = get_inventory_category(y)
        context={
            'finalrep':finalrep,
            # 'finished_box': finished_box,
        }
        return render(request, 'inventory_dashboard.html', context)


class OwenDashboard(View):
    def get(self, request):
        # queryset = Inventory_Log.objects.filter(supply='Finished_Box')
        # finished_box = sum(Inventory_Log.supply_amt in queryset)
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
                amount += item.supply_amt
            return amount

        for x in inventory_supplies:
            for y in category_list:
                finalrep[y] = get_inventory_category(y)
        context={
            'finalrep':finalrep,
            # 'finished_box': finished_box,
        }
        return render(request, 'owen_dashboard.html', context)


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
                amount += item.supply_amt
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