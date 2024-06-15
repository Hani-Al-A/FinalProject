from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
import calendar
from calendar import HTMLCalendar
from django.core.mail import send_mail
from datetime import datetime
from .forms import EventForm
import requests
import json



from .models import User, Club, Drill, Event, Calendar

# Create your views here.
def index(request):
    current_month = datetime.now().month
    current_year = datetime.now().year
    return render(request, 'training/index.html', {
        "month": current_month,
        "year": current_year,
    })

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "training/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "training/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        is_coach = request.POST["is_coach"] == 'True'
        if is_coach:
            club_name = request.POST["clubC"].upper()
        else:
            club_name = request.POST["clubP"].upper()

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "training/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.is_coach = is_coach
            user.save()
        
        except IntegrityError:
            return render(request, "training/register.html", {
                "message": "Username already taken."
            })
            
        # Check if club already exists
        try:
            club = Club.objects.get(name=club_name)
            if is_coach:
                if club.coach is None:
                    club.coach = user
                    club.save()
                    user.club = club
                    user.save()
                else:
                    User.objects.filter(username = user.username).delete()
                    return render(request, "training/register.html", {
                        "message": "There is already a coach for this club."
                    })
            else:
                user.club = club
                user.save()
                
        except Club.DoesNotExist:

            club = Club.objects.create(name=club_name, coach=user if is_coach else None)

            club.save()
            user.club = club
            user.save()
                
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "training/register.html")

@login_required
def drill_library(request):
    drills = Drill.objects.filter(coach = request.user)
    return render(request, 'training/drills.html', {
        "drills": drills
    })

@login_required
def create_drill(request):
    if request.method == "POST":
        if request.user.is_coach:
            drills = Drill.objects.filter(coach = request.user)
            drill_name = request.POST["drill_name"]
            description = request.POST["description"]
            coach = request.user
            drill_video = request.POST["drill_video"]
            drill = Drill.objects.create(name = drill_name, description = description, coach = coach, video_url = drill_video)
            drill.save()
        else:
            return render(request, 'training/drills.html', {
                "message": "You cannot add a drill as you are not a coach."
            })
    return HttpResponseRedirect(reverse('drill_library'))

def drill_view(request, drill_id):
    if len(Drill.objects.filter(pk=drill_id)) == 0:
        return render(request, 'training/drill.html', {
            "message": "This drill does not exist",
        })
    drill = Drill.objects.get(pk=drill_id)
    if (drill.coach == request.user) or (drill.coach.club == request.user.club): # if the user trying to access the drills is the coach or a player of the coach
        return render(request, 'training/drill.html', {
            "drill": drill,
        })
    else:
        return render(request, 'training/drills.html', {
            "message": "You do not have permission to view this drill"
        })
    

def schedule(request, month_num, year):
    clubOfUser = request.user.club
    calendarOfUser = Calendar.objects.get(club = clubOfUser)
    events = Event.objects.filter(date__year=year, date__month=month_num, calendar = calendarOfUser)
    cal = HTMLCalendar().formatmonth(year,month_num)
    form = EventForm()

    for event in events:
        href_redirect = reverse('day_details', args=[event.date.day, event.date.month, event.date.year])

        weekday_name = event.date.strftime('%A').lower()
        class_name = weekday_name[0:3]
        event_html = f'<div class="{event.event_type.lower()}"><a class="{event.event_type.lower()}_day" href={href_redirect}>{event.date.day}</a></div>'
        day_html = f'<td class="{class_name}">{event_html}</td>'
        cal = cal.replace(f'<td class="{class_name}">{event.date.day}</td>', day_html)
    return render(request, "training/schedule.html", {
        "cal": cal,
        "form": form,
    })

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('schedule', month_num=request.POST.get('date__month') , year=request.POST.get('date__year')))  # Redirect to the schedule view
    else:
        form = EventForm()
        return render(request, 'training/schedule.html', {'form': form})

def day_details(request, day, month, year):
    clubOfUser = request.user.club
    calendarOfUser = Calendar.objects.get(club = clubOfUser)
    month_name = list(calendar.month_name)[month]
    events = Event.objects.filter(date__year=year, date__month=month, date__day= day,calendar = calendarOfUser).order_by('start_time')
    
    return render(request, "training/day.html", {
            "events": events,
            "month_name": month_name,
            "day": day,
            "year": year,
        })

def fetch_competitions(request):
    uri = 'http://api.football-data.org/v4/competitions/'
    headers = { 'X-Auth-Token': '7fefad79448c4fefabdb4450b898e666' }

    response = requests.get(uri, headers=headers, allow_redirects=False)
    competitions = response.json()['competitions']
    return render(request, 'training/selectComp.html', {
        'competitions': competitions})

def get_teams(request, competition_id, competition_name):
    uri = f'http://api.football-data.org/v4/competitions/{competition_id}/teams'
    headers = { 'X-Auth-Token': '7fefad79448c4fefabdb4450b898e666' }
    response = requests.get(uri, headers=headers, allow_redirects=False)
    teams = response.json()['teams']
    return render(request, 'training/selectComp.html', {
        'teams': teams,
        "competition_name": competition_name,
        })


#for email sending use send_mail(subject, message, from_email, recipient_list) function, from_email will be my email, recipient list will be all the players in the club