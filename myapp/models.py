from django.db import models
import datetime
class Movie(models.Model):
    title = models.CharField(max_length=255)
    person_name = models.CharField(max_length=255)
    no_of_tickets = models.IntegerField(null=True)
    contact_number = models.IntegerField(null=True)
    date = models.DateField(auto_now_add=True)

class Tickets(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='tickets') 
    number = models.CharField(max_length=20, null=True)
    booking_date = models.DateField(default=datetime.date.today)
