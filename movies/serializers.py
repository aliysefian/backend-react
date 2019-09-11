from rest_framework import serializers

from generes.models import Geners
from movies.models import MovieModel
class GeneresSerializer(serializers.ModelSerializer):
    # ss= serializers.RelatedField(many=False, read_only=True)
    class Meta:
        model = Geners 
        fields = ('id', 'name')

class MovieSerializer(serializers.ModelSerializer):
    # ss= serializers.RelatedField(many=False, read_only=True)
    genere=GeneresSerializer(many=False)
    class Meta:
        model = MovieModel
        fields = ('id', 'title', 'genere', 'publish_date', 'rate', 'number_in_stock', 'liked')
