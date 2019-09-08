from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser

from movies.models import MovieModel
# Create your views here.
from movies.serializers import MovieSerializer


def aliView(request):
    ss = MovieModel.objects.all()
    print(ss)
    return render(request, 'ali.html', {"data": ss})


def movie_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = MovieModel.objects.all()
        serializer = MovieSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
