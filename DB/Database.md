# Database

## 데이터베이스란?

- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된 하나 이상의 자료의 모음으로 그 내용을 고도로 구조화 함으로써 검색과 갱신의 효율화를 꾀한 것
- 몇 개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜놓은 자료의 집합체

## DBMS(Database Management System)

데이터베이스 관리 프로그램

- 데이터베이스 조작 인터페이스 제공(검색, 수정, 삭제, 추가: CRUD)
- 효율적인 데이터 관리 기능 제공
- 데이터베이스 구축 기능 제공
- 데이터 복구, 사용자 권한 부여, 유지보수 기능 제공

## 관계형 데이터베이스(Relational DB)

##### 테이블(Table) 기반의 DB

##### 데이터를 테이블 단위로 관리

- 하나의 데이터(record)는 여러 속성(Attribute)을 가진다.
- 데이터 중복을 최소화
- 테이블 간의 관계를 이용하여 필요한 데이터 검색 가능

##### 테이블(Table)

- 실제 데이터가 저장되는 곳

## 관계형 데이터 베이스 관리 시스템(Relational Database Management System)

## SQL(Structed Query Language)

관계형 데이터 베이스에서 데이터 조작과 데이터 정의를 위해 사용하는 언어

- 데이터 조회
- 데이터 삽입, 삭제, 수정
- DB Object 생성 및 변경, 삭제
- DB 사용자 생성 및 삭제, 권한 제어

표준 SQL은 모든 DBMS에서 사용가능

User가 DBMS에 SQL을 날리면 DBMS는 DB에서 데이터를 가져와 User에게 return한다.

### DDL(Data Definition Language): 데이터 정의 언어

- 관계형 데이터베이스 객체의 구조(table, view, user, index 등)를 정의하기 위한 명령어.

#### CREATE: 테이블 등 데이터 객체를 생성할 때 사용

- ```sql
  CREATE DATABASE databasename;
  ```

- CREATE DATABASE 명령문은 새 데이터 베이스를 생성하는데 사용된다.

- 데이터 베이스는 여러 테이블을 포함하고 있다.

- 데이터 베이스 생성시 관리자 권한으로 생성해야 한다.

- ```sql
  SHOW DATABASES;
  --데이터베이스 생성 후, 위 명령어를 이용해서 데이터 베이스의 목록을 확인할 수 있다.
  ```

- CREATE TABLE

  - 데이터베이스에서 테이블 생성

  - ```sqlite
    CREATE TABLE table_name (
        column1 datatype [options],
        column2 datatype [options],
    );
    ```

  - 필요한 정보에 대해서는 공백으로 비워두면 안된다. (NOT NULL 설정 필요)

  - ```sqlite
    CREATE TABLE classmates (
        id INTENGER PRIMARY KEY, 
        name TEXT NOT NULL,
        age INT NOT NULL
        );
    ```

  - | 옵션           | 설명                                                         |
    | -------------- | ------------------------------------------------------------ |
    | NOT NULL       | 각 행은 해당열의 값을 포함해야 하며 null값은 허용되지 않음   |
    | DEFAULT        | 값이 전달되지 않을 때 추가되는 기본값 설정                   |
    | AUTO INCREMENT | 새 레코드가 추가 될 때 마다 필드 값을 자동으로 1 증가 시킴   |
    | PRIMARY KEY    | 테이블에서 행을 고유하게 식별하기 위해 사용. PRIMARY KEY 설정이 있는 열은 일반적으로 ID번호이며 AUTO INCREMENT와 함께 사용 |
    | UNSIGNED       | 숫자인 경우만 해당 되며 숫자가 0 또는 양수로 제한됨          |

  - 제약 조건(CONSTRANIT)

    - 컬럼에 저장될 데이터의 조건을 설정
    - 제약조건에 위배되는 데이터는 저장 불가
    - 테이블 생성시 컬럼에 지정하거나, constraint로 지정가능(ALTER를 이용하여 설정 가능)
    - ![image-20220703153805493](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703153805493.png?token=AXI75U5NZUNQ7372RPBOUSTCYE4YW)
  
- 테이블(Table) 스키마

  - 스키마(Schema): 테이블에 저장될 데이터의 구조와 형식

  - 예) 회원의 정보를 저장하기 위한 테이블

  - ![image-20220703153932499](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703153932499.png?token=AXI75U234RUQGCAWOJWDYJDCYE46E)

  - ![image-20220703153950352](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703153950352.png?token=AXI75U4PTTTPLQIWHO7DS6TCYE47I)

  - 테이블 스키마 확인하기

    - DESCRIBE 또는 DESC 명령어를 이용하여 생성된 테이블 스키마 확인

    - ```sql
      {DESCRIBE | DESC} table_name;
      ```

#### ALTER: 테이블 등 데이터 객체를 변경할 때 사용

- 데이터베이스 삭제

  - DROP: 테이블 등 데이터 객체를 삭제할 때 사용

  - 데이터베이스의 모든 테이블을 삭제하고 데이터베이스를 삭제

  - 삭제 시, DROP DATABASE 권한 필요

  - DROP SCHEMA는 DROP DATABASE와 동의어

  - IF EXISTS는 데이터가 없을 시 발생할 수 있는 에러를 방지

    - ```SQL
      DROP {DATABASE|SCHEMA} [IF EXISTS] db_name
      ```

- 데이터베이스 사용

  - 데이터베이스가 있는 경우(접근 권한이 있는 경우), USE 명령어를 이용하여 사용한다.

  - ```sql
    USE databasename;
    ```

#### RENAME: 테이블 등 객체의 이름을 변경할 때 사용

- 예시) CREATE, DROP, ALTER

  - DROP TABLE

    - 데이터베이스에서 테이블 제거

    - ```sqlite
      DROP TABLE classmates;
      ```

