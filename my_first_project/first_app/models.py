from django.db import models

# Create your models here.
class musician(models.Model):
    #id =models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True) #<input required>
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

class album(models.Model):
    # id =models.AutoField(primary_key=True)
    artist = models.ForeignKey(musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    # <select>
    #<option value='1'>Worst</option>
    rating =(
        (1, "worst"),
        (2, "Bad"),
        (3,"not Bad"),
        (4, "Good"),
        (5, "excellent !"),
    )
    num_starts = models.IntegerField(choices=rating)

    def __str__(self):
        return self.name+ ", Rating:" + str(self.num_starts)


