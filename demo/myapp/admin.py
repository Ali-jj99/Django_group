from django.contrib import admin
from .models import Vote, Team, Department, Session, User
#this adds the database to the admin page 

admin.site.register(Vote)
admin.site.register(Team)
admin.site.register(Department)
admin.site.register(Session)
admin.site.register(User)