from django.db import models
from django.contrib.auth.models import User
from main.user.models import UserInformation

class Passport(models.Model):
    class Meta:
        verbose_name = 'Passport'
        verbose_name_plural = 'Passports'

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    id                  = models.AutoField(primary_key=True)
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    user_information    = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    scan_file           = models.FileField(upload_to='passport')
    document_number     = models.CharField(max_length=40)
    first_name          = models.CharField(max_length=40)
    last_name           = models.CharField(max_length=40)
    patronymic          = models.CharField(max_length=40)
    nationality         = models.CharField(max_length=40)
    birth_date          = models.DateField()
    personal_number     = models.IntegerField()
    gender              = models.CharField(max_length=1, choices=GENDER_CHOICES)
    issue_date          = models.DateField()
    expire_date         = models.DateField()
    issuing_authority   = models.CharField(max_length=40)
