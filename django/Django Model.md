# Django Model

CRUD - create retrieve(read) update delete

- 데이터를 조작할 때 가장 일반적으로 하는 작업들



## Model

- 단일한 데이터에 대한 정보를 가짐
  - 통합된, 구조화된 데이터를 가진다.
  - 사용자가 저장하는 데이터(앱에서 사용되는 데이터)들의 필수적인 필드(각각의 데이터에 대응 ex)이름, 주소 등)들과 동작들을 포함
- 저장된 데이터베이스의 구조(layout)
- django는 model(model.py를 뜻하는게 아닌 넓은 의미의 model)을 통해 데이터에 접속하고 관리한다.
- 각각의 model은 하나의 데이터베이스 테이블에 맵핑된다.



## Database

- 데이터베이스(DB)
  - 체계화된 데이터의 모임
- 스키마
- 테이블
  - 열(컬럼/필드)
  - 행(레코드/값) (각각의 레코드(in DB.table)가 ()에서 인스턴스로 대응) 
    - 기존의 레코드의 값을 수정하려면 레코드에 대응하는 인스턴스를 수정해 주어야 한다.
    - 수정 후 save() 메소드를 호출해서 DB에 반영해 주어야 한다.



## ORM

- SQL을 사용하지 않더라도 객체지향 프로그래밍 언어인 파이썬을 사용해서 DB에 접근해서 작업을 할 수 있도록 Mapping을 시켜주는 기술
- OOP 프로그래밍에서 RDBMS을 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 안흔ㄴ 데이터를 변환하는 프로그래밍 기법

장점 

- SQL을 잘 알지 못해도 DB 조작이 가능
- SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성

단점

- ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음

현대 웹 프레임 워크의 요점은 웹 개발의 속도를 높이는 것. (생산성)



model이 변경되면 새로 makemigrations를 실행해서 설계도를 추가 해 주어야 한다.





## DB API 구문 - Making Queries

Article.objects[Article이라는 클래스에 ㄷ.all()[메소드]

이것의 return value를 QuerySet이라고 한다.

QuerySet

- DB로부터 전달받은 객체 목록
- queryset 안의 객체는 0개, 1개 혹은 여러 개일 수 있다.
  - 내가 원하는 조건에 맞는 데이터의 개수에 따라 다르다.
- DB로부터 조회, 필터, 정렬 등을 수행 할 수 있다.
  - 다만 어떤 작업을 하든 조회부터 해야 다른 작업을 수행 할 수 있다.



CREATE 관련 메서드

- save() method
  - Saving objects
  - 데이터 생성 시 save()를 호출하기 전에는 객체의 ID값이 무엇인지 알 수 없다.
    - ID 값은 django가 아니라 DB에서 계산되기 때문이다. (DB로 넘어 가야 id값 생성??)
  - 단순히 모델을 인스턴스화 하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save()가 필요하다.

- str method
- .get()
  - queryset이 아닌 인스턴스 하나만을 return한다.
    - 없으면 DoesNotExist 예외를 발생
    - 둘 이상의 객체를 찾으면 MultipleObjectReturned 예외를 발생시킨다.
    - 이와 같은 특징을 가지고 있기 때문에 primary key와 같은 고유성을 보장하는 조회에서 사용해야 한다.
- Field looksups
  - 조회 시 특정 검색 조건을 지정
  - QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인수로 지정됨
  - field명 + __(조건)
  - 사용 예시
    - Article.objects.filter(pk**__gt**=*2*)
    - Article.objects.filter(content**__contains**=*'ja'*)







csrf 

form 바로 아래에 {% csrf_token%}