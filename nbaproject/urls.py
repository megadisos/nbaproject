from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path("details/<str:name>/<str:last>",views.details,name="details"),
    path("matches/",views.matches,name="matches"),
    path("get_matches/",views.get_matches,name="get_matches"),
    path("org/<str:value>",views.organizer,name="organizer"),
]
