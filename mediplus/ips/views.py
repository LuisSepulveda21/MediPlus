from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import ips
import requests
from django.http import HttpResponse


"TO DO: get user ip-> lat,lon"
""" def my_django_view(request):
    if request.method == 'GET':
        r = requests.get(f"http://ip-api.com/json/{ip}?fields=lat,lon,", params=request.GET)
    if r.status_code == 200:
        return HttpResponse('Yay, it worked')
    return HttpResponse('Could not save data') """


latitude = 10.987602
longitude = -74.802943

user_location = Point(longitude, latitude, srid = 4326)

class Home(generic.ListView):
    model = ips
    context_object_name = 'ips'
    queryset = ips.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:3]
    template_name = 'ips/index.html'
