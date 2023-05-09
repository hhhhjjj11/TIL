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
0. 구글에 mvnrepository 홈페이지 가서 java mysql검색 -> MySQL Connector JAVA 누른담에 files항목의 jar파일 설치 ㄱㄱ
- 참고 : 파일형식이 jar 이어야 하는데 zip jar인 경우 자바 jdk 다시까니까 해결됨 
1. java project 만들고(동적프로젝트말구 그냥 project) -> 설치한 jar 파일 src > lib안에 넣고(lib폴더는 만든다)
- `참고` : JRE환경 JavaSE-17로 하니까 계속 class없다고 에러떴었는데 JavaSE-1.8로 하니까 (강의환경과 동일) 됨. 왜인지 이유는 모르겠지만
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
	public List<Board> selectAll() {
		List<Board> list = new ArrayList<>();
		
		Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/ssafy_board?serverTimezone=UTC", "root", "ssafy")
				
		return list;
	}
```
- Connection은 인터페이스 이므로 new 연산자를 통해 인스턴스를 생성하는 방식이 아님.

### 3. SQL실행 (Statement)
1. SQL문 수행위해 Statement 객체 필요
2. Connection 객체 이용해서 createStatement() 메소드 통해 생성
3. executeQuery : 필드 반환시 (데이터를 가져올때)
4. executeUpdate  : 데이터 가져오진 않고 업데이트만 할때, 반환은 정수형 반환


###  try - with - resources 
1. try에 자원 객체를 전달할경우, try블록이 끝날시 자동으로 자원을 종료해주는 기능
2. 즉, 따로 종료처리할필요 X


## autoclosable
1. 사용하는 Connection, Statement, ResultSet 모두 AutoCloseable을 구현한 인터페이스임. 
2. 따라서 AutoCloseable타입으로 바꿀 수 있음. (담을 수 있음) (다형성)


## Dao [Data Access Object]

## BoardDaoimpl
1. DBUtil 가져와서 써야댐. 그래야 db연결하지