- 데이터베이스 문자 집합(Character set) 설정하기

  - 데이터베이스 생성 시 설정 또는 생성 후 수정 가능

  - 문자집합은 각 문자가 컴퓨터에 저장될 때 어떠한 '코드'로 저장되는지 규칙을 지정한 집합이다.

  - Collaction은 특정 문자 집합에 의해 데이터베이스에 저장된 값들을 비교, 검색, 정렬 등의 작업을 수행할 때 사용하는 비교 규칙 집합이다

  - ```sql
    CREATE DATABASE db_name
    	[[DEFAULT]CHARACTER SET charset_name]
    	[[DEFAULT]COLLATE collation_name]]
    ALTER DATABASE db_name
    	[[DEFAULT]CHARACTER SET charset_name]
        [[DEFAULT]COLLATE collation_name]]
    ```


### DML(Data Manipulation Language): 데이터 조작 언어

- 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어

- #### INSERT, SELECT, UPDATE, DELETE

  - ##### INSERT: 새로운 데이터 삽입(추가)

    - 테이블에 단일 행 삽입

    - 모든 열에 데이터가 있는 경우에는 column을 명시하지 않아도 된다.
  
    - 컬럼이름과 입력 값의 순서가 일치하도록 작성

      - (NULL, DEFAULT, AUTO INCREMENT 설정 필드 생략가능)
      - DB에서 NULL은 `몰라`의 의마로 받아들이면 된다.
  
    - ```sqlite
      INSERT INTO 테이블이름 (컬럼1, 컬럼2, ...) 
      VALUES ( 값1, 값2, ...);
      ```

    - ```sql
      INSERT INTO 테이블이름 (컬럼1, 컬럼2, ...) 
      VALUES ( 값1, 값2, ...),
      (값2, 값2, ...);
      --여러 레코드를 한번에 생성할 수도 있다.
      ```
  
    - ```sqlite
      INSERT INTO ssafy_member (userid, username, userpw, emailid, emaildomain, joindate)
      VALUSE ('id_kim', '김싸피', 'pass123', 'kimssafy', 'ssafy.com', now());
      ```
  
      

  - ##### SELECT: 저장되어있는 데이터 조회

    - 테이블에서 레코드를 조회하기 위해 사용

    - 조회 시 컬럼이름이나 표현식을 조회할 수 있도 별칭(alias)사용이 가능하다.

    - *는 모든 속성을 조회한다.
  
    - WHERE 조건식을 이용하여 원하는 레코드를 조회할 수 있다.

    - ```sql
      SELECT * FROM examples;
      SELECT 컬럼1, 컬럼2 ... FROM 테이블이름; //모든 컬럼 값이 아닌 특정 컬럼만 조회하기
      SELECT 컬럼1, 컬럼2 ... FROM 테이블이름 LIMIT 숫자; // 원하는 수 만큼 데이터 조회하기
      SELECT 컬럼1, 컬럼2 ... FROM 테이블이름 LIMIT 숫자 OFFSET 숫자; // 특정 부분에서 원하는 수 만큼 데이터 조회하기
      SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
      //classmates 테이블에서 id, name 컬럼 값을 세번째에 있는 하나만 조회.
      SELECT 컬럼1, 컬럼2 ... FROM 테이블이름 WHERE 조건; //특정 데이터 확인하기
      SELECT DISTINCT 컬럼 FROM 테이블이름; //특정 컬럼을 기준으로 중복없이 가져오기
      ```
  
      - 부서번호가 30인 사원 중 급여가 1500이상인 사원의 이름, 급여, 부서번호 조회
  
        - ```sql
          SELECT ename, sal, deptno
          FROM emp
          WHERE deptno = 30 AND SAL >= 1500;
          ```
  
      - 부서번호가 20 또는 30인 부서에서 근무하는 사원의 사번, 이름, 부서번호 조회
  
        - ```sql
          SELECT ename, sal, deptno
          FROM emp
          WHERE deptno = 30 OR deptno = 20;
          ```
  
      - 부서번호가 20, 30이 아닌 부서에서 근무하는 사원의 사번, 이름, 부서번호 조회
  
        - !=와 <> 모두 not equal을 의미한다.
  
        - ```sql
          SELECT ename, sal, deptno
          FROM emp
          WHERE deptno != 30
          AND deptno <> 20;
          ```
  
        - NOT - 조건문이 NOT TRUE 일 때 레코드를 조회

        - ```sql
          SELECT ename, sal, deptno
          FROM emp
          WHERE NOT (deptno = 30 or deptno = 20);
          ```
  
        - IN - 피연산자가 여러 표현 중 하나라도 같아면 TRUE
  
          - 예시 ) 업무(job)가 'MANAGER', 'ANALYSTY', 'PRESIDENT'인 사원의 이름, 사번, 업무 조회
  
          - ```SQL
            SELECT empon, ename, job
            FROM emp
            WHERE job in ( 'MANAGER', 'ANALYSTY', 'PRESIDENT);
            ```
  
          - 예시) 부서번호가 10, 20이 아닌 사원의 사번, 이름, 부서번호 조회
  
          - ```sql
            SELECT empno, ename, deptno
            FROM emp
            WHERE deptno not in (10, 20);
            ```
  
        - BETWEEN - 값이 주어진 범위의 범위 안에 있으면 조회
  
          - 값은 숫자나 문자, 날짜가 될 수 있다.
  
          - ```SQL
            WHERE column_name BETWEEN value1 AND value2;
            ```
  
          - 급여가 2000 이상 3000이하 인 사원의 사번, 이름, 급여 조회
  
          - ```sql
            SELECT empno, ename, sal
            FROM emp
            WHERE sal BETWEEN 2000 AND 3000;
            ```
  
        - NULL 비교 - IS NULL, IS NOT NULL
  
          - ```sql
            SELECT empno, ename, sal
            FROM emp
            WHERE comm IS NOT NULL;
            ```
  
        - LIKE - WHERE 절에서 칼럼의 값이 특정 패턴을 가지는지 검사하기 위해 사용
  
          - 와일드카드(%, _)를 이용해 패턴을 표현한다.
  
            - % : 0개 이상의 문자를 의미
            - _ : 문자 하나를 의미
  
          - 이름이 'M'으로 시작하는 사원의 사번, 이름 조회
  
          - ```sql
            SELECT empno, ename
            FROM emp
            WHERE ename like 'M%';
            ```
  
        - 논리연산자 - NOT, AND, OR
  
          - ![image-20220703181137798](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703181137798.png?token=AXI75U4NJIBZF5FPBMOFZ2LCYFOYO)
  
    - 기본 SELECT문 - 별명(alias), 사칙연산
  
      - 사원의 이름, 사번, 급여 *12(연봉), 업무조회
  
      - as를 이용하여 조회 시 컬럼이름을 변경할 수 있다. (띄어 쓰기 포함 시 ""으로 묶어준다.)
  
      - ```sql
        SELECT ename as 이름, empno as 사번, sal * 12 as 연봉, job as "업 무"
        FROM emp;
        ```
  
      - 사원의 이름, 사번, 커미션, 급여, 커미션 포함 급여 조회
  
      - ```sql
        SELECT ename 이름, empno as "사번", comm 커미션, sal as 급여, sal + comm as "키미션 포함 급여", sal + IFNULL(comm,0) as "커미션 포함 급여2"
        FROM emp;
        ```
  
      - 사칙연산 사용 가능, NULL 값은 계산 불가
  
      - IFNULL 함수를 이용하여 NULL 값 처리 - IFNULL(exp1, exp2): exp1이 NULL이면 exp2가 return
  
    - CASE Function
  
      - 문법
  
        - ```sql
          CASE
          	WHEN condition1 THEN result1
              WHEN condition2 THEN result2
              WHEN conditionN THEN resultN
              ELSE result
          END;
          ```
  
      - CASE문은 조건을 통과하고 첫 번째 조건이 충족될 때 값을 반환한다
  
      - 조건이 충족되지 않으면 ELSE 절의 값을 반환한다.
  
      - 예시) 모든 사원의 사번, 이름, 급여 등급 조회(5000이상 -> 고액연봉, 2000이상-> 평균 연봉, 그 외->저액연봉)
  
      - ```sql
        SELECT empno 사번, ename 이름, sal 급여,
        	CASE WHEN sal >= 5000 THEN '고액연봉'
        		 WHEN sal >= 2000 THEN '평균연봉'
        		 ELSE '저액연봉'
            END "연봉등급"
            FROM emp;
        ```
  
      - ![image-20220703164231112](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703164231112.png?token=AXI75UZCUCG3SI56SB5RYCTCYFEKI)
  
    - OFFSET
  
      - 동일 오브젝트 안에서 오브젝트 처음부터 주어진 요소나 지점까지 변위차(위치 변화량)을 나타내는 정수형
  
      - 문자열 'abcedf'에서 문자 'c'는 시작점'a'에서 2의 OFFSET을 지닌다.
  
      - ```sqlite
        SELECT * FROM MY_TABLE LIMIT 10 OFFSET 5
        ```
  
      - 6번째 행 부터 10개 행을 조회
  
      - 0부터 시작한다.
  
    - 특정 테이블의 레코드(행) 정보를 반환한다.
  
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
          
        - ORDER BY
        
          - 조회결과를 오름차순(ASC) 또는 내림차순 (DESC)으로 정렬할 때 사용한다. (default:ASC)
        
          - 정렬 기준(칼럼)을 지정할 수 있다.
        
          - ```sql
            SELECT column1, column2, ...
            FROM table_name
            ORDER BY column1, column2, ... ASC|DESC
            ```
        
          - 직원의 모든 정보를 이름을 기준 내림차순으로 정렬하여 조회
        
          - ```sql
            SELECT *
            FROM emp
            ORDER BY ename DESC;
            ```
        
          - 20, 30번 부서에 근무하는 사원의 사번, 이름, 부서번호, 급여를 조회
        
          - 단, 부서별 오름차순 정렬 후, 급여 순 내림차순 정렬
        
          - ```sql
            SELECT empno, ename, deptno, sla
            FROM emp
            WHERE deptno in (20, 30)
            ORDER BY deptno, sal DESC;
            ```
        
          - 
  
  - ##### UPDATE: 저장되어있는 데이터 갱신
  
    - 기존 레코드를 수정
  
    - WHERE 절을 이용해 하나의 레코드 또는 다수의 레코드를 한 번에 수정할 수 있다.
  
    - SET clause 에서 테이블의 각 열에 대해 새로운 값을 설정
  
    - ```sql
      UPDATE 테이블이름
      	SET 컬럼1=값1, 컬럼2=값2 ...
          [WHERE 조건];
          !--WHERE절을 생략하면 테이블의 모든 행이 수정되므로 조건 지정을 해주어야 한다.
      ```
      
    - 중복 불가능한 값인 rowid를 기준으로 수정.
  
  - ##### DELETE: 저장되어있는 데이터 삭제
  
    - 테이블에서 행을 제거
  
    - WHERE절을 이용해 하나의 레코드 또는 다수의 레코드를 한번에 삭제할 수 있다.
  
    - ```sqlite
      DELETE FROM 테이블이름 WHERE 조건;
      ```
  
    - 중복 불가능한 값인 rowid를 기준으로 삭제

