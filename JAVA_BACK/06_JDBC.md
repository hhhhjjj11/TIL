# JDBC

## JDBC란?
- 자바랑 db랑 상호작용할 수 있도록 도와주는 api
- 클래스의 집합
- DBMS가 달라져도 설정만 조금씩 수정해가며 사용 가능

## JDBC로 연결하는 0+4단계
0. 세팅하기
1. JDBC 드라이버 로드
2. 데이터베이스 연결
3. SQL문 실행
4. 데이터베이스 연결 끊음

### 0. 세팅하기 
1. 설치한 jar 파일 src > lib안에 넣고(lib폴더는 만든다)
3. 편재 프로젝트에서 jar파일을 참조하도록 직접 지정해야함
   - 프로젝트 우클릭 > Build Path > Add Libraries > Add JARs.. ( 프로젝트 하위에서 파일을 찾겠다..) 해서 jar파일 골라서 넣고 적용.
4. 그러면 플젝폴더 하위에 Referenced Libraries 생김, 거기서 방금추가한 파일 열어보면 항목이 아주 많은데, 그 중 .jdbc 패키지 하위에 Driver.class 를 등록할거임. 

### 1. JDBC 드라이버 로드
1. 다른 클래스를 만든다음에, 거기서 Class 클래스의 forName 메서드를 이용해서 jvm메모리에 위에서 말한 Driver.class를 로드 할 수 있음. 

```java
package com.ssafy.Test;

public class JDBCtest {

    public JDBCtest() {
        // 드라이버 로드
         Class.forName("com.mysql.cj.jdbc.Driver") 


    }

}

```

### 2. DB연결
- DriverManager 클래스의 getConnection메서드를 이용
```java

```
