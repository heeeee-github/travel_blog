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
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],  # 추가된 코드
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
블로그에 작성되어 있는 게시글 목록, 상세 내용, 글 생성, 글 수정, 글 삭제 화면을 구현합니다.

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
def posts_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
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
                <li><a href="{% url 'posts_by_category' category.pk %}">{{ category.name }}</a></li>
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
        {% if not request.user.is_authenticated %}
        <a href="{% url 'signup' %}">회원가입</a> |
        <a href="{% url 'login' %}">로그인</a> |
        {% endif %}

        {% if request.user.is_authenticated %}
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
LOGIN_REDIRECT_URL = "/blog/"
LOGOUT_REDIRECT_URL = "/blog/"
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

# 8. 파일 업로드

## 가. 단일 파일 업로드
단일 파일 업로드 방법은 `Model`에서 Post내에 파일을 받는 필드를 설정합니다.

### 1) setting

#### 가) 패키지 설치
Django에서 이미지, 영상, 음악 파일을 업로드하고 처리하기 위해서는 `pillow`패키지가 필요합니다. 해당 패키지는 이미지 처리와 관련된 기능을 제공하며, Django의 `ImageField`를 사용할 수 있습니다. (영상, 음악)
```shell
python -m pip install pillow
```

#### 나) travel_blog/settings.py
업로드된 파일을 받기 위하여 미디어 파일의 경로를 새로 생성합니다.

먼저, `travel_blog` 폴더에 `media` 파일을 생성합니다.
```shell
mkdir media
```
이후 `travel_blog/travel_blog/settings.py`에서 파일 경로를 설정합니다.
```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

#### 다) travel_blog/urls.py
다음으로 미디어 파일을 제공할 수 있도록 `urls.py`에서 설정을 추가합니다.
- `from django.conf import settings` : Django의 `settings.py`에 접근할 수 있도록 설정 후 미디어 파일의 URL과 저장 경로를 가져옵니다.
- `from django.conf.urls.static import static` : 미디어 파일을 서빙하기 위한 

```python

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 기존 URL 패턴들
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

### 2) Model 수정
#### 가) Models.py 작성
파일을 업로드 할 수 있는 기능을 추가하는 과정입니다. 파일은 사진, 영상, 음악을 각각 분류하여 파일을 받습니다.
- 사진 : `ImageField`로 사진을 저장합니다.
- 영상 : `FielField`로 영상을 저장합니다. 
- 음악 : `FielField`로 음악을 저장합니다. 

`blog/models.py`에서 아래의 코드를 추가합니다.
```python
class Post(models.Model) : 
    # 생략
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    audio = models.FileField(upload_to='audios/', blank=True, null=True) 
    # 생략
```
#### 나) 마이그레이션 생성 및 적용
모델을 재정의한 후 데이터베이스에 모델을 반영하기 위하여 마이그레이션을 생성하고 적용합니다.
```shell
python manage.py makemigrations
python manage.py migrate
```

### 3) Form 수정
업로드 파일을 받을 수 있도록 폼을 수정합니다.
`blog/forms.py`에서 아래의 코드를 추가합니다.
```python
class PostForm(forms.ModelForm) : 
    class Meta : 
        model = Post 
        fields = ['title', 'content', 'category', 'image', 'video','audio'] # 수정된 코드
```

### 4) View 수정
사진, 영상, 음악을 포함한 데이터가 제대로 저장될 수 있도록 뷰도 수정합니다.  
`post_create` , `post_update` 의 `PostForm` 부분에 `request.POST` 외에도 `request.FILES`를 추가하여 form과 함께 파일이 업로드 되도록 작성합니다.

```python
@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES) # 수정된 코드
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user:  
        raise PermissionDenied  
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post) # 수정된 코드
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_update.html', {'form': form})

```

### 5) 템플릿 수정
마지막으로 이미지와 영상을 표시할 수 있도록 템플릿을 수정합니다.

#### 가) blog/post_create.html
글을 작성할 때 HTML 폼에서 파일 업로드를 처리할 때 사용하는 중요한 속성을 `post_create.html`에  추가해야 합니다.
`enctype="multipart/form-data"` 코드를 추가하여 다음의 동작 과정을 거쳐 데이터를 받을 수 있게 설정합니다.
- 폼 제출 : 사용자가 폼을 제출하면 브라우저는 입력된 텍스트와 선택된 파일을 서버로 전송합니다.
- 데이터 인코딩 : 텍스트 필드 데이터와 파일 데이터로 각각 나누어 인코딩 합니다.
- 서버 처리 : 텍스트 데이터는 `request.POST`로, 파일 데이터는 `request.FILES`로 접근합니다.
```HTML
    <!-- 생략 -->
    <!-- 수정된 코드 -->
    <form method="post" enctype="multipart/form-data"> 
    <!-- 생략 -->
```

