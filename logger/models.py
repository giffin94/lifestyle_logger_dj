from django.db import models
from django.conf import settings
from jsonfield import JSONField

# Create your models here.


class Log(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    date_for = models.DateTimeField()
    sleep_start = models.CharField(max_length=200)
    sleep_end = models.CharField(max_length=200)
    exercise = JSONField()
    nutrition = JSONField()
