# 초기 작업 클론부터

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