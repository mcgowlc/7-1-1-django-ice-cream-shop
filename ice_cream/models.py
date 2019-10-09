from django.db import models
from django.urls import reverse
from django.db.models import CharField


class IceCream(models.Model):

    VANILLA = 'vanilla'
    CHOCOLATE = 'chocolate'

    DAILY = 'daily'
    WEEKLY = 'weekly'
    SEASONAL = 'seasonal'
    FEATURED = 'featured'

    BASES = [(VANILLA, 'vanilla'), (CHOCOLATE, 'chocolate')]
    FEATURED = [(DAILY, 'daily'), (WEEKLY, 'weekly'), (SEASONAL, 'seasonal'), (FEATURED, 'featured')]

    flavor = models.CharField(max_length=255)
    base = models.CharField(max_length=255, choices=BASES)
    available = models.CharField(max_length=255, choices=FEATURED)
    featured = models.BooleanField()
    date_churned = models.DateField()
    url = models.TextField(null=True)

    def __str__(self):
        return self.flavor[:15]

    def get_absolute_url(self):
        return reverse('home')
