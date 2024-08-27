# 1. 인트로
## 기획 배경
## WBS 작성
## ERD 생성
## WF 작성

# 2. 초기 설정
## 가. 개발환경 설정
### 1) 폴더 생성
프로젝트의 루트 폴더를 생성합니다. 터미널 창을 실행한 후 명령어를 입력하여 `travel_blog`라는 폴더를 생성합니다.
```shell
mkdir travel_blog
```

폴더가 생성되었는지 확인합니다.
```shell
dir
```

생성된 폴더로 이동합니다.
```shell
cd travel_blog
```

Visual Studio Code(이하 VSCode)를 실행합니다.
```shell
code .
```

### 2) 개발환경 셋팅
동일한 개발환경과 프로그램 버전을 사용하여 프로젝트를 진행하기 위하여 가상환경을 사용합니다. 필요한 패키지의 동일한 버전을 사용하여 코드 충돌 등을 방지합니다.

#### 가상환경
##### 가상환경 생성
 
 VSCode에서 터미널 창을 엽니다. 단축키는 `ctrl + shift + ~` 입니다.
 열린 터미널 창에 아래의 명령어를 입력하여 가상환경을 생성합니다.

- 터미널 창을 열고 'PowerShell' 또는 'bash' 옆에 있는 `∨`를 클릭하면 드롭다운 메뉴가 나타납니다. 목록에서 'Command Prompt'를 클릭하면 됩니다.
 ```shell
 python -m venv .venv
 ```

따라서, 현재 폴더에서 프로젝트를 바로 생성하기 위하여 “.”을 포함하여 명령어를 작성해 주시면 됩니다.

>`venv`와 `.venv`의 차이
>
> 가상환경을 설정할 때 사용하는 폴더의 이름으로 기능적인 차이는 없습니다. 사용자의 선호에 따라 선택됩니다.
> 가상환경 폴더를 명확하게 하고 싶은 경우 `venv`를 사용하며, 폴더를 숨김처리 하여 목록에서 눈에 덜 띄게 하고 싶은 경우 `.venv`를 사용합니다.

##### 가상환경 활성화
터미널 창에 아래의 명령어를 입력하여 가상환경을 활성화합니다.
```shell
# window 버전
.venv\Scripts\activate
```
터미널 경로 앞에 가상 환경 이름이 표시되었는지 확인합니다.

##### 가상환경 비활성화
활성화한 가상환경을 더이상 사용하고 싶지 않은 경우, 아래의 명령어를 입력하여 가상환경을 끕니다.
```shell
# window 버전
deactivate
```

#### Django 설치
##### 패키지 설치
Django를 활용한 프로젝트를 개발하기 위하여 아래의 명령어를 입력하여 Django 패키지를 다운로드 합니다.
(패키기 설치 전 가상환경이 활성화되어있는지 터미널 경로 앞에 가상 환경 이름 표시 여부를 확인 후 패키지 설치를 진행합니다.)
```shell
pip install django
```
##### 설치 결과 확인
Django 패키지가 정상적으로 설치되었는지 확인하기 위하여 설치된 패키지 리스트와 패키지 버전을 확인합니다.

**설치된 패키지 리스트 확인**
```shell
pip list # asgiref, Django, pip, sqlparse, tzdata
```

**패키지 버전 확인**
```shell
django-admin --version # 5.1
```


> **패키지 목록을 활용한 설치**
> 
> 프로젝트 진행을 위해 필요한 패키지만 모아놓은 파일 목록을 활용하여 패키지를 설치합니다. 
> ```shell
> pip install -r requirements.txt
> ```
> 초기 개발시 패키지 목록을 저장하는 방법은 아래의 명령어로 `requirements.txt` 파일에 저장할 수 있습니다.
> >```shell
> >pip freeze > requirements.txt
> >```


#### 프로젝트
##### 프로젝트 생성
Django가 정상적으로 설치된 것이 확인 후 터미널 창에 아래 명령어를 입력하여 프로젝트를 생성합니다.
```shell
django-admin startproject travel_blog .
```

프로젝트 생성 시 주의해야 하는 점은 코드의 온점(.)의 여부에 따라 프로젝트가 생성되는 경로는 달라집니다.
- `travel_blog`는 현재 폴더 안에 `travel_blog`라는 새 폴더를 생성 후 프로젝트 핵심 파일들이 저장됩니다. 즉, 경로는 `travel_blog/travel_blog`가 됩니다.  
- `travel_blog .`은 현재 폴더에 직접 생성됩니다. 추가적인 상위 폴더가 만들어지지 않고, 프로젝트 핵심 파일들이 바로 생성됩니다. 즉, 경로는 `travel_blog`가 됩니다.


