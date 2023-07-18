# Repository

# Service
## 1. 어노테이션을 이용한 의존성 주입
- @AllArgsConstructor : 모든 변수 가지고 컨스트럭터 만들어줌
- @RequiredArgsConstructor  : final붙은 애들만 가지고 컨스트럭터 만들어줌 


## 2. @Transactional
- 클래스 레벨에 @Transactional을 쓰면 -> public 메서드들은 기본적으로 transactional에 걸려들어감.
- readOnly=true 로 설정을 주면 jpa가 조회하는 곳에서는 좀 더 성능을 최적화함.
- 읽기 메서드에는 readOnly=true를 넣어주고,
- 쓰기메서드에는 readOnly=true를 넣어주면 안됨. 데이터변경이 안됨.
- 그런데 클래스에 읽기 메서드가 더많으면 클래스레벨에서 readOnly=true를 걸어주고 쓰기메서드에 @Transactional을 다시 붙여서 오버라이딩 해주는 식으로 ㄱㄱ (false가 default라서 따로 readOnly=false작성 필요 X)