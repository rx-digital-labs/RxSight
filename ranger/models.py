from django.db import models

# Create your models here.

class surgery(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
    

'''
    class Meta:
         managed = True
         db_table = 'rxsight\".\"surgery'
         this is used for accesing a particular schema in database
'''
class manpower(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    type = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=100,decimal_places=2)
    available = models.BooleanField(default=True)

#-------------------------------------Report Layer------------------------------------------------------

class surR(models.Model):
    name = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(auto_now_add=True)

class ManR(models.Model):
    sid = models.IntegerField(models.ForeignKey(surgery,on_delete=models.CASCADE))
    name = models.CharField(max_length=100, null=True)