### TCL(Transaction Control Language): 트랜잭션 제어 언어

#### 트랜잭션(Transaction)

- 커밋(Commit) 하거나 롤백(Rollback)할 수 있는 가장 작은 작업 단위

- 커밋: 트랜잭션을 종료하여 변경사항에 대해서 영구적으로 저장하는 SQL

- 롤백: 트랜잭션에 의해 수행된 모든 변경사항을 실행취소하는 SQL

- | name             | description                                                  |
  | ---------------- | ------------------------------------------------------------ |
  | START TRANSATION | 트랜젝션을 시작함. COMMIT, ROLLBACK이 나오기 전까지 모든 SQL을 의미 |
  | COMMIT           | 트랜잭션에서 변경한 사항을 영구적으로 DB에 반영              |
  | ROLLBACK         | START TRANSACTION 실행 전 상태로 되돌림                      |

  MySQL에서는 기본적으로 세션이 시작하면 autocommit 설정 상태이다. 그러므로 MySQL은 각 SQL문장이 오류를 반환하지 않으면 commit을 수행한다.

- 트랜잭션단위로 실행한 명령문을 적용하거나 취소
- COMMIT, ROLLBACK: DML문이 변경한 내용을 관리. 변경사항을 저장(COMMIT)하거나 취소(ROLLBACK)할 때 사용한다. 이때 DML변경 내용은 트랜잭션 단위로 그룹화 가능하다.
- mySql의 경우에는 AutoCommit이 되어있어 바로 저장이 된다.
- ![image-20220703182532632](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703182532632.png?token=AXI75U226U7LYCWWXQAHAKLCYFQMU)

