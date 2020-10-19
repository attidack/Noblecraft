from django.shortcuts import render, get_object_or_404, reverse
from .models import Production_tracker
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
        print(form.cleaned_data)
        return super().form_valid(form)


class productiondetailview(DetailView):
    template_name = 'productions/production_detail.html'
    # queryset = Article.objects.all()

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

