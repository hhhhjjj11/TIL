# 예외처리
## 에러와 예외
- 자바에서는 둘을 구분함 
- 코드를 통해서 프로그램의 비정상적 종료를 막을 수 있는가
- 에러 -> 코드로 해결불가
- 예외 -> 코드로 해결가능
 
## 예외도 객체임. 클래스의 계층 알아보자
Object 
Throwable
Error Exception 

다시 Exception하위에 RuntimeException 등등이있음.

## Checked exception / Unchecked exception
1. Checked exception
 - 예외에 대한 대처 코드가 없으면 컴파일이 진행 되지 않음
- RuntimeException 상속 X
2. Unchecked exception
- 예외에 대한 대처 코드 없어도 컴파일 진행
- 어떤 코드가 예외가 발생할 수도 있을때, 그 예외가 unchecked 예외이면 일단 걍 진행은 된다 이말임. 반대로 checked는 진행도 안됨
- RuntimeException 상속 O

3. 예
- 길이가 1인 배열의 2번 항을 호출-> 실행은됨. -> 대처코드가 없음에도 실행이 됐다. -> uncheckedexception이다, RuntimeException을 상속받았다.

## 예외가 발생? = 내부적으로 예외 객체가 생성되서 던져진 것임
- 코드로 직접 예외 던지기
```java
throw new ArrayIndexOutOfBoundsException();
```

# 예외처리하기
## 직접처리
- try, catch ,finally

```java
package test;

public class trycatch {
	public static void main(String[] args) {
		// throw new Exception(); 작성후 Exception커서올리고 후 두번째 항목 선택
		try{
			throw new Exception();
		} catch (Exception e) {
			System.out.println("예외를 처리합니다.");
		}
		System.out.println("프로그램의 끝");
	}
	
	
}

```

```java
package test;

public class tc2 {
	public static void main(String[] args) {
		int[] nums = {10};
		
		try { 
			System.out.println(nums[1]);
			// catch() 안에 오는 예외클래스는
			// 발생하는 예외의 클래스 또는 조상클래스
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("배열의 크기가 넘어갔을 때는 대처 코드");
		}
		System.out.println("프로그램이 정상 종료");
	}
}

```

## 간접 처리 
- throws



## 사용자 정의 예외 발생시키기
- throwable 


# Throwable의 주요 메서드

1. e.getMessage() ;
 - 에러메시지
2. e.printStackTrace(); 
 - stacktrace까지 출력
3. 

## try ~ catch 흐름
1. try블록에서 예외가 발생하면
2. JVM이 Exception 클래스의 객체 생성 후 throw.
3. 던져진 exception은 catch블록에서 받은 후 처리 - 이때 적당한 catch블록을 만나지 못하면 예외 처리는 실패, 프로그램 비정상종료됨
4. 정상적으로 처리되면 try - catch 블록을 벗어나 다음 문장 진행
5. 참고. try블록에서 어떠한 예외도 발생하지 않으면 catch문을 거치지 않고 다음 코드 실행 

## 다중 exception 핸들링 
- 하나의 try 블록에 여러개 catch 블록 추가 가능
- 형태
```java
try {
   // exception 발생할만한코드..
} catch ( XXException e ) { 
  // XXException 발생시 처리 코드
} catch ( YYException e ) {
  // YYException 발생시 처리 코드
} catch ( Exception e ) {
  // Exception 발생시 처리 코드
}
```
### 다중 catch 문장 작성 순서 유의 사항
- 다형성 적용됨 -> 상위 타입의 예외가 먼저 선언되는 경우 뒤에 등장하는 catch 블록은 동작X
- 상속 관계가 아닐시 무관.
- 따라서 상속 관계 시 작은범위오류를 먼저 씀.

### 한번에 여러 예외 처리
```java
try {
     int num = Interger.parseInt("ssafy");
    // | 연산자를 이용
} catch ( ArithmeticException | ArrayIndexOutOfBoundsException | NumberFormatException e) { System.out.println( "하나의 블록에서 세 가지 예외를 처리합니다.");
}
```

## finally 사용하기 
- 예외 발생 여부에 관계 없이 항상 실행
- 중간에 return을 만나는 경우도 !! finally 블록 먼저 수행 후 return 수행;; ㄷㄷ
  

```java
package test;

public class etests {
	public static void main(String[] args) {
		// try ~ catch ~ finally
		
		// case1. "ssafy"
		try {
			String str = "ssafy";
			System.out.println("code 1 - before parse : " + str);
			int num = Integer.parseInt(str);
			System.out.println("code2 - after parse: " + str);
		} catch ( Exception e ) {	
			System.out.println( "code3 - exception handling 완료!");
		} finally {
			System.out.println("code4 - 언제나 실행?");
		}
		System.out.println("code 5 - 언제나 실행?");
		System.out.println("프로구램 끝");

	
//	code 1 - before parse : ssafy
//	code3 - exception handling 완료!
//	code4 - 언제나 실행?
//	code 5 - 언제나 실행?
//	프로구램 끝

		// case2. "1234"
	try {
		String str = "1234";
		System.out.println("code 1 - before parse : " + str);
		int num = Integer.parseInt(str);
		System.out.println("code2 - after parse: " + str);
	} catch ( Exception e ) {	
		System.out.println( "code3 - exception handling 완료!");
	} finally {
		System.out.println("code4 - 언제나 실행?");
	}
	System.out.println("code 5 - 언제나 실행?");
	System.out.println("프로구램 끝");

//	code 1 - before parse : 1234
//	code2 - after parse: 1234
//	code4 - 언제나 실행?
//	code 5 - 언제나 실행?
//	프로구램 끝

	// case3. "1234", try블록안에 return 붙이면?
	try {
		String str = "1234";
		System.out.println("code 1 - before parse : " + str);
		int num = Integer.parseInt(str);
		System.out.println("code2 - after parse: " + str);
		return;
	} catch ( Exception e ) {	
		System.out.println( "code3 - exception handling 완료!");
	} finally {
		System.out.println("code4 - 언제나 실행?");
	}
	System.out.println("code 5 - 언제나 실행?");
	System.out.println("프로구램 끝");
	
//	code 1 - before parse : 1234
//	code2 - after parse: 1234
//	code4 - 언제나 실행?
	
	}	
	
}

```

## throws 키워드를 통한 처리 위임
1. checked exception의 경우 -> 에러처리 못하면 컴파일이 안됨 -> 반드시 처리하거나 처리 위임(throw)해야함

2. 이떄  throw 사용시 ! 콜스택상으로 다음에 처리되는 함수에게 처리를 위임하는것임!!!

3. 예를들어 이해해보자
- 다음의 경우 생각
```java
main 함수에서
 method1() 실행
 method2() 실행, 
```
- method2에서 에러가 발생한다고 가정하자
- 콜스택에는 가장아래에 main , 그 위 method1, 맨 위 method2 가 있다.
- method2에서 throw한 예외는 method2로 넘어간다.
- method2에서도 throw하면 main으로 넘어간다.
- main에서도 throw하면? -> 처리되지 않은 예외로 되어 프로그램 비정상 종료됨
- 따라서 프로그램 멈춰도 괜찮은 경우 아닌 이상 결국 메인에서는 처리해야함

## throws 이용 : unchecked exception
- 실행은 됨 처리없어도
- throw하지 않아도 콜스택 상에서 저절로 전달 됨
- 예외 발생시 결국엔 try catch로 잡아줘야됨.