### DCL(Date Control Language): 데이터 제어 언어

- 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어
- Database, Table 접근 권한이나 CRUD권한 정의
- 특정 사용자에게 테이블의 검색권한 부여/금지
- GRANT: 데이터베이스 접근권한 부여
- REVOKE: 데이터베이스 접근권한 삭제
- COMMIT, ROLLBACK

### MySQL - Functions

MySQL 내장함수

MySQL은 많은 내장함수를 가지고 있다.

![image-20220703181725982](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703181725982.png?token=AXI75U3NQAA23PEG6V54IBTCYFPOG)

![image-20220703181809768](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703181809768.png?token=AXI75U2QGCPDJRT6ORAIGC3CYFPRC)

![image-20220703181833658](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703181833658.png?token=AXI75U4RSPX67CP37UB2SHTCYFPSQ)

![image-20220703181844121](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703181844121.png?token=AXI75U4HPPTE7B5BFFT6JRTCYFPTG)

![image-20220703181901640](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703181901640.png?token=AXI75U5ITUAM4X2UM3FCCZDCYFPUG)

![image-20220703181915421](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703181915421.png?token=AXI75U7LZU4WNMUEDKFGJQLCYFPVC)

![image-20220703181927486](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703181927486.png?token=AXI75U64LPHMSQS7OR2HPCLCYFPV2)

![image-20220703181940085](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703181940085.png?token=AXI75U2YLZ2ZFDKBJPMAEF3CYFPWS)

![image-20220703181949293](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703181949293.png?token=AXI75U2OJJVXYW2PAYKKTKDCYFPXG)

![image-20220703182001308](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703182001308.png?token=AXI75U7UIATLDF22CU7AGUDCYFPYA)

![image-20220703182011945](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703182011945.png?token=AXI75U2XNYVRF6QUVAB7SDDCYFPYS)

![image-20220703182022707](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703182022707.png?token=AXI75UZELQULDTVKBO4EKHLCYFPZI)

![image-20220703182036733](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703182036733.png?token=AXI75U5XC7J62N773EP3ULLCYFP2E)

![image-20220703182048797](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220703182048797.png?token=AXI75U4CFCRZ6CSKTVQ7CULCYFP24)