#### 나) blog/post_detail.html
글의 상세 내용을 보여주는 `post_detail.html`에 표시될 수 있도록 추가합니다.
`style="max-width: 100%; height: auto;"` 코드를 사용하여 보여주는 영상 또는 이미지의 크기를 제한합니다.
```HTML
    <!-- 생략 -->
<body>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
    <p>카테고리: {{ post.category.name }}</p>
    <p>작성자: {{ post.author }}</p>
    <p>게시일: {{ post.created_at }}</p>
    <p>수정일: {{ post.updated_at }}</p>
    
    {% if post.image %}
        <img src="{{ post.image.url }}" alt="Post Image" style="max-width: 100%; height: auto;">
    {% endif %}
    {% if post.video %}
        <video controls>
            <source src="{{ post.video.url }}" type="video/mp4" style="max-width: 100%; height: auto;">
        </video>
    {% endif %}
    {% if post.audio %}
        <audio controls>
            <source src="{{ post.audio.url }}" type="audio/mpeg" >
        </audio>
    {% endif %}
    <!-- 생략 -->
</body>
</html>

```


## 나. 다중 파일 업로드
다중 파일 업로드 방법은 `Model`에서 Post 내에 파일을 받는 방법이 아닌, 각각 생성하여 Post와 연결합니다.
### 1) setting
setting은 단일 파일 업로드와 크게 다르지 않습니다. 해당 과정을 진행하였다면 생략 가능합니다.

#### 가) 패키지 설치
Django에서 이미지, 영상, 음악 파일을 업로드하고 처리하기 위해서는 `pillow`패키지가 필요합니다. 해당 패키지는 이미지 처리와 관련된 기능을 제공하며, Django의 `ImageField`를 사용할 수 있습니다. (영상, 음악)
```shell
python -m pip install pillow
```

#### 나) travel_blog/settings.py
업로드된 파일을 받기 위하여 미디어 파일의 경로를 새로 생성합니다.

먼저, `travel_blog` 폴더에 `media` 파일을 생성합니다.
```shell
mkdir media
```
이후 `travel_blog/travel_blog/settings.py`에서 파일 경로를 설정합니다.
```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```
#### 다) travel_blog/urls.py
다음으로 미디어 파일을 제공할 수 있도록 `urls.py`에서 설정을 추가합니다.
- `from django.conf import settings` : Django의 `settings.py`에 접근할 수 있도록 설정 후 미디어 파일의 URL과 저장 경로를 가져옵니다.
- `from django.conf.urls.static import static` : 미디어 파일을 서빙하기 위한 

```python

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 기존 URL 패턴들
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```


### 2) Model 수정
#### 가) Models.py
파일을 업로드 할 수 있는 기능을 추가하는 과정입니다. 파일은 사진, 영상, 음악을 각각 분류하여 파일을 받습니다.
- 사진 : `ImageField`로 사진을 저장합니다.
- 영상 : `FielField`로 영상을 저장합니다. 
- 음악 : `FielField`로 음악을 저장합니다. 

`blog/models.py`에서 아래의 코드를 추가합니다.
```python
# 생략 
class Post(models.Model) : 
    title = models.CharField(max_length = 200)
    content = models.TextField()
    category = models.ForeignKey(Category, related_name = 'posts', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    
    def __str__(self) : 
        return self.title

class Image(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for {self.post.title}"

class Video(models.Model):
    post = models.ForeignKey(Post, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return f"Video for {self.post.title}"

class Audio(models.Model):
    post = models.ForeignKey(Post, related_name='audios', on_delete=models.CASCADE)
    audio = models.FileField(upload_to='audios/')

    def __str__(self):
        return f"Audio for {self.post.title}"
```

#### 나) 마이그레이션
모델 파일이 바뀐 후 마이그레이션을 진행합니다.
```shell
python manage.py makemigrations
python manage.py migrate
```

### 3) Form 수정
각각 업로드 파일을 받을 수 있도록 폼을 수정합니다.
`blog/forms.py`에서 아래의 코드를 추가합니다.
```python
#새롭게 수정
from django import forms
from .models import Post, Image, Video, Audio

class PostForm(forms.ModelForm) : 
    class Meta : 
        model = Post 
        fields = ['title', 'content', 'category']
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video']

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['audio']
```
또한 폼셋(formset)을 정의하여 여러개의 이미지를 업로드 할 수 있도록 설정합니다.
업로드 가능한 파일 수는 최대 5개로 합니다.
```python
from django.forms import modelformset_factory

ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=5, can_delete=True)
VideoFormSet = modelformset_factory(Video, form=VideoForm, extra=5, can_delete=True)
AudioFormSet = modelformset_factory(Audio, form=AudioForm, extra=5, can_delete=True)
```

### 4) View 수정
뷰에서 각 파일 타입의 폼과 폼셋(formset)을 처리하여 여러 개의 파일을 업로드 할 수 있도록 합니다.
사진, 영상, 음악을 포함한 데이터가 제대로 저장될 수 있도록 뷰도 수정합니다.

앞서 작성한 models와 forms에서 들고와 `post_create`를 변경합니다.

