from django.shortcuts import render,redirect
from django.http import request,HttpResponse
from resume.models import Resume
from resume.forms import *

def index(request):
    if request.method=="POST":
        form=ResumeForm(request.POST, request.FILES)

        if(form.is_valid()):
            form.save()
            return redirect('/fronts')
    else:
        form=ResumeForm()
    return render(request,'index.html',{'form':form})

def fronts(request):
    return render(request,'display.html',{
            'display':Resume.objects.all(), })
