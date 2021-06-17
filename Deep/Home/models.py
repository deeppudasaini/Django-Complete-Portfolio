from django.db import models

# Create your models here.
class SpecialSkills(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    def __str__(self):
        return self.name    
class CurrentInterest(models.Model):
    description=models.CharField(max_length=250)

class Skills(models.Model):
    name=models.CharField(max_length=250) 
    percent=models.IntegerField()
    def __str__(self):
        return self.name

class Work(models.Model):
    company=models.CharField(max_length=50)
    position=models.CharField(max_length=50,null=True)
    starttime=models.DateField(null=True)
    endtime=models.DateField(null=True)
    experience=models.CharField(max_length=250)
    def __str__(self):
        return self.company

class Contact(models.Model):
    email=models.EmailField(max_length=254) 
    message=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.email

class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=254)
    recent=models.BooleanField()
    link=models.CharField(max_length=254, null=True)
    image=models.ImageField(upload_to='./static/assets/uploads/',max_length=100)
    def __str__(self):
        return self.title