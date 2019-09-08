from django.db import models

from generes.models import Geners


class MovieModel(models.Model):

    title = models.CharField(max_length=100)
    genere = models.ForeignKey(
        Geners, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    number_in_stock = models.IntegerField()
    rate = models.IntegerField()
    liked = models.BooleanField(default=False)
