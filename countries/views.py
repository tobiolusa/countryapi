from itertools import count
from django.shortcuts import render
from django.http.response import JsonResponse
from requests import request
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib import messages


from countries.models import Countries
from countries.serializers import CountriesSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def countries_list(requests):
    if requests.method == 'GET':
        countries = Countries.objects.all()        
        name = requests.GET.get('name', None)
        if name is not None:
            countries = Countries.filter(name__icontans=name)
            
        countries_serializer = CountriesSerializer(countries, many=True)
        return JsonResponse(countries_serializer.data, safe=False)
    
    elif requests.method == 'POST':
        countries_data = JSONParser().parse(request)
        countries_serializer = CountriesSerializer(data=countries_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(countries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'POST', 'DELETE'])
def countries_details(requests, pk):
    try:
        countries = countries.objects.get(pk=pk)
    except countries.DoesNotExist:
        return JsonResponse({'message': 'The country do not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        countries_serializer = CountriesSerializer(countries)
        return JsonResponse(countries_serializer.data)
    
    elif request.method == 'PUT':
        countries_data = JSONParser().parse(request)
        countries_serializer = CountriesSerializer(countries, data=countries_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data)
        return JsonResponse(countries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'DELETE':
        countries.delete()
        return JsonResponse({'message':'Country was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        
    