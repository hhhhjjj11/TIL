# 실습 CRUD
# 준비물 : DBUtil, BoardDao, BoardDaoImpl, Board

## 1. DBUtil 클래스
- db연결작업등을 처리해주는 로직 작성
### 인스턴스 : jdbc드라이버를 로딩하는 역할
- 인스턴스는 스태틱으로 작성. 크래스로드시 함께 로드
- 인스턴스가 스태틱이기 위해서는 생성자또한 스태틱이어야함 (생성자가 있어야 인스턴스가 만들어지는거니까)
- 따라서 생성자 스태틱으로 만들어준다.
- 이때 생성자 본문에 jdbc드라이버 로드 하는 로직 넣어주면, 클래스 로드시 인스턴스도 로드되면서, jdbc드라이버가 로드된다.

### 메서드
1. 생성자
 - 이때 생성자 함수 본문에 jdbc드라이버 로드 로직을 작성. 
2. 접근자
 - 메서드를 써먹으려면 접근자를 이용해서 인스턴스를 가져와야겠지?
3. 연결
4. 연결해제

```java
package com.ssafy.board.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 * Mysql DB 연결 객체를 제공하주고, 사용했던 자원을 해제하는 기능을 제공하는 클래스입니다.
 */

public class DBUtil {
	/**
     * url은 jdbc:mysql://[host][:port]/[database][?propertyName1][=propertyValue1]형태로 작성한다.
     * serverTimezone=UTC 설정이 없으면 오류가 발생하므로 주의한다.
     */

	private final String url = "jdbc:mysql://localhost:3306/ssafy_board?serverTimezone=UTC";
	private final String username = "root";
	private final String password = "ssafy";
	private final String driverName = "com.mysql.cj.jdbc.Driver";


	// 싱글턴
	private static DBUtil instance = new DBUtil();

    private DBUtil() {
        // JDBC 드라이버 로딩
        try {
            Class.forName(driverName);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static DBUtil getInstance() {
        return instance;
    }


    public Connection getConnection() throws SQLException{
    	return DriverManager.getConnection(url, username, password);
    }


	// DB연결 해제
    public void close(AutoCloseable... closeables) {  //전개연산자 AutoCloseable타입 인스턴스를 쭉 쓰면 알아서 closeables로 처리해서 함수 진행된다~
        for (AutoCloseable c : closeables) {
            if (c != null) {
                try {
                    c.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }
}

```
## 2. BoardDao 인터페이스
- 쿼리 잔뜩 있음
- 인터페이스에서 쿼리들을 정한다음에 오버라이딩해서 쓸거임
```java
package com.ssafy.board.model.dao;

import java.sql.SQLException;
import java.util.List;

import com.ssafy.board.model.dto.Board;

public interface BoardDao {
	//전체 게시글을 몽땅 들고 오쎄용
	public List<Board> selectAll();
	
	//ID에 해당하는 게시글 하나 가져오기
	public Board selectOne(int id) throws SQLException;
	
	//게시글 등록
	public void insertBoard(Board board) throws SQLException;
	
	//게시글 삭제 
	public void deleteBoard(int id) throws SQLException;
	
	//게시글 수정
	public void updateBoard(Board board) throws SQLException;
	
	//조회수 증가
	public void updateViewCnt(int id) throws SQLException;
	
}
```
## 3. BoardDaoimpl 클래스 
- 인터페이스 구현 클래스
### 기억하기
1. util( DBUtil클래스의 인스턴스 ) 가져온다. 그리고 각 메서드에서 util.getConnection과 close씀.
2. 싱글턴으로 쓰면 된다. 메서드만 쓸거니까 인스턴스는 메서드를 사용하기 위해 필요할 뿐임.
3. 메서드를 오버라이딩한다.


## 4. Board 클래스 ( BoardDto )
1. 멤버변수
2. 생성자
3. 접근자, 설정자

# BoardDaoimpl 클래스 메서드
# 1. selecAll 메서드(데이터전부가져오기)
- 빈리스트 만든담에 쿼리로 끌어와서 담는다.
- 큰흐름  : 1. db연결하고 sql문 써서 resultset받아온담에 2. board클래스 인스턴스에 정보 넣고 반환

## 순서1 : db에서 데이터긁어오는 순서
1. DB연결한다. (Connection 객체생성)
2. Connecion객체를 이용해서 Statement객체를 생성한다. (이때 , createStatement() 이용)
3. stmt객체의 executeQuery메서드의 인자에 작성한 sql문을 넣는다.
4. 반환 값을 resultset 클래스에 담는다.

## 순서2: rs로부터 Board클래스 인스턴스 만들어서 반환하기  + db연결해제
- Board의 설정자 + rs의 접근자 이용한다.
- rs에 여러개 있으니까 while(rs.next())문 이용
- finally문에서 util.close로 db연결 해제한다.


