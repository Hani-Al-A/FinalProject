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
    path("schedule/<int:month_num>/<int:year>/add_event", views.add_event, name="add_event"),
    path('day_details/<int:day>/<int:month>/<int:year>', views.day_details, name='day_details'),
    path('test', views.fetch_competitions, name='fetch_competitions'),
    path('test/get_teams/<int:competition_id>/<str:competition_name>', views.get_teams, name='get_teams'),

    


]