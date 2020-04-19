"""API Serializers & Views"""

from . import models
from rest_framework import serializers, viewsets


# Serializers define the API representation.
class RawFlagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RawFlag
        fields = [
            'id',
            'url',
            'reported_user_id',
            'reported_tweet_id',
            'language',
        ]


# ViewSets define the view behavior.
class RawFlagViewSet(viewsets.ModelViewSet):
    queryset = models.RawFlag.objects.all()
    serializer_class = RawFlagSerializer
