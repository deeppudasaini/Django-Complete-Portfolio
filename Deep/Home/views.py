from django.shortcuts import render,redirect
from .models import SpecialSkills,CurrentInterest,Skills,Work,Contact,Project
from django.contrib import messages
import datetime
# Create your views here.
def Index(request):
    variable={
        'skill':SpecialSkills.objects.all(),
        'interest':CurrentInterest.objects.all(),
        'projects':Project.objects.filter(recent=True)
    }
    return render(request,"index.html",variable);

def portfolio(request):
    variable={
        'projects':Project.objects.all()
    }
    return render(request,"projects-grid-cards.html",variable);
    
def cv(request):
    variable={
        'skills':Skills.objects.all(),
        'work':Work.objects.all()
    }
    return render(request,"cv.html",variable);

def hire(request):
    if request.method=='POST':
        email=request.POST['email']
        message=request.POST['message']
        date=datetime.datetime.now()
        singleRow=Contact(email=email,message=message,date=date)
        singleRow.save()
        messages.success(request,'Your message has been sent')
        return redirect("/hire");
        
    else:
        return render(request,"hire-me.html")