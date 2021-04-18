from rest_framework.serializers import ModelSerializer
from main.user.models import UserInformation


class UserInformationSerializer(ModelSerializer):
    class Meta:
        model = UserInformation
        exclude = ('user',)

