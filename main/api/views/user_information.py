from rest_framework import serializers

from main.api.serializers.user_information import UserInformationSerializer
from main.user.models import UserInformation
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated


class UpdateUserInformationView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserInformation.objects.all()
    serializer_class = UserInformationSerializer





