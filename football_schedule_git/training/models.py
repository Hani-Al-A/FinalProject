from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.
class User(AbstractUser):
    is_coach = models.BooleanField(default = False)
    club = models.ForeignKey('Club', on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    def __str__(self):
        if self.is_superuser:
            return "admin"
        elif self.is_coach:
            return f"{self.first_name} {self.last_name} coaches {self.club}"
        else:
            return f"{self.first_name} {self.last_name} plays for {self.club}"

    
class Club(models.Model):
    name = models.CharField(max_length = 64, blank = False)
    coach = models.OneToOneField(User, on_delete=models.SET_NULL, null=True ,blank=True, related_name='coach_club', limit_choices_to={'is_coach': True})
    def __str__(self):
        if self.coach:
            return f"{self.name}"
        else:
            return f"{self.name} needs a coach"

class Drill(models.Model):
    name = models.CharField(max_length = 64, blank = False)
    description = models.TextField(blank = False)
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
        ('Rest', 'Rest'),
        ('Recovery', 'Recovery'),
        ('Match', 'Match'),
    ]

    calendar = models.ForeignKey(Calendar, blank=False, on_delete=models.CASCADE, related_name='events')
    drills = models.ManyToManyField(Drill, blank=True, null=True, related_name='drill_on_training')
    title = models.CharField(max_length=100, blank=False)
    event_type = models.CharField(max_length=20, blank=False ,choices=EVENT_TYPE_CHOICES)
    date = models.DateField(blank=False)
    start_time = models.TimeField(blank=False)
    end_time = models.TimeField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} on {self.date}"
    
    
    
