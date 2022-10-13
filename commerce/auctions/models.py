from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    startprice = models.IntegerField()

    def __str__(self):
        return f"{self.title} in {self.category}"

#ID description!, buyitnow, userposting, date posted, expires?

#ToDo: Bids and Comments on bids
