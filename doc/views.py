from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404, JsonResponse
from dateutil.relativedelta import relativedelta as rd
from doc.daily_office import DailyOffice

# Create your views here.

def detect(request):

    return render(request, 'doc/detect.html')

def home(request):
    do_yesterday = DailyOffice(now=(timezone.localtime() - rd(days=1)))
    do_today = DailyOffice(now=timezone.localtime())
    do_tomorrow = DailyOffice(now=(timezone.localtime() + rd(days=1)))

    context = {
        'cycle_yesterday': do_yesterday.cycle,
        'season_yesterday': do_yesterday.season,
        'week_yesterday': do_yesterday.week,
        'day_yesterday': do_yesterday.day,
        'hour_yesterday': do_yesterday.hour,
        'cycle_today': do_today.cycle,
        'season_today': do_today.season,
        'week_today': do_today.week,
        'day_today': do_today.day,
        'hour_today': do_today.hour,
        'cycle_tomorrow': do_tomorrow.cycle,
        'season_tomorrow': do_tomorrow.season,
        'week_tomorrow': do_tomorrow.week,
        'day_tomorrow': do_tomorrow.day,
        'hour_tomorrow': do_tomorrow.hour,
        'timezone': timezone.get_current_timezone(),
    }

    return render(request, 'doc/home3.html', context)
