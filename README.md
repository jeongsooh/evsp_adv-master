# evsp_adv-master
## 환경 설정
1. 프로젝트 폴더 및 virtual 환경 생성
```
$ cd
$ mkdir TEST
$ cd TEST
$ pwd
~/TEST
$ virtualenv venv
created virtual environment CPython3.10.6.final.0-64 in 485ms
  creator Venv(dest=C:\Users\jeongsooh\Documents\projects\python\TEST\venv, clear=False, no_vcs_ignore=False, global=False, describe=CPython3Windows)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\jeongsooh\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\Local\pypa\virtualenv)
    added seed packages: pip==22.1.2, setuptools==63.2.0, wheel==0.37.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
$
```
2. VS Code 실행
3. VS Code 터미널에서 virtual 환경 활성화 및 django 설치
```
$ source venv/scripts/activate
(venv>$ git clone https://github.com/jeongsooh/evsp_adv-master.git
Cloning into 'evsp_adv-master'...
remote: Enumerating objects: 188, done.
remote: Counting objects: 100% (188/188), done.
remote: Compressing objects: 100% (112/112), done.                             
remote: Total 188 (delta 74), reused 184 (delta 73), pack-reused 0
Receiving objects: 100% (188/188), 161.95 KiB | 1.95 MiB/s, done.
Resolving deltas: 100% (74/74), done.
(venv)$ ls
evsp_adv-master/  venv/
(venv)$ pip install django
Collecting django
  Using cached Django-4.1-py3-none-any.whl (8.1 MB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Collecting asgiref<4,>=3.5.2
  Using cached asgiref-3.5.2-py3-none-any.whl (22 kB)
Collecting tzdata
  Using cached tzdata-2022.1-py2.py3-none-any.whl (339 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.5.2 django-4.1 sqlparse-0.4.2 tzdata-2022.1
(venv) $
```
4. 실행에 필요한 python module 추가 설치
```
(venv)$ pip install channels
(venv)$ pip install djangorestframework
(venv)$ pip install requests
```
5. Application 구동
```
(venv)$ ls
evsp_adv-master/  venv/
(venv)$ cd evsp_adv-master
(venv)$ pwd
~/test/evsp_adv-master
(venv)$ ls
cardinfo/      db.sqlite3  evsp/    manage.py*  ocpp16/    static/
charginginfo/  evcharger/  evuser/  msglog/     README.md  variables/
(venv)$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 11, 2022 - 03:56:10
Django version 4.1, using settings 'evsp.settings'
Starting ASGI/Channels version 3.0.5 development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
INFO:daphne.server:HTTP/2 support not enabled (install the http2 and tls Twisted extras)
INFO:daphne.server:Configuring endpoint tcp:port=8000:interface=127.0.0.1      
INFO:daphne.server:Listening on TCP address 127.0.0.1:8000

```
## 간단한 사용
1. 기본 사용자 계정 jeongsooh1 / 1234 --> http://127.0.0.1:8000/  
2. Super  사용자 jeongsooh / 1234  --> http://127.0.0.1:8000/admin
3. 간단 Client (simulator 폴더)
4. 기타

