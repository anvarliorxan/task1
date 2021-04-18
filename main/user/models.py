from django.db import models
from django.contrib.auth.models import User

class UserInformation(models.Model):
    class Meta:
        verbose_name = 'UserInformation'
        verbose_name_plural = 'UserInformations'

    id          = models.AutoField(primary_key=True)
    user        = models.OneToOneField(User, verbose_name="User", on_delete=models.CASCADE)
    name        = models.CharField(verbose_name='Name', max_length=40)
    surname     = models.CharField(verbose_name='Surname', max_length=40)
    phone       = models.CharField(verbose_name='Phone', max_length=15)
    email       = models.EmailField()
