from __future__ import unicode_literals
from main.api.views.user_passport import ListUserPassport, UpdateUserPassport, CreateUserPassportInformation
from main.api.views.user_information import UpdateUserInformationView
from django.urls import path,include



app_name = 'api'

urlpatterns = [
    path('passport/', include(arg=[
        path('create/'           , view=CreateUserPassportInformation.as_view(), name='passport_create_view'),
        path('list/'           , view=ListUserPassport.as_view(), name='passport_list_view'),
        path('update/<int:pk>/', view=UpdateUserPassport.as_view(), name='passport_update_view'),
    ])),

    path('information/', include(arg=[
        path('update/<int:pk>/', view=UpdateUserInformationView.as_view(), name='information_update_view'),
    ])),

]
