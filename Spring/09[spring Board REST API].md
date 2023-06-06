# swagger 사용하기
1. pom.xml에 의존성추가하기 (2개추가해줘야함)
    - 2버전이랑 3버전 잇는데 3버전 쓰는 방법임.
    - mvn레파지토리에서 SpringFox Swagger UI 랑 SpringFox Swagger2. 둘다 3.0.0버전 ㄱㄱ
    ```xml
    		<!-- https://mvnrepository.com/artifact/io.springfox/springfox-swagger-ui -->
		<dependency>
		    <groupId>io.springfox</groupId>
		    <artifactId>springfox-swagger-ui</artifactId>
		    <version>3.0.0</version>
		</dependency>
				
		<!-- https://mvnrepository.com/artifact/io.springfox/springfox-swagger2 -->
		<dependency>
		    <groupId>io.springfox</groupId>
		    <artifactId>springfox-swagger2</artifactId>
		    <version>3.0.0</version>
		</dependency>
    ```
2. servlet-context.xml에 설정추가
```xml
	<resources location="classpath:/META-INF/resources/webjars/springfox-swagger-ui/" mapping="/swagger-ui/**"></resources>
```

3. com.ssafy.board.config.SwaggerConfig 클래스 만들고 설정 로직 추가
```java
package com.ssafy.board.config;

import org.springframework.context.annotation.Bean;

import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

@EnableSwagger2
public class SwaggerConfig {
	@Bean
	public Docket api() {
		return new Docket(DocumentationType.SWAGGER_2)
				.select()
				.apis(RequestHandlerSelectors.basePackage("com.ssagy.board.controller"))  // 컨트롤러지정
				.paths(PathSelectors.ant("/*/api/**"))   // 경로지정
				.build();
	}
}

```

4. bean으로등록하기 (servlet-context)
```xml
<beans:bean id="swagger2Config" class="com.ssafy.board.config.SwaggerConfig"/>
```


5. 서버키고 http://localhost:8080/mvc/swagger-ui/index.html ㄱㄱ


6. 스웨거 메인화면 설정 조작하기
```java
@EnableSwagger2
public class SwaggerConfig {
	@Bean
	public Docket api() {
		return new Docket(DocumentationType.SWAGGER_2)
				.select()
				.apis(RequestHandlerSelectors.basePackage("com.ssafy.board.controller"))
				.paths(PathSelectors.ant("/*/api/**"))
				.build()
				.apiInfo(apiInfo());
		
	}
	
	private ApiInfo apiInfo() {
		return new ApiInfoBuilder()
				.title("SSAFY 9기 BOARD REST API")
				.description("엄청나게 대단한 게시판을 위한 레스트풀한 서버입니다.")
				.version("0.1")
				.build();
	}
}

```

7. 컨트롤러에 스웨거 관련 어노테이션 추가하기
```java

package com.ssafy.board.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.ssafy.board.model.dto.Board;
import com.ssafy.board.model.dto.SearchCondition;
import com.ssafy.board.model.service.BoardService;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import springfox.documentation.annotations.ApiIgnore;

@RestController
@RequestMapping("/api")
@Api(tags="게시판 컨트롤러")    // 스웨거에서 해당 컨트롤러에 "게시판컨트롤러"라고 나타남
public class BoardController {
	
	@Autowired
	private BoardService boardService;
	

	@ApiOperation(value="게시글 조회", notes= "검색 조건도 넣으면 같이 가져옴")  // 스웨거에서 해당 api에 설명추가
	@GetMapping("/board")
	public ResponseEntity<?> list(SearchCondition condition) {
		List<Board> list = boardService.search(condition); 
		
		if(list == null || list.size() == 0)
			return new ResponseEntity<Void>(HttpStatus.NO_CONTENT);
		
		return new ResponseEntity<List<Board>>(list, HttpStatus.OK);
	}


	@ApiIgnore  // 스웨거에 해당 api 안뜸
	@PutMapping("/board")
	public ResponseEntity<Void> update(@RequestBody Board board){
		boardService.modifyBoard(board);
		
		return new ResponseEntity<Void>(HttpStatus.OK);	
	}	
	
}
	
```


8. 모델에도 추가할 수 있다.
```java
 @ApiModel(value="게시판 바구니", description="게시글 정보")
public class Board {
	private int id;
	private String title;
	private String writer;
	private String content;
	private String regDate;
	private int viewCnt;

	public Board() {
	}
...
}
```


# CORS
