# Interceptor
- 요청을 처리하는 과정에서 요청을 가로채서 처리
- HandlerInterceptor를 구현한것

## HandlerInterceptor의 주요 메서드

### preHandler()
- 컨트롤러 실행 이전에 호출해서 만약에 false를 반환하면 요청을 종료한다.

### postHandl()
- 컨트롤러 실행 후 호출
- 정상 실행 후 추가 기능 구현시 사용

### afterCompletion()
- 뷰가 클라이언트에게 응답을 전송한 뒤에 실행
- 컨트롤러에서 예

# 인터셉터사용하기
1. com.ssafy.mvc.interceprot > Interceptor.java파일 생성 후 작성
```java

```

2. servlet-context.xml에 설정 추가
- 빈파일을 훑을 패키지경로를 수정해주고
- 인터셉터 등록 및 경로 매핑
```xml
<context:component-scan base-package="com.ssafy.mvc.controller" />
	
	<interceptors>
		<interceptor>
			<mapping path="/*"/>
			<beans:bean class="com.ssafy.mvc.interceptor.AInterceptor"> </beans:bean>
		</interceptor>
	</interceptors>	
```

## 같은 요청에 대해 인터셉터가 여러개 걸렸을때 인터셉터의 작동순서
- 각각 다 servlet-context.xml에 등록해줘야함.
- 등록순서와 연관있음
- A, B, C 순으로 등록했을 경우
1. preHandle 은 
A -> B -> C 순으로
2. postHandle 과 afterComplection은 역순으로 작동

### 디스펜서서블릿과 컨트롤러사이에, 작성순서대로 인터셉터를 거치게 됨. 
- 등록순서에 따라 다음과같이 있음.
디스펜스 서블릿
A
B
C
컨트롤러

# loginRequired : 로그인 인터셉터 만들어서 활용하기
## 만난 에러1
- @GetMapping 이나 @PostMapping은 스프링 최신버전에서 지원함 그냥 레거시 만들어서썼더니 에러나고 pom.xml에서 스프링 버전 5.3.18로 수정하니까 해결됨.

1. 컨트롤러로 가기전에 거칠거니까 preHandle쓴다는 점.


## 만난 에러2
- 상황 설명 : legacy mvc로 하니까 이게 옛날 버전이라그런지 pom.xml에 버전이 옛날 거로 돼어잇어서 에러가 난다.
- 해결 방법 : 
1. properies의 자바와 스프링 버전을 바꿔줬고.
2. 또 스프링프레임워크 버전도 바꿔줬다. 5.3.18로
```xml
	<properties>
		<java-version>1.8</java-version>
		<org.springframework-version>5.3.18.RELEASE</org.springframework-version>
		<org.aspectj-version>1.6.10</org.aspectj-version>
		<org.slf4j-version>1.6.6</org.slf4j-version>
	</properties>
```
```xml
<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-context</artifactId>
			<version>5.3.18</version>
			<exclusions>
				<!-- Exclude Commons Logging in favor of SLF4j -->
				<exclusion>
					<groupId>commons-logging</groupId>
					<artifactId>commons-logging</artifactId>
				 </exclusion>
			</exclusions>
		</dependency>
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-webmvc</artifactId>
			<version>5.3.18</version>
		</dependency>

```
## 큰 흐름 ; 일단 로그인 기능 구현(매우 간소화하여 처리) -> 로그인 인터셉터 -> 로그인 권한이 필요한 요청에 대해 인터셉터 매핑
<br><br>

0. 로그인 로그아웃기능을 간단히 구현했다.
1. 로그인인터셉터 클래스를 만든다.
```java
public class LoginInterceptor implements HandlerInterceptor{
	
	@Override
	public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler)
			throws Exception {
		
		// 다음과 같이 요청객체로부터 session데이터를 가져온다
		HttpSession session = request.getSession();
		// 만약 요청의 세션에 유저정보가 담겨잇다면 그것은 로그인이 되어있따는 말이고
		// 아니라면 로그인 되어있찌 않다는 뜻임
		// 로그인하면 id에 값을 담아두도록 했다고 치자.
		// 그러면 id의 값을 확인해보면 됨. 있으면 로그인 된거고 없으면 로그인 안된거 ㅇㅇ
		if(session.getAttribute("id") == null) {
			response.sendRedirect("login");
			return false;
		}
		
		return true; //오케이 통과
	}
}
```
2. servlet-context.xml에 bean에 등록한다.
```xml
	
	<beans:bean class="com.ssafy.mvc.interceptor.LoginInterceptor" id="confirm"></beans:bean>
	
```
3. interceptor로 등록한다.
```xml
		<interceptor>
			<!-- 일단 모든 경로에 다 매핑 해두고 exclude이용해서 login페이지로 가는 경우랑 메인페이지는 로그인권한 안거치게만듬(로그인 권한 없어도 접근 가능하도록) -->
			<mapping path="/*"/>
			<exclude-mapping path="/login"/>
			<exclude-mapping path="/"/>
			<beans:ref bean="confirm"/>
		</interceptor>
```

## 만난에러3
- 브라우저에서 리다이렉트 요청이 너무 많다고 에러가 남
- 이유 : 무한 리다이렉트 루프 돌아서 그럼
    - <exclude-mapping path="/loign"/> 으로 오타내고
    - 로그인 인터셉터에서 권한없을시 "login"으로 리다이렉트 걸어놔서 
    - 무한루프 돔
- 해결 : loign에서 login으로 고침.