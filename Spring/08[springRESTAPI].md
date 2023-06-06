## spring REST관련 Annotation
```java
@GetMapping
@PostMapping
@PutMapping
@DeleteMapping 

@RestController // Controller가 REST 방식을 처리하기 위한 것임을 명시
@ResponseBody // 데이터 자체를 전달 (뷰 말고)
@PathVariable // URL 경로에 변수 썼을때 써줌
@RequestBody // JSON 데이터를 원하는 타입으로 바인딩

ResponseEntity // 데이터 응답시 [상태코드, 데이터] 함께 응답 가능
```

- 설명 : 기본적으로 컨트롤러에서 반환하는 값은 내부적으로 뷰의이름으로 인식함 -> 이것을 @ResponseBody어노테이션을 붙여서 반환하는 것이 뷰이름이 아니라 데이터임을 설정해줘야 함.
- ResponseBody 말고 컨트롤러에다가 RestController붙이면 일일이 ResponseBody안붙여도 자동으로 됨.

## jackson databind 라이브러리 이용한다.
- Map으로 반환해도 알아서 json으로 바꿔서 반환해줌 
- 그냥 Map 데이터 반환하면 에러남
- 라이브러리 써줘야 됨
- mvn에서 받아서 pom.xml의 dependencies에 추가
- 따로 코드 작성해줄 필요 없음, 걍 의존성 추가만 해주면 됨.

## RequestBody
- [배경지식]
- 폼데이터 형태로 맞춰서 넣으면 걍 되는데, 만약에 json타입으로 요청이 들어오면? 이때는 형태를 맞춰주지 않은 것이기 때문에 제대로 작동이 안됨..
- 이때 @RequestBody 어노테이션을 써주면 JSON타입의 데이터 요청도 알아서 폼데이터로 바꿔서 처리해줌!!