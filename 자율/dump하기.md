mySQL (mariaDB)덤프
1. 방법1: cli 명령어로
  - 걍 내 로컬에서 cmd 켜서 
  - C:\ProgramFile\MySQL\MySQL Server 8.0\bin 가서 
  - mysqldump --column-statistics=0 -hk9a101.p.ssafy.io -P 3309 -u root -p chat > c:\test\testtest.sql
  - 단순히 test.sql 이렇게만 하면안되고 경로지정해줘야함 위와같이
  - 대문자P로 포트번호 지정
  - DB의 root 계정, root비밀번호를 이용해야함, 그냥 일반사용자 이용할 경우 root권한을 부여하는 과정을 ec2상에서 처리해줘야하는 듯 하다.
  - --column-statistics=0 설정을 걸어줘야 함, Unknown table 'COLUMN_STATISTICS' in information_schema에러와 관련된 처리 설정임.
  - 걍 로컬 cmd에서 덤프파일 뽑아낼수있다는점
2. 방법2: workbench gui 이용하기: data -> export data 
  - 근데 에러남
  - Unknown table 'COLUMN_STATISTICS' in information_schema (1109)
  - 위 에러가 뭐 workbench 8얼마 이상 부터는 따로 설정 해주는 작업이 필요하다는 듯
  - 나중에 해보기

몽고DB덤프
1. 몽고디비설치 + mongodbdatabase tools 까지 설치 해줘야함 (구글검색하면 공식페이지 바로나옴)
  - mongodump명령어 쓰려면 mongodbdatabase tools 있어야됨.
2. mongodbdatabasetools 의 bin으로 가면 명령어있음,
```
mongodump --host k9a101.p.ssafy.io -u root -p <password>
```
- 이때 root / password 는 mysql할때 했던거랑 똑같다 (이거 아마 수현이가 설치해서 그런듯)
3. 결과
- 데이터는 BSON으로오고 스키마가 JSON으로 옴. (아마도?)