#### 가) `post_create`
```python
# import 변경
from .models import Post, Category, Image, Video, Audio
from .forms import PostForm, ImageFormSet, VideoFormSet, AudioFormSet

# post_create 변경
@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        video_formset = VideoFormSet(request.POST, request.FILES, queryset=Video.objects.none())
        audio_formset = AudioFormSet(request.POST, request.FILES, queryset=Audio.objects.none())

        if form.is_valid() and image_formset.is_valid() and video_formset.is_valid() and audio_formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        
            for form in image_formset:
                if form.cleaned_data and form.cleaned_data.get('image'):
                    image = form.save(commit=False)
                    image.post = post
                    image.save()

            for form in video_formset:
                if form.cleaned_data and form.cleaned_data.get('video'):
                    video = form.save(commit=False)
                    video.post = post
                    video.save()

            for form in audio_formset:
                if form.cleaned_data and form.cleaned_data.get('audio'):
                    audio = form.save(commit=False)
                    audio.post = post
                    audio.save()
                    
            return redirect('post_list')
                    
    else:
        form = PostForm()
        image_formset = ImageFormSet(queryset=Image.objects.none())
        video_formset = VideoFormSet(queryset=Video.objects.none())
        audio_formset = AudioFormSet(queryset=Audio.objects.none())

    return render(request, 'blog/post_create.html', {
        'form': form,
        'image_formset': image_formset,
        'video_formset': video_formset,
        'audio_formset': audio_formset,
    })
```

`post_update`를 변경합니다.

#### 나) `post_update`
```python
# post_update 변경
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user:  
        raise PermissionDenied
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.filter(post=post))
        video_formset = VideoFormSet(request.POST, request.FILES, queryset=Video.objects.filter(post=post))
        audio_formset = AudioFormSet(request.POST, request.FILES, queryset=Audio.objects.filter(post=post))
        
        if form.is_valid() and image_formset.is_valid() and video_formset.is_valid() and audio_formset.is_valid():
            post = form.save()
            
            for image_form in image_formset:
                if image_form.cleaned_data and image_form.cleaned_data.get('image'):
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()

            for video_form in video_formset:
                if video_form.cleaned_data and video_form.cleaned_data.get('video'):
                    video = video_form.save(commit=False)
                    video.post = post
                    video.save()

            for audio_form in audio_formset:
                if audio_form.cleaned_data and audio_form.cleaned_data.get('audio'):
                    audio = audio_form.save(commit=False)
                    audio.post = post
                    audio.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        image_formset = ImageFormSet(queryset=Image.objects.filter(post=post))
        video_formset = VideoFormSet(queryset=Video.objects.filter(post=post))
        audio_formset = AudioFormSet(queryset=Audio.objects.filter(post=post))
    
    return render(request, 'blog/post_update.html', {
        'form': form,
        'image_formset': image_formset,
        'video_formset': video_formset,
        'audio_formset': audio_formset,
    })

```

### 5) 템플릿 수정
마지막으로 이미지와 영상을 표시할 수 있도록 템플릿을 수정합니다.

#### 가) blog/post_create.html
템플릿에서 각 파일 유형에 맞는 입력 필드를 추가합니다.

폼셋을 사용하고 있으므로 각 폼셋의 폼들을 렌더릴 할 수 있는 코드를 포함하여 `post_create.html`에 작성 합니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <title>글 작성</title>
</head>
<body>
    <h1>글 작성</h1>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        
        <h2>이미지 업로드</h2>
        {{ image_formset.management_form }}
        {% for image_form in image_formset %}
            {{ image_form.as_p }}
        {% endfor %}

        <h2>비디오 업로드</h2>
        {{ video_formset.management_form }}
        {% for video_form in video_formset %}
            {{ video_form.as_p }}
        {% endfor %}

        <h2>오디오 업로드</h2>
        {{ audio_formset.management_form }}
        {% for audio_form in audio_formset %}
            {{ audio_form.as_p }}
        {% endfor %}
        
        <button type="submit">저장</button>  
    </form>
    <a href="{% url 'post_list' %}">목록</a> 
</body>
</html>
```

#### 나) blog/post_detail.html
글의 상세 내용을 보여주는 `post_detail.html`에 표시될 수 있도록 추가합니다.
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
    
    <h2>이미지</h2>
    {% for image in post.images.all %}
        <img src="{{ image.image.url }}" alt="Post Image" style="max-width: 100%; height: auto;">
    {% empty %}
        <p>이미지가 없습니다.</p>
    {% endfor %}

    <h2>비디오</h2>
    {% for video in post.videos.all %}
        <video controls style="max-width: 100%; height: auto;">
            <source src="{{ video.video.url }}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    {% empty %}
        <p>비디오가 없습니다.</p>
    {% endfor %}

    <h2>오디오</h2>
    {% for audio in post.audios.all %}
        <audio controls>
            <source src="{{ audio.audio.url }}" type="audio/mpeg">
            Your browser does not support the audio tag.
        </audio>
    {% empty %}
        <p>오디오가 없습니다.</p>
    {% endfor %}

    {% if post.author == request.user %}
        <a href="{% url 'post_update' post.pk %}">수정</a>
        <a href="{% url 'post_delete' post.pk %}">삭제</a>
    {% endif %}
    <a href="{% url 'post_list' %}">글 목록</a>
</body>
</html>
```


# 9. 댓글
게시글에 댓글 기능을 추가하는 단계입니다.

