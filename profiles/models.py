from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_type = models.CharField(max_length=20, default='', blank=True)
    default_phone_number = models.CharField(
        max_length=20, default='', blank=True
        )
    default_street_address = models.CharField(
        max_length=80, default='', blank=True
        )
    default_town_or_city = models.CharField(
        max_length=40, default='', blank=True
        )
    default_county = models.CharField(max_length=30, default='', blank=True)
    default_postcode = models.CharField(max_length=20, default='', blank=True)
    default_country = CountryField(
        blank_label='Country *', null=True, blank=True
        )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
