### EC2 로컬에 Jenkins 설치하기
- 먼저 jdk부터 설치 하기
```
sudo apt-get update
sudo install jdk17설치설치
```
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

<br><br>

```
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```

### jdk를 먼저 설치를 하고 나서 jenkins를 설치해야 에러가 안나는듯.


### EC2로컬의 젠킨스 포트 번호 바꾸기
1. [권장] 방법1
- https://nworlds.tistory.com/entry/Jenkins-%EC%9A%B0%EB%B6%84%ED%88%AC%EC%97%90-%EC%A0%A0%ED%82%A8%EC%8A%A4-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0
- 이 방법이 더 맞는 방법 인듯 하다. 이유는 jenkins가 업데이트 될 때 다시 8080으로 설정 되기때문인데,
이 방법을 쓰면 업데이트 되더라도 설정이 덮어씌워지는듯

2. 방법2
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