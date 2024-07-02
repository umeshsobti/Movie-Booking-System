from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Tickets
from datetime import datetime

def main(request):
    selected_date = request.GET.get('date', datetime.now().date())
    booked_date = Tickets.objects.filter(booking_date=selected_date).values_list('number', flat=True)
    return render(request, 'index.html', {'current_date': selected_date, 'booked_date': booked_date})
 
def save_movie(request):
    if request.method == "POST":
        person_name = request.POST.get('person_name')
        contact_number = request.POST.get('contact_number')
        no_of_tickets = request.POST.get('no_of_tickets')
        ticket_number = request.POST.getlist('selected_tickets')
        booking_date = request.POST.get('booking_date')
        movie = Movie(
            title="Movie Name",
            person_name=person_name, 
            no_of_tickets=no_of_tickets, 
            contact_number=contact_number
        )
        movie.save()
        
        for seat_number in ticket_number:
            Tickets.objects.create(movie=movie, number=seat_number,booking_date =booking_date)
        
        last_movie = Movie.objects.last()
        print(last_movie,'last_movie')
        ticket_details = last_movie.tickets.all()
        print(ticket_details,'ticket_details')
        return render(request, 'details.html', {'movies_data': last_movie, 'ticket_details': ticket_details})
    
    return render(request, 'details.html')
