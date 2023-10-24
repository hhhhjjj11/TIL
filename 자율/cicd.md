## 1. EC2 로컬에 Jenkins 및 Docker 설치하기
### 먼저 jdk부터 설치 하기
```
sudo apt-get update
sudo install ~~~

java -version 
하면 설치 할 수있는 목록 버전별로 보여줌. 그거 그대로 따라 쳐서 설치하면 됨.
```
### JDK 설치했으면 이제 Jenkins ㄱㄱ
- https://www.jenkins.io/doc/book/installing/linux/#debianubuntu
- 공식문서참조
- 펨키 버전이 계속 바껴서 옛날꺼 쓰면 에러뜸;;
- 항상 공식문서에서 긁어서 쓸것!!
```bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt-get update
sudo apt-get install jenkins
```



```
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```

### jdk를 먼저 설치를 하고 나서 jenkins를 설치해야 에러가 안나는듯.
<br>

### 도커 설치는 생략

<br>

### [주의] 도커 그릅에 젠킨스를 추가해야 젠킨스 스크립트로 도커 명령어를 실행시 permission 에러가 안난다. (아래의 트러블슈팅 참고)

<br>

--------------------
<br>

### [참고] EC2로컬의 젠킨스 포트 번호 바꾸기
- 자율플젝때 수현이가 이미 도커로 띄운 젠킨스 때문에 8080을 쓰고있어서 젠킨스 설치해도 activated안되고 에러뜸. 이유는 포트 문제였음.
#### 1. [권장] 방법1
- https://nworlds.tistory.com/entry/Jenkins-%EC%9A%B0%EB%B6%84%ED%88%AC%EC%97%90-%EC%A0%A0%ED%82%A8%EC%8A%A4-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0
- 이 방법이 더 맞는 방법 인듯 하다. 이유는 jenkins가 업데이트 될 때 다시 8080으로 설정 되기때문인데,
이 방법을 쓰면 업데이트 되더라도 설정이 덮어씌워지는듯

#### 2. 방법2
- https://velog.io/@kungsboy/EC2-%EC%9A%B0%EB%B6%84%ED%88%AC20.4-%EC%A0%A0%ED%82%A8%EC%8A%A4-%EC%84%A4%EC%B9%98-%EB%B0%8F-%EC%A0%A0%ED%82%A8%EC%8A%A4-%ED%8F%AC%ED%8A%B8-%EB%B3%80%EA%B2%BD
- 두 군데의 설정 파일을 동시에 바꿔주어야 함 
```
sudo vi /etc/default/jenkins
sudo vi /usr/lib/systemd/system/jenkins.service
```
- 그 다음 jenkins 재 시작
```
sudo systemctl daemon-reload
sudo service jenkins restart
```
<br>

----------------------------
<br>

### 포트뚫기 (다 잘 됐는데 방화벽에 막히는 경우) 
```
sudo iptables -A INPUT -p tcp --dport 9090 -j ACCEPT
```
- gpt가 알려줌,
- ec2를 껐다키면 다시 설정해줘야 한다는데 그럴일은 없으니까 뭐.. 걍 쓰면 될듯
- 9090 포트에 대해서, 모든 외부 ip의 모든 포트에서의 접근을 허용한다는 의미.

<br><br><br>

## 2. 브라우저로 젠킨스 접속
### 1. cat var/lib/jenkins/secrets/initialAdminPassword 로 접속 시작 비밀번호 ㄱㄱ

<br>

## 3. 젠킨스에서 설정
### 1. gitlab 플러그인 설치
### 2. credentials 두개 만들기
- 1. gitLab API token 
  - 깃랩에서 발급받은 토큰 넣어주면 됨.
- 2. username with passwrod 
  - 이 때 아이디는 깃랩계정(huhwo00@naver.com)
  - 비밀번호는 깃랩계정 비밀번호가 아니라 깃랩에서 발급받은 api토큰!
### 3. 깃랩 연결
  - GitLab host URL : https://lab.ssafy.com
  - credentials 로 gitlab API token 선택

<br>

## 4. 이제 파이프라인 만들기
1. gitlab connection : 위에서 연결한거 선택
2. Build Triggers : 
  - Build when a change is pushed to GitLab. GitLab webhook URL:어쩌고저쩌고
  - 그리고 저 webhook URL인 '어쩌고저쩌고'를 가지고 깃랩으로 가서 웹훅 설정 해줌.
  - 깃랩에서 웹훅 테스트까지 해준다음 OK응답 까지 확인.
  - 이때 고급설정 하위에서 Secret token을 생성해서 깃랩 웹훅 설정시에 넣어줘야함.
3. 고급 설정
  - Allowed branches: 브랜치 특정해주기
