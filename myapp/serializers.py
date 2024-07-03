from rest_framework import serializers
from .models import Tickets

class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ['number','booking_date']
    