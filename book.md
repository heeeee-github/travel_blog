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

#### 가) 가상환경
##### (1) 가상환경 생성
 
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

##### (2) 가상환경 활성화
터미널 창에 아래의 명령어를 입력하여 가상환경을 활성화합니다.
```shell
# window 버전
.venv\Scripts\activate
```
터미널 경로 앞에 가상 환경 이름이 표시되었는지 확인합니다.

##### (3) 가상환경 비활성화
활성화한 가상환경을 더이상 사용하고 싶지 않은 경우, 아래의 명령어를 입력하여 가상환경을 끕니다.
```shell
# window 버전
deactivate
```

#### 나) Django 설치
##### (1) 패키지 설치
Django를 활용한 프로젝트를 개발하기 위하여 아래의 명령어를 입력하여 Django 패키지를 다운로드 합니다.
(패키기 설치 전 가상환경이 활성화되어있는지 터미널 경로 앞에 가상 환경 이름 표시 여부를 확인 후 패키지 설치를 진행합니다.)
```shell
pip install django
```
##### (2) 설치 결과 확인
Django 패키지가 정상적으로 설치되었는지 확인하기 위하여 설치된 패키지 리스트와 패키지 버전을 확인합니다.

**설치된 패키지 리스트 확인**
```shell
pip list # asgiref, Django, pip, setuptools, sqlparse, tzdata
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


#### 다) 프로젝트
##### (1) 프로젝트 생성
Django가 정상적으로 설치된 것이 확인 후 터미널 창에 아래 명령어를 입력하여 프로젝트를 생성합니다.
```shell
django-admin startproject travel_blog .
```

프로젝트 생성 시 주의해야 하는 점은 코드의 온점(.)의 여부에 따라 프로젝트가 생성되는 경로는 달라집니다.
- `travel_blog`는 현재 폴더 안에 `travel_blog`라는 새 폴더를 생성 후 프로젝트 핵심 파일들이 저장됩니다. 즉, 경로는 `travel_blog/travel_blog`가 됩니다.  
- `travel_blog .`은 현재 폴더에 직접 생성됩니다. 추가적인 상위 폴더가 만들어지지 않고, 프로젝트 핵심 파일들이 바로 생성됩니다. 즉, 경로는 `travel_blog`가 됩니다.


##### (2) 프로젝트 설정
Django 프로젝트를 생헌한 후, 프로젝트를 실제로 사용하기 전 여러 가지 설정과 구정을 진행합니다.
- **`DEBUG`** : 개발 중에는 `DEBUG = True`로 설정하지만 배포 시에는 반드시 `False`로 설정합니다.
- **`ALLOWED_HOST`** : 배포 환경에서 서용할 도메인이나 IP 주소를 설정합니다. 
    - `ALLOWED_HOSTS = ['*']` : 모든 호스트에서 접근 가능하도록 설정하기 위해서 입력합니다. 그러나, 보안상 매우 위험하므로 실제 배포 시에는 사용하지 않습니다.
- **`LANGUAGE_CODE`** : 프로젝트의 기본 언어를 설정합니다. `ko-kr`로 설정합니다.
- **`TIME_ZONE`** : 프로젝트의 시간대를 설정합니다. `Asia/Seoul`로 설정합니다.

##### (3) 마이그레이트
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
### 1) 서버 실행
관리자 계정을 활성화화려면 Django 마이그레이션 후 개발 서버를 실행합니다.
```shell
python manage.py runserver
```

### 2) 관리자 페이지
#### 가) 접속
관리자 페이지 접속을 위하여 웹 브라우저에서 다음 URL로 이동합니다.
```
http://127.0.0.1:8000/admin/
```
#### 나) 로그인 및 활성화 확인
생성한 관리자 계정의 사용자 이름과 비밀번호로 로그인합니다. 로그인 후, 관리자 대시보드에 접속할 수 있습니다. 여기에서 사용자를 관리하고, 데이터베이스의 모델을 조회하거나 수정할 수 있습니다.



# 4. 메인화면
## 가. 메인 앱 생성
입장하기 화면을 관리할 새로운 앱 `main`을 생성합니다.

```shell
python manage.py startapp main
```

## 나. URL 설정
### 1) main/urls.py
`main`앱 폴더 안에 `urls.py` 파일을 생성하고 사용자가 웹사이트의 기본 페이지를 접속하였을 때, `home`이라는 함수를 실행하도록 하는 코드를 작성합니다.
- ` path('', views.home , name = 'home')` : 기본주소(공백은 아무것도 추가되지 않은 상태)에 접속하였을 때, views.py에 있는 home이 실행되어 사용자가 볼 페이지를 결정합니다. 해당 경로는 `home`이라는 이름을 사용하여 다른 파일에서 해당 URL 패턴을 참조할 때 `home`이라는 이름을 사용할 수 있습니다.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
]
```

### 2) travel_blog/urls.py
`travel_blog`앱 폴더 안 `urls.py` 에 `main`으로 이동할 수 있도록 urlpattern을 추가합니다.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # 메인 페이지로 이동하는 URL 설정
]

