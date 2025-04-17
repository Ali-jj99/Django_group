from django.shortcuts import render
#imports the database into the website
from .models import Vote, Team, Department, Session, User

# Create your views here.
def home(request):
    #this passes the Vote table into the html page
    all_votes = Vote.objects.all
    return render(request, "landing_page.html", {'vote' : all_votes})

def join(request):
    return render(request, "join.html", {})

def login_view(request):
    return render(request, "log_in.html")

def vote_view(request):
    return render(request, "voting_page.html")

def progress_view(request):
    return render(request, "progress_page.html")

def signup_view(request):
    return render(request, "sign_up.html")

def summary_view(request):
    return render(request, "team_summary.html")


