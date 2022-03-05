# API 사용법

1. import requests로 모듈 불러오기

2. api요청 주소를 활용해서 requests로 요청

   ```python
   BASE_URL = 'https://api.themoviedb.org/3'
       path = '/movie/top_rated'
       params = {
           'api_key': '3beacdbb8f7b35eb8c782851ddc5b403',
           'language': 'ko',
           'region': 'KR',
       }
   #의 형태로 api url을 요청하고
   response = requests.get(BASE_URL + path, params=params)
   #requests함수를 이용해서 파일을 요청한다.
   
   # json 파일로 변환해서 사용하면 된다.
   data=response.json()
   
   ```

   