```

## 다. View 설정
이제 메인화면을 렌더링할 뷰를 생성합니다.
이미 생성되어 있는 `main/views.py` 파일에 코드를 작성합니다.
코드는 `home` 연결을 요청할 때, 이후에 작성할 `main/home.html` 로 연결하도록 작성합니다.

```python
from django.shortcuts import render

def home(request) : 
    return render(request, "main/home.html")
```

## 라. Template 설정
마지막으로 `home`화면을 생성합니다. 먼저, 앱과 화면을 구축하기 위하여 스타일링은 진행하지 않습니다.
### 1) 폴더 및 파일 생성

`main`앱 폴더 내에 `templates` 폴더를 만들고, 그 안에 `main`폴더를 생성하여 `home.html` 파일을 생성합니다. 파일 생성 시 `main/templates/main/home.html` 로 한 번에 작성하면 폴더와 파일이 함께 생성됩니다.

### 2) Template 작성
메인 화면과 "입장하기" 버튼을 포함한 기본 템플릿을 작성합니다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>메인 페이지</title>
</head>
<body>
    <h1>환영합니다!</h1>
    <p>여기는 메인 페이지입니다.</p>
    <a href="{% url 'home' %}">
        <button>입장하기</button>
    </a>
</body>
</html>
```
### 3) setting
#### (가) INSTALLED_APPS
마지막으로 Django 프로젝트에 생성한 앱을 연결하는 과정입니다.
`travel_blog/settings.py`에서 `INSTALLED_APPS` 부분에 `main`앱을 연결합니다.
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main", # 추가된 코드
]
```
#### (나) TEMPLATES
Django에서 생성한 `tmeplates`폴더를 알려주는 과정입니다.
Django가 `BASE_DIR/templates/` 경로를 인식하여 그곳에서 템플릿 파일을 찾을 수 있게 설정합니다.
```python
import os
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')], # 추가된 코드
        # "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

## 마. 서버 실행 및 결과 확인
모든 설정이 완료된 후 저장 및 서버를 실행합니다.
```shell
python manage.py runserver
```

다음 URL로 이동하여 결과를 확인합니다.
```
http://127.0.0.1:8000/
```





# 5. 블로그

## 가. 메인 앱 생성
본격적으로 블로그 글과 관련된 기능을 설계하는 단계입니다.
블로그를 관리할 새로운 앱 `blog`을 생성합니다.

```shell
python manage.py startapp blog
```

## 나. Model 설정
블로그의 핵심인 **블로그 글에서 보여줄 정보(데이터)** 를 정의하는 과정입니다. 블로그 방문객들에게 글을 전달하기 위해 필요한 모든 정보를 포함합니다. 

`blog`앱의 `models.py`에서 블로그 글을 표현할 모델, 즉 데이터베이스에 저장할 구조를 정의합니다.

여기서는 아래와 같이 모델을 정의하였습니다.
- 작성글을 구분할 수 있도록 "분류(category)" 기능을 생성합니다.
- 작성글에는 제목(title), 내용(content) ,분류(category), 작성일(created_at) , 수정일(updated_at)으로 구성되도록 생성합니다.

```python
from django.db import models

class Category(models.Model) : 
    name = models.CharField(max_length = 100 , unique = True)
    def __str__(self) : 
        return self.name

class Post(models.Model) : 
    title = models.CharField(max_length = 200)
    content = models.TextField()
    category = models.ForeignKey(Category, related_name = 'posts', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) : 
        return self.title
```

## 다. 마이그레이션 생성 및 적용
모델을 정의한 후 데이터베이스에 모델을 반영하기 위하여 마이그레이션을 생성하고 적용합니다.
```shell
python manage.py makemigrations
python manage.py migrate
```


## 라. CRUD 기능
앞서 설계한 모델을 활용하여 글쓰기/읽기/수정/삭제 기능을 구현하는 과정입니다.

### 1) Form 설계
form은 블로그를 방문하여 **글을 작성하는 사용자에게 어떤 정보를 직접 입력받아 글을 보여줄지 설정**하는 과정입니다. 앞에서 설계한 모델을 바탕으로 입력받고자 하는 항목을 설정합니다.
- 작성글 증 제목(title), 내용(content) ,분류(category)를 사용자가 직접 입력하는 항목으로 설정합니다.

`blog`앱에서 `forms.py`파일을 생성 후 코드를 작성합니다.

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm) : 
    class Meta : 
        model = Post 
        fields = ['title', 'content', 'category']
