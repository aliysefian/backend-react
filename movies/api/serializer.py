from rest_framework import serializers

from generes import models
from movies.models import MovieModel
from movies.serializers import GeneresSerializer


class MovieSerializer(serializers.ModelSerializer):
    # genere = GeneresSerializer(many=False)

    class Meta:
        model = MovieModel
        fields = ('id', 'title', 'genere', 'publish_date', 'rate', 'number_in_stock', 'liked')
