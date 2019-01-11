from datetime import datetime, date, time
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404, JsonResponse
from doc.daily_office import DailyOffice

# Create your views here.

def home(request):
    do = DailyOffice(now=datetime.now())

    context = {
        'cycle': do.cycle,
        'season': do.season,
        'week': do.week,
        'day': do.day,
        'hour': do.hour
    }

    return render(request, 'doc/home.html', context)
