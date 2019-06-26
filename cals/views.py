from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from datetime import datetime, timedelta, date
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .utils import *
import calendar
from .forms import *
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.core import serializers
import json

from django.conf import settings
import requests
bot_token = settings.TELEGRAM_BOT_TOKEN

def my_calendar(request, month = None):
    if month:
        request.session['ses_month'] = month
        year, month = (int(x) for x in month.split('-'))
        d = date(year, month, day=1)
    else:
        ses_month = request.session.get('ses_month', 'None')
        if ses_month == 'None':
            d = datetime.today()    
        else:
            year, month = (int(x) for x in ses_month.split('-'))
            d = date(year, month, day=1)
            
    cal = Calendar(d.year, d.month)
    html_cal, month_name = cal.formatmonth(request, withyear=True)
    form = EventForm()
    context = {
        'form': form,
        'calendar': mark_safe(html_cal),
        'month_name': month_name,
        'prev_month': prev_month(d),
        'next_month': next_month(d),
    }
    
    return render(request, 'cals/calendar.html', context)

@require_POST
@login_required
def edit(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if event.user == request.user:
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
    return redirect('calendar:calendar')

@require_POST
def create(request, year, month, day):
    if request.user.is_authenticated:
        title = request.POST.get('title')
        description = request.POST.get('description')
        title_type = request.POST.get('title_type')
        user = request.user
        temp = f'{year}-{month}-{day}'
        uploaded_at = datetime.strptime(temp, '%Y-%m-%d')
        event = Event(title = title, description = description, title_type = title_type, uploaded_at=uploaded_at, user=user)
        event.save()
        
        return redirect('calendar:calendar')
    else:
        return redirect('accounts:login')

@login_required
def detail(request, year, month, day):
    cur_temps = request.user.event_set.filter(uploaded_at__year=year, uploaded_at__month=month, uploaded_at__day=day)
    cur_dates = serializers.serialize('json', cur_temps)
    all_temps = request.user.event_set.filter(uploaded_at__month=month, uploaded_at__day=day)
    all_dates = serializers.serialize('json', all_temps)
    context = {
        'cur_dates': cur_dates,
        'all_dates': all_dates,
         }
    return JsonResponse(context)

@login_required
def delete(request, content_id):
    contents = get_object_or_404(Event, pk=content_id, user_id=request.user.pk)
    contents.delete()
    return redirect('calendar:calendar')

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = str(next_month.year) + '-' + str(next_month.month)
    return month

def get_today_events(request):
    d = datetime.today()
    for user in User.objects.all():
        today_events = Event.objects.filter(uploaded_at__month=d.month, uploaded_at__day=d.day, user_id=user.pk)
        text='Remember the today./n'
        lastin = len(today_events)
        for today_event in today_events:
            if today_event == today_events[lastin-1]:
                text+=f'{today_event.title}가 있습니다.'
            else:
                text+=f'{today_event.title}, '
        requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={user.tel_id}&text={text}')

'''
# modelForm 적용 create 
def create(request, year, month, day):
    if request.method == 'POST':
        print("포스트")
        form = EventForm(request.POST)
        if form.is_valid():
            # 유저 기능 넣으면 해제 및 수정할 것
            # board = form.save(commit=False)
            # board.user = request.user
            temp = f'{year}-{month}-{day}'
            uploaded_at = datetime.strptime(temp, '%Y-%m-%d')
            event = form.save(commit=False)
            event.uploaded_at = uploaded_at
            event.save()
            return redirect('calendar:calendar')
    else:
        form = EventForm()
    context = {'form' : form,}
    return HttpResponse(context)
'''   