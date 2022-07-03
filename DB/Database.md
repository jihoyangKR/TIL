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

- CREATE: 테이블 등 데이터 객체를 생성할 때 사용

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

- ALTER: 테이블 등 데이터 객체를 변경할 때 사용

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

- RENAME: 테이블 등 객체의 이름을 변경할 때 사용

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

  - 


### DML(Data Manipulation Language): 데이터 조작 언어

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

- #### INSERT, SELECT, UPDATE, DELETE

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

### TCL(Transaction Control Language): 트랜젝션 제어 언어

- 트랜잭션단위로 실행한 명령문을 적용하거나 취소
- COMMIT, ROLLBACK: DML문이 변경한 내용을 관리. 변경사항을 저장(COMMIT)하거나 취소(ROLLBACK)할 때 사용한다. 이때 DML변경 내용은 트랜잭션 단위로 그룹화 가능하다.
- mySql의 경우에는 AutoCommit이 되어있어 바로 저장이 된다.

### DCL(Date Control Language): 데이터 제어 언어

- 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어
- Database, Table 접근 권한이나 CRUD권한 정의
- 특정 사용자에게 테이블의 검색권한 부여/금지
- GRANT: 데이터베이스 접근권한 부여
- REVOKE: 데이터베이스 접근권한 삭제
- COMMIT, ROLLBACK