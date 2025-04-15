from django.db import models

# Create your models here
class Vote(models.Model):
    voteID = models.IntegerField(primary_key=True)
    userID = models.ForeignKey('User', on_delete=models.CASCADE, db_column='userID')
    healthCardID = models.ForeignKey('HealthCard', on_delete=models.CASCADE, db_column='healthCardID')
    sessionID = models.ForeignKey('Session', on_delete=models.CASCADE, db_column='sessionID')
    progressNote = models.TextField(null=False, blank=True)
    timestamp = models.DateTimeField()
    voteValue = models.CharField(max_length=6, null=False,
                                 choices = [
                                     ('Green', 'Green'),
                                     ('Amber', 'Amber'),
                                     ('Red', 'Red')
                                 ])
    
#Created table for Team
class Team(models.Model):
    teamID = models.IntegerField(primary_key=True)
    name = models.TextField(null=False)
    teamLeadID = models.IntegerField()
    userID = models.ForeignKey('User', on_delete=models.CASCADE, db_column='userID')
    healthCardID = models.ForeignKey('HealthCard', on_delete=models.CASCADE, db_column='healthCardID')
    departmentID = models.ForeignKey('Department', on_delete=models.CASCADE, db_column='departmentID')

class Department(models.Model):
    departmentID = models.IntegerField(primary_key=True)
    name = models.TextField(null=False)

class Session(models.Model):
    sessionID = models.IntegerField(primary_key=True)
    sessionDate = models.DateTimeField(null=False)
    status = models.CharField(max_length=4, null=False, 
                                            choices = [('Open', 'Open'),
                                                       ('Closed', 'Closed')
                                                ])