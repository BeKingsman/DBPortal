from django.db import models
from django.contrib.auth.models import User

class State(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class user_profile(models.Model):

     GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    )

     adhaar_no = models.IntegerField()
     name = models.CharField(max_length = 100)
     DOB = models.DateTimeField(null=True)
     gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
     city = models.ForeignKey(City, on_delete=models.CASCADE,null=True)
     state = models.ForeignKey(State, on_delete=models.CASCADE,null=True)



class user_excel(models.Model):
    sheet = models.FileField(upload_to='',null=True)
    uploaded_by = models.ForeignKey(User,on_delete = models.CASCADE,null = True,related_name= 'excel_sheets')
