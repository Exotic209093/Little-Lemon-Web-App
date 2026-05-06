from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} : {self.price}'


class Booking(models.Model):
    name = models.CharField(max_length=200)
    no_of_guests = models.PositiveIntegerField()
    bookingdate = models.DateTimeField()

    class Meta:
        ordering = ['bookingdate']

    def __str__(self):
        return f'{self.name} ({self.no_of_guests}) @ {self.bookingdate:%Y-%m-%d %H:%M}'
