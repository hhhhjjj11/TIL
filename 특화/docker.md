### 1. ec2에 서버 열기
- 인스턴스 만들고 
- 서버상에서 git clone 하고
- 빌드하고 ./gradlew build
- build/libs로 가서 실행
- java jar- project.0.0.1.SNAPSHOT.jar 
- https://kang-james.tistory.com/entry/%EB%B0%B0%ED%8F%AC-AWS%EB%A5%BC-%ED%86%B5%ED%95%9C-%EB%B0%B0%ED%8F%AC-%EB%B0%A9%EB%B2%95-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0EC2-%EC%84%9C%EB%B2%84-%EC%8B%A4%ED%96%89
### 2. 로컬에 도커로 서버열기
- 내 로컬에 도커 설치하고
- 프로젝트 안에 Dockerfile 만들고 
- 도커 이미지만들고 
- 도커 실행 (이때 포트 번호 지정 해주기)
-  https://yooooonnf.tistory.com/5
### 3. ec2에 도커로 서버열기
- [방법1] 도커를 로컬에 설치한다음에 도커허브 쓰기
    - 로컬에 도커 설치한다음에
    - 로컬에서 이미지 파일만들고
    - 도커 허브에다가 push (이때 도커 이미지 이름을 반드시 id/레포지이름 으로 해야하는 듯)
    - 만약에 이름을 이렇게 안해놨으면 이름 바꿔주기
- [방법2] 도커를 EC2에 설치하기
    - https://haengsin.tistory.com/128
    - (에러관련) https://league-cat.tistory.com/347

### 4. EC2 + Docker + Jenkins CI/CD
- 우선, 알아야할 것은 도커를 명령어를 통해 젠킨스를 깐다는 점. (훨씬 간편한 방법이다.)
- 3의 방법2 에서 도커를 EC2에 설치한 것 그대로 EC2안에 도커를 설치해준다.
- 그다음에 도커명령어로 젠킨스를 설치해준다.


### 도커 에러 및 명령어
- 포트 번호 설정해줘야함 
- 안그랬더니 서버는 켜졌는데 접근거부라고 뜸.
```
docker run -p 8080:8080 testimage
```
### 이름 바꾸기
```
docker tag 원래이름 바꿀이름 
```

### 도커로 젠킨스 실행하기

### 컨테이너 중지하기
- https://www.lainyzine.com/ko/article/docker-stop-and-docker-kill/