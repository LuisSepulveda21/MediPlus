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


queryset = None

def Initial(request):
    return render(request, 'ips/base.html')


def Home(request):
    if (request.GET.get('lat')is not None and request.GET.get('lon')is not None):
        latitude = float(request.GET.get('lat'))
        longitude = float(request.GET.get('lon'))
        user_location = Point(longitude, latitude, srid = 4326)
        global queryset
        queryset = ips.objects.annotate(distance=Distance('location', user_location) ).order_by('distance')[0:3]
    
    return render(request, 'ips/index.html', {'ips': queryset})

""" class Home(generic.ListView):
    "Obtener latitud y longitud basado en GPS"

    def get_lat_lon(self):
        self.lon = self.request.GET.get('lon')
        self.lat = self.request.GET.get('lat')
        self.user_location = Point(self.lon, self.lat, srid = 4326)
        return user_location

    model = ips
    context_object_name = 'ips'
    queryset = ips.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:3]
    template_name = 'ips/index.html' """
