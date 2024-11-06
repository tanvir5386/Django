from django.db import models
from datetime import date 

# Create your models here.
class MOdelPractise(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(default='email')
    roll = models.IntegerField(primary_key=True, default=None)
    date = models.DateField(default=date.today)
    fathers_name = models.TextField(default=None, blank=True, null=True)
    date_time_field = models.DateTimeField(default=None)
    

    
    
    def __str__(self):
        return self.name
    