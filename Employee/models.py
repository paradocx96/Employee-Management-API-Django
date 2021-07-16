from django.db import models
from datetime import datetime
from django.utils.timezone import now


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    create_date = models.DateTimeField(default=now, blank=True)

    class Meta:
        verbose_name_plural = 'employees'

    def __str__(self):
        return self.first_name
