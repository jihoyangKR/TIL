# 데이터베이스 (DB)

데이터 베이스는 체계화된 데이터의 모임이다.

여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합

논리적으로 연관된 (하나 이상의) 자료의 모음.

내용을 고도로 구조화 함으로써 검색과 갱신의 효율화를 꾀한 것

즉 **몇 개의 자료 파일을 조직적으로 통합**하여 **자료 항목의 중복을 없애고 자료를 구조화**하여 기억시켜 놓은 **자료의 집합체**

## 데이터베이스로 얻는 장점들

데이터 중복 최소화

데이터 무결성(정확한 정보를 보장한다.)

데이터 일관성

데이터 독립성 (물리적 / 논리적)

데이터 표준화

데이터 보안 유지

# RDB (관계형 데이터베이스)

Relational Database

키(key)와 값(value)들의 관계(relation)를 표 형태로 정리한 데이터베이스

관계형 모델에 기반한다.

- 스키마 (schema)

  - 데이터베이스에서 자료의 구조, 표현방법, 관계 등 **전반적인 명세**를 기술한 것

  - | column  | datatype |
    | ------- | -------- |
    | id      | INT      |
    | name    | TEXT     |
    | address | TEXT     |
    | age     | INT      |

- 테이블 (table)

  - 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합

  - |  id  |  name  | address | age  |
    | :--: | :----: | :-----: | :--: |
    |  1   | 홍길동 |  제주   |  20  |
    |  2   | 김길동 |  서울   |  30  |
    |  3   | 박길동 |  독도   |  40  |

  - 열 (column / field) : 각 열에는 고유한 데이터 형식이 지덩된다.

  - 행 (row / record) : 실제 데이터가 저장되는 형태

  - 기본키 (Pirmary Key) : 각 행의 고유 값, 반드시 설정해야 하며 데이터베이스 관리 및 관계 설정 시 주요하게 활용된다.

# RDBMS (Relational Database Management System)

관계형 모델을 기반으로 하는 데이터베이스 관리시스템

## SQLite

서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 하용하는 비교적 가벼운 데이터베이스

### Sqlite Data Type

1. NULL
2. INTEGER : 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트에 저장된 부호있는 정수
3. REAL : 8바아트 부동 소수점 숫자로 저장된 부동 소수점 값
4. TEXT
5. BLOB : 입력된 그대로 정확히 저장된 데이터 (별다른 타입 없이 그대로 저장)

### Sqlite Type Affinity

- Type Affinity
  - 특정 컬럼에 저장하도록 권장하는 데이터 타입

1. INTEGER
2. TEXT
3. BLOB
4. REAL
5. NUMERIC

# SQL (Structured Query Language)

관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적 프로그래밍 언어

- SQL의 기능
  - 데이터베이스 스키마 생성 및 수정
  - 자료의 검색 및 관리
  - 데이터베이스 객체 접근 조정 관리

### SQL 분류

| 분류                                                     | 개념                                                         | 예시                                        |
| -------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------- |
| DDL -데이터 정의 언어<br />(Data Definition Language)    | 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 | CREATE<br />DROP<br />ALTER                 |
| DML - 데이터 조작 언어<br />(Data Manipulation Language) | 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어        | INSERT<br />SELECT<br />UPDATE<br />DELETE  |
| DCL - 데이터 제어 언어<br />(Date Control Language)      | 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어       | GRANT<br />REVOKE<br />COMMIT<br />ROLLBACK |

### SQL Keywords - Data Manipulation Language

#### CRUD 정리

- INSERT : 새로운 데이터 삽입(추가) (C)

  - 테이블에 단일 행 삽입

  - ```sqlite
    INSERT INTO 테이블이름 (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ...);
    ```

  - SQLite는 따로 PRIMARY KEY 속성의 컬럼을 작성하지 않으면 값이 자동으로 증가하는 PK 옵션을 가진  rowid 컬럼을 정의한다.

