# Generated by Django 3.2 on 2021-04-18 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('surname', models.CharField(max_length=40, verbose_name='Surname')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'UserInformation',
                'verbose_name_plural': 'UserInformations',
            },
        ),
    ]
