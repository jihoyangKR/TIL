# Python math 모듈

! 달리 명시되지 않는 한 모든 반환 값은 float이다.

주로 사용하는 함수

math.sqrt(x) : x의 제곱근을 반환한다.

math.atan(x) : x의 아크 탄젠트(arc tangent)를 라디안으로 반환한다. 결과는 -pi/2와 pi/2 사이이다.

math.atan2(y, x) : `atan(y / x)`를 라디안으로 반환합니다. 결과는 `-pi`와 `pi` 사이입니다. 평면에 있는 원점에서 점 `(x, y)`까지의 벡터는 양의 X 축과 이 각도를 이룹니다. [`atan2()`](https://docs.python.org/ko/3/library/math.html?highlight=atan2#math.atan2)의 요점은 두 입력의 부호가 모두 알려져 있기 때문에 각도에 대한 정확한 사분면을 계산할 수 있다는 것입니다. 예를 들어, `atan(1)`과 `atan2(1, 1)`은 모두 `pi/4`이지만, `atan2(-1, -1)`은 `-3*pi/4`입니다

math.degrees(x): 각도 x를 라디안에서 도(degree)로 변환한다.

math.radians(x): 각도 x를 도(degree)에서 라디안으로 변환한다.

## 상수

math.pi: 사용 가능한 정밀도로, 수학 상수 *π* = 3.141592…