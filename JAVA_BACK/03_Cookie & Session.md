# 쿠키와 세션
## 쿠키와 세션이 필요한 이유
- 우리가 사용하는 Http protocal은 비연결 지향형 통신 프로토콜이다.
- 무슨말이냐면 응답 후 연결을 종료해버린단 말임 ( 지속적인 연결 유지로 인한 자원낭비를 위해 연결 해제 )
- 그렇기 때문에 응답 후에 클라이언트 정보를 기억하지 못함
- 쿠키와 세션에 이런 정보들을 저장해둠

## 쿠키
- 서버가 생성하는 클라이언트 정보를 가지고 있는 파일
- 클라이언트 컴퓨터에 저장됨! 
- 브라우저 별로 쿠키 생성(크롬, 익스플로러 별로 다르다 이말)
- 사용자의 행동과 패턴을 분석하고 기록하는데 사용된다.

## 쿠키 동작 순서
- 클라이언트가 요청 생성
- WAS는 Cookie를 생성하고 Http Header에 Cookie를 넣어 응답
- Client(Browser)는 Cookie를 저장하고 요청시 함께 전송
- 쿠키는 만료기간전까지는 브라우저가 종료되더라도 계속 저장되기 때문에, 동일 사이트 재방문하여 요청 시 필요에 따라 cookie가 재 전송 된다.

### 예
- 쿠팡에서 아이폰14 장바구니에 추가
- 서버에서 응답할때 쿠키에 아이폰14 넣어줌
- 브라우저의 쿠키에 아이폰14가 저장됨

## 쿠키특징
- key-value, 만료일(Expire date), 경로정보로 구성
- 하나의 클라이언트에 최대 300개의 쿠키저장가능
- 하나의 도메인 당 20개의 쿠키 저장가능
- 쿠키하나는 4KB 까지저장가능
- Q. 요새 이미지하나에 용량이 얼만데 300개 해봐야 1.2MB인데?? 
   - 이미지는 따로저장해놓구 참조값(링크나 주소)만 보내주는 식으로! 

## 쿠키만들고 응답에 실어보내기
1. 쿠키생성 
```java
Cookie cookie = new Cookie("userid", "ssafy");
```
2. 쿠키 응답에 추가
```java
response.addCookie(cookie);
```

## 주요메서드
### set
- void set Comment(String comment) : 쿠키에 대한 설명 설정
- void setDomain(String domain) : 쿠키의 유효한 도메인 설정
- void setMaxAge(int expiry) : 쿠키 유효기간설정
- void setPath(String path) : 쿠키 유효 디렉토리 설정
- void setValue(String value) : 쿠키 값 설정
### get
- String getComment() : 쿠키설명반환
- String getDomain(): 쿠키 유효 도메인 반환
- int getMaxAge() : 쿠키 유효기간 반환
- String getPath() : 쿠키 유효 디렉토리 반환
- String getValue() : 쿠키 값 반환

# 쿠키실습 [꼭 철저히 복습하자]



# HttpSession
- 사용자가 웹 서버에 접속해 있는 상태를 하나의 단위로 보고 그것을 세션이라고 한다.
- 세션은 sessionid를 갖는다.
- WAS의 메모리에 객체 형태로 저장
- 쿠키는 클라이언트에 저장되기 때문에 공유PC의 경우 보안에 취약, 하지만 세션은 서버에 저장되어서 쿠키에 비해 보안이 좋다.
- 쿠키와 비슷한 기능 : 로그인 정보 및 장바구니 등

## 세션 동작 흐름
1. 클라리언트가 페이지요청
2. 서버는 쿠키에 세션id있는지 확인
3. session id 없으면 session id를 만들어서 쿠키에 넣어서 클라이언트로 반환
4. 생성된 session id 로 서버 내 메모리 생성
5. 클라이언트가 다음 요청 시 쿠키에 session id를 포함해서 전달 -> 서버에 저장된 session id 랑 비교후 처리

## 세션에 데이터담기
1. 요청객체로부터 session 객체에 접근
2. session에 데이터 저장
```java
HttpSession session = request.getSession();
session.setAttribute("userid", "ssafy");
```
- HttpSession은 인터페이스이지만 다형성을 이용해서 객체생성가능 이때 request.getSession()을 이용한다는 점.
- session객체에 user : saffy 키밸류 쌍을 저장

### 참고.
- session에서 값을 반환하는 메서드인 getAttribute은 Object형이기때문에, 형변환해줘야함
```java
String userid = (String)session.getAttribute("userid");
```

### 참고2.
- 세션은 브라우저 스코프의 객체임
- redirect를해서 요청객체가 바껴도 유지 된다이말임(?)

## Session 주요 메서드
1. void setAttribute(key, value) : 값추가
2. 사용자가 다음 요청 보낼 때 까지 세션을 유지하는 최대시간을 설정하기 
  - void setMaxInactiveInterval(int interval)
3. void invalidate() : 세션삭제
4. String getId() : 세션 id 반환
5. long getLastAccessTime() : 현재 세션에 클라이언트가 마지막으로 요청을 보낸 시간을 반환 (long)
6. Object getAttribute(String name) : name에 해당하는 속성값 반환 ,  Object형임을 유의하자
7. long getCreationTime() : 만들어진시간반환
8. void removeAttribute(String name) : 값제거
9. Enumeration getAttributeNames() : 세션에서 모든 객체의 이름을 Enumeration형으로 반환

# 실습 [servlet없이 jsp만으로 간단한 로그인기능 구현]
1. 로그인페이지 jsp파일 만들어서 그안에 로그인폼 ㄱㄱ
2. jsp에서 if(id.equals("ssafy") && pw.equals("1234")) 시 세션에 데이터 넣어주기
- 이때, 이미 jsp에 session이있기 때문에 따로 생성할 필요 X
```jsp
// loginForm.jsp에서
// 로그인폼 만들으셈 생략

```
```jsp
// test.jsp에서
<%
    String id = request.getParameter("id");
    String pw = request.getParameter("password");
    if (id.equals("ssafy") && pw.equals("1234")){
    //로그인 성공(세션을 데이터에넣자)
    //세션을 얻어오자
    // HttpSession session = request.getSession();
    session.setAttribute("loginUser", id);
    response.sendRedirect("main.jsp");
} else {
    //로그인 실패 
    response.sendRedireect("loginForm.jsp");
}


```jsp
//main.jsp에서

<body>
    <% 
        if (session.getAttribute("loginUser") == null ) {
            response.sendRedirect("loginForm.jsp");
        } else {
    %>
                        <%=session.getAttribute("loginUser")%> 님 반갑습니다.
    <%
}
    %>
    
<!-- 로그아웃 -->
<form action = "Logout.jsp" method="POST">
    <button>로그아웃</button>
</form>
```

```jsp
// 로그아웃을 하는 방법으로는 2가지 가 잇다
// 방법1. session의 속성을지우거나
// 방법2. session전체를 지워버리거나
<% session.removeAttribute("loginUser"); %>
<% session.invalidate(); %>

<script type = "text/javascript">
    alert("로그아웃되셨습니다.);
    location.href = "loginForm.jsp";
</script>
```