from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from requests import Response

from main.api.serializers.user_passport import UserPassportSerializer,CreateUserPasswordInformationSerializer
from main.passport.models import Passport
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated



class CreateUserPassportInformation(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Passport.objects.all()
    serializer_class = CreateUserPasswordInformationSerializer



class ListUserPassport(generics.ListAPIView):
    queryset = Passport.objects.all()
    serializer_class = UserPassportSerializer



class UpdateUserPassport(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Passport.objects.all()
    serializer_class = UserPassportSerializer
    lookup_field = 'pk'