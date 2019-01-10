from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404, JsonResponse

# Create your views here.

def home(request):

    context = {
        'title': 'Daily Office Companion'
    }

    return render(request, 'doc/home.html', context)
