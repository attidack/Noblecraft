from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1> Hello World</>")
    return render(request, "home.html", {})

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