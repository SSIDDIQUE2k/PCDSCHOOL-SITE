from django.db import models
from django.urls import reverse
# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    grade= models.IntegerField()
    description = models.TextField(max_length=250)
    subject = models.CharField(max_length=100)

    # new code below
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this animal's details
        return reverse('educators')
