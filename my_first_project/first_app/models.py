from django.db import models

# Create your models here.
class musician(models.Model):
    #id =models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class album(models.Model):
    # id =models.AutoField(primary_key=True)
    artist = models.ForeignKey(musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    num_starts = models.IntegerField()

def __str__(self):
    return self.first_name+ " " + self.last_name
