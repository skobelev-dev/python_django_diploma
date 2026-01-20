# from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet
from django.db.models import F

from media.models import Avatar
from my_auth.models import Profile
from my_auth.serializers import MyProfileSerializer, ProfileSerializer


class ProfileViewSet(ViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def list(self, request):

        response = []
        for profile in self.queryset:
            fullName = profile.user.username
            email = profile.user.email
            phone = str(profile.phone)
            image =  profile.user.avatar.image
            src = "" if not image else image.url or ""
            avatar = {
                "src": src,
                "alt": profile.user.avatar.alt
            }
            serialized = MyProfileSerializer(
                data={
                    "fullName": fullName,
                    "email": email,
                    "phone": phone,
                    "avatar": avatar
                }
            )
            serialized.is_valid(raise_exception=True)
            response.append(serialized.data)

        return Response(response)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        user = User(username=data.get("fullName"), email=data.get("email"))
        user.save()
        profile = Profile(phone=data.get("phone"), user=user)
        profile.save()
        avatar = Avatar(alt=data["avatar"].get("alt"), user=user)
        avatar.save()
        return Response(serializer.data)
