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