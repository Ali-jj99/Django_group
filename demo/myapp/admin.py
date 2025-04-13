from django.contrib import admin
from .models import Vote, Team
#this adds the database to the admin page 

admin.site.register(Vote)
admin.site.register(Team)