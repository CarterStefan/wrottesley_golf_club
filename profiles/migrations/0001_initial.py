# Generated by Django 3.1.6 on 2021-04-11 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_type', models.CharField(blank=True, default='', max_length=20)),
                ('default_phone_number', models.CharField(blank=True, default='', max_length=20)),
                ('default_street_address', models.CharField(blank=True, default='', max_length=80)),
                ('default_town_or_city', models.CharField(blank=True, default='', max_length=40)),
                ('default_county', models.CharField(blank=True, default='', max_length=30)),
                ('default_postcode', models.CharField(blank=True, default='', max_length=20)),
                ('default_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
