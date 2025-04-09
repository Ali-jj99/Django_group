from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "team_summary.html")

def login_view(request):
    return render(request, "log_in.html")