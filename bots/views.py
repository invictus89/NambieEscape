from django.shortcuts import render
from django.conf import settings
from accounts.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime
import requests
import json
import random

bot_name = settings.TELEGRAM_BOT_NAME
bot_token = settings.TELEGRAM_BOT_TOKEN
redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL

domain = 'https://nambie.herokuapp.com/accounts/' # 'nambie.herokuapp.com/accounts/' # https://5cd5ee8a.ngrok.io/accounts/
invitemgs = f'아래의 사이트에 접속하여 회원 정보를 등록해주세요.\n{domain}'

d = datetime.today()

@csrf_exempt
def telegram(request, token):
    body = request.body.decode('utf8').replace("'", '"')
    data = json.loads(body)
    msg = data.get('message')
    id = msg.get('from').get('id')
    text = msg.get('text')
    user = User.objects.filter(tel_id=id)
    if user.exists():
        user = user.first()
        categorys = user.inter_cate.all()
        if text=='소식' or text=='news' or text=='뉴스':
            msg+=f'◎ 키워드 뉴스\n{user.last_name} {user.first_name}님이 선택하신 카테고리는 '
            for category in categorys:
                msg+=f'[{category.name}] '

            msg+='입니다.\n도움이 필요하시면 /help를 입력해 주세요~\n\n<뉴스>\n'
            msg+=f'({user.last_name} {user.first_name})님의 선택하신\n'
            date = d.year*10000 + d.month*100 + d.day -1
            for category in categorys:
                keywords = category.keyword_set.all()
                msg+=f'\n[{category.name}]\n'
                for keyword in keywords:
                    keynewses = keyword.keynews_set.all()
                    if keynewses.exists() and keynewses.first().date==date:
                        keynewses = list(keyword.keynews_set.filter(date=date))
                        msg = msg + f' @ {keyword.name} {len(keyword.keynews_set.all())}개\n'
            msg+='의 새로운 기사가 등록되었습니다.\n자세한 내용은 여기를 클릭해주세요.'

        else:
            if text=='today' or text=='오늘':
                year = d.year
                month = d.month
                day = d.day
                msg+=f'\n{year}.{month}.{day} 오늘의 냄비소식입니다.\n\n'
                for category in categorys:
                    date = (d.year-1)*10000 + d.month*100 + d.day -1
                    today_date = (d.year)*10000 + d.month*100 + d.day -1
                    today_list = list(category.ranknews_set.filter(date=today_date))
                    if len(today_list) == 0:
                        msg += f'오늘 날짜의 이슈가 되었던 [{category.name}] 소식이 없습니다.\n\n'
                        continue
                    else:
                        msg+=f'{month}월{day}일에 이슈가 되었던 [{category.name}] 소식입니다.\n\n'
                        today_news = random.sample(today_list,1)
                        msg += f' - 오늘: {today_news[0].title}\n'    
                        for _ in range(2):
                            ranknewses = list(category.ranknews_set.filter(date=date))
                            l=len(ranknewses)
                            if l>0:
                                ranknewses = random.sample(ranknewses,2)
                                for ranknews in ranknewses:
                                    msg = msg+f' -  {int(date/10000)}년 오늘: {ranknews.title}\n'
                                date -= 10000
                            else:
                                msg = msg+f' -  {int(date/10000)}년 오늘의 데이터가 없습니다.\n'     
            else :
                try:
                    [month, day]=text.split('/')
                    month = int(text[0:2])
                    day = int(text[3:5])
                except:
                    pass
            try:
                events = user.event_set.filter(uploaded_at__month=month, uploaded_at__day=day)
                length = len(events)
                msg+='* 나만의 냄비 소식 입니다. * \n'
                if length==0:
                    msg+=f'오늘은 아무런 일정이 없습니다.'
                for event in events:
                    msg = msg + f' - {event.title}({event.uploaded_at.year})\n'
            except:
                msg="ex) '06/26'의 형식 혹은 '오늘', '뉴스' 으로 입력해 주세요."
    else:
        msg=invitemgs
    requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={id}&text={msg}')
    return HttpResponse(status=200)