```java
	@Override
	public List<Board> selectAll() {
		List<Board> list = new ArrayList<>();
		
		// 선언을 try블록 안에서 해버리면 scope이슈로 finally블록에서 사용 못하므로,
		// 밖에서 선언하고, try블록 안에서 값을 할당
		// 밖에서 할당하면 안되나 ?  또 예외처리하라고 뜨기 때문에 이런식으로 한다.
		Connection conn = null;
		Statement stmt = null;
		ResultSet rs = null;
		
		try {
			conn = util.getConnection();
			
			stmt = conn.createStatement();
			
			// 전체 값을 가져오는 sql문 작성
			String sql = "SELECT * FROM board";
					
			rs = stmt.executeQuery(sql); // 쿼리가 반환하는 데이터 집합임.
			
			//데이터가 여러개일 수 있으므로 while이용
			while(rs.next()) {
				Board board = new Board();
				// rs.getInt("id"); // resultSet 에서 데이터 하나를 고를거임 getInt메서드를 이용해서 필드의값이 정수인
				board.setId(rs.getInt("id"));
				board.setTitle(rs.getString("title"));
				board.setWriter(rs.getString("writer"));
				board.setContent(rs.getString("content"));
				board.setRegDate(rs.getString("reg_date"));
				board.setViewCnt(rs.getInt("view_cnt"));
				
				list.add(board);
			}

		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			util.close(rs,stmt,conn); 
		}
		
		return list;
	}

```
# 데이터 삽입 메서드
## 개념설명하나 하고가자 : PreparedStatement
( 좀 더 진보된 방식의 statement )

- ? 기호를 사용해서 SQL문에 변수를 포함시킬 수 있다.
### 순서
1. 변수처리('?'처리)해서 sql문 쓰고
2. preparedStatment 객체 만들고
3. setString메소드 이용해서 '?'자리에 값 정해준다
  - 이때, setString메소드 쓰는방법
  - pstmt.setString( 변수인덱스, 값 )
  - 즉, 변수세개만들면 
  - pstmt.setString(1, v1) // db는 인덱스 1부터
  - pstmt.setString(2, v2) 
  - pstmt.setString(3, v3)
4. pstmt.executeUpdate() ; 로 실행

## 순서
1. db연결 + 변수처리해서 sql문 작성하고
2. pstmt객체 만들고
3. 변수에 값넣고
4. pstmt객체 실행
5. db연결해제

```java
	@Override
	public void insertBoard(Board board) throws SQLException {
		// TODO Auto-generated method stub
		String sql = "INSERT INTO board (title, writer, content) VALUES (?,?,?)";
		
		Connection conn = null;
		PreparedStatement pstmt = null;
		
		conn = util.getConnection();
		pstmt = conn.prepareStatement(sql);
		
		pstmt.setString(1, board.getTitle());
		pstmt.setString(2, board.getWriter());
		pstmt.setString(3, board.getContent());
		
		pstmt.executeUpdate();
		
		util.close(pstmt, conn);
	}
```

# 삭제하기메소드
```java
	@Override
	public void deleteBoard(int id) throws SQLException {
		String sql = "DELETE FROM board where id=?";
		
		Connection conn = null;
		PreparedStatement pstmt = null;
		
		try {
			conn = util.getConnection();
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setInt(1, id);
			int result = pstmt.executeUpdate();
			
			System.out.println(result + "개의 데이터가 지워졌습니다");	
		} finally {
			util.close(pstmt, conn);
		}
		
	}
```

# updateViewCnt
```java
	@Override
	public void updateViewCnt(int id) throws SQLException {
	
		String sql = "UPDATE board SET view_cnt = view_cnt+1 WHERE id=?";
		Connection conn = null;
		PreparedStatement pstmt = null;
		
		try {
			conn = util.getConnection();
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setInt(1, id);
			pstmt.executeUpdate();
			
		} finally {
			util.close(pstmt, conn);
		}
	}

```

# 데이터 하나 가져오기
## resultset 개념 
1. resultset 은 BOF, data, EOF 부분으로 나뉘어 있음
2. 처음에는 커서가 BOF에 가있음.
3. 그래서 바로 rs.getInt(1) 해도 오류가남. data를 가리키고 있는게 아니라 BOF를 가리키고 있으므로
4. 그래서 rs.next()로 커서를 데이터로 옮기는 처리를 해줘야함.
```java
	@Override
	public Board selectOne(int id) throws SQLException {
		String sql = "SELECT * FROM board WHERE id = ?";
		
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		Board board = new Board();
		try {
			conn = util.getConnection();
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setInt(1, id);
			
			rs = pstmt.executeQuery();
			
			while(rs.next()) {
				// 필드 인덱스랑 설정자랑 잘 맞아야됨!! 안그러면오류남
				board.setId(rs.getInt(1));
				board.setWriter(rs.getString(2));
				board.setTitle(rs.getString(3));
				board.setContent(rs.getString(4));
				board.setViewCnt(rs.getInt(5));							
				board.setRegDate(rs.getString(6)); 
			}
			
		} finally {
			util.close(rs, pstmt, conn);
		}
		return board;
	}
```

# 데이터수정하기
```java
	@Override
	public void updateBoard(Board board) throws SQLException {
		String sql = "UPDATE board SET title = ?, content =? WHERE id = ?";
		Connection conn = null;
		PreparedStatement pstmt = null;
		
		try {
			conn = util.getConnection();
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setString(1, board.getTitle());
			pstmt.setString(2, board.getContent());
			pstmt.setInt(3, board.getId());
		
			pstmt.executeUpdate();
			
		} finally {
			util.close(pstmt, conn);
		}
		 
	}
```