```



### 2) View 설계
다음으로 `blog`앱의 `views.py`에서 뷰를 구현합니다.
블로그에 작성되어 있는 게시글 목록, 상세 목록, 글 생성, 글 수정, 글 삭제 화면을 구현합니다.

#### 가) 게시글 목록
블로그에 게시 중인 글들을 볼 수 있는 목록 화면을 구현합니다.
```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
```

#### 나) 상세 내용
게시 중인 글 하나를 클릭하였을 때, 세세한 내용을 볼 수 있는 화면을 구성합니다.
```python
# 이어서 작성합니다.
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
```
> `get_object_or_404` 란?
>
> Django에서 특정 객체를 데이터베이스에서 조회할 때, 해당 객체가 존재하지 않을 경우 HTTP404오류를 자동으로 발생시키는 유용한 내장함수 입니다. 
> 블로그 앱에서 객체는 각 게시번호(pk)에 해당하는 블로그 글 1개를 뜻합니다.


#### 다) 글 생성
게시 중인 글 외 새로운 글을 작성하는 화면을 구성합니다. 이 때 앞에서 설계한 폼(From)을 사용하여 사용자가 입력하는 정보를 받아 데이터베이스에 저장합니다.

글 생성이 완료된 후에는 글 목록으로 돌아가 글 생성 결과를 확인할 수 있도록 설계합니다.
```python
# 이어서 작성합니다.
from django.shortcuts import redirect # redirect를 추가합니다.
from .forms import PostForm  # PorstForm을 활용합니다.

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})
```
> `redirect` 란?
>
> Django의 `shortcuts` 모듈에서 제공하는 함수로 사용자가 다른 페이지로 이동시키는 기능입니다. 
> 
>사용자가 데이터를 제출(글 작성), 상태 변경(글 수정), 작업 완료(글 삭제) 등 데이터 입력을 처리하거나 상태를 변경하는 경우 다른 페이지로 이동(`redirect`)시킵니다.
>
>단순히 정보를 표시하는 단계(글 목록, 세부 정보)는 기존에 있는 정보에서 변경되는 과정이 없으므로 `redirect` 기능이 필요하지 않습니다.


#### 라) 글 수정 
게시 중인 글에서 글을 수정하는 화면을 구성합니다. 수정 가능한 범위는 앞에서 설계한 폼(From)으로 제한하며, 글 수정이 완료된 후에는 세부 정보로 돌아가 수정 내용을 확인할 수 있도록 설계합니다.
```python
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_update.html', {'form': form})
```

#### 마) 글 삭제
마지막으로 글을 삭제하는 기능입니다.

삭제하고자 하는 글이 존재하는지 확인하는 과정을 거쳐, 글 존재하지 않는 경우 404 오류를 발생시킵니다.

삭제하려는 글이 존재하는 경우 "삭제 확인 화면"을 사용자에게 보여주도록 합니다. 이후 글 삭제가 완료되면 글 목록 화면으로 이동하도록 설계합니다.
```python
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_delete.html', {'post': post})
```

### 3) URL 설정
#### 가) blog/urls.py
`blog`앱 폴더 안에 `urls.py` 파일을 생성하고 사용자가 웹사이트의 기본 페이지를 접속하였을 때, `home`이라는 함수를 실행하도록 하는 코드를 작성합니다.
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_update, name='post_update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]
```

#### 나) travel_blog/urls.py
`travel_blog`앱 폴더 안 `urls.py` 에 `blog`로 이동할 수 있도록 url을 추가합니다.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), 
    path('blog/', include('blog.urls')), # 추가된 코드
]

```

### 4) Template 작성
#### 가) 폴더 및 파일 생성
`blog`앱 폴더 내에 `templates` 폴더를 만들고, 그 안에 `blog`폴더를 생성하여 템플릿 파일을 생성합니다.
- 생성해야 할 파일 목록(5종) : `post_list.html`,  `post_detail.html`,  `post_create.html`,  `post_update.html`,  `post_delete.html`

#### 나) 글 목록 템플릿
(`post_list.html`) 블로그 게시글 목록을 보여주는 템플릿입니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>게시글 목록</title>
</head>
<body>
    <h1>게시글 목록</h1>
    <ul>
        {% for post in posts %}
            <li>
                <a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a>
                <a href="{% url 'post_update' post.pk %}">수정</a>
                <a href="{% url 'post_delete' post.pk %}">삭제</a>
            </li>
        {% empty %}
            <li>게시글이 없습니다.</li>
        {% endfor %}
    </ul>
    <a href="{% url 'post_create' %}">새 게시글 작성하기</a>
</body>
</html>

```
#### 다) 상세 내용 템플릿
(`post_detail.html`) 상세 내용을 보여주는 템플릿입니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
    <p>카테고리: {{ post.category.name }}</p>
    <p>게시일: {{ post.created_at }}</p>
    <p>수정일: {{ post.updated_at }}</p>
    <a href="{% url 'post_update' post.pk %}">수정</a>
    <a href="{% url 'post_delete' post.pk %}">삭제</a>
    <a href="{% url 'post_list' %}">글 목록</a>
</body>
</html>
```

#### 라) 글 생성 템플릿
(`post_create.html`) 글 생성 화면을 보여주는 템플릿입니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <title>글 작성</title>
</head>
<body>
    <h1>글 작성</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}  <!-- 폼을 단락으로 렌더링 -->
        <button type="submit">저장</button>  
    </form>
    <a href="{% url 'post_list' %}">목록</a> 
</body>
</html>
```
#### 마) 글 수정 템플릿
(`post_update.html`) 글 수정 화면을 보여주는 템플릿입니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <title>{% if form.instance.pk %}수정{% else %}작성{% endif %} 게시</title>
</head>
<body>
    <h1>{% if form.instance.pk %}수정{% else %}작성{% endif %} 게시</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">저장</button>
    </form>
    <a href="{% url 'post_list' %}">목록</a>
