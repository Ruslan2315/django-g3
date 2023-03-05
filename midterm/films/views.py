from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from films.models import Film
from films.serializers import FilmsSerializer
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def employees_handler(request):
    if request.method == 'GET':
        categories = Film.objects.all()
        serializer = FilmsSerializer(categories, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = FilmsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)


def get_employee_list(pk):
    try:
        film = Film.objects.get(id=pk)
        return {
            'status': 200,
            'film': film
        }
    except Film.DoesNotExist as e:
        return {
            'status': 404,
            'film': None
        }


@csrf_exempt
def employee_handler(request, pk):
    result = get_employee_list(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'Film not found'}, status=404)

    film = result['film']

    if request.method == 'GET':
        serializer = FilmsSerializer(film)
        return JsonResponse(serializer.data, status=200)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = FilmsSerializer(data=data, instance=film)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data=serializer.errors, status=400)
    if request.method == 'DELETE':
        film.delete()
        return JsonResponse({'message': 'Film deleted successfully!'})
    return JsonResponse({'message': 'Request is not supported'}, status=400)
