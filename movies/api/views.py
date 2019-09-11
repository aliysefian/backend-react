from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from movies import serializers
from movies.api.serializer import MovieSerializer
from movies.models import MovieModel


class MovieApiView(ListAPIView):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer


class MovieDetailApiView(RetrieveAPIView):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer


class MovieUpdateApiView(UpdateAPIView):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer


class MovieDeleteApiView(DestroyAPIView):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer


class MovieCreateApiView(CreateAPIView):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer
