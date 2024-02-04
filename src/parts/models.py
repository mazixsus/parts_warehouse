from django.db import models
from hashid_field import HashidAutoField

LOCATION_OPTION = [
    ("room", "Room"),
    ("bookcase", "Bookcase"),
    ("shelf", "Self"),
    ("cuvette", "Cuvette"),
    ("column", "Column"),
    ("row", "Row"),
]

# Create your models here.
class Parts(models.Model):
    id = HashidAutoField(primary_key=True, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price= models.FloatField(decimal_places=2)
    location=models.ArrayField(
        models.CharField(max_length=20, choices=PROFIT_OPTIONS),
        size=len(PROFIT_OPTIONS),
    )