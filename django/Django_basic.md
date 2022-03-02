



클라이언트는 서버로 요청을 보내고 서버는 클라이언트에 응답한다.

클라이언트 : 서버에 원격 접속할 수 있는 기기 혹은 응용프로그램을 뜻한다.

MVC: 대부분의 프레임워크가 Model-View-Controller를 사용한다.

UI와는 별도로 시각적인 부분 뒤편의 영역을 개발할 수 있다.

Django는 MTV Pattern 이라고 한다. (특별한 이유는 없다.)



## MTV Pattern

#### Model

- 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)

#### Template(View)

- 파일의 구조나 레이아웃을 정의
- 실제 내용을 보여주는 데 사용(presentation)

#### View(Controller)

- HTTP 요청을 수신하고 HTTP 응답을 반환
- Model 을 통해 요청을 충족시키는데 필요한 데이터에 접근
- template에게 응답의 서식 설정을 맡김



![장고1](https://user-images.githubusercontent.com/97648339/156375430-993a2fec-9cc9-495a-a4ec-588cc758dc49.JPG)



## 장고 사용전 필수 과정

## Django 시작하기

#### 1. 가상환경 생성 및 활성화

- 가상환경 생성

```shell
$ python -m venv vevn
```

- 활성화

```shell
$ source venv/Scripts/activate
```

- 비활성화

```shell
$ deactivate
```

- VScode에서 가상환결 설정
- `ctrl + shift + p` 누르고

#### 2. django 설치하기

```shell
$ pip install django==3.2.12
$ pip list
```

- 반드시 패키지를 설치하면 freeze 한다.

```shell
$ pip freeze > requirements.txt
```

- 다시 설치하기

```plaintext
$ pip install -r requirements.txt
```

#### 3. 프로젝트 생성

- `.gitignore` `README.md` 생성하기

```shell
$ django-admin startproject <프로젝트이름> .
```

#### 4. 서버 실행해서 로켓 확인

```shell
$ python manage.py runserver
```

- 종료는 `ctrl + c`

#### 5. 앱 생성

- **[중요]** 앱을 생성하고 `settings.py` 등록하시오.
- `INSTALLED_APPS ` 에 먼저 등록하고 앱을 생성하면 다음과 같은 오류가 발생

![장고3](https://user-images.githubusercontent.com/97648339/156375456-59d09a9a-d1b8-41b2-9ec6-e7c309603c40.png)

#### 6. 앱 등록

- urls.py 에 등록한 함수가 정의되지 않았을 경우
- ![장고4](https://user-images.githubusercontent.com/97648339/156375471-a3d87aa1-de46-4fd5-a39f-dce55da9f44b.png)

### 장고 폴더 내 파일

1. `__init__.py`
   1. 하나의 패키지로 인식하도록 한다.
   2. 우리가 건들 일은 없다.
2. asgi.py
3. settings.py
   1. 장고 프로젝트내 전반적인 설정을 관리
4. urls.py
   1. 사이트의 url과 적절한 views간의 연결을 지정.
   2. 요청을 받는 첫번째
5. wsgi.py
   1. 장고 어플리케이션이 웹서버와 연결 및 소통하는 것을 도움
6. manage.py
   1. 장고 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
   2. manage.py + command

### Application 생성

- 일반적으로 Application명은 복수형으로 하는 것을 권장

### Application 구조

- admin.py
  - 관리자용 페이지를 설정 하는 곳
- apps.py (don't touch)
  - 앱의 정보가 작성된 곳 (수정하지 않을 곳)
- models.py
  - 앱에서 사용하는 Model을 정의하는 곳
- tests.py (don't touch)
  - 프로젝트의 테스트 코드를 작성하는 곳
- views.py
  - view 함수들이 정의 되는 곳
- migrations
  - model과 연관



## Project & Application

- ### Project

  - Project는 Application(이하 앱)의 집합 (collection of apps)
  - 프로젝트에는 여러 앱이 포함될 수 있다.
  - 앱은 여러 프로젝트에 있을 수 있다.

- ### Application

  - 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담방
  - 하나의 프로젝트는 여러 앱을 가진다.
  - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성한다.

- ### 프로젝트에 앱 등록하기

- 물리적으로 프로젝트와 앱이 같은 위치에 존재하기 때문에 프로젝트는 앱이 존재하는지 알 수 없다. 이를 위해 프로젝트가 앱을 인식하기 위해 앱을 프로젝트에 등록해주는 과정이 필요하다. 

- project 내의 setting.py의 INSTALLED_APPS 내 맨 위에 앱의 이름을 작성(권장사항)

- ##### 앱 생성 시 주의 사항

  - **반드시 생성 후 등록해야 한다.**
  - INSTALLED_APPS에 먼저 작성(등록)하고 생성하려면 앱이 생성되지 않는다.

- 앱 등록시 권장사항

  - ![장고2](https://user-images.githubusercontent.com/97648339/156375443-c6ae7115-5adb-4a3c-af4c-164f0afccadf.JPG)
  - #Local apps
    - 내가 만든 앱들
  - #Third party apps
    - 다른 곳에서 가져온 앱
  - #Django apps
    - 장고 기본 설치 앱
  - 순으로 앱을 등록한다.
  - 해당 순서를 지키지 않아도 문제는 없지만 advanced한 내용을 위해 지키는것을 권장.

#### urls.py

- urlpatterns 코드
  - path('admin/', admin.site.urls)
    - admin/ : 주소
    - 클라이언트에서 admin/에 대한 요청을 보내면 urls.py 내에서 admin에 해당하는 path 함수를 응답한다.
    - 즉 클라이언트에서 주소에 admin을 입력하는 것은 서버에 요청을 보내는 것.
- '/'
  - 장고는 url을 설정할때 /(end slash)를 반드시 입력해줘야한다.
  - 실제 주소창에서 url 접속시에는 /를 넣지않아도 됨
- ',' (trailing comma)
  - 파이썬 문법에선 권하지 않지만 장고에서는 사용. 바로 다음 요소를 입력하기 위함

### views.py

- view 함수가 무조건 받아야 하는 인자 (request) 
- ulr.py가 객체를 넘겨줄 때 받아주기 위한 인자.
- 



# url - views - templates



# DTL 문법

## Variable

```python
{{ variable }}
```

- 중괄호 두개로 표현한다.
  - 중괄호와 key 사이에는 공백 한칸씩 넣어줘야 한다.



### Filters

- 표시할 변수를 수정할 때 사용



## Tags

{% tag %}

- 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어흐름을 만드는 등 변수보다 복잡한 일들을 수행

- 일부 태그는 시작과 종료 태그가 필요

  ```django
  {% if %}{% endif %}
  ```

  