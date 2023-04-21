# 자료구조

## Collections : 자바에서 자료구조 모아둔

## 정적 자료구조, 동적자료구조
1. 정적 자료구조 : 배열
  - 선언시 크기를 명시하면 바꿀 수 없음
2. 동적 자료구조 : 리스트, 스택, 큐 등
  - 요소의 개수에 따라 자료구조의 크기가 동적으로 증가하거나 감소

## 자료구조의 종류
- 종류는 결국 얼마나 빨리 원하는 데이터를 찾고 추가, 삭제, 수정할수 있는가에 따라 결정된다.
- 또, 순서유지여부, 중복허용여부 등에 따라 종류가 나뉜다.
1. List
    - 순서가 있는 데이터의 집합. 순서가 있으니까 데이터의 중복을 허락.
    - ArrayList, LinkedList, Vector
2. Set
    - 중복X
    - HashSet, TreeSet
3. Queue
    - 큐. 선입선출
    - LinkedList
4. Map (객체랑 비슷한듯?)
    - key,value 쌍으로 데이터 관리.
    - 순서는없음,
    - key 중복 불가  
    - value는 중복 허용

## List
- 배열과 list를 구분한다는점 알자.
- 순서O, 중복O
- ArrayList, LinkedList, Vector가 있다.
1. ArrayList  
2. LinkedList
3. Vector
- 알고있기 : 작동방식이 조금씩 달라서, 어떤 메서드를 사용할 것인지에 따라 성능차이가 있다.
- 각 특징은 좀 더 구글링 ㄱ

## 주요 메서드
- add, remove 등

## LinkedList 살펴보기
- 각 요소를 Node로 정의함
- Node는 현재 요소의 데이터 + 다음 요소의 주소값(참조값)으로 구성
- 각 요소가 다음 요소의 링크 정보를 가지기때문에 연속적으로 구성될 필요가 없다.
- 따라서 중간에 값을 추가하거나, 삭제하는것이 빠르다. 앞뒤로 참조값만 바꿔주면 되므로.


## Set
- 순서가 없고, 중복허용 X
- HashSet, TreeSet


### HashSet
- hashcode, equals 두개가 같아야 같은 걸로 봄


### TreeSet
- 레드블랙트리에 저장하는 set


## Map
- 키,밸류
- HashMap , TreeMap
- 키는 중복X , 값은 중복O

# Map 생성하기

```java
package test;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class test {
	public static void main(String[] args) {
		Map<String, String> map = new HashMap<>();
		
		//맵에 값 저장
		map.put("Hong", "1");
		map.put("Yang", "2");
		map.put("Lee", "3");
		
		// 중복된 키로 값을 넣을 경우 새로운 값으로 대체
		map.put("Hong", "4");
		
		System.out.println(map);
		
		// 값을 가져오려면?
		System.out.println(map.get("Yang"));
		
		// 없는 키로 가져오면?
		System.out.println(map.get("Kim"));
		
		// 키가 있는지 미리 확인
		System.out.println(map.containsKey("Kim"));
		
		// 값이 있는지 확인
		System.out.println(map.containsValue("5"));
		
		// 반복문 돌리기
		for(Map.Entry<String, String> entry : map.entrySet()) {
			System.out.println(entry.getKey()+" : " + entry.getValue());

		// 반복문 돌리기2 - keySet()으로 키만가져와서 이터레이터 만들기
		Iterator<String> e = map.keySet().iterator();
		while(e.hasNext()) {
			String key = e.next();
			System.out.printf("키: %s, 값: %s, \n", key, map.get(key));
		}
		
		// 반복문 돌리기3 - foreach
		for(String key : map.keySet()) {
			System.out.println("키: %s, 값: %s, \n", key, map.get(key));
		}
		
		// 원소개수
		System.out.println(map.size());
		
		}
		
	}
}

```
 



# Set : hashcode랑 equals 오버라이딩하기

- 같은 값을 hashset에서같은 값으로 인식하도록  만들고 싶다.
- hascode와 equals는 Objects의 (최상위 객체) 의 메소드 이므로, 하위 클래스에서 오버라이딩 할 수 있음을 상기하자.
- 문자열이 같으면 해시코드가 같도록
- 아이디끼리 비교해서 같으면 equals가 true를 리턴 하도록
```java
public boolean equals(Object obj) {
    if (obj instanceof Person) {
        Person other = (Person) obj;
        return this.id.equals(other.id);
    }  else {
        return false;  
    }
}
```


# Queue
- 자바에서 큐는 인터페이스, 구현체는 linkedlist를 사용
## 메서드
- E offer() : 값 집어넣기
- E peek() : 가장 앞에 있는 데이터 조회
- E poll(): 가장 앞에 있는 데이터 빼내기
- boolean isEmpty(): 큐가 비어있는지 여부

# 스택
- 스택클래스사용
## 메서드
- E push(E e) : 데이터추가
- E peek() : 가장 위에 있는 데이터 조회
- E pop() : 가장 위 데이터 빼내기
- boolean isEmpty() : 스택이 비어있는지 여부


# 정렬
- 요소를 기준에 대한 내림차순 또는 오름차순으로 배치 하는것
- 순서를 가지는 Collection들만 정렬 가능
- List계열 , SortedSet의 자식 객체, SortedMap의 자식 객체

## 정렬방법
```java
Collections.sort(lsit)
```
## 원리 
- 객체가 Comparable을 구현하고 있는 경우 내장 알고리즘을 통해 정렬

# Comparable Interface
- 이 인터페이스를 구현하는 클래스는 Collection.sort()를 사용할 수 있다.
- 다음처럼생겼음
```java
public Interface Comparable<T> {
    public int compraeTo(T o);
}
```
- 추상메서드 comparteTo를 오버라이딩 해주어야함.
## comparteTo
- compareTo는 인트형(int)를 반환함,
- 두개의 객체를 비교하여 양수가나오면 자리를바꾸고, 음수 또는 0 -> 자리 유지

## compareTo 오버라이딩
```java
public int compareTo(Person o) {
    // 이름 순으로 String의 메서드를 그대로 사용
    return this.name.comparteTo(o.name);

    // 나이 순으로
    return Integer.parseInt(this.id) - Integer.parseInt(o.id);
}

```

# 정렬 또다른 방법 : Comparator활용
## 객체가 Comparable을 구현하고 있지 않거나 사용자 정의 알고리즘으로 정렬하려는 경우
```java
package test08_comparator;

import java.util.Comparator;

public class AgeComparator implements Compare<Person> {
    
    @Override
    public int compare(Person o1, Person o2){
        return Interger.parseInt(o1.getId()) - Integer.parseInt(o2.getId());
    }
}

```