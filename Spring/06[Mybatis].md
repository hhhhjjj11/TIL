# 마이바티스 실습

## 흐름
### 마이바티스설정 -> dao매핑설정 -> sqlSession설정
<hr>
<br>

## 1. java 프로젝트 하나만듬
<br>

## 2. 프레임워크 디펜던시 추가(jar파일 추가)
  - lib폴더 만들고 mysql이랑 mybatis추가하자
  - mvnrepository > mybatis검색 > 3.5.9버전 ㄱㄱ > jar파일 다운받자
 
[참고] 밑에 코드복사하는거는 pom.xml로 설정할때 쓰고 lib폴더에 jar파일 넣어서 쓸때는 jar파일 다운 받자

<br>

## 3. 등록해주기
- [참고] dynamic web project의 경우에는 jar파일을 넣어주면 자동으로 등록이 됐었지만,
java project의 경우에는 등록도 따로 해주어야함.
- 프로젝트 우클릭 > configure build path > Java Build Path > Addjars > 방금 넣은 jar파일 두개 (mysql이랑 mybatis) 등록 ㄱ
- Referenced Libraries에 등록 된것 확인

<br>

## 4. mybatis-config.xml 설정 작성
- 소스폴더 하나 만들자 (resources) > "config"패키지 만들고 > "mybatis-config"xml파일 생성ㄱ ㄱ
- mybatis공식문서가서 > 시작하기 > xml코드 긁어서 복붙
- [설명] 윗부분코드 : 현재 xml파일이 my-batis설정을 하도록 연결설정
- 아래부분 : configuration

  ```xml
  <?xml version="1.0" encoding="UTF-8" ?>
  <!DOCTYPE configuration
    PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
    "https://mybatis.org/dtd/mybatis-3-config.dtd">
  <configuration>
  <!-- 여기서 가져와라잉 -->
  <properties resource="config/db.properties"></properties>
    <environments default="development">
      <environment id="development">
        <transactionManager type="JDBC"/>
        <dataSource type="POOLED">
          <property name="driver" value="${driver}"/>
          <property name="url" value="${url}"/>
          <property name="username" value="${username}"/>
          <property name="password" value="${password}"/>
        </dataSource>
      </environment>
    </environments>
    <mappers>
      <mapper resource="mapper/boardMapper.xml"/>
    </mappers>
  </configuration>
  ```
1. `<configuration>` 작성시 순서가 있음.(공식문서) 순서대로 작성해줘야함
2. `<environments>` : 환경, 여러개가 있을 수 있음.
 - 예를들어, 디비를 여러개를 연결해놓을 수 이씀
 - 개발용 테스트 디비와, 배포용 디비
3. `<mappers>` : sql을 경로를 적어줌으로써 sql을 매핑 해준다.

<br>

## 5. db.properties파일 만들어서 변수 따로 관리하기
  - 환경설정할건데, property 설정할때, 값 직접 넣지 않고, 다른 파일에다가 변수-값으로 저장해놓고 그거 불러다가 쓴다!!
   - resources >config > db.properties File(클래스아니고 File임) 생성 (.properties를 확장자로 가지는 db라는 이름의 파일)
   
 - 
    ```file
    url=jdbc:mysql://localhost:3306/ssafy_board?serverTimezone=UTC (DButil.java에서 긁어오면됨)
    driver=com.mysql.cj.jdbc.Driver
    username=ssafy
    password=ssafy
    ```

<br>

 ## 6. resources > mapper > boardMapper.xml 만든다.
- 다음. boardMapper.xml에 코드를 다음과 같이 넣는다. 
- 공식문서에서 긁어온것에 알맞은 dao경로를 넣어주면 됨.
- 
  ```xml
  <?xml version="1.0" encoding="UTF-8" ?>
  <!-- 매퍼파일임을 나타내주는 설정코드 -->
  <!DOCTYPE mapper
    PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
    "https://mybatis.org/dtd/mybatis-3-mapper.dtd">
    
  <!-- 어떤 dao와 매핑할것인지 경로를 넣어준다.. -->  
  <mapper namespace="com.ssafy.board.model.dao.BoardDao">
  </mapper>
  ```

<br>

## 7. dto랑 dao를 가져온다. (src/main/java/com.ssafy.board.model.dao)

<br>

## 8. sqlSession이용할건데, sqlSession을 조작하는 코드(만들고, 꺼내는 등)를 매번작성하기 보다는, 클래스 따로 만들어서 사용(MyAppSqlConfig) ㄱㄱ
### [개념] sqlSession
  - 마이바티스는 db에 쿼리날릴때 , sqlSession이용해서 날린다.
  - sqlSessionFactory로 sqlSession 만들어서 쓴다.
  - sqlSessionFactory는 이름에서 보듯 SqlSession인스턴스를 만들 수 있다 .
  - SqlSession은 db에 SQL문을 실행하기 위해 필요한 모든 메소드를 갖고 있다.

