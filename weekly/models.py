from django.db import models
from colorfield.fields import ColorField

# Create your models here.

DAY_CHOICES = (("saturday", "Saturday"), ("sunday", "Sunday"),("monday", "Monday"), ("tuesday", "Tuesday"), ("wensday", "Wensday"), ("thursday", "Thursday"), ("friday", "Friday"))

TIME_CHOICES = (("9-10:30", "9-10:30"), ("10:30-12", "10:30-12"), ("13-15", "13-15"), ("15-17", "15-17"), ("17-19", "17-19"))

class Object(models.Model):

    title = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=500)
    day = models.CharField(default="saturday", choices=DAY_CHOICES, max_length=200)
    time = models.CharField(default="9-10:30", choices=TIME_CHOICES, max_length=200)
    color = ColorField(default='#FFFF00', null=True)
    
    def __str__(self):
        return self.title


