from django.db import models
from django.utils import timezone


class SubEmail(models.Model):
    FREQUENCY_CHOICE = [
        ('weekly', 'weekly'),
        ('monthly', 'monthly'),
    ]
    name = models.CharField(max_length=144)
    email = models.EmailField(max_length=254)
    sub_state = models.BooleanField(default=True)
    frequency = models.CharField(
        max_length=10, choices=FREQUENCY_CHOICE, default='weekly')
    last_sent = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name + ' | ' + self.email
