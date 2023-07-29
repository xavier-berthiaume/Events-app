from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.shortcuts import render, redirect
from .models import Event, Venue
from .forms import VenueForm, EventForm
from datetime import datetime
from calendar import HTMLCalendar

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

import calendar
import csv
import io


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
    event_list = Event.objects.all().order_by('event_date', 'venue')
    context = {
        'event_list': event_list,
    }

    return render(request, 'events/event_list.html', context)


def add_event(request, *args, **kwargs):
    submitted = False

    context = {}

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    context['form'] = form
    context['submitted'] = submitted

    return render(request, 'events/add_event.html', context)


def update_event(request, event_id, *args, **kwargs):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)

    if form.is_valid():
        form.save()
        return redirect('events-list')

    context = {
        'event': event,
        'form': form,
    }

    return render(request, 'events/update_event.html', context)


def delete_event(request, event_id, *args, **kwargs):
    event = Event.objects.get(pk=event_id)
    event.delete()

    context = {

    }

    return redirect('events-list')


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

    else:
        return render(request, 'events/search_venue.html', {})

    context = {
        "search_term": search_term,
        "venues": found_venues
    }

    return render(request, 'events/search_venue.html', context)


def update_venue(request, venue_id, *args, **kwargs):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)

    if form.is_valid():
        form.save()
        return redirect('list-venue')

    context = {
        'venue': venue,
        'form': form
    }

    return render(request, 'events/update_venue.html', context)


def delete_venue(request, venue_id, *args, **kwargs):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()

    context = {

    }

    return redirect('list-venue')


def venue_text(request):
    response = HttpResponse(content_type="text/plain")
    response['Content-Disposition'] = 'attachment; filename=venues.txt'

    venues = Venue.objects.all()

    lines = []

    for venue in venues:
        lines.append(f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n')

    response.writelines(lines)
    return response


def venue_csv(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=venues.csv'

    writer = csv.writer(response)

    venues = Venue.objects.all()

    writer.writerow(['Venue Name', 'Address', 'Zip Code', 'Phone Number', 'Web Address', 'Email'])

    for venue in venues:
        writer.writerow([venue.name, venue.address, venue.zip_code, venue.phone, venue.web, venue.email_address])

    return response