4. 파이프라인 스크립트
```
pipeline {
        agent any
        // 없어도 됨. gradle 관련 설정.
        // tools {
        //     gradle 'gradle_101'
        // }
        stages {
            
            stage('git clone') {
                steps {
                    git branch: 'test', credentialsId: 'gitlab_HJ', url: 'https://lab.ssafy.com/s09-final/S09P31A101.git'
                }
            }
            
          stage('build'){
                steps{
                        sh'''
                            echo "빌드 시작"
                            cd /var/lib/jenkins/workspace/test/backend/starcard
                            chmod +x gradlew
                            ./gradlew clean build
                        '''
                }
            }
            
            stage('deploy'){
                steps{
                        sh'''
                            echo "도커 이미지 생성"
                            cd /var/lib/jenkins/workspace/test/backend/starcard
                            docker build -t test .
                            echo "기존 컨테이너 삭제"
                            docker container rm -f test
                            echo "도커 컨테이너 실행"
                            docker run -d -p 8090:8080 --name test -e SPRING_PROFILE=prod test
                            //docker run -d -p 8090:8090 --name test -e SPRING_PROFILE=prod test

                        '''
                }
            }
        }
    }
```
- 특화때는 8090:8090 으로 했는데, 포트를 뚫어줬는데도 안돼서
- 걍 8090:8080으로 해서 8090으로 들어온것도 8080에서 받도록 처리해서 해결 했음
- 포트 뚫었는데도 왜 안되는건지는 못알아냄
### + 포트뚫어줘야댐, 위의 iptable 관련 명령어로 뚫으면 원래 되야하는것 같음.
- 아마 docker in docker 로 해서 안되는건가? 모르겠음.
- 어쨌든 8080으로 돌려서 해결하긴함.
- 재우한테 물어볼까..?


<br>


## 5. 깃랩프로젝트 파일 관련
  1. DOCKERFILE 들어있어야함
  ```
  FROM openjdk:11-jdk
  ENV SPRING_PROFILE prod
  ADD build/libs/*.jar app.jar
  ENTRYPOINT ["java", "-Dspring.profiles.active=${SPRING_PROFILE}", "-jar", "/app.jar"]

  ```
  2. application-prod.yml 있어야함. (ENV SPRING_PROFILE prod 가 의미하는게 prod이름 붙은 yml 쓴다는거) 
  3. 근데 application.yml 도 있어야 할거임 아마. 왜냐면 빌드할때 application.yml이 있어야 빌드가 됨. 걍 디폴트 설정인듯.
  4. 빌드 안될시 putty가지고 직접 ec2들어가서 빌드 해보자.
    - 이때 빌드한다음에 build 폴더 삭제 해주자 안그러면 cleanbuild 안된다고 젠킨스에서 할때 에러남


### [참고] 그래들설정관련..
- 그래들을 파이프라인 내부에서 지정해줄 경우에는 그래들 플러그인을 설치한다음에 설정>도구에서 그래들 설정을 해주어야하는것 같은데, 스프링 부트 내부에 이미 gradle 버전을 지정하고 있어서 빌드시에 그거보고 그래들을 자동으로 불러와서 빌드하기때문에 젠킨스에서 따로 설정 안해줘도 되는 듯하다.
- 어쨌든 젠킨스에서 그래들 설정 안하고도 빌드 배포 다 됨.

<br><br>


## 트러블 슈팅
### 1. clean build 시 갑자기 build 폴더 삭제할 수 없다고 하면서 빌드 실패하는 이유
- 이거는 폴더 삭제할 권한이 없어서 그런거임.
- ec2안에서 직접 빌드를 해본 다음에 젠킨스를통해 clean build 하려고 하면 삭제못한다고하는데
- 그 이유는 ec2 안에서 만든 폴더이기때문에 폴더 소유권한?? 이 젠킨스에 없어서 그런 문제라고 함.
- 해결방법은 2가지가 있는데 하나는
- 방법1: 젠킨스에게 폴더관련 권한을 부여하는 로직사용(해보진않음) 
```
sudo chown -R jenkins:jenkins /var/lib/jenkins/workspace
```
- 방법2 : ec2안에서 직접 빌드 폴더 삭제하면 됨 ㅋㅋ
```
build있는 곳으로 가서,,
rm -rf build
```

### 2. 그래들 문제.. 
- 의존성을 자동으로 불러오는 기능이 이상하게도(?) gradle8.0부터는 그 기능이 빠져서 빌드가 안된다고함
- 그래들7.4.1 (7번대) 를 쓰면 빌드 되긴함..


### 3. 젠킨스를 가지고 도커 이미지 생성시 권한 문제
- 도커 권한을 가지고 있는 그룹에 jenkins를 추가하고나서
- 젠킨스를 restart까지 해줘야 적용됨
```
sudo usermod -aG docker jenkins
sudo service jenkins restart
```
- docker그룹(도커관련작업을 할 수 있는 사용자 그룹을 뜻하는듯 하다.)을 확인해보는 명령어
```
getent group docker
```