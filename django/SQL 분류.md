# SQL 분류

## DDL(Data Definition Language): 데이터 정의 언어

- 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어.

- 예시) CREATE, DROP, ALTER

  - CREATE TABLE

    - 데이터베이스에서 테이블 생성

    - ```sqlite
      CREATE TABLE classmates (
          id INTENGER PRIMARY KEY, 
          name TEXT);
      ```

    - 필요한 정보에 대해서는 공백으로 비워두면 안된다. (NOT NULL 설정 필요)

    - ```sqlite
      CREATE TABLE classmates (
          id INTENGER PRIMARY KEY, 
          name TEXT NOT NULL,
          age INT NOT NULL
          );
      ```

  - DROP TABLE

    - 데이터베이스에서 테이블 제거

    - ```sqlite
      DROP TABLE classmates;
      ```

## DML(Data Manipulation Language): 데이터 조작 언어

- 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어

  - ```sqlite
    //csv 파일을 table로 만들기
    $ sqlite3 tutotlial.sqlite3
    sqlite> .database
    sqlite> .mode csv
    sqlite> .import hellodb.csv examples
    sqlite> .tables
    examples
    ```

- ### INSERT, SELECT, UPDATE, DELETE

  - ##### INSERT: 새로운 데이터 삽입(추가)

    - 테이블에 단일 행 삽입

    - ```sqlite
      INSERT INTO 테이블이름 (컬럼1, 컬럼2, ...) VALUES ( 값1, 값2, ...);
      ```

    - ```sqlite
      INSERT INTO classmates (name, age) VALUES('홍길동', 23);
      ```

    - classmates 테이블에 이름이 홍길동이고 나이가 23인 데이터 삽입하기

    - 모든 열에 데이터가 있는 경우에는 column을 명시하지 않아도 된다.

  - ##### SELECT: 저장되어있는 데이터 조회

    - ```sqlite
      SELECT * FROM examples;
      SELECT 컬럼1, 컬럼2 ... FROM 테이블이름; //모든 컬럼 값이 아닌 특정 컬럼만 조회하기
      SELECT 컬럼1, 컬럼2 ... FROM 테이블이름 LIMIT 숫자; // 원하는 수 만큼 데이터 조회하기
      SELECT 컬럼1, 컬럼2 ... FROM 테이블이름 LIMIT 숫자 OFFSET 숫자; // 특정 부분에서 원하는 수 만큼 데이터 조회하기
      SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
      //classmates 테이블에서 id, name 컬럼 값을 세번째에 있는 하나만 조회.
      SELECT 컬럼1, 컬럼2 ... FROM 테이블이름 WHERE 조건; //특정 데이터 확인하기
      SELECT DISTINCT 컬럼 FROM 테이블이름; //특정 컬럼을 기준으로 중복없이 가져오기
      
      ```

      - OFFSET

        - 동일 오브젝트 안에서 오브젝트 처음부터 주어진 요소나 지점까지 변위차(위치 변화량)을 나타내는 정수형

        - 문자열 'abcedf'에서 문자 'c'는 시작점'a'에서 2의 OFFSET을 지닌다.

        - ```sqlite
          SELECT * FROM MY_TABLE LIMIT 10 OFFSET 5
          ```

        - 6번째 행 부터 10개 행을 조회

        - 0부터 시작한다.

    - 특정 테이블의 레코드(행) 정보를 반환한다.

    - SQLite는 따로 PRIMARY KEY 속성의 칼럼을 작성하지 않으면 값이 자동으로 증가하는 PK옵션을 가진 rowid 컬럼을 정의한다.

    - 다양한 절(clause)와 함께 사용한다.

      - ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY 등..
        - LIMIT
          - 쿼리에서 반환되는 행 수를 제한
          - 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용하기도 함
        - WHERE
          - 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정
        - SELECT DISTINCT
          - 조회 결과에서 중복 행을 제거
          - DISTINCT 절은 SELECT키워드 바로 뒤에 작성해야 한다.

  - ##### UPDATE: 저장되어있는 데이터 갱신

    - 기존 행의 데이터를 수정

    - SET clause 에서 테이블의 각 열에 대해 새로운 값을 설정

    - ```sqlite
      UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2=값2 ... WHERE 조건;
      ```

    - 중복 불가능한 값인 rowid를 기준으로 수정.

  - ##### DELETE: 저장되어있는 데이터 삭제

    - 테이블에서 행을 제거

    - ```sqlite
      DELETE FROM 테이블이름 WHERE 조건;
      ```

    - 중복 불가능한 값인 rowid를 기준으로 삭제

    - sqlite는 기본적으로 id를 재사용한다.

    - AUTOINCREMENT

      - SQLite가 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
      - 테이블을 생성하는 단계에서 설정 하능하다.

