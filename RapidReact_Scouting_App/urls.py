from django.urls import path
from . import views


app_name = 'RapidReact_Scouting_App'
urlpatterns = [
    path('', views.index, name='index'),
]