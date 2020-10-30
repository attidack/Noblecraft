from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from production.models import Production_tracker
from inventory.models import Inventory_Log
# Create your views here.


class Home(LoginRequiredMixin, View):
    login_url = 'login/'

    def get(self, request):
        context = {
            'queryset': Production_tracker.objects.filter(user_id=self.request.user).order_by('-pk')[:3],
            'object_list': Inventory_Log.objects.filter(user_id=self.request.user).order_by('-pk')[:10],
        }
        return render(request, "home.html", context)

@login_required(login_url='/login')
def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

@login_required(login_url='/login')
def about_view(request, *args, **kwargs):
    my_context = {
        "title": "this is about us",
        "this is true": True,
        "my_number": 123,
        "my_list": [123, 424, 4654, "Abc"],
        "my_html":"<h1>Hello World</h1>"
    }
    return render(request, "about.html", my_context)

@login_required(login_url='/login')
def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})