## DCL(Date Control Language): 데이터 제어 언어

- 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어
- GRANT, REVOKE, COMMIT, ROLLBACK

## Aggregate Functions

집계 함수

값 집합에 대한 계산을 수행하고 단일 값을 반환

- 여러 행으로부터 하나의 결괏값을 반환하는 함수

SELECT 구문에서만 사용된다. (조회시에만 사용)

예시

- 테이블 전체 행 수를 구하는 **COUNT(*)**
- age 컬럼 전체 평균 값을 구하는 **AVG(age)**

종류

- COUNT

  - 그룹의 항목 수를 가져옴

  - ```sqlite
    SELECT COUNT(컬럼) FROM 테이블이름;
    ```

- AVG

  - 모든 값의 평균을 계산

- MAX

  - 그룹에 있는 모든 값의 최대값을 가져옴

- MIN

  - 그룹에 있는 모든 값의 최소값을 가져옴

- SUM

  - 모든 값의 합을 계산

- AVG, SUM, MIN, MAX 함수들은 기본적으로 해당 컬럼이 숫자(INTENGER)일 때만 사용 가능하다.



## LIKE operator

패턴 일치를 기반으로 데이터를 조회하는 방법

SQLite는 패턴 구성을 위한 2개의 wildcards를 제공한다.

- % (percent sign)

  - 0개 이상의 문자
  - 이 자리에 문자열이 있을 수도, 없을 수도 있다.

- _ (underscore)

  - 임의의 단일 문자
  - 반드시 이 자리에 한 개의 문자가 존재해야 한다.

- | 와일드카드 패턴  | 의미                                          |
  | ---------------- | --------------------------------------------- |
  | 2%               | 2로 시작하는 값                               |
  | %2               | 2로 끝나는 값                                 |
  | %2%              | 2가 들어가는 값                               |
  | _2%              | 아무 값이 하나 있고 두 번째가 2로 시작하는 값 |
  | 1___(1 _ _ _)    | 1로 시작하고 총 4자리인 값                    |
  | 2_% _% / 2 _ _ % | 2로 시작하고 적어도 3자리인 값                |

  

- [참고사항] wildcard character

  - 파일을 지정할 때, 구체적인 이름 대신에 여러 파일을 동시에 지정할 목적으로 사용하는 특수 기호
    - *, ? 등
  - 주로 특정한 패턴이 있는 문자열 혹은 파일을 찾거나, 긴 이름을 생략할 때 쓰임
  - 텍스트 값에서 알 수 없는 문자를 사용할 수 있는 특수문자로, 유사하지만 동일한 데이터가 아닌 여러 항목을 찾기에 매우 편리한 문자
  - 지정된 패턴 일치를 기반으로 데이터를 수집하는데도 도움이 될 수 있음

- ```sqlite
  SELECT * FROM 테이블 WHERE 컬럼 LICE '와일트카드 패턴';
  ```



## ORDER BY clause

ORDER BY

조회 결과 집합을 정렬

SELECT 문에 추가하여 사용

정렬 순서를 위한 2개의 keyword 제공

- ASC - 오름차순 (default)
- DESC - 내림차순

```sqlite
SELECT * FROM 테이블 ORDER BY 컬럼 ASC;
SELECT * FROM 테이블 ORDER BY 컬럼 DESC;
```

## GROUP BY clause

GROUP BY

행 집합에서 요약 행 집합을 만듦

SELECT 문의 optional 절

선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦

문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성해야 함

```sqlite
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
```

AS를 활용해서 COUNT에 해당하는 컬럼 명을 바꿔서 조회할 수 있음

## ALTER TABLE statement

ALTER TABLE의 3가지 기능

1. table 이름 변경

2. 테이블에 새로운 column 추가

3. column 이름 수정

   - ```sqlite
     ALTER TABLE 기존테이블이름 RENAME TO 새로운테이블이름;
     ```

   - 새로운 컬럼 추가

   - ```sqlite
     ALTER TABLE 테이블이름 ADD COLUMN 컬럼이름 데이터타입 설정ㅅ
     ```

   - 이때 테이블에 있던 기존 레코드들에는 새로 추가할 필드에 대한 정보가 없다. 그렇기 때문에 NOT NULL 형태의 컬럼은 추가가 불가능하다.

   - 해결 방법 2가지

     -  NOT NULL 설정 없이 추가하기

     - 기본값(DEFAULT) 설정하기

     - ```sqlite
       ALTER TABLE 테이블이름 ADD COLUMN 컬럼이름 TEXT NOT NULL DEFAULT 소제목
       ```

     - 