</body>
</html>
```

#### 바) 글 삭제 템플릿
(`post_delete.html`) 글 삭제 화면을 보여주는 템플릿입니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <title>글 삭제</title>
</head>
<body>
    <h1>글 삭제</h1>
    <p> <strong>"{{ post.title }}"</strong>글을 삭제하시겠습니까? </p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">삭제</button>
    </form>
    <a href="{% url 'post_list' %}">취소</a>
</body>
</html>
```

## 마. 카테고리 검색 기능
카테고리를 선택하여 해당 카테고리에 속하는 게시물만 필터링하는 기능을 생성합니다. 

### 1) View 작성
카테고리를 기준으로 게시물을 검색하는 뷰를 먼저 작성합니다. `blog/views.py`에 아래의 코드를 작성합니다.

```python
# 이어서 작성
def posts_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)

    return render(request, 'blog/posts_by_category.html', {'category': category, 'posts': posts})

```

### 2) URL 패턴 설정  
다음으로 URL 패턴을 설정합니다. `blog/urls.py`에 아래의 코드를 작성합니다.
```python
# 이어서 작성
urlpatterns = [
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'), # 추가된 코드
]
```

### 3) Template 작성
이제 검색 결과를 표시할 템플릿을 작성하는 과정입니다. `posts_by_category.html` 파일을 생성하고 아래의 코드를 작성합니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <title>{{ category.name }} 게시글 목록</title>
</head>
<body>
    <h1>게시글 목록 in {{ category.name }}</h1>

    {% if posts %}
        <ul>
            {% for post in posts %}
                <li>
                    <a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a>
                </li>
            {% endfor %}
        </ul>
    {% else %}
        <p>게시글이 없습니다.</p>
    {% endif %}

    <a href="{% url 'post_list' %}">목록으로 돌아가기</a>
</body>
</html>
```

### 4) 업데이트
#### Template 업데이트
카테고리별로 게시물을 검색할 수 있도록 카테고리를 선택할 수 있는 드롭다운이나 링크 목록을 메인페이지에 추가합니다. `post_list.html`을 업데이트합니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <title>All Posts</title>
</head>
<body>
    <h1>All Posts</h1>

    <div>
        <h2>Filter by Category</h2>
        <ul>
            {% for category in categories %}
                <li><a href="{% url 'posts_by_category' category.id %}">{{ category.name }}</a></li>
            {% endfor %}
        </ul>
    </div>

    <ul>
        {% for post in posts %}
            <li>{{ post.title }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```
#### View 업데이트
`blog/views.py`에 작성되어 있는 `post_list`를 재정의합니다.
글 뿐만 아니라 카테고리 정보까지 함께 가져오는 코드로 수정합니다.

```python
def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()  # 모든 카테고리 가져오기
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})
```

> **`blog/views.py`에서 `posts_by_category`를 작성했는데, `post_list`를 업데이트 하는 이유**
>
> 두 함수는 다른 화면을 보여주기 위해 정의합니다.  
> **`post_list`** 는 블로그의 모든 글을 보여주며, **`posts_by_category`** 는 선택한 카테고리애 해당하는 글들만 필터링이 되어 화면에 보여줍니다.



## 바. 시간순 게시글 정렬 기능
게시된 글들을 최근 작성일순으로 정렬하는 기능을 추가합니다.

### 1) View 수정
#### 가) post_list
`blog/views.py`의 `post_list` 정의에 글을 최근 작성일 순으로 정리하는 코드를 추가합니다.
- `order_by('-created_at')` : 작성일(`created_at`)의 역순(`-`)인 최근일자부터 정렬하는 코드입니다.
```python

def post_list(request):
    posts = Post.objects.all().order_by('-created_at') # 수정된 코드
    categories = Category.objects.all()  
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})


```

#### 나) posts_by_category
`blog/views.py`의 `posts_by_category` 정의에 글을 최근 작성일 순으로 정리하는 코드를 추가합니다.

```python
def posts_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category).order_by('-created_at') # 수정된 코드
    return render(request, 'blog/posts_by_category.html', {'category': category, 'posts': posts})
```


### 2) Template 수정
#### 가) post_list
`blog/templates/blog/post_list.html`에 글의 작성일을 보여주는 코드를 추가합니다.
```HTML
<ul>
    {% for post in posts %}
        <li>
            <!-- 수정된 코드 -->
            <a href="{% url 'post_detail' post.pk %}">{{ post.title }}  -  {{ post.created_at}}  </a> 
        </li>
    {% empty %}
        <li>게시글이 없습니다.</li>
    {% endfor %}
</ul>
```

#### 나) posts_by_category
`blog/templates/blog/posts_by_category.html`에 글의 작성일을 보여주는 코드를 추가합니다.

```HTML
<!-- 수정된 코드 -->
{% for post in posts %}
    <li>
        <a href="{% url 'post_detail' post.pk %}">{{ post.title }}  -  {{ post.created_at}}  </a>
    </li>
{% endfor %}
```



