from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Movie
from datetime import datetime
def main(request):
    current_date = datetime.now()
    return render(request,'index.html',{'current_date': current_date})

def save_movie(request):
    if request.method == "POST":
        person_name = request.POST.get('person_name')
        contact_number = request.POST.get('contact_number')
        no_of_tickets = request.POST.get('no_of_tickets')
        
        movie = Movie(person_name=person_name, no_of_tickets = no_of_tickets, contact_number=contact_number)
        movie.save()
        
        movies_data = Movie.objects.all()
        
        return render(request, 'details.html', {'movie': movies_data}) 
    
    return render(request, 'details.html')