##### 프로젝트 설정
Django 프로젝트를 생헌한 후, 프로젝트를 실제로 사용하기 전 여러 가지 설정과 구정을 진행합니다.
- **`DEBUG`** : 개발 중에는 `DEBUG = True`로 설정하지만 배포 시에는 반드시 `False`로 설정합니다.
- **`ALLOWED_HOST`** : 배포 환경에서 서용할 도메인이나 IP 주소를 설정합니다. 
    - `ALLOWED_HOSTS = ['*']` : 모든 호스트에서 접근 가능하도록 설정하기 위해서 입력합니다. 그러나, 보안상 매우 위험하므로 실제 배포 시에는 사용하지 않습니다.
- **`LANGUAGE_CODE`** : 프로젝트의 기본 언어를 설정합니다. `ko-kr`로 설정합니다.
- **`TIME_ZONE`** : 프로젝트의 시간대를 설정합니다. `Asia/Seoul`로 설정합니다.

#####  마이그레이트
Django가 기본적으로 제공하는 앱(`auth`, `admin`, `contenttype`, `sessions` 등)들의 데이터베이스 테이블을 설정하기 위하여 마이그레이트를 실행합니다.
```shell
python manage.py migrate
```
그 결과 폴더 내부에는 

>`makemigrations`? `migrate`?
>
>Django로 프로젝트를 생성한 직후에는 기본 앱들에 대한 마이그레이션 파일들이 이미 존재하기 때문에, `migrate` 명령어만으로도 기본 앱들이 필요로 하는 데이터베이스 테이블들을 생성할 수 있습니다.
> 새로운 앱 또는 모델을 추가하거나 기존 모델을 수정하는 경우 `makemigraions`를 실행해야 Django가 이러한 변경 사항을 반영하는 마이그레이션 파일을 생성할 수 있습니다.

# 3. 관리자 계정
## 가. 관리자 계정 생성

Django에서는 `createsuperuser` 명령어를 사용하여 관리자 계정을 생성할 수 있습니다.터미널 창에 아래 명령어를 입력합니다.
```shell
python manage.py createsuperuser
```
## 나. 계정 정보 입력
명령어를 실행하면 아래와 같은 정보를 입력하라는 안내가 나타납니다. 관리자 계정은 쉽게 유추할 수 없도록 생성합니다. `cmd`입력창에서 비밀번호와 비밀번호 재입력시 텍스트가 작성되는 액션을 볼 수 없습니다. 
- Username(사용자 이름) : 관리자 계정에 사용할 사용자 이름(아이디)를 입력합니다. 
- Email address(이메일 주소) : 관리자 계정에 사용할 이메일 주소를 입력합니다.
- Password(비밀번호) : 관리자 계정에 사용할 비밀번호를 입력합니다.
- Password(again)(비밀번호 재입력) : 비밀번호를 다시 입력하여 확인합니다.

모든 정보를 올바르게 입력하면, "Superuwer created successfully."라는 메세지가 나타나며, 관리자 계정이 생성됩니다.

## 다. 계정 활성화 및 관리자 페이지
### 서버 실행
관리자 계정을 활성화화려면 Django 마이그레이션 후 개발 서버를 실행합니다.
```shell
python manage.py runserver
```

### 관리자 페이지
#### 접속
관리자 페이지 접속을 위하여 웹 브라우저에서 다음 URL로 이동합니다.
```
http://127.0.0.1:8000/admin/
```
#### 로그인 및 활성화 확인
생성한 관리자 계정의 사용자 이름과 비밀번호로 로그인합니다. 로그인 후, 관리자 대시보드에 접속할 수 있습니다. 여기에서 사용자를 관리하고, 데이터베이스의 모델을 조회하거나 수정할 수 있습니다.



# 4. 메인화면
## 가. 메인 앱 생성
입장하기 화면을 관리할 새로운 앱 `main`을 생성합니다.
```
python manage.py startapp main
```

## 나. URL 설정
### main/urls.py
`main`앱 폴더 안에 `urls.py` 파일을 생성하고 사용자가 웹사이트의 기본 페이지를 접속하였을 때, `home`이라는 함수를 실행하도록 하는 코드를 작성합니다.
- ` path("", views.home , name = 'home')` : 기본주소(공백은 아무것도 추가되지 않은 상태)에 접속하였을 때, views.py에 있는 home이 실행되어 사용자가 볼 페이지를 결정합니다. 해당 경로는 `home`이라는 이름을 사용하여 다른 파일에서 해당 URL 패턴을 참조할 때 `home`이라는 이름을 사용할 수 있습니다.

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home , name = 'home')
]
```

### travle_blog/urls.py
`travel_blog`앱 폴더 안에 `urls.py` 파일을 생성하고 사용자가 웹사이트의 기본 페이지를 접속하였을 때, `home`이라는 함수를 실행하도록 하는 코드를 작성합니다.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # 메인 페이지로 이동하는 URL 설정
]

```


# 5. 게시글
## 글 작성
## 글 읽기
## 글 수정
## 글 삭제


# 6. 로그인/로그아웃
## 사용자 계정
## 인증

# 7. 댓글

# 8. 생성AI 활용

# 9. 배포


