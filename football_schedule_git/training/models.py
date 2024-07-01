from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.
class User(AbstractUser):
    is_coach = models.BooleanField(default = False)
    club = models.ForeignKey('Club', on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    time_zone = models.CharField(max_length = 64, blank = False, null= False, default="UTC")
    def __str__(self):
        if self.is_superuser:
            return "admin"
        return f"{self.first_name} {self.last_name}"


    
class Club(models.Model):
    name = models.CharField(max_length = 64, blank = False)
    coach = models.OneToOneField(User, on_delete=models.SET_NULL, null=True ,blank=True, related_name='coach_club', limit_choices_to={'is_coach': True})
    club_api_id = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Drill(models.Model):
    name = models.CharField(max_length = 64, blank = False, null= False)
    description = models.TextField(blank = False, null=False)
    coach = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None, limit_choices_to={'is_coach': True})
    video_url = models.URLField(blank = True)
    def __str__(self):
        return self.name
    
class Calendar(models.Model):
    club = models.OneToOneField('Club', on_delete=models.CASCADE, related_name='calendar')

    def __str__(self):
        return f"{self.club.name} Calendar"
    

class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('Training', 'Training'),
        ('Recovery', 'Recovery'),
        ('Match', 'Match'),
    ]

    calendar = models.ForeignKey(Calendar, blank=False, on_delete=models.CASCADE, related_name='events')
    drills = models.ManyToManyField(Drill, blank=True, related_name='drill_on_training')
    title = models.CharField(max_length=100, blank=False)
    event_type = models.CharField(max_length=20, blank=False , choices=EVENT_TYPE_CHOICES)
    date_time = models.DateTimeField(blank=False, null=True)
    description = models.TextField(blank=True)

    #for matches only
    match_id = models.IntegerField(blank=True, null=True)
    match_type = models.TextField(blank=True,null=True)
    match_competition = models.TextField(blank=True)
    competition_emblem = models.URLField(blank=True)
    match_matchday = models.IntegerField(blank=True, null=True)
    home_team_name = models.TextField(blank=True,null=True)
    home_team_crest = models.URLField(blank=True, null=True)
    home_team_goals = models.IntegerField(blank=True, null=True)
    away_team_name = models.TextField(blank=True,null=True)
    away_team_crest = models.URLField(blank=True, null=True)
    away_team_goals = models.IntegerField(blank=True, null=True)
    matchday = models.IntegerField(blank=True, null=True)
    stage = models.TextField(blank=True,null=True)
    status = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title}"
    
    
    
