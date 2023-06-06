1. jsp를 쓸필요가 없다 -> 관련 설정 ㄴㄴ

2. 스웨거설정해주기 -> 이번에는 springFox boot starter 라이브러리 추가해줘야함! (라이브러리 다름 주의)

3. import file system -> existing file ->  스웨거 코드 import해오고

4. application.properties에 설정추가 

5. webconfig로 설정코드 옮겨적기


## 포트번호바꾸는법
```properties
# application.properties에서

serve.port=9999
```
## 컨텍스트path 설정하기
```
# application.properties에서
server.servlet.context-path=/board
```

## cors에러 해결
방법 1. @CrossOrigin("*") 
- 각 컨트롤러마다 붙여줘야됨
방법 2. addcorsmapping / webconfig 클래스에서 한번에 처리
```

```