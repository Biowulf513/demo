from django.shortcuts import render_to_response, render
from onesite.models import OneSiteDemo

def one_site_demo(request):
    demo = 'this is DEMO page'
    return render_to_response('onesitedemo_one.html', {'demo':demo})

def one_site_all(request):
    to_one_site_all = OneSiteDemo.objects.all()
    return render_to_response('onesitedemo_all.html', {"to":to_one_site_all})

def one_site_last_record(request):
    last_record = OneSiteDemo.objects.order_by().last()
    return render_to_response('onesitedemo_last.html', {'last_record':last_record})