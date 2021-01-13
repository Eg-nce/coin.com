from django.db import models


class data_loader(models.Model):
    date = models.DateField()
    close = models.FloatField()
    opens= models.FloatField()
    objects = models.Manager()
    
 

class values(models.Model):
    data = models.ManyToManyField(data_loader )
    name =  models.CharField(max_length=30)
    objects = models.Manager()
    def __str__(self):
        return self.name
        








       