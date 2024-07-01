from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("drill_library", views.drill_library, name="drill_library"),
    path("drill_library/create_drill", views.create_drill, name="create_drill"),
    path("drill/<int:drill_id>", views.drill_view, name="drill_view"),
    path("schedule/<int:month_num>/<int:year>", views.schedule, name="schedule"),
    path("schedule/add_event", views.add_event, name="add_event"),
    path("schedule/sync_calendar/<int:team_id>", views.sync_calendar, name="sync_calendar"),
    path('day_details/<int:day>/<int:month>/<int:year>', views.day_details, name='day_details'),
    path('day_details/<int:day>/<int:month>/<int:year>/delete_event/<int:event_id>', views.delete_event, name="delete_event"),
    path('reminder', views.event_reminder, name="event_reminder"),
    path('schedule/update_timezone', views.update_timezone, name="update_timezone"),

]