## 사. main App 업데이트
앞서 생성한 `main`앱에서 "입장하기" 버튼을 눌렀을 대 `blog`앱의 블로그 페이지가 표시되도록 설계하는 단계입니다.

### 1) View 업데이트
`main`앱의 `main/views.py` 파일에서 `enter_blog` 뷰를 추가하여 블로그 페이지로 이동하도록 정의합니다.
```python
# 추가 작성
from django.shortcuts import redirect
def enter_blog(request) : 
    return redirect('post_list')
```

### 2) URL 업데이트
`main`앱의 `main/urls.py` 파일에서 보여지는 화면(redirection)을 처리할 뷰를 추가합니다.
```python
# 추가 작성
urlpatterns = [
    path('enter_blog/', views.enter_blog, name='enter_blog'),  # 블로그로 이동하는 URL
]
```

### 3) Template 업데이트
"입장하기" 버튼을 클릭하였을 때 이동하는 링크를 변경합니다.
- `main`앱의 `templates/main/home.html` 파일에서 기존에 연결한 'home'에서 'enter_blog'로 변경합니다. 
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>메인 페이지</title>
</head>
<body>
    <h1>환영합니다!</h1>
    <p>여기는 메인 페이지입니다.</p>
    <!-- 아래 부분을 'home'에서 'enter_blog'로 변경 -->
    <a href="{% url 'enter_blog' %}"> 
        <button>입장하기</button>
    </a>
</body>
</html>
```

## 아. setting
### INSTALLED_APPS
마지막으로 Django 프로젝트에 생성한 앱을 연결하는 과정입니다.
`travel_blog/settings.py`에서 `INSTALLED_APPS` 부분에 `main`앱을 연결합니다.
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main", 
    "blog",  # 추가된 코드
]
```

## 자. 관리자 사이트 연결
블로그 글을 Django 관리자(admin)화면에서 "Category", "Post" 섹션을 관리할 수 있도록 연결합니다.
`blog/admin.py` 파일에 아래의 코드를 입력 후 저장합니다.
```python
from django.contrib import admin
from .models import Category, Post

admin.site.register(Category)
admin.site.register(Post)
```

## 차. 서버 실행 및 결과 확인
모든 설정이 완료된 후 저장 및 서버를 실행합니다.
```shell
python manage.py runserver
```

다음 URL로 이동하여 결과를 확인합니다.
```
http://127.0.0.1:8000/
```



# 6. 회원가입 및 로그인/아웃
회원을 관리하기 위해 회원가입 및 로그인/아웃기능을 설계하는 단계입니다.

## 가. 메인 앱 생성
회원읠 관리할 새로운 앱 `accounts`를 생성합니다.

```shell
python manage.py startapp accounts
```

## 나. 회원가입 기능 추가
### 1) Form 설계
회원가입 때 받을 사용자 정보를 
`accounts`앱에서 `forms.py`파일을 생성 후 코드를 작성합니다.
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm) : 
    email = forms.EmailField(required= True, label = '이메일 주소')

    class Meta : 
        model = User
        fields = ('username', 'email', 'password1','password2')
```
### 2) View 설계
`forms.py`에서 설계한 `SignUpForm` 받아 회원가입 화면을 보여주는 단계입니다.
`accounts/views.py` 파일에서 회원가입 후 
```python
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
```
### 3) URL 설계 
회원가입 URL 설정을 위하여 `accounts/urls.py` 파일을 생성하고 코드를 작성합니다.
```python
from django.urls import path
from .views import signup
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
]
```

### 4) Template 설정
#### 가) 폴더 및 파일 생성
`accounts`앱 폴더 내에 `templates` 폴더를 만들고, 그 안에 `accounts`폴더를 생성하여 `signup.html` 파일을 생성합니다. 파일 생성 시 `accounts/templates/accounts/signup.html` 로 한 번에 작성하면 폴더와 파일이 함께 생성됩니다.

#### 나) Template 작성
회원가입을 위한 기본 화면을 작성합니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <title>회원가입</title>
</head>
<body>
    <h2>회원가입</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">가입하기</button>
    </form>
</body>
</html>
```

>**`{% csrf_token %}`을 사용하는 이유**
>
> **CSRF(Cross-Site Request Forgery)** 는 사용자가 로그인된 상태에서 악의적인 웹페이지가 사용자의 권한으로 요청을 보내는 공격 방식입니다. 예를 들어, 금융사이트에 로그인한 상태에서 악의적인 웹페이지를 방문하면 해당 웹페이지에서 금융 계좌에 이체 요청을 보낼 수 있습니다.
>
> **CSRF token** 은 이러한 공격을 방지하기 위하여 사용합니다.
> * 사용자가 페이지를 요청할 때 서버가 랜덤 토큰을 생성하여 사용자에게 전달합니다. 이 토큰은 서버에서만 알고 있는 값입니다.
> * 생성된 랜덤 토큰은 HTML에 포함되어 사용자에게 전송됩니다. 폼이 제출될 때 함께 전송하도록 합니다.
> * 사용자가 폼을 제출하면 서버는 요청에 포함된 토큰과 서버에 저장된 토큰이 일치하는지 비교 후 요청을 처리합니다. 일지하지 않는 경우 요청을 거부합니다.


