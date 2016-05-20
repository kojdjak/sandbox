from django.db import models


class House(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=1024, blank=True)
