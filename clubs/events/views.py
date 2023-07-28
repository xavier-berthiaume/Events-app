from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Event, Venue
from .forms import VenueForm
from datetime import datetime
from calendar import HTMLCalendar
import calendar

# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B'), *args, **kwargs):

    month = month.capitalize()
    month_numeral = list(calendar.month_name).index(month)
    month_numeral = int(month_numeral)

    cal = HTMLCalendar().formatmonth(year, month_numeral)

    now = datetime.now()
    current_year = now.year

    context = {
        "current_year": current_year,
        "year": year,
        "month": month,
        "cal": cal,
    }
    return render(request, 'events/home.html', context)


def all_events(request, *args, **kwargs):
    event_list = Event.objects.all()
    context = {
        'event_list': event_list,
    }

    return render(request, 'events/event_list.html', context)


def add_venue(request, *args, **kwargs):
    submitted = False

    context = {}

    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')

    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    context['form'] = form
    context['submitted'] = submitted

    return render(request, 'events/add_venue.html', context)


def list_venue(request, *args, **kwargs):
    venue_list = Venue.objects.all()

    context = {
        "venue_list": venue_list,
    }

    return render(request, 'events/venues.html', context)


def show_venue(request, venue_id, *args, **kwargs):

    venue = Venue.objects.get(pk = venue_id)

    context = {
        'venue': venue
    }

    return render(request, 'events/show_venue.html', context)

def search_venue(request, *arg, **kwargs):

    if request.method == "POST":
        search_term = request.POST["SearchBar"]
        found_venues = Venue.objects.filter(name__contains=search_term)

    context = {
        "search_term": search_term,
        "venues": found_venues
    }

    return render(request, 'events/search_venue.html', context)
