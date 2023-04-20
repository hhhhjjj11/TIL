# 인터페이스

## 추상클래스도 어쨌든 클래스라서 다중상속 안됨. 근데 추상클래스는 여러 클래스한테 자기 속성 나눠주고싶은 애란말임. 인터페이스를 이용하면 다중상속 가능

<br>

## 인터페이스 개념 : "두 시스템이 만나서 상호작용하는 접점."
- 규격, 공통약속, 틀 .. 이런게 필요함
- 즉, 모양을 맞춰줘야 한다이말임.
- ex) USB, HDMI, 

- 자바에서는 객체와 객체가 인터페이스를 통해서 상호작용 하겠다...

<br>

## 인터페이스
- 완벽히 추상화된 설계도 : 모든 메서드가 추상 메서드이며 클래스 앞에 interface붙이면 "public abstract"생략가능
- 모든 멤버변수가 public static final(상수라는말)(더이상 안고쳐)이며 마찬가지로 생략가능
- interface 키워드 사용하여 선언

<br>

## 인터페이스를 구현하는 클래스 만들기(인터페이스를 상속받는 클래스) : implements 키워드
```java
public class myClass imlements myInterface{

}
```
- 다중구현가능

<br>

## 인터페이스끼리 상속 : extends이용, 다중상속가능

<br>

## 일반클래스가 인터페이스 구현할경우 -> 반드시 메서드 오버라이딩 해야함
- 구현하지 않을경우 추상메서드를 남겨두는 것이므로 abstract클래스로 표시해야함

<br>

## [중요] 인터페이스로 다형성 적용가능
- 인터페이스의 객체로 인터페이스의 자식클래스로 만든 객체포함 시킬 수 있음
- 인터페이스 또한, 그 자식클래스로 만든 객체를 참조 가능.
```java
myInterface a1 = new Child();
```
<br>

## 인터페이스 실습;;;

<br>

## 왜 인터페이스를 사용해야하는가

- 기술이 발달할 수록, 설계도(클래스)는 달라질 수 있음.
- 객체는 다른게 만들어 질 수 있음.
- 클래스가 바뀔때마다 코드를 다시 고쳐야 하나??
- 인터페이스를 구현하기만 하면 어떤 클래스의 객체든 사용할 수 있다면 
- 코드를 고칠 필요가 없다

<br>

## 인터페이스 다중상속 해보기




<br><br><br>


# Generics 제네릭

## 제네릭 클래스란?
- 클래스를 정의할때 인자의 타입을 지정하지 않고, 타입또한 인자로 처리한 클래스 
- 이렇게 하면 정해진 타입만 쓰는 것이 아니라 다른타입들도 쓸수 있음

<br>

## 왜 필요할까?
- 제네릭은 미리 사용할 타입을 명시해서 형 변환을 하지 않아도 됨!
- 객체 타입에 대한 안전성 향상 및 형 변환의 번거로움 감소

<br>

## 제네릭 클래스 (인터페이스) 생성
- 클래스 또는 인터페이스 선언시 <>에 타입 파라미터 표시
```java
public class CalssNmae <T>{}
public interface InterfaceName <T>{}
```
- 참고: 
   - 제네릭 표시안한 경우를 raw type
   - 한경우 generic type 이라고 함
   - 보통 T(type),E(eleemnt),K(key),V(value)등을 씀

<br>

## 제네릭 메서드
- easy. 걍 메서드에서도 타입을 파라미터로 처리할 수 있음
```java
public class GenericBox<T> {
    private T data;
    
    public <K> void genericmethod(K k) {
        System.out.println("T: " + data.getClass().getName()); 
        System.out.println("K: " + k.getClass().getName());
    }
}

```
- 참고. 타입 출력방법
```java
Sysout(data.getClass().getName())
//data의 타입이 출력됨
```

<br>

## 제네릭도 제한 걸 수 있음
- 타입에도 위계가 있음을 기억하자.
- 다음과같이 <T extends Number> 하면 숫자관련 타입들만 올 수 있게 됨 (int float double 등)

```java
class NumberBox <T extends Number> {
    public void addSomes(T... ts){    
    double d = 0;
    for ( T t: ts) {
        d += t.doubleValue();
    }
    System.out.println("총 합은: " + d);
    }
}
```

<br>

## 제네릭 활용
1. <?> : 전부 가능
2. <? extends className> : 자손
3. <? super  className> : 조상
```java
package test09_wildcard;

public class Test {
	public static void main(String[] args) {
		genericbox<Student> studentBox = new genericbox<>();
		genericbox<Person> personBox = new genericbox<>();
		genericbox<Object> objectBox = new genericbox<>();
		
		// ? : 어떤 타입이든
		genericbox <?> allBox = objectBox;
		allBox = personBox;
		allBox = studentBox;
		
		// ? extends T : T 또는 T의 자손만
		genericbox<? extends Person> personAndChild = personBox;
		personAndChild = studentBox;
		personAndChild = objectBox; //오류 Person의 자식클래스의 객체만 가능
		
		// ? super T : T 또는 T의 조상만
		genericbox<? super Person> personAndParent = personBox;
		personAndParent = objectBox;
		personAndParent = objectBox;
	}
}
```
