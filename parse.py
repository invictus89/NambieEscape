from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime
from urllib import parse
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nambie.settings")
import django
django.setup()
# model import
from news.models import Category, RankNews

dt = datetime.datetime.now()
date = dt.strftime("%Y%m%d")
int_date= int(dt.strftime("%Y%m%d"))
#print(date)
browser= webdriver.PhantomJS()
browser.implicitly_wait(3)

data = {}
news= {}
past_int_date = 20130626
data[past_int_date] = news

def parse_rank():
    # Category DB에 저장된 URL 순차적으로 호출
    for num in range(0,6):
        
        page_num = num+100   
        section = ['정치', '경제', '사회', '문화', '세계', 'IT']
        cate = section[num]
        
        url= f'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId={page_num}&date=20130626'
        browser.get(url)
        print(f'{section[num]}뉴스 페이지에 접근합니다.')
        print('---------------------')
        
        # 랭킹 불러오기 
        bundle=[]
        for n in range(1,31):
            try:
                #뉴스 세부내용 얻기
                #title
                ranking_title = browser.find_element_by_xpath(f'//*[@id="wrap"]/table/tbody/tr/td[2]/div/div[4]/ol/li[{n}]/div[2]/div[1]/a')
                current_title = ranking_title.get_attribute('title')
                ranking_title.click()
               
                #url
                current_url = browser.current_url
                url = parse.urlparse(current_url)
               
                #content
                contents = browser.find_elements_by_css_selector("#articleBodyContents")
                for content in contents:
                    #print(content.text) # rank_news DB에 content 저장
                    detail = [current_title, current_url, content.text]
                #print(current_title)
                bundle.append(detail)
                news[cate]=bundle
               
                browser.back()
                
            except :
                pass
 
        time.sleep(3)
    print('DB저장합니다')
    return data
#print(parse_rank())
if __name__ == '__main__':
    dates_news = parse_rank()
    for date, news in dates_news.items():
        print(date) #date
        count=1
        for name, news in news.items():
            print(f'{count}번째')
            print(name) #category
            #category = Category(name=name)
            #category.save()
            for new in news:
                category = Category.objects.get(pk=count)
                print(new[0]) #title
                print(new[1]) #url
                #print(new[2]) #content
                print('---------------------------------------------------------------------------')
                rankNews = RankNews(title=new[0], url=new[1], content=new[2],date=date, category=category)
                rankNews.save()
            count+=1    


