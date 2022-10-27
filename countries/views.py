from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from countries.models import Countries
from countries.serializers import CountriesSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def countries_list(requests):
    if requests.method == 'GET':
        countries = countries.objects.all()
        
        
        name = requests.GET.get('name', None)
        if name is not None:
            countries = countries.filter(name__icontans=name)
            
        countries_serializer = CountriesSerializer(countries, many=True)
        return JsonResponse(countries_serializer.data, safe=False)
