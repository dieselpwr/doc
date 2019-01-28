from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404, JsonResponse
from doc.daily_office import DailyOffice

# Create your views here.

def detect(request):

    return render(request, 'doc/detect.html')

def home(request):
    do = DailyOffice(now=timezone.localtime())

    context = {
        'cycle': do.cycle,
        'season': do.season,
        'week': do.week,
        'day': do.day,
        'hour': do.hour,
        'timezone': timezone.get_current_timezone(),
    }

    return render(request, 'doc/home3.html', context)
