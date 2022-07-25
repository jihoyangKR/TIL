## HTTP

HTTP는 HyperText Transfer Protocol의 약자로, Client와 Server 사이에 요청과 응답을 처리하기 위한 규약이다.

해당 규약을 지키게 된다면 살펴보는 것 만으로도 어떤 요청을 하는지에 대해서 간략하게 알 수 있다.

HTTP는 요청과 응답 모두 크게 세 가지 요소로 구성된다.



먼저, HTTP 요청은 **Start Line**, **Headers**, **Body**의 세 가지 요소로 구성된다.

- Start Line은 method, URL, version으로 이루어져 있으며, 서버에서 요청을 받아들이는 첫 줄이다.
- Headers는 요청에 대한 접속 운영체제, 브라우저, 인증 정보와 같은 부가적인 정보를 담고 있다.
- Body는 요청에 관련된 json, html과 같은 구체적인 내용을 포함한다.

HTTP 응답은 다른 요소인 Status Line과 요청도 가지고 있는 Headers, Body로 구성된다.

- Status Line은 HTTP 버전과 함께 헤딩 요청에 대한 처리의 상태를 나타낸다. 200, 404와 같은 숫자 코드로 나타낸다.





## ResponseEntity

Spring Framwork에서 제공하는 클래스 중 `HttpEntity`라는 클래스가 존재한다. 이것은 Http 요청(Request) 또는 응답(Response)에 해당하는 HttpHeader와 HttpBody를 포함하는 클래스이다.

이 HttpEntity 클래스를 상속받아 구현한 클래스가 **RequestEntity**, **ResponseEntity** 클래스이다. ResponseEntity는 사용자의 HttpRequest에 대한 응답 데이터를 포함하는 클래스이다. 따라서 HtpStatus, HttpHeaders, HttpBody를 포함한다.

