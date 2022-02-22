from urllib import request
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from RapidReact_Scouting_App.models import Team

# Create your views here.
def index(request):
    model = Team
    