from django.db import models

# Create your models here.
class Vote(models.Model):
    voteID = models.IntegerField()
    userID = models.IntegerField()
    healthCardID = models.IntegerField()
    sessionID = models.IntegerField()
    voteColour = models.CharField(max_length=5)
    ProgressNote = models.CharField(max_length=255)
    Timestamp = models.DateTimeField( db_comment="Date and time when the user voted",)
    
class Team(models.Model):
    teamID = models.Field.primary_key=True
    Name = models.CharField(max_length=30)
    departmentID = models.IntegerField()
    teamLeadID = models.IntegerField()