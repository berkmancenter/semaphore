"""API Serializers & Views"""

from . import models
from rest_framework import serializers, viewsets


# Serializers define the API representation.
class BazSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Baz
        fields = ['id', 'url', 'foo', 'bar']


# ViewSets define the view behavior.
class BazViewSet(viewsets.ModelViewSet):
    queryset = models.Baz.objects.all()
    serializer_class = BazSerializer
