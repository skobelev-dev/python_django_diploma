from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
from django.core.files import File
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from media.models import Avatar
from my_auth.models import Profile
from my_auth.serializers import ProfileSerializer, PasswordSerializer


class ProfileViewSet(ViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def list(self, request):

        response = []
        for profile in self.queryset:
            full_name = profile.user.username
            email = profile.user.email
            phone = str(profile.phone)
            image = profile.user.avatar.image
            src = "" if not image else image.url or ""
            avatar = {"src": src, "alt": profile.user.avatar.alt}
            serialized = ProfileSerializer(
                data={
                    "fullName": full_name,
                    "email": email,
                    "phone": phone,
                    "avatar": avatar,
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

    @action(detail=False, methods=["post"], serializer_class=PasswordSerializer)
    def password(self, request):
        serialized = PasswordSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        user = self.request.user
        if user.is_authenticated and user.check_password(serialized.data.get("currentPassword")):
            user.set_password(serialized.data.get("newPassword"))
            return Response({"msg": "password has changed successfully"}, status=200)

        return Response({"msg": "bad request"}, status=400)

    @action(detail=False, methods=["post"])
    def avatar(self, request: Request):
        file: File = request.FILES["avatar"]
        user: AbstractBaseUser= request.user
        new_avatar = Avatar(alt="", image=file)
        new_avatar.save()
        if user.is_authenticated:
            user: User
            user.avatar = new_avatar
            user.save()
        return Response({"msg": "avatar has changed successfully"}, status=200)
