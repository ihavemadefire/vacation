from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=250)
    location = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Trip(models.Model):
    name = models.CharField(max_length=250)
    desinations = models.ManyToManyField(Destination)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.nameccc


class Post(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=300)
    created = models.DateField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title