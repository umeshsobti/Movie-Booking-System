from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Movie
from.models import Tickets
from datetime import datetime
def main(request):
    current_date = datetime.now()
    return render(request,'index.html',{'current_date': current_date})

def save_movie(request):
    if request.method == "POST":
        person_name = request.POST.get('person_name')
        contact_number = request.POST.get('contact_number')
        no_of_tickets = request.POST.get('no_of_tickets')
        ticket_number = request.POST.getlist('selected_tickets')
        
        movie = Movie(title = "Movie Name",person_name=person_name, no_of_tickets = no_of_tickets, contact_number=contact_number)
        movie.save()
        
        for seat_number in ticket_number:
            Tickets.objects.create(movie=movie, number=seat_number)
        movies_data = Movie.objects.all()
        
        all_tickets = Tickets.objects.all()

        # Extract numbers from each ticket
        booked_tickets = [ticket.number for ticket in all_tickets]

        return render(request, 'index.html', {'booked_tickets': list(booked_tickets)}) 
    
    return render(request, 'details.html')