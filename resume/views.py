from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from resume.models import Resume
from PyPDF2 import PdfFileReader
from resume.forms import *
from files.files import *
import datetime
import os



def index(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)

        if(form.is_valid()):
            form.save()

            return redirect('/fronts')
    else:
        form = ResumeForm()
    return render(request, 'index.html', {'form': form})


def fronts(request):
    return render(request, 'display.html', {
        'display': Resume.objects.all(), })


def file(request):
    pdfFileObj = open('/home/yogesh/Desktop/cv/files/files/cv.pdf', 'rb')
    pdfReader = PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text=pageObj.extractText()
    return render(request, 'display.html', {
    'display': text.split(' '),
})
