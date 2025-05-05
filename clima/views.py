import requests
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse

GEORREF_API = 'https://apis.datos.gob.ar/georef/api/'
OPENWEATHERMAP_API = 'https://api.openweathermap.org/data/2.5/'

def home(request):
    response = requests.get(GEORREF_API + 'provincias').json()
    provincias = response.get('provincias', [])
    return render(request, 'clima/home.html', {'provincias': provincias})


def get_departamentos(request):
    provincia = request.GET.get('provincia')
    response = requests.get(GEORREF_API + f'departamentos?provincia={provincia}&max=5000').json()
    departamentos = response.get('departamentos', [])
    return JsonResponse({'departamentos': departamentos})


def get_localidades(request):
    departamento = request.GET.get('departamento')
    response = requests.get(GEORREF_API + f'localidades?departamento={departamento}&max=5000').json()
    localidades = response.get('localidades', [])
    return JsonResponse({'localidades': localidades})


def get_clima(request):
    localidad = request.GET.get('localidad')
    data = requests.get(GEORREF_API + f'localidades?id={localidad}&max=1').json()
    if data['localidades']:
        loc = data['localidades'][0]
        lat = loc['centroide']['lat']
        lon = loc['centroide']['lon']
        clima = requests.get(
            OPENWEATHERMAP_API + f'weather?lat={lat}&lon={lon}&appid={settings.OPENWEATHERMAP_API_KEY}&units=metric&lang=es'
        ).json()
        return JsonResponse({'clima': clima})
    return JsonResponse({'error': 'Localidad no encontrada'})
