# HTML 'form' element

- 웹에서 사용자 정보를 입력하는 여러 방식(text, button, checkbox, file, hidden, image, password, radio, reset, submit)을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당
- 핵심 속성(attribute)
  - action : 입력 데이터가 전송될 URL 지정
  - method : 입력 데이터 전달 방식 지정

# HTML 'input' element

- 사용자로부터 데이터를 입력 받기 위해 사용
- type 속성에 따라 동작 방식이 달라짐
- 핵심 속성(attribute)
  - name
  - 중복 가능, 양식(form)을 제출했을 때 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있음
  - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터(name은 key, value(실제 입력한 값)는 value)로 매핑하는 것
  - GET 방식에서는 URL에서 ?key=value&key=value 형식으로 데이터를 전달함



# HTML 'label' element

- 사용자 인터페이스 항목에 대한 설명(caption)을 나타냄
- label을 input 요소와 연결하기
  - label에 id 속성 부여
  - label 에는 input의 id와 동일한 값의 for 속성이 필요
- label과 input 요소 연결의 주요 이점
  - 시각적인 기능 뿐만 아니라 화면 리더기에서 label을 읽어 사용자가 입력해야하는 텍스트가 무엇인지 더 쉽게 이해할 수 있도록 돕는 프로그래밍적 이점도 있음

# HTML 'for' attribute

- for 속성의 값과 일치하는 id를 가진 문서의 첫 번째 요소를 제어
  - 연결 된 요소가 lablelable인 경우 이 요소에 대한 labeled control이 됨

# HTML 'id' attribute

- 전체 문서에서 고유(must be unique)해야하는 식별자를 정의
- 사용 목적
  - linking, scripting, styling 시 요소를 식별

# HTTP

- HyperText Transfer Protocol
- 웹에서 이루어지는 모든 데이터 교환의 기초
- 주어진 리소스가 수행 할 작업을 나타내는 request method를 정의
- HTTP request method 종류
  - GET, POST, PUT, DELETE ...

# HTTP request method - 'GET'

- 서버로부터 정보를 조회하는 데 사용
- 데이터를 가져올 때만 사용해야 함
- 데이터를 서버로 전송할 때 body가 아닌 Query String Parameters를 통해 전송
- 우리는 서버에 요청을 하면 HTML 문서 파일 한 장을 받는데, 이때 사용하는 요청의 방식이 GET



클라이언트가 ~/throw/ 로 서버에 요청을 하면 서버는  def throw() 함수를 통해 요청을 처리해 throw.html을 클라이언트에게 응답한다. 

클라이언트는 반환받은 throw.html에 정보를 입력해서 ~/catch/? 로 입력정보를 다시 서버에 요청하고 서버는 def catch(request)를 통해 결과를 클라이언트에게 응답으로 전달한다.



## Naming URL patterns

Template에 직접 연결하기 위한 방법

url이 길어질수록 참조하기가 힘들어진다. (하드코딩)

url에 이름을 붙여 이름을 써서 연결.

path() 함수의 name 인자를 정의해서 사용한다.

- Django Template Tag 중 하나인 url 태그를 사용해서 path()함수에 작성한 name을 사용할 수 있다.



같은 이름의 html이 있으면 탐색과정에서 햇갈릴 수 있기 때문에 app내의 templates 폴더 내에 app 명의 폴더를 만들어 거기 html파일을 넣어주고 경로를 새로 설정한다. ex) articles/index.html



다른 앱에서 같은 이름의 페이지를 구분하기 위해서

각 앱의 url.py에 app_name을 등록하고 (app이름과 똑같이)

url 태그에서 appname:이름으로 연결한다.