(1) com.ssafy.board.config > MyAppSqlConfig클래스 만들기

(2) 아래와 같이 코드작성

- ```java
  package com.ssafy.board.config;

  import java.io.IOException;
  import java.io.Reader;
  import java.sql.Connection;

  import org.apache.ibatis.io.Resources;
  import org.apache.ibatis.session.Configuration;
  import org.apache.ibatis.session.ExecutorType;
  import org.apache.ibatis.session.SqlSession;
  import org.apache.ibatis.session.SqlSessionFactory;
  import org.apache.ibatis.session.SqlSessionFactoryBuilder;
  import org.apache.ibatis.session.TransactionIsolationLevel;

  public class MyAppSqlConfig {
    private static SqlSession session;
    
    static {
      try {
        //MyBatis 설정파일을 가져오기
        
        // sqlsessionfactory 객체 만들기
        String resource = "config/mybatis-config.xml";
        Reader reader = Resources.getResourceAsReader(resource);
        SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(reader); 
        
        // 팩토리 이용해서 세션인스턴스 ㄱㄱ
        session = sqlSessionFactory.openSession(true);
        System.out.println("세션 생성 성공");
      } catch (IOException e) {
        System.out.println("세션 생성 실패");
      }
      
    }
    
    public static SqlSession getSession() {
      return session;
    }
  }
  ```

## 9. 테스트 ㄱㄱ
- 위와같이 쭉 따라 왔으면 실행했을때 콘솔에 "세션 생성 성공"이 떠야 함.
  ```java
  package com.ssafy.board.test;

  import com.ssafy.board.config.MyAppSqlConfig;
  import com.ssafy.board.model.dao.BoardDao;

  public class Test {
    public static void main(String[] args) {
      // 이렇게 하면 마이바티스가 dao를 구현해서 구현체를 반환해줌. getMapper를 이용한다는 점.
      // 이렇게 하면 전에 했던 것 처럼 DaoImpl클래스를 따로 만들 필요가 없게됨.
      BoardDao dao = MyAppSqlConfig.getSession().getMapper(BoardDao.class);
    }
  }
  ```

## 여기까지하면.. Dao랑 mapper파일을 연동해서 DaoImpl을 만든것임!!


<hr>
<br>

# 이제 boardMapper 메서드 설정 마저 해서 쿼리 날려보자
## [1] 전체글 조회
### 1. 읽어오고 싶을때 -> `<select>` 쓴다.
- 이때 태그의 id에는 메서드 이름이 들어가주어야 한다.
- resultType으로 반환타입 지정.(dto)
- `<select id="selsectAll" resultType="com.ssafy.board.model.dto.Board">`

### 2. typeAliase이용해서 긴 경로를 변수에 담아서 쓰기
- [설명] com.ssafy.board.model.dto.Board -> 존나 김.
변수에 담아서 변수 갖다 쓰고 싶다..
1. mybatis-config.xml에 다음과 같이 작성하면 됨
- [주의] 코드 순서 중요하다고 했지? 알리아스는 properties다음에 와야됨.
  ```xml
  <configuration>
  <!-- 여기서 가져와라잉 -->
  <properties resource="config/db.properties"></properties>

    <typeAliases>
      <typeAlias type="com.ssafy.board.model.dto.Board" alias="Board"/>
    </typeAliases>

    <environments default="development"> 어쩌구저쩌구...
  ```

### 3. 그러면, boardMapper에서
```xml
<mapper namespace="com.ssafy.board.model.dao.BoardDao">
	<!-- 전체글 조회 -->
  <select id="selectAll" resultType="Board">
      SELECT *
      FROM board;
  </select>
</mapper>

  <!-- dao의 selectAll메서드에 SELECT * FROM board SQL문을 적용, 이때 결과타입은 알리아스 변수 Board.-->
  <!-- [참고] selectAll은 리스트를 반환함. 알아서 리스트에 담아줌... 개꿀.-->
```

- [중요] 주의!! db의 컬럼명과 dto의 컬럼명이 다르면, 데이터가 올바르게 전송이 안됨. 예를들어, dto에서는 viewCnt, regDate이고 db에는 view_cnt , reg_date임. 이 경우 컬럼명이 맞지 않기 때문에 db의 데이터가 바구니(board)에 제대로 담기지 않는다!!
- 이경우 db또는 dto의 컬럼명을 수정해서 맞춰 줄 수도 있지만 sql문을 통해 수정할 수도 있다. 
- 두가지 방법이 있다. 
  - (방법1) as를 이용해서 매핑해줄 수 있다.
  - (방법2) `<resultMap>`을 이용한다