- SELECT : 저장되어있는 데이터 조회 (R)

  - 다양한 절(clause)와 함께 사용한다.

    - ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY...

      - LIMIT

        - 쿼리에서 반환되는 행 수를 제한
        - 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용하기도 한다

      - WHERE

        - 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정한다.

      - SELECT DISTINCT

        - 조회 결과에서 중복 행을 제거한다.
        - DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 한다.

      - ```sqlite
        -- 모든 컬럼 값이 아닌 특정 컬럼만 조회하기
        -- SELECT 컬럼1, 컬럼2, .. FROM 테이블 이름;
        -- classmates 테이블에서 id, name 컬럼 값만 조회하기
        SELECT id, name FROM classmates;
        -- 원하는 수 만큼 데이터 조회하기
        -- SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 LIMIT 숫자;
        SELECT rowid, name FROM classmates LIMIT 1;
        -- 특정 부분에서 원하는 수 만큼 데이터 조회하기
        -- SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 LIMIT 숫자 OFFSET 숫자;
        -- classmates 테이블엣 id, name 컬럼 값을 세번째에 있는 하나만 조회
        SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
        ```

      - OFFSET

        - 동일 오브젝트 안에서 오브젝트 처음에서 주어진 요소나 지점까지의 변위차(위치 변화량)을 나타내는 정수형

        - 예시

          - 문자열 'abcedf'에서 문자 'c'는 시작점'a'에서 2의 OFFSET을 지닌다

          - ```sqlite
            SELECT * FROM MY_TABLE LIMIT 10 OFFSET 5
            ```

          - 6번째 행 부터 10개 행을 조회

          - 0부터 시작한다.

      - WHERE

      - ```sqlite
        -- 특정 데이터(조건) 조회하기
        -- SELECT 컬럼1, 컬럼2 ... FROM 테이블이름 WHERE 조건;
        -- classmate 테이블에서 id, name 컬럼 값 중에 주소가 서울인 경우의 데이터를 조회
        SELECT rowid, name FROM classmates WHERE address = '서울';
        ```

      - DISTINCT

      - ```sqlite
        -- 특정 컬럼을 기준으로 중복없이 가져오기
        -- SELECT DISTINCT 컬럼 FROM 테이블이름;
        -- classmates 테이블에서 age값 전체를 중복없이 조회
        SELECT DISTINCT age FROM classmates;
        ```

- UPDATE : 저장되어있는 데이터 갱신 (U), 기존 행의 데이터를 수정

  - SET clause에서 테이블의 각 열에 대해 새로운 값을 설정

  - ```sqlite
    UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2=값2, ... WHERE 조건;
    -- 중복 불가능한 값인 rowid를 기준으로 수정
    UPDATE classmates Set name='홍길동', address='제주도' WHERE rowid=5;
    ```

    

- DELETE : 저장되어있는 데이터 삭제 (D), 테이블에서 행을 제거

  - ```sqlite
    -- 조건을 통해 특정 레코드 삭제하기
    -- DELETE FROM 테이블이름 WHERE 조건;
    -- 중복 불가능(UNIQUE)값인 rowid를 기준으로 삭제.
    DELETE FROM classmates WHERE rowid=5;
    ```

  - SQLite는 기본적으로 id를 재사용한다. 이를 방지하기 위해서 테이블 생성 단계에서 PRIMARY KEY를 설정할 때 AUTOINCREMENT를 작성한다.

  - ```sqlite
    CREATE TABLE 테이블이름 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ...
    );
    ```

### 테이블 생성 및 삭제 statement

- CREATE TABLE
  - 데이터베이스에서 테이블 생성
- DROP TABLE
  - 데이터베이스에서 테이블 제거

```sqlite
CREATE TABLE classmates (
	name TEXT,
	age INT,
	address TEXT
);
```



# Clause 활용하기

### TABLE

```sqlite
CREATE TABLE users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTENGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTENGER NOT NULL
);
```

- ### WHERE

  - ```sqlite
    -- users 테이블에서 age가 30 이상인 유저의 모든 컬럼 정보를 조회
    SELECT * FROM users WHERE age>=30;
    -- users 테이블에서 age가 30 이상인 유저의 first_name 컬럼 정보를 조회
    SELECT first_name FROM users WHERE age>=30;
    -- users 테이블에서 age가 30 이상, 성이 '김'인 사람의 나이와 성만 조회
    
    SELECT age, last_name FROM users WHERE age>=30 AND last_name='김';
    ```

