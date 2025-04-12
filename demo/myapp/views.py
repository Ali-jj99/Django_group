from django.shortcuts import render
#imports the database into the website
from .models import Vote

# Create your views here.
def home(request):
    #this passes the Vote table into the html page
    all_votes = Vote.objects.all
    return render(request, "team_summary.html", {'vote' : all_votes})

def login_view(request):
    return render(request, "log_in.html")

def join(request):
    return render(request, "join.html", {})