```sql
CREATE DATABASE `SCOTT` default character SET utf8mb4;

show databases;

use scott;

CREATE TABLE IF NOT EXISTS `BONUS` (
`ENAME` varchar(10) DEFAULT NULL,
`JOB` varchar(9) DEFAULT NULL,
`SAL` double DEFAULT NULL,
`COMM` double DEFAULT NULL);

drop table if exists dept;

create table if not exists `DEPT` (
`DEPTNO` int(11) not null,
`dname` varchar(14) default null,
`loc` varchar(13) default null,
primary key (`DEPTNO`));

insert into `DEPT` (`DEPTNO`, `DNAME`, `LOC`)
values(10, 'ACCOUNTING', 'NEW YORK'),
(20, 'RESEARCH', 'DALLAS'),
(30, 'SALES', 'CHICAGO'),
(40, 'OPERATIONS', 'BOSTON');

CREATE TABLE IF NOT EXISTS `EMP` (
`EMPNO` int(11) NOT NULL,
`ENAME` varchar(10) DEFAULT NULL,
`JOB` varchar(9) DEFAULT NULL,
`MGR` int(11) DEFAULT NULL,
`HIREDATE` datetime DEFAULT NULL,
`SAL` double DEFAULT NULL,
`COMM` double DEFAULT NULL,
`DEPTNO` int(11) DEFAULT NULL,
PRIMARY KEY(`EMPNO`), -- primary key를 `EMPNO`로 하겠다.  
KEY `PK_EMP` (`DEPTNO`)); -- 왜래키 `DEPTNO`를 가져오겠다.

insert into `EMP` (`EMPNO`,`ENAME`,`JOB`,`MGR`,`HIREDATE`, `SAL`, `COMM`, `DEPTNO`)
VALUES
(7838, 'KING', 'PRESIDENT', NULL, '1981-11-17 00:00:00', 5000, NULL, 10),
(7782, 'CLARK', 'MANAGER', 7839, '1981-06-09 00:00:00', 2450, NULL, 10),
(7934, 'MILLER', 'CLERK', 7782, '1982-01-23 00:00:00', 1300, NULL, 10),
(7566, 'JONES', 'MANAGER', 7839, '1981-04-02 00:00:00', 2975, NULL, 20),
(7788, 'SCOTT', 'ANALYST', 7566, '1981-04-19 00:00:00', 3000, NULL, 20),
(7876, 'ADAMS', 'CLERK', 7788, '1987-05-23 00:00:00', 1100, NULL, 20),
(7902, 'FORD', 'ANALYST', 7566, '1981-12-03 00:00:00', 3000, NULL, 20),
(7369, 'SMITH', 'CLERK', 7902, '1980-12-17 00:00:00', 800, NULL, 20),
(7698, 'BLAKE', 'MANAGER', 7839, '1981-05-01 00:00:00', 2850, NULL, 30),
(7499, 'ALLEN', 'SALESMAN', 7869, '1981-02-20 00:00:00', 1600, 300, 30),
(7521, 'WARD', 'SALESMAN', 7698, '1981-02-22 00:00:00', 1250, 500, 30),
(7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28 00:00:00', 1250, 1400, 30),
(7844, 'TURNER', 'SALESMAN', 7698, '1981-09-08 00:00:00', 1500, 0, 30),
(7900, 'JAMES', 'CLERK', 7698, '1981-12-03 00:00:00', 950, NULL, 30);

CREATE TABLE IF NOT EXISTS `SALGRADE` (
`GRATE` double DEFAULT NULL,
`LOSAL` double DEFAULT NULL,
`HISAL` double DEFAULT NULL);

DROP TABLE SALGARTE;

ALTER TABLE SALGRADE RENAME COLUMN GRATE TO GRADE; 

INSERT INTO `SALGRADE` (`GRADE`, `LOSAL`, `HISAL`)
VALUES (1, 700, 1200),
(2, 1201, 1400),
(3, 1401, 2000),
(4, 2001, 3000),
(5, 3001, 9999);

ALTER TABLE `EMP` ADD CONSTRAINT `PK_EMP` FOREIGN KEY (`DEPTNO`) REFERENCES `DEPT` (`DEPTNO`)
ON DELETE SET NULL ON UPDATE CASCADE; 
/* ADD CONSTRAINT `PK_EMP` FOREIGN KEY (`DEPTNO`) REFERENCES `DEPT` (`DEPTNO`)
PK_EMP 라는 이름의 FOREING KEY는 DEPTNO를 쓸 것인데 이건 DEPT라는 TABLE의 DEPTNO컬럼을 참조할 것이다.
ON DELETE SET NULL; 
만약 참조하는 DEPTNO 값이 지워지면 NULL 로 바꾼다.
ON UPDATE CASCADE
참조하는 DEPTNO가 수정되면 같이 바꾼다.*/

SHOW TABLES;

DESC emp;

-- mysql 숫자관련 함수.

SELECT POW(2, 3)
FROM DUAL;

SELECT round(1526.159), round(1526.159, 0), round(1526.159, 1), round(1526.159, 2), round(1526.159, 3), round(1526.159, -1);

SELECT concat('회장님의 이름은', ename, '입니다.')
FROM emp
WHERE job = 'PRESIDENT';

SELECT length('ssafy');

SELECT locate('abc', 'ababcabc');

-- 모든 사원에 대하여 사원수, 급여 총액, 평균 급여, 최고급여, 최저급여를 조회
SELECT COUNT(*) 사원수, SUM(sal) 급여총액, AVG(sal) 평균급여, MAX(sal) 최고급여, MIN(sal) 최저급여
From emp;

-- 모든 사원에 대하여 사원수, 급여 총액, 평균 급여, 최고급여, 최저급여를 부서별로 조회, 단 평균 급여는 소수점 둘째자리 반올림
SELECT deptno, COUNT(*) 사원수, SUM(sal) 급여총액, round(AVG(sal), 2) 평균급여, MAX(sal) 최고급여, MIN(sal) 최저급여
From emp
group by deptno;

-- 모든 사원에 대하여 부서, 업무, 사원수, 급여 총액, 평균 급여, 최고급여, 최저급여를 부서별-직급별 로 조회, 단 평균 급여는 소수점 둘째자리 반올림
SELECT deptno 부서, job 업무,  COUNT(*) 사원수, SUM(sal) 급여총액, round(AVG(sal), 2) 평균급여, MAX(sal) 최고급여, MIN(sal) 최저급여
From emp
group by deptno, job;

-- 모든 사원에 대하여 이름, 부서, 업무, 사원수, 급여 총액, 평균 급여, 최고급여, 최저급여를 부서별-직급별 로 조회, 단 평균 급여는 소수점 둘째자리 반올림
SELECT ename 이름, deptno 부서, job 업무,  COUNT(*) 사원수, SUM(sal) 급여총액, round(AVG(sal), 2) 평균급여, MAX(sal) 최고급여, MIN(sal) 최저급여
From emp
group by deptno, job;
-- 불필요한, 관련없는 레코드가 하나의 레코드로 조회된다. 
-- MySQL 에서는 GROUP BY로 묶이지 않은 칼럼을 조회했을 때, 불필요한 데이터가 조회될 수 있으므로 조심해야한다.

-- 급여(커미션 포함) 평균이 2000이상인 부서번호, 부서별 사원 수, 평균급여(커미션 포함) 조회(급여는 소수점둘째점 반올림)
SELECT deptno as "부서 번호", COUNT(*) as "사원수", ROUND(AVG(sal+ IFNULL(COMM, 0)),2) as "평균급여(커미션 포함)" 
FROM emp
GROUP BY deptno
HAVING AVG(sal+ IFNULL(COMM, 0)) >= 2000;
```

## JOIN

둘 이상의 테이블에서 데이터를 조회하기 위해서 사용

일반적으로 조인조건은 PK(Primary Key) 및 FK(Foreign Key)로 구성된다.

PK 및 FK 관계가 없더라도 논리적인 연관만으로도 JOIN 가능하다.

### JOIN의 종류

- INNER JOIN: 조인 조건에 해당하는 칼럼 값이 양쪽 테이블에 모두 존재 하는 경우에만 조회, 동등 조인(Equi-join)이라고도 한다. N개의 테이블 조인 시 N-1개의 조인 조건이 필요
- OUTER JOIN: 조인 조건에 해당하는 칼럼 값이 한 쪽 테이블에만 존재하더라도 조회 기준 테이블에 따라 LEFT OUTER JOIN, RIGHT OUTER JOIN으로 구분

### 카타시안 곱(Cartesian Product)

두 개 이상의 테이블에서 데이터를 조회할 때

- 조인 조건을 지정하지 않음
- 조인 조건이 부적합 함

첫 번째 테이블의 모든 행이 두 번째 테이블의 모든 행에 조인되어 처리됨

```sql
SELECT empno, ename,job, emp.deptno, dname
FROM emp, dept;
```

### 적절한 WHERE 절을 사용하여 유의미하게 데이터 추출

```sql
-- WHERE을 사용하여 유의미하게 데이터 뽑기
SELECT empno, ename,job, emp.deptno, dname
FROM emp, dept
WHERE emp.deptno = dept.deptno;
```

### 조인의 필요성

예) 사번이 7788인 사원의 이름, 업무, 부서번호, 부서이름 조회