- ### Aggregate function

  - 집계함수

  - 값 집합에 대한 계산을 수행하고 단일 값을 반환한다.

  - 여러 행으로부터 하나의 결괏값을 반환하는 함수

  - SELECT 구문에서만 사용된다.

  - 예시

  - 테이블 전체 행 수를 구하는 COUNT(*)

  - age 컬럼 전체 평균 값을 구하는 AVG(age)

  - COUNT : 그룹의 항목 수를 가져온다.

  - ```sqlite
    -- users 테이블의 레코드의 총 개수 조회
    SELECT COUNT(*) FROM users;
    ```

  - 아래의 함수들은 기본적으로 컬럼이 숫자(INTEGER)일 때만 사용 가능하다.

  - AVG : 모든 값의 평균을 계산

  - ```sqlite
    -- 30살 이상인 사람들의 평균 나이
    SELECT AVG(age) FROM users WHERE age>=30;
    -- 나이 30 이상인 사람의 계좌 평균 잔액 조회
    SELECT AVG(balance) FROM users WHERE age>=30;
    ```

  - MAX : 그룹에 있는 모든 값의 최대값을 가져온다.

  - ```sqlite
    -- 계좌 잔액(balance)이 가장 높은 사람과 그 액수 조회
    SELECT first_name, MAX(balance) FROM users WHERE balance;
    ```

  - MIN : 그룹에 있는 모든 값의 최소값을 가져온다.

  - SUM : 모든 값의 합을 계산한다.

- ### LIKE

  - 패턴 일치를 기반으로 데이터를 조회하는 방법, SQLite는 패턴 구성을 위한 2개의 wildcards를 제공한다.

  - % (percent sign)

    - 0개 이상의 문자
    - 이 자리에 문자열이 있을 수도, 없을 수도 있다.

  - _ (underscore)

    - 임의의 단일 문자
    - 반드시 이 자리에 한 개의 문자가 존재해야 한다.

  - ```sqlite
    SELECT * FROM 테이블 WHERE 컬럼 LIKE '와일드카드패턴';
    ```

  - | 와일드카드패턴 | 의미                                          |
    | -------------- | --------------------------------------------- |
    | 2%             | 2로 시작하는 값                               |
    | %2             | 2로 끝나는 값                                 |
    | %2%            | 2가 들어가는 값                               |
    | _2%            | 아무 값이 하나 있고 두 번째가 2로 시작하는 값 |
    | 1___           | 1로 시작하고 총 4자리인 값                    |
    | 2_%_% / 2 __%  | 2로 시작하고 적어도 3자리인 값                |

  - ```sqlite
    -- users 테이블에서 나이가 20대인 사람만 조회
    SELECT * FROM users WHERE age LIKE '2_';
    -- users 테이블에서 지역번호가 02인 사람만 조회
    SELECT * FROM users WHERE phone LIKE '02-%';
    ```

- ### ORDER BY

  - 조회 결과 집합을 정렬

  - SELECT 문에 추가하여 사용

  - 정렬 순서를 위한 2개의 keyword를 제공한다

    - ASC - 오름차순 (default)
    - DESC - 내림차순

  - ```sqlite
    -- SELECT * FROM 테이블 ORDER BY 컬럼 ASC;
    -- SELECT * FROM 테이블 ORDER BY 컬럼 DESC;
    SELECT * FROM users ORDER BY age, last_name ASC LIMIT 100; -- 처음 order by 한 colum 을 먼저 정렬한다.
    SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;
    ```

- ### GROUP BY

  - 행 집합에서 요약 행 집합을 만든다.

  - SELECT 문의 optional 절

  - 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만든다.

  - 문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성해야 한다.

  - ```sqlite
    SELECT 컬럼1, aggregate_function(컬럼2) FROM 테이블 GROUP BY 컬럼1, 컬럼2;
    -- users에서 각 성(last_name)씨가 몇 명씩 있는지 조회
    SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
    -- 이때 AS를 활용해서 COUNT에 해당하는 컬럼 명을 바꿔 조회할 수 있다.
    SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
    ```

- ### ALTER TABLE

  - table 이름 변경

  - 테이블에 새로운 column 추가

  - column 이름 수정 (sqlite 3.25.0부터 추가)

  - ```sqlite
    -- 테이블 이름 변경
    ALTER TABLE 기존테이블이름 RENAME TO 새로운 테이블이름;
    ALTER TABLE articles RENAME TO news;
    -- 새로운 컬럼 추가
    ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;
    -- 위의 SQL문을 쓰면 오류가 난다. 테이블에 있던 기존 레코드에는 새로 추가할 필드에 대한 정보가 없기 때문이다. 그렇기 때문에 NOT  NULL형태의 컬럼은 추가가 불가능하다.
    -- 이를 해결하기 위한 2가지 방법
    -- 1. NOT NULL 설정 없이 추가하기
    ALTER TABLE news ADD COLUMN created_at TEXT;
    -- 2. 기본값(DEFAULT) 설정하기
    ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';
    ```