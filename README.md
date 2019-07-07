[TOC]



# 냄비탈출 프로젝트

- 바쁜 삶으로 인한 소중한 기억과 이슈를 쉽게 잊어버리는 현대인들을 위한 챗봇 알림 서비스 입니다.

  

## 프로젝트 기획 배경

>냄비 근성이란? 
>
>- 빨리 끓어오르고 빨리 식는 냄비에 빗대어 어떤 화두에 대한 열기가 금방 식는다는 것을 표현한다.

개발 교육에 참여하며 공부와 취업 준비로 바쁜 나날을 보냈다. 오늘이 무슨 날인지도 모른채 바쁘게 지냈고, 기억하지 못한 날 중에 하루가 4월 16일였다. 작년 까지만 해도 기억하였는데 중요한 날을 기억하지 못한 내 자신에 부끄러움을 느끼며 해당 프로젝트를 기획하게 되었다.



냄비 근성의 심각성은 많은 예에서 찾아 볼 수 있다.

- 2002년 월드컵 때의 축구 열풍 이후 급격히 줄어든 K리그에 대한 관심
- 독도 문제와 동북공정 등의 역사 문제
- 허니버터칩, 꼬꼬면 등의 생활 속 이슈

우리의 개인 생활에서도 냄비 근성을 쉽게 찾아 볼 수 있다. 위의 4월 16일은 세월호 침몰 사고가 발생한 날이다. 현재 이 날을 기억하고 있는 사람은 몇 명이나 될까? 사회 이슈 뿐만 아니라 가족, 연인, 친구의 생일 또는 기념일, 여러 소중한 추억이 담긴 날들을 기억하는 것도 쉽지 않을 것이다.

이러한 냄비 근성은 잘못된 것이 이니다. 시간이 지나감에 따라 기억은 희미해지며 사람 마다 관심사가 다르고, 관심사에 대한 애정 또한 다르다. 다만, 이러한 냄비 근성을 조금이나마 극복하고자 해당 프로젝트를 기획하게 되었다.

## 프로젝트 목적

- 과거 년도의 오늘 날에 있었던 개인의 소중한 날과 관심있는 분야의 이슈를 챗봇 서비스를 통해 알림을 받고, 오늘 하루의 의미를 되새기자.

- 관심 있는 분야의 이슈를 뉴스 포탈 사이트 정보를 기반으로 지속적으로 챗봇 서비스로 알림을 받아, 냄비 근성을 극복하자. 

  

## 개발환경 및 사용언어

#### [개발환경 및 툴]

- VS Code
- Selenium / PhantomJS
- Heroku Cloud Platform / NGROK
- Crontab
- Telegram API / SNS Login / Webhook 

#### [사용 언어]

- Python3 / Django Framework

- sqlite3

- HTML[Bootstrap]

- CSS

- JavaScript 및 vue.js for axios


#### [협업 툴]
- github / slack / notion

  

## 기능 요약

1. 주기적으로 오늘 날짜의 네이버 랭킹뉴스와 다음 뉴스의 세부이슈 크롤링(Crontab, 하루에 한 번 크롤링)
2. 챗봇을 통해 사용자 관심 분야의 업데이트 된 새 기사 알림(후속 보도, 심층 취재에 대해 알 수 있다. )

3. 챗봇을 통해 사용자 관심 분야의 다른년도, 같은 날짜의 다음 랭킹 뉴스를 알림 (과거 년도의 오늘 어떤 이슈가 있었는지 확인)

4. 캘린더를 통해 사용자의 기억하고 싶은 개인 이슈를 관리하고 이를 챗봇 서비스를 통해 알림을 받는다.
5. 관심 분야 수정



## 기능 설명

1. crontab을 활용한 주기적인 크롤링 기능 구현

   주기적인 크롤링을 하기위해서 Mac, Linux Terminal 내장기능인 crontab을 이용했고 하루에 두번 크롤링을 진행하였음.

   `crontab -l` :  crontab에 저장된 내용을 보여줌

   `crontab -e` : crontab에 내용을 추가

   ```
   * 7,19 * * * python /your/site/parse.py
   ```

   매일 7시와 19시에 크롤링을 진행함.

   다음뉴스의 이슈파트 

   네이버랭킹뉴스 

   selenium의 Xpath, selector를 통하여 html 값을 받아옴

   크롤링한 데이터를 ORM을 통하여 sqlite3 DB를 업데이트 하였음.

   

4. 캘린더 기능 구현

   - 기념일 / 뉴스 / 역사 / 사건사고 카테고리로 기억하고 싶은 이슈 등록

     <img src="./git_images/4-1.insert.PNG" width="65%"></img>

   - 등록된 이슈는 카테고리 별 색상을 달리하여 직관적으로 정보 제공

     <img src="./git_images/4-2.list.PNG" width="65%"></img>

   - 등록된 제목 길이가 너무 길 경우 일부 내용만 표기하고, 등록된 정보가 많을 경우 '...' 으로 표시

     >[위의 그림 참조]

   - 파이썬 Calendar API 기반의 캘린더 UI와 CRUD 구현

   - 년도와 상관 없이 월/일로 등록한 개인 이슈 확인

     <img src="./git_images/4-3.detailed.PNG" width="65%"></img>

   - 텔레그램 봇과 연동

     <img src="./git_images/4-4.bot.PNG" width="65%"></img>

   - 이슈 등록은 비동기식 구현을 위해 json 데이터 형식과 axios 기능 활용

     

5. 네이버와 다음 뉴스의 카테고리 기반으로 사용자의 관심 사항 수정



## 초기 작업 세팅

1. git clone --recurse-submodules \<url> 로 클론하시기 바랍니다.(submodul 설치 됨.)
   - git clone \<url>로 설치한 경우.
     서브모듈 설치(pyTelegramBotAPI)
      git submodule init
      git submodule update
2. 가상환경 설치.
   `python -m venv Nambie-venv`
3. 가상환경 활성화.
   `source Nambie-venv/Scripts/activate`
4. pip 업그레이드.
   `python -m pip install --upgrade pip`
5. 의존성 가져오기.
   `pip install -r requirements.txt`
6. DB모델 migrate
   `python manage.py migrate`
7. 관리자 생성
   `python manage.py createsuperuser`
   관리자의 pk=1 이 되도록 먼저.
   관리자 ID : admin
   관리자 PW : admin
   가급적 통일해주세요. (다른 사람이 잠깐 쓸때라도 통일된 부분이 있으면 편하니까요.)



## 보완 계획

[기존 프로젝트]

1. 크롤링
   - AWS Web Cloud 서비스 활용과 Crontab 보완
   - 백과 위키와 나무 위키 크롤링 추가 및 보완
2. 캘린더
   - 개인 일기장 기능 보완을 위하여 개인 일정 관리 가능하도록 보완
   - '오늘' 하면 오늘, '주간' 하면 주간의 일정을 챗봇 서비스로 알림

[새로운 프로젝트]

- 취업 준비생을 위한 채용 알림 및 기업 분석 웹/챗봇 서비스 계획 중...
- 구글 익스텐션 개발 필요성
  - 자소설 닷컴 즐겨찾기 한 일정 받아와 캘린더와 연결
- 기업 검색 및 비교 기능
  - Ex) 삼성 전자 vs 하이닉스
- 회사 검색 시 신뢰성 높은 기사로의 정보 제공



