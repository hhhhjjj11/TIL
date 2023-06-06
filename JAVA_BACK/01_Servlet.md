# Servlet
## 요약
1. 서버돌릴려면 톰캣 (was)
2. 요청처리해주는 애 - 서블릿
3. 인터페이스임
4. 구현귀찮음, 그래서 구현해놓은 추상클래스가 있음 - GenericServlet
5. GenericServlet 은 다른거는 다 돼있고 service메서드만 오버라이딩 해서 쓰면 됨
6. 근데 이것도 귀찮음. 더 편하게 해놓은 클래스가 있음 - HttpServlet
7. 얘는 doget, dopost같은거 작성해주면 됨. 그러면 알아서 service 메서드 동작..
8. ...

<hr>

## Servlet이란
- 자바에서, http요청을 분기하고 처리하고 응답까지 해주는 자바 클래스임.
- server + applet의 합성어
- 자바를 이용하여 웹에서 실행되는 프로그램을 작성하는 기술
- 자바를 이용하여 웹페이지를 동적으로 생성할 수 있음
- Servlet은 자바 코드 안에 HTML을 포함.

<br>

## Servlet 이랑 라우터랑 비교해보기
1. 공통점 : 둘 모두, 요청이 들어왔을 때 적절한 처리가 되도록 연결시켜주는 기능 수행
2. 차이점 : 
   - 서블릿은 요청 분기, 처리, 응답까지
   - 라우터는 요청을 분석하여 적절한 핸들러로 연결시켜줌, 처리와 응답은 핸들러가 함.
## 세팅하기
1. Tomcat 설치 (수업때는 9버전깔았음)
2. eclipse -> perspective -> javaEE선택
(만약에 없으면 IDE for web으로 이클립스 다시설치 하기)
3. window > preference > enco검색 > 전부 utf-8로 설정
4. 톰캣등록하기 : servers  > new server어쩌고 누르고 tomcat 경로 지정

## 시작해보기
1. 웹프로젝트 생성 : project explorer > new > Dynamic Web Project 
- 참고 : dynamic web project 구조
   1. Java Resources : 자바관련파일 
 	2. WebContent : html, js, image등 웹 컨텐츠 포함, 웹 어플리케이션 설정파일인 web.xml도 여기 들어 있다.
2. 서블릿클래스 생성:  JavaResouces > new > newServlet
- package : com.ssafy.hello
- classname : HelloServlet
3. 서블릿클래스에서 다음과 같이 작성
	```java
		protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
			PrintWriter writer = response.getWriter();
			writer.append("<html>");
			writer.append("<head>");
			writer.append("<title>Hello</title>");
			writer.append("</head>");
			writer.append("<body>");
			writer.append("<h1>Hello Servlet</h1>");
			writer.append("</body>");
			writer.append("</html>");
			
		}

	```

4.  우클릭 > Run as > Run on server > 서버선택 (Tomcat v9.0) > next

5. 브라우저 창 뜸 ㅋ

<br>

## 컨텍스트 루트에 대한 설명
- 톰캣에는 여러 프로젝트가 올라갈 수 있다.
- 따라서 어떤 요청이 들어왔을 때 그것이 어느 프로젝트에 대한 요청인지 구분하기위해서, 요청경로에 프로젝트 구분을 위한 식별자가 포함되어있는것이 좋다. 
- 그렇게 하기위해 일반적으로 포트번호 다음에 프로젝트 이름이 경로에 포함되는데, 이것을 컨텍스트 루트라고 한다.
- 즉, 컨텍스트 루트는 톰캣안의 프로젝트를 구분하기위해 경로에 표시하는 것이다.

<br>


## servlet사용하기 : 방법 3가지, 그 중  HttpServlet 쓴다.
 
### 방법1: implements Servlet
- 서블릿 인터페이스를 구현해야함. 온갖 메서드 다 오버라이딩 직접 해서 써야됨
### 방법2 : extends GenericServlet
- 서블릿을 구현한 추상클래스임, 서비스 메서드만 오버라이딩 하면 됨
### 방법3[이거쓴다] : extends HttpServlet
- 얘는 doget, dopost등의 메서드들을 오버라이딩해주면 됨.
- do~ 메서드들은 알아서 service메서드에 포함되어서(?) 동작시킴.

<br>

## Servlet 등록하기 : 방법 2가지 (방법2 쓴다.)
### 방법1 : web.xml에 직접 등록하기
- web.xml이 있으려면 프로젝트 생성시 마지막 설정창에서 Generate web.xml체크해주어야함!!
```
<servlet>
    <servlet-name>이름1(작명)</servlet-name>
    <servlet-class>com.ssafy.myservlet.Myservlet4(풀패키지경로)</servlet-class>
</servlet>

<servlet-mapping>
    <servlet-name>이름1</servlet-name>
    <url-pattern>/경로1</url-pattern>
</servlet-mapping>
```
- 결과 : 풀패키지경로에 있는 서블릿을 이름1로 명명하고, 경로1과 매핑한다.
- 서버키고 -> 주소창에 : 로컬주소/프로젝트시작시설정한경로/경로1 -> 페이지뜸 

<br>

### 방법2 : @WebServlet("경로") 어노테이션이용하기
- 이때 다른 서블릿에서 정한 경로랑 중복되지 않도록 조심

	```java
	package com.ssafy.myservlet;

	import java.io.IOException;
	import java.io.PrintWriter;

	import javax.servlet.ServletException;
	import javax.servlet.annotation.WebServlet;
	import javax.servlet.http.HttpServlet;
	import javax.servlet.http.HttpServletRequest;
	import javax.servlet.http.HttpServletResponse;

	@WebServlet("/MyServlet2")
	public class MyServlet5 extends HttpServlet{
		protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
			PrintWriter writer = response.getWriter();
			writer.append("<html>");
			writer.append("<head>");
			writer.append("<title>Hello</title>");
			writer.append("</head>");
			writer.append("<body>");
			writer.append("<h1>Hello Servlet5</h1>");
			writer.append("</body>");
			writer.append("</html>");
			
		}
	}

	```

## 서블릿 생명주기 ( 작동 주기 ) 
1. 서버를키면-> JVM메모리에 서블릿 클래스 로드
2. 서블릿 클래스 인스턴스 생성
3. 인스턴스 초기화
4. 웹컨테이너(탐캣)에의한 메서드 호출(여러번,)(요청이들어온만큼)
5. destroy메서드로 서블릿 종료

<br>

## 서블릿 동작방식
1. 사용자(클라이언트)가 URL을 입력하면 HTTP Request가 Servlet Container로 전송됩니다.
2. 요청을 전송받은 Servlet Container는 HttpServletRequest, HttpServletResponse 객체를 생성합니다.
3. web.xml을 기반으로 사용자가 요청한 URL이 어느 서블릿에 대한 요청인지 찾습니다.
4. 해당 서블릿에서 service메소드를 호출한 후 클리아언트의 GET, POST여부에 따라 doGet() 또는 doPost()를 호출합니다.
5. doGet() or doPost() 메소드는 동적 페이지를 생성한 후 HttpServletResponse객체에 응답을 보냅니다.
6. 응답이 끝나면 HttpServletRequest, HttpServletResponse 두 객체를 소멸시킵니다.