from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=10000,blank=True,null=True)
    timelimit = models.CharField(max_length=300,blank=True,null=True)
    datecreated = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name