## 가. 댓글 작성
먼저 작성된 게시글에 댓글을 작성할 수 있도록 댓글 작성 기능을 구현합니다.
### 1) Model 수정
먼저 `blog/models.py`파일에 댓글을 저장할 모델을 만듭니다. 
 * 기존에 작성한 `Post`과 외래키로 연결합니다.
 * 내장되어 있는 `User`과 외래키로 연결합니다.
```python
class Comment(models.Model) : 
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True )
    
    def __str__(self) : 
        return f"댓글 : {self.author} on {self.post}"
```

### 2) 마이그레이션 생성 및 적용
모델을 재정의한 후 데이터베이스에 모델을 반영하기 위하여 마이그레이션을 생성하고 적용합니다.
```shell
python manage.py makemigrations
python manage.py migrate
```

### 3) Form 추가
댓글을 작성한 폼을 `blog/forms.py`에서 작성합니다.
* models.py에서 작성한 comment를 불러옵니다.
* 사용자에게 받는 데이터는 `content`입니다.
```python
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
```

### 4) Views 수정
기존에 작성한 게시글 상세 내용 뷰에서 댓글을 작성하고 저장하는 기능을 추가합니다.
* models.py에서 작성한 comment를 불러옵니다.
* forms.py에서 작성한 commentForm을 불러옵니다.
* post에 있는 모든 comments를 불러오는 명령어를 작성합니다.
* comment 입력값 여부를 확인 후 결과를 제공합니다.

```python
from .models import Comment
from .forms import CommentForm

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
# 코드 추가
    comments = post.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post, 
        'comments': comments,
        'comment_form': comment_form
    })
```

### 5) Template 수정
댓글을 표시하고, 새로운 댓글을 작성할 수 있는 폼을 추가합니다.
`post_detail.html` 파일에 다음과 같이 수정합니다.

```HTML
<!-- 생략("오디오" 아래) -->
    <h2>댓글</h2>
    <div>
        {% for comment in comments %}
            <p><strong>{{ comment.author }}</strong>: {{ comment.content }}</p>
            <p>작성일: {{ comment.created_at }}</p>
            <hr>
        {% endfor %}
    </div>

    {% if request.user.is_authenticated %}
        <h3>댓글 작성</h3>
        <form method="post">
            {% csrf_token %}
            {{ comment_form.as_p }}
            <button type="submit">댓글 달기</button>
        </form>
    {% else %}
        <p>댓글을 작성하려면 로그인하세요.</p>
    {% endif %}
    <!-- 생략("수정" 위) -->

```
댓글 작성 기능이 구현되었습니다.
테스트를 통해 사용자들이 각 게시글에 댓글을 작성하고 댓글을 확인할 수 있는지 확인합니다.

## 나. 댓글 수정 및 삭제
작성한 댓글을 수정하거나 삭제할 수 있도록 기능을 추가하는 단계입니다.
* 댓글의 작성자에게만 권한을 부여합니다.
* 수정 또는 삭제를 처리하는 뷰를 추가합니다.
* 수정 또는 삭제를 처리하는 URL을 추가합니다.
* 수정 또는 삭제를 위한 Template 화면을 생성합니다.

### 1) View 추가
댓글을 수정하고 삭제하는 뷰를 작성합니다.   
앞서 `models.py`와 `forms.py`에서 각각 `Comment`와 `CommentForm`을 가져왔기 때문에, 해당 과정에서는 댓글을 수정하고 삭제하는 기능만 정의합니다.
```python
@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user:
        raise PermissionDenied

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            print(comment.post.pk)  
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/comment_edit.html', {'form': form, 'comment' : comment})

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user:
        raise PermissionDenied

    if request.method == "POST":
        post_pk = comment.post.pk
        comment.delete()
        return redirect('post_detail', pk=post_pk)

    return render(request, 'blog/comment_delete.html', {'comment': comment})
```

### 2) URL
댓글을 수정하고 삭제할 수 있는 URL패턴을 추가하여 해당 경로로 들어가 수정할 수 있도록 설정합니다.
다음의 코드를 `blog/urls.py`에 작성합니다.

```python
urlpatterns = [
    # 생략
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]

```

### 3) Templates
댓글 수정과 삭제를 위한 템플릿을 추가합니다. 

#### 가) comment_edit.html
댓글 수정을 위해 새로운 HTML 파일을 생성하여 아래의 코드를 작성합니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <title>댓글 수정</title>
</head>
<body>
    <h1>댓글 수정</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">수정</button>
    </form>
    <a href="{% url 'post_detail' pk=comment.post.pk %}">취소</a>
</body>
</html>
```

#### 나) comment_delete.html
댓글 삭제를 위해 새로운 HTML 파일을 생성하여 아래의 코드를 작성합니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <title>댓글 삭제</title>
</head>
<body>
    <h1>댓글 삭제</h1>
    <p>정말로 댓글을 삭제하시겠습니까?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">삭제</button>
    </form>
    <a href="{% url 'post_detail' pk=comment.post.pk %}">취소</a>
</body>
</html>
```

