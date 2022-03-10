from multiprocessing import context
from multiprocessing.synchronize import Event
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
import calendar
from calendar import HTMLCalendar, month_name
from datetime import datetime
from events.forms import EventForm, VenueForm
from events.models import Event, Venue

# Create calendar views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    context = {}
    month = month.capitalize()
    #change the month string to month number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    #get a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    #get current time
    now = datetime.now()
    time = now.strftime('%I:%M:%S %p')

    context = {
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "time": time,
    }


    return render(request, 'events/home.html', context)

# Create event_list views 
def all_events(request):
    context = {}
    event_list = Event.objects.all()
    context = {
        "event_list": event_list
    }
    return render(request, 'events/event_list.html', context)



# Create add event views
def add_event(request):
    context = {}
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_event.html', {"form": form, "submitted": submitted})


# Create update_event views
def update_event(request,event_id):
    context={}
    events = Event.objects.get(pk=event_id)
    if request.method == "POST":
        form = EventForm(request.POST,instance=events)
        if form.is_valid:
            form.save()
            return redirect('list-events')
    else:
        form = EventForm(instance=events)
        context = {
            "form": form
        }
        return render(request, 'events/update_event.html', context)

# Create all_venue views
def all_venues(request):
    context = {}
    venue_list = Venue.objects.all()
    context = {
        "venue_list": venue_list
    }
    return render(request, 'events/venue_list.html', context)

# Crate add_venue views
def add_venue(request):
    context = {}
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {"form": form, "submitted": submitted})

# Create show venue views
def show_venue(request, venue_id):
    context = {}
    venue = Venue.objects.get(pk=venue_id)
    context = {
        "venue": venue
    }
    return render(request, 'events/show_venue.html', context)

# Create search venue views 
def search_venues(request):
    context = {}
    if request.method == "POST":
        searched = request.POST["Searched"]
        venues = Venue.objects.filter(name__contains=searched)
        context = {
            "searched": searched,
            "venues": venues,
        }
        return render(request, 'events/search_venues.html', context)

    else: 
        return render(request, 'events/search_venues.html', context)


# Create update venue views
def update_venue(request, venue_id):
    context={}
    venues = Venue.objects.get(pk=venue_id)
    if request.method == "POST":
        form = VenueForm(request.POST,instance=venues)
        if form.is_valid:
            form.save()
            return redirect('list-venues')
    else:
        form = VenueForm(instance=venues)
        context = {
            "form": form
        }
        return render(request, 'events/update_venue.html', context)
