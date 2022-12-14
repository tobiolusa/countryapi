from email.policy import default
from django.db import models


class Countries(models.Model):
    name = models.CharField(max_length=50, null=False, default='')
    capital = models.CharField(max_length=50, null=False, default='')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('id',)