#### 다) post_detail.html
기존에 작성한 `post_detail.html`에서 작성된 댓글 목록을 들고올 때, 작성자인 경우 수정, 삭제 버튼이 보이도록 코드를 추가합니다.
```HTML
    <h2>댓글</h2>
    <div>
        {% for comment in comments %}
            <p><strong>{{ comment.author }}</strong>: {{ comment.content }}</p>
            <p>작성일: {{ comment.created_at }}</p>
            {% if comment.author == request.user %}
                <a href="{% url 'comment_edit' comment.pk %}">수정</a>
                <a href="{% url 'comment_delete' comment.pk %}">삭제</a>
            {% endif %}
            <hr>
        {% endfor %}
    </div>
```

서버를 실행 후 댓글이 정상적으로 수정 및 삭제가 되는지 확인합니다.


## 다. 답글
댓글에 대한 댓글을 구현하는 단계입니다. 기존 댓글 시스템을 확장하여 답글을 작성할 수 있도록 구현합니다.

### 1) Model 수정
답글을 구현하기 위하여 `blog/models.py`내 `Comment`함수에 `related_name='replies'` 코드를 사용하여 자기참조 필드를 추가합니다.
```python
class Comment(models.Model) : 
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True )
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE) # 추가된 코드
    
    def __str__(self) : 
        return f"댓글 : {self.author} on {self.post}"
```

### 2) Migrate
모델을 재정의한 후 데이터베이스에 수정된 내용을 반영하기 위하여 마이그레이션을 진행하고 적용합니다.
```shell
python manage.py makemigrations
python manage.py migrate
```

### 3) View
답글 기능을 처리하기 위하여 필요항 요청을 처리하는 뷰 함수를 정의합니다. 해당 함수로 사용자가 댓글에 답글을 작성할 수 있도록 하고, 답글을 댓글과 게시글에 연결하는 역할을 합니다.
* 답글을 처리할 수 있도록 `parent` 필드를 처리하는 코드를 작성합니다.
* 댓글과 답글을 구분하여 템플릿에 전달합니다.
`blog/views.py`에서 작성한 기존 게시글 상세 내용 폼에서 `comments`부분을 수정합니다.

```python
@login_required
def comment_reply(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = get_object_or_404(Post, pk=request.POST['post'])
            reply_to_pk = request.POST.get('reply_to')
            if reply_to_pk:
                reply_to_comment = get_object_or_404(Comment, pk=reply_to_pk)
                comment.parent = reply_to_comment
            comment.save()
            return redirect('post_detail', pk=comment.post.pk)
    return redirect('index')
```

### 3) URL 추가
작성한 뷰를 화면에서 볼 수 있도록 url을 추가합니다.
```python
urlpatterns = [
    # 생략
    path('comment/reply/', views.comment_reply, name='comment_reply'),
]
```

### 5) Template 수정
#### 가) blog/post_detail.html
답글을 작성할 수 있는 폼과 답글을 보여주는 기능을 `blog/post_datail.html`에 추가합니다.
```HTML
    <h2>댓글</h2>
    <div>
        {% for comment in comments %}
            <p><strong>{{ comment.author }}</strong>: {{ comment.content }}</p>
            <p>작성일: {{ comment.created_at }}</p>
            {% if comment.author == request.user %}
                <a href="{% url 'comment_edit' comment.pk %}">수정</a>
                <a href="{% url 'comment_delete' comment.pk %}">삭제</a>
            {% endif %}

            <!-- 답글 작성 버튼 -->
            <a href="?reply_to={{ comment.pk }}">답글</a>

            <!-- 답글 폼 표시 -->
            {% if request.GET.reply_to == comment.pk|stringformat:"s" %}
                <form method="post" action="{% url 'comment_reply' %}">
                    {% csrf_token %}
                    <input type="hidden" name="post" value="{{ post.pk }}">
                    <input type="hidden" name="reply_to" value="{{ comment.pk }}">
                    <textarea name="content" required></textarea>
                    <button type="submit">답글 작성</button>
                </form>
            {% endif %}

            <!-- 답글 목록 -->
            <div class="replies">
                {% for reply in comment.replies.all %}
                    <div class="comment" style="margin-left: 20px;">
                        <p><strong>{{ reply.author }}</strong>: {{ reply.content }}</p>
                        <p>작성일: {{ reply.created_at }}</p>
                        {% if reply.author == request.user %}
                            <a href="{% url 'comment_edit' reply.pk %}">수정</a>
                            <a href="{% url 'comment_delete' reply.pk %}">삭제</a>
                        {% endif %}
                        <!-- 답글 작성 버튼 -->
                        <a href="?reply_to={{ reply.pk }}">답글</a>
            
                        <!-- 답글 폼 표시 -->
                        {% if request.GET.reply_to == comment.pk|stringformat:"s" %}
                            <form method="post" action="{% url 'comment_reply' %}">
                                {% csrf_token %}
                                <input type="hidden" name="post" value="{{ post.pk }}">
                                <input type="hidden" name="reply_to" value="{{ comment.pk }}">
                                <textarea name="content" required></textarea>
                                <button type="submit">답글 작성</button>
                            </form>
                        {% endif %}

                        <!-- 답글의 답글 목록 -->
                        <div class="replies">
                            {% for nested_reply in reply.replies.all %}
                                <div class="comment" style="margin-left: 40px;">
                                    <p><strong>{{ nested_reply.author }}</strong>: {{ nested_reply.content }}</p>
                                    <p>작성일: {{ nested_reply.created_at }}</p>
                                    {% if nested_reply.author == request.user %}
                                        <a href="{% url 'comment_edit' nested_reply.pk %}">수정</a>
                                        <a href="{% url 'comment_delete' nested_reply.pk %}">삭제</a>
                                    {% endif %}
                                </div>
                            {% endfor %}
                        </div>
                    </div>
                {% endfor %}
            </div>
                <hr>
        {% endfor %}
    </div>
```

