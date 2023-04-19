# 클래스간 상속

- 상위클래스 = 부모클래스 = super class
- 하위클래스 = 자식클래스 = sub class
- 생성자는 상속 안됨
- 인스턴스다음에 점찍어보면 사용가능한 메서드 나오는데 그거 보면 어느 클래스에서 상속받은 메서드인지 옆에 써있음

- Objects : 모든 객체는 내장 클래스인 Objects를 상속받는다. 거기 들어있는 메소드같은거 기본으로 쓸 수 있음.

- 자바는 다중상속은 지원 안한다. 부모는 하나만!

- 주의 : 상속받았더라도 접근제한자에 따라 사용가능 여부가 달라진다.

## super 키워드이용해서 조상클래스 접근하기
- super를 통해 조상 클래스의 생성자 호출
- super(); -> 생성자 호출
- super.멤버변수
- super.메서드()

### 자식클래스의 객체를 생성할때 부모클래스에서 정의한 변수도 정의하기
- 생성자의 super() 함수에 인자로 넣어준다.

```java
//부모 클래스에서
public class Person{
    String name;
    int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public void eat() {
        System.out.println("음식을 먹는다.");
    }
}

// 자식클래스에서
public class Student extends Person{
    String major;
    
    public Student(String name, int age, String major) {
        super(name, age)        // 생성자의 super의 인자로 넣어준다.
        this.major = major
    }

    public void study() {
        System.out.println("공부를 한다.");
    }
}

```
### 조상클래스의 메서드 호출


## 메서드 오버라이딩(overridding)
- 자식클래스에서 부모클래스의 메서드를 재정의하는 것

### 어노테이션 
- 컴파일러가 읽는 주석
- 오버라이딩 시에는 @override를 붙인다
- 기능 : 해당 메서드와 같은 이름의 메서드가 부모클래스에 없으면 오버라이딩이 아니므로 에러처리

### 하위클래스의 접근제어자의 범위가 상위클래스보다 크거나 같아야한다.

### 메서드 오버로딩(overloadding)과 헷갈리지 말기
- 오버로딩은 한 클래스에서 같은 이름의 메서드를 여러개 만들 수 있었음. 그렇게 같은 이름의 메서드를 여러개 만드는 것이 메서드 오버로딩이었음. 파라미터가 다른 경우 그렇게 할 수 있었음.
- 오버라이딩은 부모클래스의 메서드를 재정의하는 것임. 
```java
@Override
public String toString() {
    return "student [name = "+ super.name + ", age =" + super.age + ", major =" + this.major+ "";
}

```

# Object클래스의 equals메서드 오버라이딩하기
- 객체의 주소비교 : == 이용
- 객체의 내용비교 : equals 재정의
## Object 클래스
- 가장 최상위 클래스. 모든 클래스의 조상
- 따라서 모든 클래스에서 object의 멤버와 메서드를 쓸 수 있다.


## Object 메서드 오버라이딩 하기(이름만 같아도 true반환하도록)
- 우리는 equals 재정의 해보자
- 우클릭 > source > override implement Methods
- 그러면 우리가 오버라이드 할 수 잇는 메서드들이 나옴 그 중에서 equals 고르자.
```java
package test03_super;

public class Student extends Person {
	String major;
	
	public Student(String name, int age, String major) {
		super(name, age);
		this.major = major;
	}
	
	public void study() {
		System.out.println("공부를 한다.");
	}

	@Override
	public boolean equals(Object obj) {
		// TODO Auto-generated method stub
		return name.equals(((Student)obj).name);  //(Student)obj -> 형변환.. 자식클래스이므로 형변환 자유로운듯. 
		//학생객체가 되었으므로, name속성에 접근 할 수 있다.  
	} 
	
}

```

- 그러면 이제 이름만 같아도 true임

```java
package test03_super;

public class Test {
	public static void main(String[] args) {
		Student st = new Student("박사홍", 28, "나이");
		st.eat();
		
		System.out.println(st.toString());
		
		Student st2 = new Student("박사홍",20, "자바");
		System.out.println(st==st2); //다른객체
		System.out.println(st.equals(st2)); 
        // 오버라이딩 전에는 다르다고나옴, false반환. 주소값을 비교하고 있으니까. 오버라이딩 전에는 st==st2과 같은 코드임
		// 오버라이딩 후에는 같다고나옴, true반환. 이름만 같아도 true를 리턴하도록 오버라이딩 했으므로.
		Object o = new Object();
		o.equals(st);
		
	}

}

```


## equals메서드를 오버라이딩 할 경우에는 hashcode도 같이 재정의 해준다.
  - ### 해쉬코드란? 
    - 객체를 구별하기 위해 사용되는 정수값
    - 객체의 동일성을 확인하기 위해 사용
    - 두 객체가 같은지 판별할 때, equals와 hashcode를 함께 비교한다.

```java
    // Student 클래스에서 hashCode메서드 오버라이딩 해주고
	@Override
	public int hashCode() {
		return name.hashCode();
	}

```

```java
package test03_super;

import java.util.HashSet;
import java.util.Set;

public class Test {
	public static void main(String[] args) {
		Student st = new Student("박사홍", 28, "나이");
		st.eat();
		
		System.out.println(st.toString());
		
		Student st2 = new Student("박사홍",20, "자바");
		System.out.println(st==st2); //다른객체
		System.out.println(st.equals(st2)); //다르게나옴, 주소값을 비교하고 있으니까.
		
		Object o = new Object();
		o.equals(st);
		
		//집합
		Set<Student> set = new HashSet<>();
		set.add(st);
		set.add(st2);
		
		System.out.println(set.size()); // 집합에 들어있는 원소의 개수
		// set에서는 동일서을 판단하기 위해서 equals(), hashcode();
		// hashcode를 재정의하고 나서야 두 객체가 같은것으로 봄.
        // hashcode를 재정의 하기전에는 st와 st2가 다른 것으로 간주되어 집합의 원소가 2가나옴
        // 재정의 후에는 같은 것이므로 집합 원소가 1개로 나옴
	}

}

```

# final
- 클래스 앞에 붙으면 : 상속금지
- 메소드 앞에 붙으면 : overridding 금지
- 변수 앞에 붙으면 : 더 이상 값을 바꿀 수 없음을 상수화 


# 다형성
- 상속관계에 있을때, 조상 클래스의 타입으로 자식 클래스 객체를 참조할 수 있다.
  
## 