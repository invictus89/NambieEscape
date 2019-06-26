from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.conf import settings

from django_telegram_login.widgets.constants import LARGE, DISABLE_USER_PHOTO
from django_telegram_login.widgets.generator import create_redirect_login_widget, create_redirect_login_widget
from django_telegram_login.authentication import verify_telegram_authentication
from django_telegram_login.errors import NotTelegramDataError, TelegramDataIsOutdatedError

from .models import User
from news.models import Category

import requests

bot_name = settings.TELEGRAM_BOT_NAME
bot_token = settings.TELEGRAM_BOT_TOKEN
redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL

def index(request):
    context = {
        'telegram_login_widget': get_wiget()
    }
    return render(request, 'accounts/index.html', context)
    # return HttpResponse('This is Index page')

def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    else:
        if not request.GET.get('hash'):
            context = {
                'telegram_login_widget': get_wiget(),
            }
            return render(request, 'accounts/login.html', context)
        else:
            reault = verify_telegram_authentication(bot_token=bot_token, request_data=request.GET)
            tel_id = reault['id']
            first_name = reault['first_name']
            last_name = reault['last_name']
            user = User.objects.filter(tel_id = tel_id)
            if user.exists():
                user = user.first()
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                auth_login(request, user)
                text = f'{user}님께서 접속하셨습니다.'
            else :
                user = User(username = f'{tel_id}', tel_id = tel_id, first_name = first_name, last_name = last_name)
                user.save()
                auth_login(request, user)
                text = f'{user}님 가입을 환영합니다.'
            print(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={user.tel_id}&text={text}')
            requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={user.tel_id}&text={text}')
    return redirect('accounts:index')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

@login_required
def per_edit(request):
    if request.method == 'POST':
        pass
    else:
        context={
            'categorys': Category.objects.all(),
        }
    return render(request, 'accounts/_cate_edit.html', context)

@require_POST
@login_required
def edit_cate(request, category_pk):
    if request.is_ajax():
        category = get_object_or_404(Category, pk=category_pk)
        user = request.user
        if category.inter_users.filter(pk=user.pk).exists():
            category.inter_users.remove(user)
        else:
            category.inter_users.add(user)
        return JsonResponse()
    return HttpResponseBadRequest()


###########################################################################
# repeated method
def get_wiget():
    telegram_login_widget = create_redirect_login_widget(
        redirect_url,
        bot_name,
        size=LARGE,
        # user_photo = DISABLE_USER_PHOTO
    )
    return telegram_login_widget