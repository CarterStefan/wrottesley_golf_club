from django.db import models

# Create your models here.


class Tournament(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    start_date = models.CharField(max_length=254, null=True, blank=True)
    start_time = models.CharField(max_length=254, null=True, blank=True)
    location = models.CharField(max_length=254, null=True, blank=True)
    entry_fee = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name