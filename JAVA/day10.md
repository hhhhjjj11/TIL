 # 파일 입출력

# Sream [입출력시 이용하는 추상클래스]
## I/O 와 Stream
- 파일 입출력은 Stream을 통해 이뤄짐
- Stream은 byte가 흘러가는 통로!
- 데이터는 한쪽에서 주고 한쪽 에서 받는 일방통행 구조임을 알자.
- 이때, 입력과 출력의 끝단을 node라고한다.
- 두 노드를 연결하고 데이터를 전송할 수 있도록 하는 것 = stream
- stream은 단방향 통신이 가능  -> 하나의 스트림으로 입력과 출력을 같이 처리 할 수 없음

## stream 구분
- 입력 , 출력
- 문자, 바이트
- 네가지 추상클래스 : 문자입력, 문자출력, 바이트입력, 바이트출력
- 모든 입출력 객체는 위 네가지 추상클래스의 자식 클래스

## InputStream - 바이트입력

## Redear - 문자입력

## OutputStream - 바이트출력

## Writer - 문자출력

# File : 파일과 디렉터리를 다루는 클래스
- 파일 입출력을 할때는, 파일 이름을 가지고 File 클래스의 컨스트럭트를 이용해서 객체를 만든다음에 그거를 쓴다.

## 바이트단위 파일 입출력: FileInputStream, FileOutputStream
- 각각 inputStream, OutputStream을 상속받은 클래스임
- 이미지파일이나, .exe등 과같은 실행파일

## 문자단위 파일 입출력: FilesReader, FileWriter
- 텍스트파일이나 소스코드같은 파일 


# 보조스트림
- 부가적인 기능 제공
- 예
  - 데이터타입 바꿔서 전송하거나
  - 버퍼링기능
  - 객체입출력
- 체이닝가능하다.

## byte스트림을 char스트림으로 바꾸기
- InputStreamReader
- OutputStreamWriter

## 버퍼링을 통한 속도 향상
1. byte기반
- BufferedInputStream
- BuferedOutputStream
2. char기반
- BufferedReader
- BufferedWriter


## 객체전송
- ObjectInputStream
- ObjectOutputStream

## 보조스트림 사용 방법
- 이전스트림을 생성자의 파라미터에 연결
```java
new BufferedInputStream(System.in);

new DataInputStream(new BufferedInputStream(new FileInputStream());
```





# File 클래스 사용

```java
package test05;

import java.io.File;

public class Test1 {
    public static void main(String[] args) {
    
    File f  = new File("input.txt");
    System.out.println("이름: " + f.getName());
    System.out.println("경로:" + f.getPath());
    System.out.println("디렉토리 여부: " + f.isDirectory());
    System.out.println("파일 여부: " + f.isFile());
    System.out.println(f);
    }
}

```



# 객체 직렬화 - 보조 스트림 활용 
- 자바에서는 Serializable 인터페이스를 이용해서 직렬화하는데, 직렬화 하면 바이트코드로 된다.
- 이를통해 연속된 데이터 한줄로 쭉 나열할 수 있다. 이를 직렬화 라고한다. 
- json같은 다른 형식으로 직렬화 하려면 다른 라이브러리 써야한다. 

## 몇가지 키워드
1. transient -> 직렬화제외
2. serialVersionUID  :  직렬화, 역직렬화하려는데 클래스가 뭔가 바뀌어있으면 예외발생. 클래스의 변경 여부를 파악하기 위해 사용.
- 직렬화할때 UID가 설정되지 않았으면 컴파일러가 자동생성해줌
```java
class Person implements Serializable {
    private String name;
    private int age;
    private transient String ssn; //직렬화제외
    private LoginInfo lInfo;
}

```

## 직렬화하기 : 보조스트림이용
- ObjectInputStream, ObjectOutputStream
### 메서드
 - ObjectOutputStream()
 - writeObject()
 - ObjectInputStream()
 - readObject()
## 