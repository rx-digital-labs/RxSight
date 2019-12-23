from django.db import models

# Create your models here.

class surgery(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')

'''
    class Meta:
         managed = True
         db_table = 'rxsight\".\"surgery'
'''
class manpower(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    type = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=100,decimal_places=2)
    available = models.BooleanField(default=True)
