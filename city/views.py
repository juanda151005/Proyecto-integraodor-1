from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from reviews.models import Reviews
from .models import *
from openai import OpenAI
import os
from dotenv import load_dotenv
import time
from datetime import datetime
from django.utils import timezone

def top_250_cities(request):
    # Obtener las mejores 250 ciudades basadas en la calificación
    top_cities = City.objects.order_by('-rate')[:250]
    return render(request, 'top_250.html', {'top_cities': top_cities})

def home(request):
    searchTerm=request.GET.get('searchCity')
    if searchTerm:
        cities = City.objects.filter(name__icontains=searchTerm)
    else:  
        cities=City.objects.all()
    cities = cities.order_by('-rate')
    return render(request, 'home.html', {'searchTerm': searchTerm, 'cities': cities})

def city(request):
    searchTerm = request.GET.get('searchCity')
    rating = request.GET.get('rating')
    sort = request.GET.get('sort')
    country = request.GET.get('country')
    
    # Obtener todas las ciudades inicialmente
    cities = City.objects.all()

    # Filtrar por nombre si se proporciona un término de búsqueda
    if searchTerm:
        cities = cities.filter(name__icontains=searchTerm)

    # Filtrar por país
    if country:
        cities = cities.filter(country=country)

    # Filtrar por calificación
    if rating:
        if rating == 'high':
            cities = cities.filter(rate__gte=8)
        elif rating == 'medium':
            cities = cities.filter(rate__gte=4, rate__lt=6)
        elif rating == 'low':
            cities = cities.filter(rate__lt=4)

    # Diccionario de opciones de ordenamiento
    sort_options = {
        'name-asc': 'name',
        'name-desc': '-name',
        'rate-asc': 'rate',
        'rate-desc': '-rate',
        'country-asc': 'country',
        'country-desc': '-country'
    }

    # Aplicar la ordenación si 'sort' es válido
    if sort in sort_options:
        cities = cities.order_by(sort_options[sort])
    
    # Obtener la lista de países distintos
    countries = City.objects.values_list('country', flat=True).distinct()

    # Renderizar la plantilla con los datos de las ciudades
    return render(request, 'city.html', {'searchTerm': searchTerm, 'cities': cities, 'countries': countries})

def top_cities_view(request):
    searchTerm = request.GET.get('searchCity', '').strip()  # Usa el mismo nombre que el del formulario
    
    top_cities = City.objects.order_by('-rate')[:250]
    
    # Filtrar las ciudades según el término de búsqueda
    if searchTerm:
        top_cities = [city for city in top_cities if searchTerm.lower() in city.name.lower()]


    

    context = {
        'top_cities': top_cities,
        'searchTerm': searchTerm,
    }
    
    return render(request, 'top_250.html', context)

def city_reviews(request, city_name):
    city = get_object_or_404(City, name=city_name)
    reviews = Reviews.objects.filter(city=city.name)

    context = {
        'city': city,
        'reviews': reviews
    }
    
    return render(request, 'city_reviews.html', context)

def city_of_the_day(request):
    load_dotenv(".env")
    api_key = os.getenv("openai_apikey")
    client = OpenAI(api_key=api_key)
    today = datetime.now().date()

    # Verificar si ya hay una recomendación para hoy
    recommendation = CityRecommendation.objects.filter(date=today).first()
    if recommendation:
        city = recommendation.city
    else:
        try:
            # Solicitar la ciudad a OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  
                messages=[
                    {"role": "user", "content": "Dime una ciudad donde haya un evento o celebración hoy en Colombia (SOLO EL NOMBRE DE LA CIUDAD, SIN TILDES Y CON LA PRIMERA EN MAYUSCULA)."}
                ]
            )
            
            # Procesar la respuesta de OpenAI
            city_name = response.choices[0].message.content.strip()
            print(f"Ciudad recomendada por ChatGPT: {city_name}")

            # Buscar la ciudad en la base de datos
            city = City.objects.get(name=city_name)
            
            # Guardar la recomendación del día
            CityRecommendation.objects.create(city=city, date=today)
        except City.DoesNotExist:
            return HttpResponse(f"La ciudad recomendada por OpenAI ({city_name}) no existe en la base de datos.")

    # Renderizar la ciudad del día
    return render(request, 'city_of_the_day.html', {'city': city})
