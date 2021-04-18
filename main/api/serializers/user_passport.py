from rest_framework.serializers import ModelSerializer
from main.passport.models import Passport
from main.user.models import UserInformation
from main.api.serializers.user_information import UserInformationSerializer


class UserPassportSerializer(ModelSerializer):
    class Meta:
        model = Passport
        exclude = ('user',)


class CreateUserPasswordInformationSerializer(ModelSerializer):
    user_information = UserInformationSerializer()

    class Meta:
        model = Passport
        fields = ('scan_file', 'document_number', 'first_name', 'last_name', 'patronymic', 'nationality', 'birth_date',
                  'personal_number', 'gender', 'issue_date', 'expire_date', 'issuing_authority', 'user_information',)

    def create(self, validated_data):
        user = self.context['request'].user
        user_information_data = validated_data.pop('user_information')
        user_information = UserInformation.objects.filter(user=user).first()

        if not user_information:
            user_information = UserInformation.objects.create(user=user, **user_information_data)

        passport = Passport.objects.create(user=user, user_information=user_information, **validated_data)

        return passport
