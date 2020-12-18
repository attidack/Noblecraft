import django_filters
from django_filters import DateFilter, CharFilter
from production.models import Production_tracker
from inventory.models import Inventory_Log


class ProductionFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='Start_time', lookup_expr='gte')
    end_date = DateFilter(field_name='Start_time', lookup_expr='lte')
    notes = CharFilter(field_name='notes', lookup_expr='icontains')
    class Meta:
        model = Production_tracker
        fields = '__all__'
        exclude = ['Date']


class InventoryFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='Date', lookup_expr='gte')
    end_date = DateFilter(field_name='Date', lookup_expr='lte')
    notes = CharFilter(field_name='notes', lookup_expr='icontains')
    class Meta:
        model = Inventory_Log
        fields = '__all__'
        exclude = ['cost_of_task', 'Date']
