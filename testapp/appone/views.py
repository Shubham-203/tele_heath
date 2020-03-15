from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geoip2 import GeoIP2
# Create your views here.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    g=GeoIP2()
    return HttpResponse(g.city("72.14.207.99"))
