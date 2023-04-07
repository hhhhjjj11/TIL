-- id, 이름, 직업, 능력, 

-- SQL문 작성 시 주의사항
-- 세미콜론을 기준으로 하나의 SQL문을 판별

-- 새로운 테이블을 생성하기
CREATE TABLE superheroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    이름 TEXT NOT NULL,
    직업 TEXT NOT NULL,
    능력 TEXT,
    국적 TEXT,
    소속회사 TEXT,
    나이 INTEGER
); 

-- 기본키 : 레코드를 판별(식별)하는 데 사용.
--         - 테이블 당 하나만 존재가능.
--         - 중복X

-- 테이블명 변경하기
ALTER TABLE superheroes RENAME TO superhero;

-- 새로운 컬럼 추가
ALTER TABLE superhero ADD COLUMN 가입날짜 DATE;

-- 임시 컬럼 추가 후 이름 변경
ALTER TABLE superhero
ADD COLUMN 임시 TEXT;

-- 
ALTER TABLE superhero RENAME 임시 TO 곧삭제;

ALTER TABLE superhero DROP COLUMN 곧삭제;
-- "DROP COLUMN"은 sqlite3 extension버전이 딸려서 사용 못함.
-- 그래서 shell로 걍 써야됨

-- shell 사용법
-- 터미널에서 db를연다
-- $ sqlite3 db.sqlite3
-- sqlite> ALTER TABLE superhero DROP COLUMN 곧삭제;
-- !주의! db가들어있는 상위폴더까지 들어가서 실행해야 되는듯. db파일이 들어있는 곳 까지 cd명령어로 이동한다음에
-- $ sqlite3 db.sqlite3 해줘야함

-- 
-- .import superheroes.csv 테이블이름
