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
2. Super  사용자 jeongsoo / 1234  --> http://127.0.0.1:8000/admin
3. 간단 Client
4. 기타