#### 나) blog/comment_reply.html
답글 화면을 구현합니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <title>답글 작성</title>
</head>
<body>
    <h1>답글 작성</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">답글 작성</button>
    </form>
    <a href="{% url 'post_detail' pk=post.pk %}">취소</a>
</body>
</html>
```

# 10. 마이페이지
사용자의 마이페이지를 생성하고 추가 기능을 구현하는 단계입니다.

## 가. 프로필 생성
### 1) Model
사용자가 자신의 프로필 정보를 수정하거나 자신과 관련된 게시글을 확인할 수 있는 마이페이지 생성이 필요합니다. `profile`모델을 추가하여 사용자의 추가정보를 저장합니다.

```python

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}의 프로필"
```

### 2) Signal
`user`모델이 생성될 때마다 자동으로 `profile`모델도 함께 생성되도록 신호(signals)를 사용할 수 있습니다.  
`blog/models.py`에 이어서 작성할 수 있으나 향후 사용자가 많아지는 상황을 가정하여 `blog/signals.py`라는 별도의 파일을 만들어 신호 관련 코드를 관리합니다.

#### 가) signal.py
```python
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
```

##### 나) apps.py
신호 핸들러가 제대로 동작하게 설정하기 위하여 `blog/apps.py`에서 해당 신호 핸들러를 불러오는 코드를 추가합니다.

```python
from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"

    # 추가된 코드
    def ready(self):
        import blog.signals
```
### 3) Migrations

### 4) View 설정
마이페이지를 보여줄 뷰를 설정합니다.

기존에 생성된 사용자의 경우 프로필이 없으므로, 사용자가 마이페이지를 요청할 때 `profile`이 없으면 자동으로 생성되도록 작성합니다.

#### mypage_view
```python
from django.contrib.auth.models import User
from .models import Profile

@login_required
def mypage_view(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)
    posts = Post.objects.filter(author=user)

    return render(request, 'mypage.html', {'user': user, 'profile': profile, 'posts': posts})
```

### 5) URL 설정
뷰를 연결할 URL 설정을 진행합니다.
```python

urlpatterns = [
    path('mypage/<str:username>/', mypage_view, name='mypage'),
]
```
### 6) Template 작성
마이페이지의 HTML 템플릿을 작성하여 사용자의 프로필 정보와 관련된 게시글을 보여줍니다.

#### 가) mypage.html
`templates/blog` 폴더에 `mypage.html` 파일을 생성합니다.

프로필 내용 중 사진이 없는 사용자가 있을 수 있으므로 사진 파일 유무를 확인 후 파일이 있을 때에만 사진을 표시하도록 작성합니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{{ user.username }}의 프로필</h1>
    {% if profile.profile_picture %}
    <img src="{{ profile.profile_picture.url }}" alt="Profile Picture">
    {% else %}
        <p>프로필 사진이 존재하지 않습니다.</p>
    {% endif %}

    <p>소개: {{ profile.bio }}</p>
    <p>지역: {{ profile.location }}</p>

    <a href="{% url 'post_list' %}">글 목록</a>
</body>
</html>
```

#### 나) post_list.html
`templates/blog` 폴더 안 `post_list.html` 파일에서 프로필을 조회할 수 있도록 코드를 추가합니다.   
URL pattern에서 작성한 주소는 사용자이름(`user id`)를 요청하는 값 까지이므로 `request.user.username` 명령어를 작성하여 로그인 중일 때 마이페이지 버튼이 보이며, 사용자 이름을 제공하도록 작성합니다.
```HTML
    <div>
        {% if not request.user.is_authenticated %}
        <a href="{% url 'signup' %}">회원가입</a> |
        <a href="{% url 'login' %}">로그인</a> |
    {% endif %}
    
    {% if request.user.is_authenticated %}
        <form action="{% url 'logout' %}" method="post">
            {% csrf_token %}
            <button type="submit">로그아웃</button>
        </form>
        <a href="{% url 'mypage' request.user.username %}">마이페이지</a>
    {% endif %}
        <a href="{% url 'mypost' request.user.username %}">마이페이지</a>
    {% endif %}
    </div>
```

## 나.프로필 수정 
프로필을 수정할 수 있는 기능을 추가합니다.