문제: 사원의 이름, 업무, 부서번호는 emp 테이블에 있고, 부서의 이름은 dept 테이블에 있다.

```sql
SELECT 
```

#### INNER JOIN

두 테이블에서 일치하는 값을 가진 레코드를 조회

```sql
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```



```sql
-- 조인을 해서 가져오자
select ename, job, emp.deptno, dname
from emp, dept
where emp.deptno = dept.deptno
and empno = 7788;

-- inner join 키워드를 사용해보자.
select ename, job, emp.deptno, dname
from emp
inner join dept
on emp.DEPTNO = dept.DEPTNO
where empno = 7788;

-- inner join 키워드를 사용해보자.(alias 사용)
select e.ename, e.job, e.deptno, d.dname
from emp e
inner join dept d
on e.DEPTNO = d.DEPTNO
where e.empno = 7788;

select e.ename, e.job, e.deptno, d.dname
from emp e
inner join dept d
USING (deptno) -- USING : 위에서 deptno을 언급해 주었기 때문
where e.empno = 7788;
```

#### OUTER JOIN

두 테이블에서 하나의 테이블에 조인조건 데이터가 존재하지 않더라도 (조인조건을 만족하지 않음) 데이터를 조회하기 위해서 사용

기준 테이블에 따라 LEFT OUTER JOIN(LEFT JOIN), RIGHT OUTER JOIN(RIGHT JOIN)으로 구분, (FULL OUTER JOIN은 MySQL에서는 지원하지 않음)

