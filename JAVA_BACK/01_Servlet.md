# Servlet
## Servlet이란
- server + applet의 합성어
- 자바를 이용하여 웹에서 실행되는 프로그램을 작성하는 기술
- 자바를 이용하여 웹페이지를 동적으로 생성할 수 있음
- Servlet은 자바 코드 안에 HTML을 포함.

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
   2 .WebContent : html, js, image등 웹 컨텐츠 포함, 웹 어플리케이션 설정파일인 web.xml도 여기 들어 있다.
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


## servlet사용하기 : 방법 3가지, 그 중  HttpServlet 쓴다.
 
### 방법1: implements Servlet
### 방법2 : extends GenericServlet

### 방법3[이거쓴다] : extends HttpServlet

## Servlet 등록하기 : 방법 2가지
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