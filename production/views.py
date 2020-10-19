from django.shortcuts import render, get_object_or_404
from .models import Production_tracker
from .forms import Productionform

def production_tracker_view(request):
    queryset = Production_tracker.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "productions/production_tracker.html", context)

def production_create_view(request):
    form = Productionform(request.POST or None)
    if form.is_valid():
        form.save()
        form = Productionform()
    context = {
        'form': form
    }

    return render(request, "productions/production_create.html", context)

def production_detail_view(request, id):
    obj = get_object_or_404(Production_tracker, id=id)
    context = {
        'object': obj
    }
    return render(request, "productions/production_detail.html", context)

def production_delete_view(request, id):
    obj = get_object_or_404(Production_tracker, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../')
    context = {
        "object": obj
    }
    return render(request, "productions/productions_delete.html", context)