### 1) 폼 생성 
기존 뷰 파일(`blog/forms.py`)에서 사용자가 로그인한 상태에서 사용자가 수정할 프로필 내용을 받습니다.
```python
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']
    
    # 선택적 필드 추가 (예: username은 User 모델의 필드이므로 별도 처리)
    username = forms.CharField(max_length=150)

    def __init__(self, *args, **kwargs):
        # instance는 user.profile이 전달되므로, username을 초기값으로 설정
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['username'].initial = user.username

    def save(self, commit=True):
        # user instance 저장
        user = self.instance.user
        user.username = self.cleaned_data.get('username')
        user.save()

        # profile instance 저장
        profile = super().save(commit=commit)
        return profile
```

### 2) 뷰 수정 
기존 뷰 파일(`blog/views.py`)에서 사용자가 로그인한 상태에서 수정을 할 수 있는 뷰를 작성합니다.
```python
from .forms import ProfileForm
@login_required
def edit_profile(request):
    user = request.user
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user.profile, user=user)
        if form.is_valid():
            form.save()
            return redirect('mypage', username=user.username)
    else:
        form = ProfileForm(instance=user.profile, user=user)
    
    context = {
        'form': form
    }
    return render(request, 'blog/edit_profile.html', context)
```

### 3) URL 설정
기존 뷰 파일(`blog/urls.py`)에서 뷰와 연결할 URL을 설정합니다.
```python
urlpatterns = [
    # 추가한 코드
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
```

### 4) Template 
새로운 템플릿(`templates/blog/edit_profile.html`)을 생성 후 저장합니다.
```HTML
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>프로필 수정</h1>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">저장하기</button>
    </form>
</body>
</html>
```

## 비밀번호 변경
## 닉네임 추가


# 11. 글 조회수
게시글을 조회한 횟수를 보여주는 기능을 구현하는 과정입니다.    
## 가. Model 수정
게시글 모델에 조회수 필드를 추가합니다.
코드는 `blog/models.py` 파일 내에 작성합니다.
```python
class Post(models.Model) :
    # 생략
    views = models.IntegerField(default = 0)
```

## 나. Migration
모델을 수정한 후 데이터베이스에 반영합니다.
```shell
python manage.py makemigrations
python manage.py migrate
```

## 다. View 설정
게시글을 조회할 때마다 조회수가 증가하도록 뷰를 수정합니다.
코드는 `blog/views.py` 파일 내에 작성합니다.

### 1) post_detail
```python
def post_detail(request, pk):
    
    # 조회수 증가코드 추가
    post.views += 1
    post.save()

```

한 사용자가 하나의 게시글을 짧은 시간동안 여러번 조회하여 조회수가 증가하는 것을 방지하기 위하여, 특정 시간동안 동일한 게시글을 여러 번 조회하더라도 조회수가 한 번만 증가하도록 설정할 수 있습니다.
```python
from datetime import timedelta

    # 쿠키를 이용하여 중복 조회 방지
    session_key = f'viewed_post_{post.pk}'
    if not request.session.get(session_key):
        post.views += 1
        post.save()
        request.session[session_key] = True
        request.session.set_expiry(timedelta(hours=1))  # 1시간 후 쿠키 만료```
```

### 2) post_list
조회수로 게시글을 정렬하여 인기글을 확인하는 화면을 제공할 수 있습니다.
```python
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    # Post 객체를 조회하고 정렬 및 슬라이스
    top_posts = Post.objects.all().order_by('-views')[:10]
    # 생략
