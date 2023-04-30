# MVC패턴 (Model + View + Controller)
큰흐름 
1. 컨트롤러에 서비스메서드랑 핸들러메서드들 있다.
2. 요청이들어오면 -> 서비스메서드에서 분기해서 적당한 핸들러 호출 -> 각 핸들러에서 -> jsp호출 (또는 리다이렉트)
 
# 실습

## 개념1 : 
1. jstl에서, ${board.id} 의 id가 접근하는 것은 board의 변수가아니라 접근자 getId임. 
- getId에서 get을빼고 앞글자를 소문자로바꾼것과 같다!!!
-  그래서 getter랑 이름 맞춰줘야됨.
- 예를들어, 접근자이름을 getTitle2 라고하면 jsp에서도 %{board.title2} 로 해줘야 에러없이 작동됨
 
## 개념2 
- `<a href="board?act=writeform">글등록</a>`
- 위 처럼, 슬래쉬를 안붙이면 현재경로의 마지막 슬래쉬 뒤에 덧붙이는거임
- 그래서 문제가 생길 수 있음 (올바른 경로로 접근할 시 문제 없음)
- 만약 문제가 발생할 경우에는
- `<a href="/BackEnd07_Board_web/board?act=writeform">` 
- 이렇게 풀경로로 쓰면 되는데, 이때 다음과 같이 req.getContextPath이용하여 변수처리를 한다.
- `<a href=<%=request.getContextPath() %>/board?act=writeform">글등록</a>`
  
- 또 다른 방법 : 다른 파일에서 처리해놓고 include로 불러와서 쓰기
1. webapp > common > header.jsp 만들고
2. 다음과같이 request에 경로 넣어주고
```jsp
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>

<%
	request.setAttribute("root", request.getContextPath());
%>
```
3. list.jsp에다가 include써주고 불러와서쓴다.
```jsp
<%@ include file="/common/header.jsp" %>
.
.
.
<a href="${root}/board?act=writeform">글등록3</a>
```

## 개념3 : 글작성 한다음에 -> redirect해줘야함 (doList말고)
### 배경지식(gpt검색함)
- 새로고침 -> 새로운 get요청이 아니라, 페이지를 다시 로드하는것이라고 함(?) -> 서비스 메서드가 호출, 이때 이전 요청에 대한 정보또한 저장되어있음 -> 어쨌든 목록으로 get요청인데, 이전요청(dowrite으로 post)도 있어서 결과적으로 요청 두 개 들어감 -> 데이터가 또 추가되고 목록이 뜸.

```java
	private void doWrite(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		Board board = new Board(); //껍데기 생성
		
		board.setTitle(req.getParameter("title"));
		board.setContent(req.getParameter("content"));
		board.setWriter(req.getParameter("writer"));
		
		try {
			dao.insertBoard(board);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		// 등록 했으면 1. 상세페이지로 가서 그 글의 내용을 보여주는 것
		//			2. 전체 글 목록으로 돌아가기
		
		// 전체글 목록으로 가기
		// doList(req,resp);  // 이렇게 하면 안됨. list화면에서 새로고침 할 때마다 추가됨.
		// 이유 : list화면에서 새로고침 -> get요청 -> service메서드에의해 doList()호출 -> doList는 포워드 메서드
		// req에 데이터가 남아있음 -> ?? 뭔소리임 이게?? 이해 안됨
		
		//resp.sendRedirect("board?act=list");
			
	}
```