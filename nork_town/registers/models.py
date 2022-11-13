from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    cpf = models.CharField(max_length=50)
    sale_oportunity = models.BooleanField()

    def __str__(self):
        return self.name

    def get_cars(self):
        try:
            return self.car_set.all()
        except:
            return None


class Car(models.Model):
    vehicle_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)


    def __str__(self):
        return self.vehicle_name

    class Meta:
        ordering = ['vehicle_name']