## 시스템 동작환경 구성
### django 기반의 EVSP 구성
* Cardinfo: 사용자 인증용 card 등록 및 현황
* Charginginfo: 충전데이터 현황
* Evcharger: 충전기 등록 및 현황
* Evuser: 회원등록 및 현황
* Variables: 시스템 운용과 관련된 설정값
* Clients: 시스템운용에 필요한 모듈로 연결된 chargepoint 관련 현황
* Msglog: OCPP 메시지 로그와 관련된 부분 (사용하지 않음)
* Ocpp16: OCPP 서버로 msglog 기능 포함
* Simulator: OCPP16 client simulator로 본 시스템과는 상관없음. 소스 보관용 폴더
### OCPP16 - CSMS 메세지 처리 모듈 구현
* consumer: channels 기반의 ocpp 서버모듈
* Central_system: 메시지 처리 모듈
* Client_gateway: CSMS -> CP datatransfer 처리를 위하여 임시로 작성한 코드
### 간단한 구성도
![EVSP](https://user-images.githubusercontent.com/29830424/185800244-dfbc0d5d-4c72-4cb0-83b4-fe8070197707.JPG)


### Github로 부터 NCLOUD로 publishing 하는 방법

1. github로 부터 url 복사 (https://github.com/jeongsooh/evsp_adv-master.git)
2. NCLOUD에 code 복사
```
(venv) jeongsooh@jssvr:~$
(venv) jeongsooh@jssvr:~$ cd ~/projects/evsp
(venv) jeongsooh@jssvr:~/projects/evsp$ ls
evsp  evsp_221117  venv
(venv) jeongsooh@jssvr:~/projects/evsp$ git clone https://github.com/jeongsooh/evsp_adv-master.git
Cloning into 'evsp_adv-master'...
remote: Enumerating objects: 608, done.
remote: Counting objects: 100% (608/608), done.
remote: Compressing objects: 100% (351/351), done.
remote: Total 608 (delta 395), reused 457 (delta 253), pack-reused 0
Receiving objects: 100% (608/608), 1.79 MiB | 18.55 MiB/s, done.
Resolving deltas: 100% (395/395), done.
(venv) jeongsooh@jssvr:~/projects/evsp$
```
3. 현재 실행중인 code를 backup 하고 새로 복사한 code를 실행시킬 수 있도록 directory 단위 이름 변경 (이를 위해서 현재 실행 중인 서비스 중지할 것)
```
(venv) jeongsooh@jssvr:~/projects/evsp$
(venv) jeongsooh@jssvr:~/projects/evsp$ sudo systemctl stop evsp
(venv) jeongsooh@jssvr:~/projects/evsp$ sudo systemctl status evsp
● evsp.service - EVSP Service
   Loaded: loaded (/etc/systemd/system/evsp.service; enabled; vendor preset: enabled)
   Active: inactive (dead) since Thu 2022-11-17 18:18:28 KST; 9s ago
  Process: 2385 ExecStart=/home/jeongsooh/start.sh (code=killed, signal=TERM)
 Main PID: 2385 (code=killed, signal=TERM)

Nov 17 18:09:19 jssvr start.sh[2385]: HTTP GET /charginginfo/ 200 [0.01, 59.12.54.93:13803]
Nov 17 18:09:19 jssvr start.sh[2385]: INFO:django.channels.server:HTTP GET /charginginfo/ 200 [0.01, 59.12.54.93:13803]
Nov 17 18:09:20 jssvr start.sh[2385]: HTTP GET /cardinfo/ 200 [0.01, 59.12.54.93:13803]
Nov 17 18:09:20 jssvr start.sh[2385]: INFO:django.channels.server:HTTP GET /cardinfo/ 200 [0.01, 59.12.54.93:13803]
Nov 17 18:09:22 jssvr start.sh[2385]: HTTP GET /evcharger/ 200 [0.01, 59.12.54.93:13803]
Nov 17 18:09:22 jssvr start.sh[2385]: INFO:django.channels.server:HTTP GET /evcharger/ 200 [0.01, 59.12.54.93:13803]
Nov 17 18:09:31 jssvr start.sh[2385]: HTTP GET /ocpp16/ 200 [0.01, 59.12.54.93:13803]
Nov 17 18:09:31 jssvr start.sh[2385]: INFO:django.channels.server:HTTP GET /ocpp16/ 200 [0.01, 59.12.54.93:13803]
Nov 17 18:18:27 jssvr systemd[1]: Stopping EVSP Service...
Nov 17 18:18:28 jssvr systemd[1]: Stopped EVSP Service.
(venv) jeongsooh@jssvr:~/projects/evsp$
(venv) jeongsooh@jssvr:~/projects/evsp$ ls
evsp  evsp_221117  evsp_adv-master  venv
(venv) jeongsooh@jssvr:~/projects/evsp$ mv evsp evsp_221118
(venv) jeongsooh@jssvr:~/projects/evsp$ mv evsp_adv-master evsp
(venv) jeongsooh@jssvr:~/projects/evsp$
(venv) jeongsooh@jssvr:~/projects/evsp$ ls
evsp  evsp_221117  evsp_221118  venv
(venv) jeongsooh@jssvr:~/projects/evsp$

```
4. Windows와 Ubuntu의 설정 간 차이가 있는 부분을 조정한 후 다시 서비스 실행. settings.py 화일의 내용을 아래와 같이 변경
```
INSTALLED_APPS = [
    # 'daphne',

    'channels',
]

TIME_ZONE = 'UTC'
# TIME_ZONE = 'Asia/Seoul'
```
```
INSTALLED_APPS = [
    'daphne',

    # 'channels',
]

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'
```
```
(venv) jeongsooh@jssvr:~/projects/evsp$
(venv) jeongsooh@jssvr:~/projects/evsp$
(venv) jeongsooh@jssvr:~/projects/evsp$ sudo systemctl start evsp
(venv) jeongsooh@jssvr:~/projects/evsp$ sudo systemctl status evsp
● evsp.service - EVSP Service
   Loaded: loaded (/etc/systemd/system/evsp.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2022-11-17 18:26:06 KST; 7s ago
 Main PID: 2592 (start.sh)
    Tasks: 4 (limit: 2301)
   CGroup: /system.slice/evsp.service
           ├─2592 /bin/bash /home/jeongsooh/start.sh
           ├─2601 python manage.py runserver 0.0.0.0:8000
           └─2611 /home/jeongsooh/projects/evsp/venv/bin/python manage.py runserver 0.0.0.0:8000

Nov 17 18:26:06 jssvr systemd[1]: Started EVSP Service.
Nov 17 18:26:07 jssvr start.sh[2592]: Watching for file changes with StatReloader
Nov 17 18:26:07 jssvr start.sh[2592]: INFO:daphne.server:HTTP/2 support not enabled (install the http2 and tls Twisted extras)
Nov 17 18:26:07 jssvr start.sh[2592]: INFO:daphne.server:Configuring endpoint tcp:port=8000:interface=0.0.0.0
Nov 17 18:26:07 jssvr start.sh[2592]: INFO:daphne.server:Listening on TCP address 0.0.0.0:8000
(venv) jeongsooh@jssvr:~/projects/evsp$
(venv) jeongsooh@jssvr:~/projects/evsp$

```

### 추가된 내용 (2023년 1월 10일 업데이트)
1. 회원관리에 검색 관련 내용 추가
- evuser.html에서 input에 입력된 내용을 name = 'q'로 받아서 views.py로 전달하고 이를 반영한 queryset 생성
- 검색된 queryset을 evuser.html을 통해서 list로 보여주지만 전후로 이동하면 검색된 내용이 해제되면서 검색 이전의 리스트로 복귀되는 문제
- evuser.html 변경된 내용
```
    <form method="get" action="/evuser">
      <div class="input-group input-group-sm">
        <input type="text" class="form-control" name="q" placeholder="" aria-label="Recipient's userid" aria-describedby="button-addon2">
        <button class="btn btn-primary" type="submit" id="button-addon2">
          <i class="bi bi-search"></i>
        </button>
      </div>
    </form>
```
- views.py의 EvuserList class에 추가된 내용
```
def get_queryset(self):
  queryset = Evuser.objects.all()
  query = self.request.GET.get("q", None)
  if query is not None:
    queryset = queryset.filter(
      Q(userid__icontains=query) |
      Q(name__icontains=query) |
      Q(phone__icontains=query)
    )
  return queryset
```  

2. 카드관리에서는 상기 회원관리에서 나타난 문제점을 해결하기 위하여 pagination에 아래와 같이 templatetags 기법을 적용
- cardinfo.html과 views.py의 CardinfoList class는 상기 회원관리와 같이 변경
- templatetags/__init__.py 화일을 만들고 내용을 공백으로 둔다.
- templatetags/cardinfo_extras.py 화일을 만들고 내용을 아래와 같이 작성하여 my_url 함수를 만든다.
```
from django import template

register = template.Library()

@register.simple_tag
def my_url(value, field_name, urlencode=None):
  url = '?{}={}'.format(field_name, value)

  if urlencode is not None:
    querystring = urlencode.split('&')
    filtered_querystring = filter(lambda p: p.split('=')[0]!=field_name, querystring)
    encoded_querystring = '&'.join(filtered_querystring)
    url = '{}&{}'.format(url, encoded_querystring)

  return url
```
- 이와 같이 만들어진 my_url을 이용하여 cardinfo.html 화일의 pagination 관련 내용을 아래와 같이 변경한다. (Comment 처리된 원래 내용 참조)
```
    <div class="pagination justify-content-center mt-5">
      <ul class="step-links">
        {% if page_obj.has_previous %}
        <a class="btn btn-sm btn-outline-primary" href="{% my_url 1 'page' request.GET.urlencode %}">처음으로</a>
        <a class="btn btn-sm btn-outline-primary" href="{% my_url page_obj.previous_page_number 'page' request.GET.urlencode %}">이전으로</a>
        <!-- <a class="btn btn-sm btn-outline-primary" href="?page=1">처음으로</a>
        <a class="btn btn-sm btn-outline-primary" href="?page={{ page_obj.previous_page_number }}">이전으로</a> -->
        {% else %}
        <a class="btn btn-sm btn-outline-primary disabled" href="#">처음으로</a>
        <a class="btn btn-sm btn-outline-primary disabled" href="#">이전으로</a>
        {% endif %}
      <span class="current">
        {{ page_obj.number }} / {{ page_obj.paginator.num_pages }}
      </span>
        {% if page_obj.has_next %}
        <a class="btn btn-sm btn-outline-primary" href="{% my_url page_obj.next_page_number 'page' request.GET.urlencode %}">다음으로</a>
        <a class="btn btn-sm btn-outline-primary" href="{% my_url page_obj.paginator.num_pages 'page' request.GET.urlencode %}">마지막으로</a>
        <!-- <a class="btn btn-sm btn-outline-primary" href="?page={{ page_obj.next_page_number }}">다음으로</a>
        <a class="btn btn-sm btn-outline-primary" href="?page={{ page_obj.paginator.num_pages }}">마지막으로</a> -->
        {% else %}
        <a class="btn btn-sm btn-outline-primary disabled" href="#">다음으로</a>
        <a class="btn btn-sm btn-outline-primary disabled" href="#">마지막으로</a>
        {% endif %}
      </ul>
    </div>
```
### AWS EC2 publishing
추가되는 모듈
```
$ pip install boto3
$ pip install django-storages
```
S3에 static 화일 등 저장을 위한 설정 작성
```
# AWS S3
AWS_ACCESS_KEY_ID = 'AKIA4GOZC7MV67ZZHPX4'
AWS_SECRET_ACCESS_KEY = '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'
AWS_DEFAULT_ACL = 'public-read'
AWS_REGION = 'us-east-1'
AWS_STORAGE_BUCKET_NAME = 'jsbucket0120'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME, AWS_REGION)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```
static files을 S3에 저장
```
$ python manage.py collectstatic
```
#### settings.py 분리후 runserver 실행
settings.py -> settings/base.py
            -> settings/dev.py
            -> settings/prod.py

base.py: 공통 내용 정리
dev.py: dev 단계에서 사용하는 settings
prod.py: production 단계에서 사용하는 settings

development 단계이면 환경변수를 다음과 같이 설정 후 실행
```
$ export DJANGO_SETTINGS_MODULE=evsp.settings.dev
$ python manage.py runserver
```

production이면 환경변수를 다음과 같이 설정 후 실행
```
$ export DJANGO_SETTINGS_MODULE=evsp.settings.prod
$ python manage.py runserver
```
## Github에 등록
project 제일 상단 폴더에 각 module의 버전을 정리한 requirements.txt 화일 작성
```
Django==4.1.5
django-debug-toolbar==3.8.1
# Pillow==6.0.0
django-storages==1.13.2
gunicorn==19.9.0
boto3==1.26.79
```
## EC2 접속 후 설정
```
$ ssh -i EC2_connect_sec_key ubuntu@publicdomain  # default user ubuntu로 접속
```
```
$ sudo apt update
$ sudo apt install git
$ sudo apt install nginx
$ sudo apt install python3-pip
$ sudo apt install vim
$ sudo su
# cd /etc/nginx/sites-available
/etc/nginx/sites-available#
/etc/nginx/sites-available# mv default default.bak
```
백업한 default 대신 reverse proxy 기능을 담은 default 재 작성
```
upstream django {
        server 127.0.0.1:8000;
}

server {
        listen 80;

        proxy_set_header X-Forwarded-Proto $scheme;

        # gunicorn app
        location / {
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Url-Scheme $scheme;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header Host $http_host;

                proxy_redirect off;
        }
}

```
nginx 실행 후 git clone을 통해서 소스 복사
```
/etc/nginx/sites-available# service nginx restart
/etc/nginx/sites-available# exit
$ cd
$ ls
$ 
$ git clone https://github.com/jeongsooh/evsp_adv-master.git
$ cd evsp_adv-master
$ pip3 install -r requirement.txt
```
.bashrc 화일에 django production 환경변수 설정
```
$ cd 
$ vi .bashrc 
export DJANGO_SETTINGS_MODULE=evsp.settings.prod 
```
gunicorn 실행시켜서 wsgi 같은 역할을 구동한다. -D 옵션을 줘서 터미날 빠져도 계속 실행되도록
```
$ gunicorn evsp.wsgi -- bind 0.0.0.0:8000 -D
$
$
$ pkill gunicorn
```




