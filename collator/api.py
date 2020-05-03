"""API Serializers & Views"""

from . import models
from django.utils import timezone
from rest_framework import serializers, viewsets
from rest_framework import permissions

# Serializers define the API representation.
class RawFlagSerializer(serializers.HyperlinkedModelSerializer):

    flagger = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.RawFlag
        fields = [
            'id',
            'url',
            'flagger',
            'reported_user_id',
            'reported_tweet_id',
            'language',
        ]
        read_only_fields = [
            'created',
            'modified'
        ]


# ViewSets define the view behavior.
class RawFlagViewSet(viewsets.ModelViewSet):
    queryset = models.RawFlag.objects.all()
    serializer_class = RawFlagSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]