```

## 라. Template 수정
기존에 작성된 템플릿에서 아래의 코드를 추가합니다.   

### 1) post_detail
코드는 `templates/blog/post_detail.html` 파일 내에 작성합니다.

```HTML
<!-- 추가한 코드 -->
<p>조회수: {{ post.views }}</p>
<!-- 기존 코드 -->
<p>{{ post.content }}</p>
```

### 2) post_list
코드는 `templates/blog/post_list.html` 파일 내에 `{% for post in posts %}` 부분을 `{% for post in top_posts %}` 로 작성하면 조회순이 높은 게시글 순으로 글을 확인할 수 있습니다.

```HTML
    <ul>
        {% for post in top_posts %} # 수정된 부분
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
```

서버 실행 후 결과를 확인합니다.


# 12. 컨텐츠 필터링
특정 단어나 문구를 자동으로 필터링하거나 경고 메세지를 표시하고 관리자 페이지에서 관리 할 수 있도록 기능을 구현하는 단계입니다.

## 모델 작성 
금지어를 데이터베이스에 저장하고 관리할 수 있도록 설정합니다.
### blog/models.py
`BannedWord` 함수로 금지어 저장 데이터베이스를 생성합니다.
```python
class BannedWord(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word
```
## 마이그레이션
모델을 정의한 후 모델을 데이터베이스에 반영하기 위하여 마이그레이션을 생성하고 적용합니다.

**마이그레이션 생성**
```shell
python manage.py makemigrations
```

**마이그레이션 적용**
```shell
python manage.py migrate
```

## 관리자페이지 등록
금지어를 관리하기 위하여 관리자페이지에 `BannedWord` 모델을 등록합니다.
`blog/admin.py`파일에 다음 코드를 추가하여 `BannedWord` 모델을 관리자 페이지에 등록합니다.

```python
from .models import BannedWord
admin.site.register(BannedWord)
```

페이지 등록 후 금지어를 추가, 삭제, 수정할 수 있습니다.

## 검열 함수
`blog/views.py` 파일에 검열 함수 정의(`censor_text`)를 작성하여 데이터베이스에 저장된 금지어를 기준으로 검열이 이루어지도록 합니다.

`censor_text` 위치는 게시글 관련 정의 앞부분에 작성하여 검열함수가 먼저 정의된 후 글 또는 댓글에서 해당 함수가 동작하도록 배치합니다.
```python
import re
from .models import BannedWord

def censor_text(text):
    banned_words = BannedWord.objects.values_list('word', flat=True)
    for word in banned_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub("*" * len(word), text)
    return text

```

## 검열 적용
글 또는 댓글을 저장하기 전에 검열 기능을 적용하도록 코드를 수정합니다.
### 1) 게시글
#### 가) 글 생성
`blog/views.py` 파일 안 `post_create`정의 부분에서 작성글 검열 기능을 적용합니다.
```python
@login_required
def post_create(request):
    if request.method == "POST":
    # 생략
        if form.is_valid() and image_formset.is_valid() and video_formset.is_valid() and audio_formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # 글에 검열 기능 적용
            post.content = censor_text(post.content)
            post.save()
    # 생략
```
#### 나) 글 수정
`blog/views.py` 파일 안 `post_update`정의 부분에서 작성글 검열 기능을 적용합니다.
```python
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user:  
        raise PermissionDenied
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.filter(post=post))
        video_formset = VideoFormSet(request.POST, request.FILES, queryset=Video.objects.filter(post=post))
        audio_formset = AudioFormSet(request.POST, request.FILES, queryset=Audio.objects.filter(post=post))
        
        if form.is_valid() and image_formset.is_valid() and video_formset.is_valid() and audio_formset.is_valid():
            # 글에 검열 기능 적용
            post.content = censor_text(post.content)
            post.save()
    # 생략
```

### 2) 댓글
`blog/views.py` 파일 안 `post_detail`정의 부분에서 댓글 검열 기능을 적용합니다.
```python
def post_detail(request, pk):
    # 생략
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            
            # 댓글에 검열 기능 적용
            comment.content = censor_text(comment.content)
            
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    # 생략
```

관리자로 로그인 후 관리자페이지에서 금지어를 추가/수정/삭제 후 글 또는 댓글 작성 시 해당 금지어가 잘 검열되는지 확인합니다.


## 단어 저장
이번 과정은 shell을 활용하여 비방 단어를 데이터베이스에 저장하는 방법입니다.

먼저, 새로운 shell창을 열어 준비합니다.
```shell
python manage.py shell
```
이후 `BannedWord` 모델을 불러와 저장할 단어 목록을 제공합니다.

```shell
from blog.models import BannedWord
banned_words = [
    "쓰레기", "멍청한", "거짓말쟁이", "치사한", "배신자"
    ## 등등 작성합니다.
]

for word in banned_words:
    BannedWord.objects.create(word=word)

# 또는 BannedWord.objects.bulk_create([BannedWord(word=word) for word in banned_words])

```






























# 9. 생성AI 활용

# 10. 배포

# 11. 추가 기능
## 파일 추가 폼 변경
1개의 파일을 올린 후  extra매개변수를 사용하여 추가 폼을 표시하는 기능입니다.
### Form 설정
```python
# forms.py
from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

ImageFormSet = forms.inlineformset_factory(
    ParentModel,  # Parent model for the formset
    Image,        # Model for the formset
    form=ImageForm,
    extra=1,      # Initial number of forms to display
    can_delete=True
)

```

### View 설정
```python
# blog/views.py
from django.shortcuts import render, redirect
from .models import ParentModel, Image
from .forms import ImageFormSet

def upload_images(request):
    if request.method == 'POST':
        formset = ImageFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect('success_url')  # Redirect after successful form submission
    else:
        formset = ImageFormSet()

    return render(request, 'upload_images.html', {'image_formset': formset})

```
### URL 설정


# 12. bootstrap
각 html 파일 확인



# 13. 추가 기능
## 가. 검색
## 나. 사이드바 ( 진행 완료 )
## 다. 썸네일
## 라. 생성AI



# 14. 참고
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

## 나. 최근 makemigrations 삭제
Django 어플리케이션을 구축하며 models.py파일을 잘 못 작성하였을 경우 migrate가 제대로 진행되지 않아 makemigrations로 생성된 파일을 삭제해야 하는 상황이 발생합니다. 파일 삭제가 필요한 경우 아래와 같은 방법으로 파일 삭제를 진행할 수 있습니다.

1) **파일 직접 삭제**   
    해당하는 파일을 마우스 우클릭 후 파일 삭제 버튼으로 삭제합니다.
2) **파일 삭제 명령어**   
    삭제 명령어로 생성된 파일을 삭제합니다.
    ```shell
    rm '파일경로/파일명'
    ```


## 다. git commit imoji
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