![image-20220704012344685](https://raw.githubusercontent.com/jihoyangKR/image_repo/master/img/image-20220704012344685.png?token=AXI75U2IMGP2SDJPKN4J37DCYHBM4)

##### LEFT OUTER JOIN의 필요성

부서가 없는 직원이 있다고 가정

```sql
-- 부서가 없는 직원을 넣어보자.
INSERT INTO emp
VALUES (4885, 'MESSI', 'MANAGER', 7839, '2022-03-16', 6000, NULL, NULL);

-- 동등조인을 했을 경우
SELECT ename, e.deptno, d.dname
FROM emp e, dept d
WHERE e.deptno = d.deptno; -- MESSI가 조회가 안된다.
```

왼쪽 테이블을 기준으로 JOIN하여 조건에 일치하지 않는 데이터 까지 조회

```sql
-- 기준을 한군데에 두고 붙어라 (LEFT OUTER JOIN)
SELECT ename, e.deptno, d.dname
FROM emp e LEFT OUTER JOIN dept d -- 왼쪽 테이블(emp e)를 기준으로 dept d를 조회를 하겠다.
ON e.deptno = d.deptno;
```

##### RIGHT OUTER JOIN의 필요성

```sql
-- 기준을 부서 기준으로 사원을 붙여보자.
-- 해당 부서에서 일하는 사원들을 가져오기
SELECT d.dname, d.dname, e.empno, e.ename,  
FROM emp e RIGHT OUTER JOIN dept d -- 왼쪽 테이블(emp e)를 기준으로 dept d를 조회를 하겠다.
ON e.deptno = d.deptno;
```

#### 셀프 조인(SELF JOIN)

같은 테이블 2개를 조인

모든 사원의 이름, 매니저번호, 매니저 이름 조회

사원의 정보는 e1, 매니저의 정보는 e2에서 조회

조인 조건은 e1.mgr = e2.empno

```sql
-- 셀프 조인
-- 모든 사원번호, 이름, 매니저 번호, 매니저 이름
SELECT e1.empno, e1.ename, e2.empno, e2.ename
FROM emp e1, emp e2
WHERE e1.mgr = e2.mgr;

-- INNER JOIN 키워드를 사용하여 작성
SELECT e1.empno 사원번호, e1.ename 사원이름, e2.empno 매니저번호, e2.ename 매니저이름
FROM emp e1
INNER JOIN emp e2
ON e1.mgr = e2.empno;

-- KING도 반환하고 싶음
SELECT e1.empno 사원번호, e1.ename 사원이름, e2.empno 매니저번호, e2.ename 매니저이름
FROM emp e1
LEFT OUTER JOIN emp e2
ON e1.mgr = e2.empno;
```

#### 비 동등 조인(Non-Equi JOIN)

조인조건이 table의 PK, FK 등으로 정확히 일치하는 것이 아닐 때 사용

모든 사원의 사번, 이름, 급여, 급여등급을 조회

```sql
-- 모든 사원의 사번, 이름, 급여, 급여등급을 조회

SELECT e.empno, e.ename, e.sal as 급여, sg.grade as "급여 등급"
FROM emp e, salgrade sg
WHERE e.sal BETWEEN sg.LOSAL AND sg.HISAL
ORDER BY  sg.grade DESC, e.sal DESC;

SELECT e.empno, e.ename, e.sal as 급여, sg.grade as "급여 등급"
FROM emp e, salgrade sg
WHERE e.sal >= sg.LOSAL AND e.sal <= HISAL -- BETWEEN을 몰라도 쓸 수 있다.
ORDER BY  sg.grade DESC, e.sal DESC;
```



## SUBQUERY

### 서브쿼리란?

서브쿼리란 하나의 SQL문 안에 포함되어 있는 SQL문을 의미한다.

서브 쿼리를 포함하는 SQL을 외부 쿼리(outer query) 또는 메인 쿼리라고 부르며, 서브 쿼리는 내부 쿼리(inner query)라고도 부른다.

### 서브 쿼리의 종류

중첩 서브 쿼리(Nested Subquery) - WHERE절에 작성하는 서브 쿼리

- 단일-행, 다중-행, 다중-열

인라인 뷰(Inline-view) - FROM 절에 작성하는 서브 쿼리

스칼라 서브 쿼리(Scalar Subquery) - SELECT 문에 작성하는 서브 쿼리

### 서브 쿼리를 포함할 수 있는 SQL 문

SELECT, FROM, WHERE, HAVING, ORDER BY

INSERT 문의 VALUES

UPDATE 문의 SET

### 서브쿼리의 사용시 주의사항

서브쿼리는 반드시 ()로 감싸서 사용한다

서브쿼리는 단일 행 또는 다중 행 비교 연산자와 함께 사용 가능하다.

- 단일 행 비교연산자는 서브 쿼리 결과가 1건 이하이어야 하고, 복수 행 비교 연산자는 결과 건수와 상관없다.

### 서브 쿼리의 필요성

사번이 7788인 사원의 부서 이름을 조회

```sql
SELECT d.dname
FROM emp e, dept d
WHERE e.deptno = d.deptno
AND e.empno = 7788;
```

dname을 조회하기 위해서 INNER JOIN을 수행. JOIN의 경우 경우에 따라 쿼리가 복잡해지거나 카테시안곱으로 인해 속도가 느려질 수 있다.

JOIN 없이 어떻게 조회할까?

```sql
SELECT deptno
FROM emp
WHERE empno = 7788;

SELECT dname
FROM dept
WHERE deptn = 20;=
```

### 서브쿼리 - 중첩 서브 쿼리(Nested Subquery), 단일행

서브 쿼리 결과가 단일 행을 반환

```sql
-- 서브쿼리 활용하기
SELECT dname
FROM dept
WHERE deptno = (SELECT deptno
				FROM emp
				WHERE empno = 7788);
```

```sql
-- 매니저의 이름이 'KING'인 사원의 사번, 이름, 부서번호, 업무조회
SELECT empno, ename, deptno, job
FROM emp
WHERE mgr = (SELECT empno
			FROM emp
			WHERE ename = 'KING');
```

```sql
-- 7566 사원보다 급여를 많이 받는 사원의 이름, 급여를 조회
SELECT ename, sal
FROM emp
WHERE sal > (SELECT sal
				FROM emp
                WHERE empno=7566);
```

```sQL
-- 20번 부서의 평균 급여보다 급여가 많은 사원의 사번, 이름, 업무, 급여 조회
SELECT empno, ename, job, sal
FROM emp
WHERE sal > (SELECT avg(SAL)
				FROM emp
                WHERE deptno = 20);
```

```sql
-- 업무가 'TURNER'와 같고, 사번이 7934인 직원보다 급여가 많은 직원의 사번, 이름, 업무 조회
SELECT empno, ename, job
FROM emp
WHERE job = (SELECT job
				FROM emp
                WHERE ename = "TURNER")
	AND sal > (SELECT sal
				FROM emp
                WHERE empno = 7934);
```

### 서브쿼리 - 중첩 서브 쿼리(Nested Subquery), 다중행

서브쿼리 결과가 다중행을 반환 : IN, ANY, ALL 연산자와 함께 사용

```SQL
-- 업무가 'SALESMAN'인 직원들 중 최소 한 명 이상보다 많은 급여를 받는 사원의 이름, 급여, 업무를 조회
SELECT ename, sal, job
FROM emp
WHERE sal > ANY (SELECT sal
                	FROM emp
                	WHERE job = "SALESMAN")
AND job != 'SALESMAN';

-- > ANY 는 최소값 보다 큼
-- < ANY 는 최대값 보다 작음
```

```sql
-- 업무가 'SALESMAN'인 모든 직원보다 급여(커미션 포함)를 많이 받는 사원의 이름, 급여, 업무, 입사일, 부서번호 조회
SELECT ename, sal, job, hiredate, deptno
FROM emp
WHERE sal > ALL (SELECT sal+IFNULL(COMM, 0)
                FROM emp
                WHERE job = 'SALESMAN')
AND job != 'SALESMAN'

-- > ALL 는 최대값 보다 큼
-- < ALL 는 최소값 보다 작음
```

```SQL
-- 직원이 최소 한 명이라도 근무하는 부서의 부서번호, 부서이름, 위치
SELECT deptno, dname, loc
FROM dept
WHERE deptno in (SELECT DISTINCT deptno
					FROM emp);
-- DISTINCT 키워드를 이용해 중첩되는 행은 제거
-- in 다중행에 하나라도 일치하면 조회, =ANY와 같다.
```

### 서브쿼리 - 중첩 서브 쿼리(Nested Subquery), 다중열

서브쿼리의 결과값이 두 개 이상의 칼럼을 반환하는 서브쿼리

PK가 복합키(Composite Key)이거나, 여러 칼럼의 값을 한꺼번에 비교해야 할 경우 사용

행 생성자(row constructor)를 이용하여 다중 열 서브 쿼리를 비교

아래 두 SQL은 의미상 동일, 동일한 방식으로 처리됨

```sql
SELECT * FROM t1 WHERE(column1, column2) = (1,1);
SELECT * FROM t1 WHERE column1 = 1 AND column2 =1;
```

결과가 다중 행일 경우 IN 연산자를 이용한다.

```sql
SELECT column1, column2, column3
FROM t1 WHERE (column1, column2, column3) IN
				(SELECT column1, column2, column3 FROM t2)
```

```sql
-- 이름이 'FORD'인 사원과 매니저 및 부서가 같은 사원의 이름, 매니저번호, 부서번호를 조회, (단 FORD 정보는 조회X)
SELECT ename, mgr, deptno
FROM emp
WHERE (mgr, deptno) = (SELECT mgr, deptno
                      	FROM emp
                      	WHERE ename = 'FORD')
AND ename <> 'FORD';
```

```sql
-- 각 부서별 입사일이 가장 빠른 사원의 사번, 이름, 부서번호, 입사일을 조회
SELECT empno, ename, deptno, hiredate
FROM emp
WHERE (deptno, hiredate) IN (SELECT deptno, MIN(hiredate)
								FROM emp
                                GROUP BY deptno);
```

### 서브 쿼리 - 상호연관 서브 쿼리(Correlated Subqueries)

외부 쿼리에 있는 테이블에 대한 참조를 하는 서브 쿼리를 의미한다.

```sql
SELECT * FROM t1
WHERE column1 = ANY(SELECT solumn1 FROM t2
                   		WHERE t2.column2=t1.column2);
```

서브 쿼리의 FROM에는 t1에 대한 선언이 존재하지않는다. 따라서 서브쿼리는 외부 쿼리(메인 쿼리)에서 t1을 참조한다.

테이블에서 행을 먼저 읽어서 각 행의 값을 관련된 데이터와 비교하는 방법 중 하나이다.

기본 질의에서 고려된 각 후보행에 대해 서브 쿼리가 다른 결과를 반환해야 하는 경우에 사용한다.

서브쿼리에서는 메인 쿼리의 컬럼명을 사용할 수 있으나, 메인 쿼리에서는 서브 쿼리의 컬럼명을 사용할 수 없다.

```sql
-- 소속 부서의 평균 급여보다 많은 급여를 받는 사원의 이름, 급여, 부서번호, 입사일, 업무를 조회
SELECT ename, sal, deptno, hiredate, job
FROM emp e
WHERE sal > (SELECT AVG(sal)
				FROM emp
				WHERE deptno = e.deptno);
```

### 서브 쿼리 - 인라인 뷰(Inline View)

FROM 절에서 사용되는 서브 쿼리

동적으로 생성된 테이블로 사용 가능하다. 뷰(View)와 같은 역할을 사용한다.

```sql
SELECT ... FROM (subquery) [AS] tbl_name(col_list)...
```

인라인 뷰는 SQL문이 실행될 때만 임시적으로 생성되는 뷰 이기 때문에 데이터베이스에 해당 정보가 저장되지 않는다. 그래서 동적 뷰(Dynamic View)라고도 한다.

```sql
-- 모든 사원의 평균급여보다 적게 받는 사원들과 같은 부서에서 근무하는 사원의 사번, 이름, 급여, 부서번호를 조회

SELECT AVG(sal)
FROM emp;

SELECT DISTINCT deptno
FROM emp
WHERE sal < (SELECT AVG(sal)
				FROM emp);
-- ----------------------------------------------------------
SELECT e.empno, e.ename, e.sal, e.deptno
FROM emp e, (SELECT DISTINCT deptno
				FROM emp
				WHERE sal < (SELECT AVG(sal)
                             FROM emp)) d
WHERE e.deptno = d.deptno;
```

```sql
-- 모든 사원에 대하여 사원의 이름, 부서번호, 급여, 사원이 소속된 부서의 평균 급여럴 조회(단, 이름순 오름차순으로)

SELECT deptno, AVG(sal) as "avgsal"
FROM emp
GROUP BY deptno;
-- --------------------------------------------------
SELECT e.ENAME, e.DEPTNO, e.sal, d.avgsal
FROM emp e, (SELECT deptno, AVG(sal) as "avgsal"
				FROM emp
				GROUP BY deptno) d
WHERE e.deptno = d.deptno
ORDER BY e.ename;
```

### 서브 쿼리 - 인라인 뷰(Inline View), TOP-N

사용자 정의 변수(User-Defined Variables)

- 한 문장에서 사용자 정의 변수를 값을 저장하고 다른 문장에서 이를 참조할 수 있음
- 변수는 `@var_name` 형태로 작성할 수 있음

```sql
SET @v1 = 'A';
SET @v2 = b'1000001' + 0;
SET @v3 = CAST(b'1000001' AS UNSIGNED);
SELECT @v1, @v2, @v3;
```

```sql
-- 모든 사원의 사번, 이름, 급여를 조회
-- 사원 정보를 급여순으로 정렬
-- 한 페이지당 5명을 조회
-- 현재 페이지가 2페이지라고 가정 (급여 순 6등 ~ 10등 조회)
SET @pageno = 2;

SELECT rownum, empno, ename, sal
FROM (SELECT @rownum := @rownum +1 as rownum, a.*
		FROM (SELECT empno, ename, sal
				FROM emp
				ORDER BY sal desc) a,
                (SELECT @rownum := 0) rn
		)ilnv
WHERE ilnv.rownum > (@pageno*5-5) and ilnv.rownum <= (@pageno*5);
```



#### TOP-N

##### LIMIT

결과 집합에서 지정된 수의 행만 필요한 경우 LIMIT 절을 사용

하나 또는 2개 양의 정수를 인자로 받음

첫 번째 인자: offset, 두 번째 인자 개수, 첫 번째 인자를 생략 할 경우 기본값은 0

```sql
SELECT empno, ename, sal
FROM emp
ORDER BY sal DESC limit 5, 5;
```

### 서브 쿼리 - 스칼라 서브 쿼리 (Scalar Subquery)

하나의 행에서 하나의 컬럼 값만 반환하는 서브 쿼리

다음과 같은 경우에 사용 가능

- GROUP BY를 제외한 SELECT의 모든 절
- INSERT 문의 VALUES
- 조건 및 표현식 부분
- UPDATE 문의 SET 또는 WHERE절에서 연산자 목록

#### SELECT에 스칼라 서브 쿼리 사용

```SQL
-- 사원이름, 부서번호, 급여, 소속부서의 평균 급여를 조회
SELECT ename, deptno, sal,
			(SELECT AVG(sal)
            	FROM emp
            	WHERE deptno = e.deptno) as avgsal
FROM emp e;
```

#### ORDER BY에 스칼라 서브 쿼리 사용

```sql
-- 모든 사원의 번호, 이름, 부서번호, 입사일을 조회. 단, 부서 이름 기준 내림차순 사용
UPDATE emp SET deptno = 40 WHERE ename = 'MESSI';
SELECT empno, ename, deptno, hiredate
FROM emp e
ORDER BY (SELECT dname
         	FROM dept
         	WHERE deptno = e.deptno) DESC;
```

### 서브쿼리를 이용한 CREATE문

```sql
-- emp table을 emp_copy라는 이름으로 복사(컬럼 이름 동일)
CREATE TABLE emp_copy (SELECT * FROM emp);
-- emp table 구조만 emp_blank라는 이름으로 복사하여 생성
CREATE TABLE emp_blank (SELECT * FROM emp WHERE 1 = 0);
```

### 서브 쿼리를 이용한 INSERT문

```sql
-- 부서 번호가 30인 사원의 모든 정보를 emp_blank에 INSERT
INSERT INTO emp_blank
(SELECT *
FROM emp
WHERE deptno = 30);
```

