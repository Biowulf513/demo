from django.shortcuts import render, render_to_response
from onesite.models import OneSiteDemo

def one_site_demo(request):
    name = 'one_site_demo'
    return render_to_response('onesitedemo_one.html', {'name':name})

def one_site_all(request):
    to_one_site_all = OneSiteDemo.objects.all()
    return render_to_response('onesitedemo_all.html', {"to":to_one_site_all})
