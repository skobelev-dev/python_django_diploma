# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from my_auth.models import Profile
from my_auth.serializers import ProfileSerializer


class ProfileViewSet(ViewSet):
    """
    Получение списка тегов.
    """

    queryset = Profile.objects.all()


    def list(self, request):
        profiles = self.queryset
        count = profiles.count()
        many = True if count > 1 else False
        serializer = ProfileSerializer(profiles, many=many)
        return Response(serializer.data)