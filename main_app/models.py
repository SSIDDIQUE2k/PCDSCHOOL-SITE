from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    grade= models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    subject = models.IntegerField()

    # new code below
    def __str__(self):
        return self.name