## 다. 로그인/로그아웃

### 1) URL 설정
#### 가) accounts/urls.py
기존에 작성한 `accounts/urls.py` 파일에 로그인과 로그아웃 url 코드를 작성합니다.
```python
from django.urls import path
from .views import signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),#추가된 코드
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), #추가된 코드
]

```
#### 나) blog/urls.py
연결할 앱의 url 파일을 열어 `accounts`앱의 URL을 추가합니다.
```python
# 이어서 작성
from django.urls import  include

urlpatterns = [
    # 다른 URL 패턴들...
    path('accounts/', include('accounts.urls')),
]
```

#### 다) travel_blog/urls.py
연결할 앱의 url 파일을 열어 `accounts`앱의 URL을 추가합니다.
```python
# 이어서 작성
urlpatterns = [
    # 다른 URL 패턴들...
    path('accounts/', include('accounts.urls')), # 추가된 코드
]
```

### 2) Template 설정
#### 가) login
(`login.html`) 로그인 화면을 보여주는 템플릿을 `accounts/templates/accounts` 폴더에 생성합니다.
CSRF토큰을 사용하여 보안을 유지하며, 폼 필드를 자동으로 렌더링합니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <title>로그인</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1>로그인 페이지</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">로그인</button>
    </form>
</body>
</html>

```
#### 나) logout
(`logout.html`) 로그인 화면을 보여주는 템플릿을 `accounts/templates/accounts` 폴더에 생성합니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <title>로그아웃</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1>로그아웃되었습니다.</h1>
    <p>로그아웃이 완료되었습니다. <a href="{% url 'login' %}">로그인 페이지로 돌아가기</a></p>
</body>
</html>
```

### 3) Update 
위의 과정에서 생성된 login, logout 화면을 `accounts/urls.py`에서 받을 수 있게 수정하고, `blog` 화면에 보여지도록 개선합니다.

#### 가) URL 설정
기존에 작성한 `accounts/urls.py` 파일에 `template_name=` 코드를 추가하여 로그인과 로그아웃 html 파일 경로를 설정합니다.
```python
urlpatterns = [
    # 생략
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),#추가된 코드
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'), #추가된 코드
]
```

#### 나) blog/post_list.html
사용자 계정과 관련된 페이지로의 링크를 추가합니다.
```HTML
<body>
    <h1>게시글 목록</h1>
    <!-- 사용자 계정 관련 링크 추가 -->
    <div>
        <a href="{% url 'signup' %}">회원가입</a> |
        <a href="{% url 'login' %}">로그인</a> |
        <form action="{% url 'logout' %}" method="post">
            {% csrf_token %}
            <button type="submit">로그아웃</button>
        </form>
    </div>
    <!-- 생략 -->
</body>
```
>왜 `로그아웃`은 회원가입, 로그인과 다르게 `form` 형태로 작성할까?
> 회원가입(`signup.html`)과 로그인(`login.html`)은 `{% csrf_token %}` 코드가 입력되어 사용자(토큰) 일치 여부를 확인할 수 있습니다. 그러나 `logout.html`에는 해당 과정이 작성되어 있지 않습니다.
>
> 또한, 로그아웃 처리는 POST 요청을 통해 이루어집니다. 회원가입, 로그인과 동일하게 `<a href = >` 형태로 받게되면 GET 요청으로 로그아웃으로 시도하며 `405 Methoed Not Allowed` 오류가 발생합니다.
>
> 따라서 로그아웃 링크를 `<form>`을 사용하여 POST 요청을 보내 로그아웃 과정을 진행합니다.


## 라. setting
### 1) settings.py 설정
#### 가) INSTALLED_APPS
마지막으로 Django 프로젝트에 생성한 앱을 연결하는 과정입니다.
`travel_blog/settings.py`에서 `INSTALLED_APPS` 부분에 `accounts`앱을 연결합니다.

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
    "blog",
    "accounts",     # 추가된 코드
]
```

#### 나) REDIRECT_URL
사용자가 로그인하거나 로그아웃한 후 보여질 URL을 지정합니다.

여기서는 게시글 목록확인 및 CRUD 제한 기능을 확인하기 위하여 `/blog/`로 URL을 지정합니다.

```python
LOGIN_REDIRECT_URL = '/blog/'
LOGOUT_REDIRECT_URL = '/blog/'
```

> **`REDIRECT_URL`**
> 
> REDIRECT_URL은 웹 애플리케이션에서 사용자가 특정 화면이나 동작을 수행한 후 자동으로 다른 화면으로 이동하도록 하는 URL을 지정할 때 사용합니다.
> 
> 기본 설정은 `'/'` 명령어를 사용하며 기본 화면으로 돌아가도록 합니다. 특정 화면을 보여주고 싶은 경우, 해당 화면을 볼 수 있도록 설정할 수 있습니다.
> 여기서는 `'/'` 으로 설정할 경우 "입장하기"화면이 보이는 기본화면으로 이동합니다. 만약 `'/blog/'` 로 설정할 경우 글 목록이 보이는 화면으로 이동합니다.


## 마. 서버 실행 및 결과 확인
모든 설정이 완료된 후 저장 및 서버를 실행합니다.
```shell
python manage.py runserver
```

다음 URL로 이동하여 결과를 확인합니다.
```
http://127.0.0.1:8000/
```

# 7. 사용자 인증
기존에 작성된 CRUD 기능에서 로그인한 사용자만 접근할 수 있도록 권한을 설정하는 단계입니다. DJango의 사용자 인증 시스템을 활용하여 접근을 제어합니다.

## 가. Model 업데이트
### 1) Medel에 작성자 필드 추가
먼저, 게시글을 작성한 사용자를 기록하기 위하여 앞서 작성한 `Post`모델에 작성자(`author`)필드를 추가합니다.
```python
from django.contrib.auth.models import User # 추가된 코드
from django.db import models

