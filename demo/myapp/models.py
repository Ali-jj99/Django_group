from django.db import models

# Create your models here
class Vote(models.Model):
    voteID = models.IntegerField(primary_key=True)
    userID = models.ForeignKey('User', on_delete=models.CASCADE, db_column='userID')
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
    departmentID = models.ForeignKey('Department', on_delete=models.CASCADE, db_column='departmentID')

class Department(models.Model):
    departmentID = models.IntegerField(primary_key=True)
    name = models.TextField(null=False)

class Session(models.Model):
    sessionID = models.IntegerField(primary_key=True)
    sessionDate = models.DateTimeField(null=False)
    status = models.CharField(max_length=6, null=False, 
                                            choices = [('Open', 'Open'),
                                                       ('Closed', 'Closed')
                                                ])
#Created User Table
class User(models.Model):
    userID = models.IntegerField(primary_key=True)
    name = models.TextField(null=False)
    username = models.CharField(max_length=150, unique=True, null=False)
    email = models.CharField(max_length=254, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    role = models.CharField(
        max_length=20,
        choices=[
            ('Engineer',         'Engineer'),
            ('TeamLeader',       'TeamLeader'),
            ('DepartmentLeader', 'DepartmentLeader'),
            ('SeniorManager',    'SeniorManager'),
        ],
        null=False
    )
    teamID = models.ForeignKey(
        'Team',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        db_column='teamID'
    )
    departmentID = models.ForeignKey(
        'Department',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        db_column='departmentID'
    )

    class Meta:
        db_table = 'User'