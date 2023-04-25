# EL & JSTL
# EL (Expression Language)
- JSP에서 사용하는 문법임. 
- 표현식을 좀더 간단하게 나타낼 수 있음
- 연산자도 사용가능
## 사용법 : ${ }
## 어떤식인지 맛만보자
```jsp
<body>
<!-- EL안쓰면 -->
<%
    int num1 = (Integer) request.getAttribute("num1");
    int num2 = (Integer) request.getAttribute("num2");
%>
<%=num1 %> + <%=num2 %> = <%=num1+num2 %> <hr>

<!-- EL안쓰면 -->
${num1} + %{num2} = ${num1 + num2}
</body>
```
- 이런식으로, 훨 간단하게 작성가능
- num1, num2 가 어디서 온애들인데?
- [알고있기]EL은 변수를 어디서 찾아서가져오냐? 
   - 스코프 순으로 뒤진다 : 페이지영역 -> 리퀘스트영역 -> 세션영역 -> 어플리케이션영역


# JSTL(JSP Standard Tag Library)
- JSP스크립트와 html코드가 섞여서 지저분함
- 이를 간결하게 작성하기 위해서 자바코드를 태그 형태로 만들어 놓은 것.
- 유용한 커스텀 태그들을 모아서 표준화 한 

## 사용법
1. 설치해야됨
2.  