class Category(models.Model) : 
    name = models.CharField(max_length = 100 , unique = True)
    def __str__(self) : 
        return self.name

class Post(models.Model) : 
    title = models.CharField(max_length = 200)
    content = models.TextField()
    category = models.ForeignKey(Category, related_name = 'posts', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 추가된 코드

    def __str__(self) : 
        return self.title
```

### 2) 마이그레이션 생성 및 적용
모델을 재정의한 후 데이터베이스에 모델을 반영하기 위하여 마이그레이션을 생성하고 적용합니다.
```shell
python manage.py makemigrations
python manage.py migrate
```

> **`It is impossible to add a non-nullable field 'author' to post without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:` 알림이 뜨는 경우**
> 
> 해당 메세지는 Django에서 새로운 필드를 기존 모델에 추가할 때 발생하는 오류입니다. 이를 해결하기 위하여 데이터베이스의 기존 행(데이터)에 새로 추가하는 필드의 값을 제공해야 합니다. (필드를 추가할 때 null = False로 설정되면 해당 필드는 비워둘 수 없기때문에 기존 데이터에 어떤 값으로 채울지를 Django에서 요청합니다.)
>
> 기본값(Default) 설정 / Null 허용 / One-off Defult 지정 / DB에서 직접 처리 방법 중 "기본값(Default) 설정"으로 진행합니다.  
> "1) Provide a one-off default now (will be set on all existing rows with a null value for this column)"  
> "2) Quit and manually define a default value in models.py."   
> 답변 중 "2"를 입력 후  
>
> `models.py`에서 "author = models.ForeignKey(User, on_delete=models.CASCADE, default=1) " 로 코드를 변경 후 재진행합니다. 
>

## 나. View에서 사용자 인증 확인
### 1) 글 작성 제한
로그인한 사용자만 게시글을 작성할 수 있도록 뷰를 수정합니다.
`blog/views.py` 파일에서 로그인 데코레이터 기능을 사용할 수 있도록 기능을 가져옵니다. 이후 게시글 작성 정의에 `@login_required` 데코레이터 추가 및 게시글 작성 과정을 보완합니다. 

> 로그인 데코레이터(`@login_required`)는 사용자가 로그인을 하지 않은 경우 로그인 페이지로 이동합니다.

```python
from django.contrib.auth.decorators import login_required

# post_create 부분을 수정합니다.
@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

```

> **`post.save()`에서 `post = form.save(commit=False)`로 변경한 이유**
>
> `post.save()`는 저금통에 돈을 넣는 것과 비슷합니다. 돈을 넣는 순간 돈은 바로 저금통에 들어가는 것처럼, 입력한 데이터가 바로 데이터 베이스에 저장됩니다.
>
> `post = form.save(commit=False)`는 돈을 저금통에 넣기 전 손에 들고 있는 것과 같습니다. 손에 들고 있는 돈을 다시 한 번 확인하거나 추가 또는 변경할 수 있습니다. 최종 확인 후 저금통에 돈을 넣는 것처럼 사용자가 데이터를 입력 후 추가 또는 수정의 과정을 거쳐 데이터베이스에 저장됩니다.

### 2) 글 수정 및 삭제 제한

게시글 수정 또는 삭제 기능의 경우 작성자만 접근할 수 있도록 변경합니다.
```python
from django.core.exceptions import PermissionDenied

# post_update 부분을 수정합니다.
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user:  
        raise PermissionDenied  
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'post_update.html', {'form': form})

# post_delete 부분을 수정합니다.
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user: 
        raise PermissionDenied  
    
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    
    return render(request, 'post_confirm_delete.html', {'post': post})
