from email.policy import default
from django.db import models


class Countries(models.Model):
    name = models.CharField(max_length=50, null=False, default='')
    capital = models.CharField(max_length=50, null=False, default='')
    
    class Meta:
        ordering = ('id',)