### 방법1 
```xml
<mapper namespace="com.ssafy.board.model.dao.BoardDao">
	<!-- 전체글 조회 -->
	<select id="selectAll" resultType="Board">
		SELECT id, content, writer, title, view_cnt as viewCnt, date_format(reg_date, '%Y-%M-%d') as regDate
		FROM board;
	</select>
</mapper>
```
- 또한, date_format이라는 날짜 전용 sql메서드를 이용해서 나타낼 수도 잇다는 점~ 
### 방법2
- resultMap을쓰고,
- `<select>`의 resultType에 resultMap에서 정한 id로 넣어줌.
```xml
<mapper namespace="com.ssafy.board.model.dao.BoardDao">
	<resultMap type="Board" id="boardMap">
		<result column="id" property="id"/>
		<result column="writer" property="writer"/>
		<result column="title" property="title"/>
		<result column="content" property="content"/>
		<result column="view_cnt" property="viewCnt"/>
		<result column="reg_date" property="regDate"/>
	</resultMap>

	<!-- 전체글 조회 -->
	<select id="selectAll" resultType="Board">
		SELECT id, content, writer, title, view_cnt, date_format(reg_date, '%Y-%M-%d') as reg_date
		FROM board;
	</select>
	<!-- view_cnt의 경우 as를 지워줘도 되지만 reg_date의 경우는 형태가 깨지니까 오히려 as reg_date로 해줘야 매핑이 적용되서 regDate됨.-->
```


### 4. test클래스에서 데이터가져와서 프린트찍어보기
```java
public class Test {
	public static void main(String[] args) {
		BoardDao dao = MyAppSqlConfig.getSession().getMapper(BoardDao.class);
		
		for(Board b : dao.selectAll()) {
			System.out.println(b);
		}
	}
}
```
<br><br>

## [2] 상세글 조회
1. dao에서 상세글 메서드는 다음과 같이 id를 인자로 받았었음
    ```java
      //ID에 해당하는 게시글 하나 가져오기
      public Board selectOne(int id);
    ```
2. select에서 paramType속성을 이용해서 받고, #{id}처럼 샾괄호에 넣어서 쓴다..
```xml
	<!-- 상세글 조회 -->
	<select id="selectOne" parameterType="int" resultType="Board">
		SELECT id, content, writer, title, view_cnt as viewCnt, date_format(reg_date, '%Y-%M-%d') as regDate
		FROM board
		WHERE id = #{id};	
	</select>
```

3. 테스트~
```java
public class Test {
	public static void main(String[] args) {
		BoardDao dao = MyAppSqlConfig.getSession().getMapper(BoardDao.class);
		
		System.out.println(dao.selectOne(1));
	}
}
```

<br><br>

## 게시글 등록
1. select 아니고 `<insert>`쓴다.
2. dao에서 board 인스턴스를 인자로 받았으니까, parameterType에 Board넣는다.
3. 넘겨받은거 #{}에 넣어서 쓴다.
```xml
	<!-- 게시글 등록 -->
	<insert id="insertBoard" parameterType="Board">
		INSERT INTO board (title, writer, content)
		VALUES(#{title}, #{writer}, #{content})
	</insert>
```
4. 테슷트
```java
		Board board = new Board("타이틀ㅋ", "작성잨", "내용~ㅋ");
		
		dao.insertBoard(board);
		
		for(Board b : dao.selectAll()) {
		System.out.println(b);
		}
```
<br>

## 게시글 삭제
```xml
	<!-- 게시글 삭제 -->
	<delete id="deleteBoard" parameterType="int">
		DELETE FROM board
		WHERE id = #{id}
	</delete>
```

```java
		dao.deleteBoard(2);

		for(Board b : dao.selectAll()) {
		System.out.println(b);
		}
```

## 게시글수정(조회수1증가시키기)
```xml
	<!-- 수정:조회수증가 -->
	<update id="updateViewCnt" parameterType="int">
		UPDATE board
		SET view_cnt = view_cnt+1
		WHERE id=#{id}
	</update>
```

```
dao.updateViewCnt(4);
```

## 게시글수정
```xml
	<!-- 게시글수정 -->
	<update id="updateBoard" parameterType="Board">
		UPDATE board
		SET title = #{title}, content= #{content}
		WHERE id =#{id}
	</update>
```
```java
		Board bb = dao.selectOne(3);
		bb.setTitle("제목수정하귀");
		bb.setContent("내용수정하귀");
		
		dao.updateBoard(bb);
```