```

## 다. Template 수정
템플릿에서는 아래의 내용으로 개선합니다.
- 상세 내용 화면에서 작성자 정보를 제공합니다.
- 글 작성 링크를 로그인한 사용자에게만 보여주도록 작성합니다.
- 수정 및 삭제 링크를 작성자에게만 보여주도록 작성합니다.

### 1) 글 목록 템플릿
`blog/templates/blog/post_list.html` 파일에서 아래의 내용을 수정합니다. 
- 로그인한 사용자에게만 글 작성 버튼을 보여줍니다.
- 작성자와 현재 사용자가 같은 경우 글 수정 및 삭제 버튼을 보여주도록 코드를 추가합니다. 
```HTML
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>게시글 목록</title>
</head>
<body>
    <h1>게시글 목록</h1>
    <div>
        <a href="{% url 'signup' %}">회원가입</a> |
        <a href="{% url 'login' %}">로그인</a> |
        <form action="{% url 'logout' %}" method="post" style="display:inline;">
            {% csrf_token %}
            <button type="submit">로그아웃</button>
        </form>
    </div>

    <div>
        <h2>카테고리별 필터링</h2>
        <ul>
            <li><a href="{% url 'post_list' %}">전체</a></li>
            {% for category in categories %}
                <li><a href="{% url 'posts_by_category' category.id %}">{{ category.name }}</a></li>
            {% endfor %}
        </ul>
    </div>

    <ul>
        {% for post in posts %}
            <li>
                <a href="{% url 'post_detail' post.pk %}">{{ post.title }}  -  {{ post.created_at}}  </a>
                {% if post.author == request.user %}  
                <a href="{% url 'post_update' post.pk %}">수정</a>
                <a href="{% url 'post_delete' post.pk %}">삭제</a>
            {% endif %}            
            </li>
        {% empty %}
            <li>게시글이 없습니다.</li>
        {% endfor %}
    </ul>

    {% if user.is_authenticated %}
        <a href="{% url 'post_create' %}">새 게시글 작성하기</a>
    {% endif %}
</body>
</html>


```

### 2) 상세 내용 템플릿
`blog/templates/blog/post_detail.html` 파일에 작성자 정보를 제공하는 코드를 추가합니다. 또한, 로그인한 사용자에게만 글 작성 버튼을 보여주고, 작성자와 현재 사용자가 같은 경우 글 수정 및 삭제 버튼을 보여주도록 코드를 추가합니다. 
```HTML
<!DOCTYPE html>
<html>
<head>
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
    <p>카테고리: {{ post.category.name }}</p>
    <p>작성자: {{ post.author }}</p>
    <p>게시일: {{ post.created_at }}</p>
    <p>수정일: {{ post.updated_at }}</p>
    {% if post.author == request.user %}  
        <a href="{% url 'post_update' post.pk %}">수정</a>
        <a href="{% url 'post_delete' post.pk %}">삭제</a>
    {% endif %}
    <a href="{% url 'post_list' %}">글 목록</a>
</body>
</html>
```















































# 8. 댓글

# 9. 생성AI 활용

# 10. 배포

# 11. 추가 기능
# 사진 업로드

# 게시글 조회수

# 댓글(앞 부분에서 제외 시 추가 기능으로 작성)
## 댓글 추가
## 댓글 수정
## 댓글 삭제
## 대댓글

# 마이페이지
## 비밀번호 변경
## 프로필 수정
## 닉네임 추가

# 파일 모으기

# 번역



# 12. 참고
## 가. URL 패턴 확인
`django-extensions` 패키지를 활용하여 URL 패턴을 확인할 수 있습니다.
먼저, 패키지를 설치 합니다.
```shell
pip install django-extensions
```
다음으로 `settings.py` 파일에서 `INSTALLED_APPS` 부분에 `django_extensions`를 추가합니다. 패키지 명에는 하이픈(-)을 사용하지만 설정파일에 추가하는 이름에는 언더바(_)로 입력해야하는 점을 주의합니다.

마지막으로 명령어를 작성하여 URL 패턴을 확인합니다.
```shell
python manage.py show_urls
```

## 나. git commit imoji
### 주요 이모지와 의미
| 이모지  | 코드 (`:`)        | 의미                              |
|---------|-------------------|-----------------------------------|
| 🎉      | `:tada:`          | 새로운 프로젝트 시작, 초기 커밋   |
| ✨      | `:sparkles:`      | 새로운 기능 추가                  |
| 🐛      | `:bug:`           | 버그 수정                         |
| 🔨      | `:hammer:`        | 코드 리팩토링                     |
| 📝      | `:memo:`          | 문서 추가 또는 수정               |
| 💄      | `:lipstick:`      | UI 또는 스타일 관련 수정          |
| 🚀      | `:rocket:`        | 성능 개선                         |
| 🔥      | `:fire:`          | 코드나 파일 삭제                  |
| 🚑️     | `:ambulance:`     | 긴급 수정                         |
| 🔧      | `:wrench:`        | 설정 파일 수정                    |
| 🚨      | `:rotating_light:`| 린트 규칙 등 코드 규칙 관련 수정  |
| 🔒      | `:lock:`          | 보안 문제 해결                    |
| ♻️      | `:recycle:`       | 코드 구조 변경 (리팩토링)         |
| ➕      | `:heavy_plus_sign:`| 의존성 추가                      |
| ➖      | `:heavy_minus_sign:`| 의존성 제거                     |
| ⬆️      | `:arrow_up:`      | 의존성 버전 업그레이드            |
| ⬇️      | `:arrow_down:`    | 의존성 버전 다운그레이드          |
| 🚧      | `:construction:`  | 작업 진행 중 (WIP: Work In Progress) |
| 🔍      | `:mag:`           | 검색, 탐색 기능 관련 수정         |
| 💚      | `:green_heart:`   | CI 빌드 통과                      |
