# JSP [Java Server Page]
- 서블릿 : 자바코드 내에 HTML코드를 작성 
- JSP : HTML내에 자바코드 작성

## 요약
1. jsp는 말하자면 dtl 
2. 서블릿을 기반으로 만들어진 개발언어임
3. 그래서 
<hr>

## JSP로 hellojsp찍어보기
1. Webapp하위에 jsp파일 만들기(자바파일이 아니므로 java resource말고 webapp에만든다)
2.  자바코드를 작성하려면 <% %> 안에 써야함
```jsp
<body>
	<%
		String name = "호우재";
	%>
	<h2>Hello JSP</h2>
	<h4>안녕하세요. <%=name %>입니다.</h4>
</body>

```
- 서버 restart해주면됨

## JSP태그 종류
1. <%  %> : 자바코드 작성
2. <%!  %> : [선언자]변수와 메소드 선언
3. <%=  %> : [표현자]문자열 형태로 출력
4. <%-- --%> : 주석 (jsp주석문은 클라이언트로 안넘어감) ( html주석은 넘어감)
5. <%@ %> : [지시자]페이지 속성 지정


## 들어야하는 궁금증 : <% %> 안에 선언하는거랑 <%! %> 안에 선언하는거랑 뭔차이?
- 일단 전자로 해도 선언은 됨. 근데다름
- 전자는 클래스변수로 들어가고
- 후자는 service 메서드안에서 정의됨
- 다음과 같이 jsp파일을 작성했다고 하자.
```java
<%! int cnt1 = 0;
%>
<body>
    <%
        int cnt2 = 0;
        out.print("cnt1 : " );
        out.print(++cnt1);
        out.print("<br>");
    %>
</body>
```
- 서버키고 새로고침할때마다 cnt1과 cnt2의 값은 어케될까?
- cnt1은 계속 1씩 증가하는반면, cnt2는 계속1임
- 왜? 선언태그로 선언한 변수는 servlet클래스가 jvm메모리에 올라갈때 같이 올라가는 반면, 그냥태그에서 선언하면 서비스메서드안에서 정의됨. 근데 요청할때마다 서비스메서드는 새로호출이 됨. 따라서 cnt2는 매번갱신되고 cnt1는 서버가 꺼질때까지 유지됨.
- cnt2 : 서비스메서드의 지역변수

## 지시자
### include
- jsp내에 다른html문서나 jsp페이지의 내용을 삽입할 때 사용


# JSP 기본객체
1.  request
2. response
3. pageContext
4. session
## 기본객체의 영역
- 각 객체는 scope를 가지고있음
- 대충  page < Request < session < application 순임


# 페이지이동 

##  요청을 받아서 화면을 변경하는 방법 2가지
### 방법1 :  처리해주는애한테 넘겨주기[포워드 방식]
- 처음 들어온 요청이 계속 유지됨
```java
RequestDispatcher dispatcher = request.getRequestDispatcher("이동할 페이지");
dispatcher.forward(request, response);
```


### 방법2 : 리다이렉트 
- url변경해서 새로운 요청 ㄱㄱ

```java
response.sendRedirect("location");
```

### 차이점
- 포워드방식은 서버내부적으로만 토스 가능
- 리다이렉트방식은 외부 url로도 요청가능하다는 점