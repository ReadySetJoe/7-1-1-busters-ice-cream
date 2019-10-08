import datetime
from django.db import models
from django.utils import timezone


class IceCream(models.Model):
    flavor = models.CharField(max_length=200)
    featured = models.BooleanField()
    base = models.CharField(max_length=20, choices=[    
      ('vanilla', 'Vanilla'),
      ('chocolate', 'Chocolate'),
      ])
    available = models.CharField(max_length=20, choices=[
      ('daily','Daily'),
      ('weekly','Weekly'),
      ('seasonal','Seasonal'),
      ])
    date_churned = models.DateTimeField('date published',default=timezone.now())
    score = models.IntegerField(default=0)

    def __str__(self):
      return self.flavor
    
    def isFresh(self):
      return self.date_churned >= timezone.now() - datetime.timedelta(days=0)