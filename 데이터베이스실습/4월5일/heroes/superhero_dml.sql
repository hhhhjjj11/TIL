-- 전체조회
-- SELECT <원하는필드> FROM <테이블>
SELECT * FROM superhero;

-- 특정 필드 조회
SELECT 이름 FROM superhero;
SELECT 이름, 소속회사 FROM superhero;

-- 만약에 없는 필드로 작성하게 되면 에러 
SELECT 없는필드 FROM superhero;

-- 별칭 지어주기
SELECT 이름 AS 활동명 FROM superhero;

-- 콤마로 구분 지어서 여러 개 별칭 짓기
SELECT 이름 AS 활동명 , 소속회사 AS 팀 FROM superhero;


--  나이가 적은순으로 정렬하여 출력
-- SELECT <필드> FROM <테이블>
--  ORDER BY <필드>
SELECT * FROM superhero
ORDER BY 나이;

-- 문자열도 정렬 가능
SELECT * FROM superhero ORDER BY 이름;

-- 나이가 많은순으로 조회하기
SELECT * FROM superhero
ORDER BY 나이 DESC;

-- 여러 필드로 정렬하기
-- 소속회사 별로 나이가 많은 순으로 조회하기
SELECT 이름, 나이, 소속회사 FROM superhero ORDER BY 소속회사,나이 DESC;


-- 중복 제거하기
SELECT 소속회사 FROM superhero;

-- 소속회사 중복 제거
SELECT DISTINCT 소속회사 FROM superhero; 

-- 여러 필드를 사용하면, 모두 동일한 데이터를 삭제
SELECT DISTINCT 직업, 소속회사 FROM superhero;


-- 나이, 소속회사가 겹치지 않는 사람들 중
-- 소속회사, 나이 순으로 정렬
SELECT 나이,소속회사 FROM superhero ORDER BY 소속회사, 나이;


----------------------------------------------------------------

-- 조건문(WHERE)

-- 직업이 악당인 사람들만 조회
SELECT * FROM superhero WHERE 직업 = '악당';

-- 비교연산자 사용하기
-- 나이가 50살이 넘는 사람들만 조회
SELECT * FROM superhero WHERE 나이 > 50;

-- 가입날짜가 2000년 1월 1일 이전인 사람 조회
SELECT * FROM superhero WHERE 가입날짜 LIKE '1%';
SELECT * FROm superhero WHERE 가입날짜 < '2000-01-01' ORDER BY 가입날짜;

-- 소속회사가 마블이고 직업이 영웅인 사람들만 조회
SELECT * FROM superhero WHERE 소속회사 = '마블' AND 직업 = '영웅';

-- 국적이 미국이거나 러시아인 사람들만 조회
SELECT * FROm superhero WHERE 국적 = '미국' OR 국적 = '러시아';


-- 특정패턴 만족하는 데이터 조회
-- EX) 2글자인 데이터, ~~맨으로 끝나는 데이터

-- Like Operator
-- 1. %(percent): 글자 수 제한 없이 패턴을 만족하면 조회

-- 이름이 ~~맨 으로 끝나는 사람들 조회 
SELECT * From superhero where 이름 like '%맨';

-- 2. _(underscore): 개수 만큼 글자 수 제한하여 패턴을 만족하면 조회
-- 이름이 두 글자인 사람들만 조회 
SELECT * from superhero where 이름 like '__';


-- 특정 데이터에 포함여부(IN)
-- 마블, DC 소속의 사람들을 조회
SELECT * FROM superhero WhERE 소속회사 = '마블' or 소속회사 = 'DC';

SELECT * FROM superhero WHERE 소속회사 IN ('마블','DC');

SELECT * FROM superhero WHERE 소속회사 NOT IN ('마블','DC');


-- 특정 조건 사이에 존재하는 데이터 조회(BETWEEN ... AND ...)
-- 나이가 100-500살 사이의 사람들을 조회
SELECT * FROM superhero WHERE 나이 BETWEEN 100 AND 500;

-------------------------------------------------------------------

-- 원하는 행 개수만큼만 조회 (LIMIT) (저장된순서로)
SELECT * FROM superhero LIMIT 1;

SELECT * FROM superhero LIMIT 3;


-- 나이가 가장 적은 사람 1명
SELECT * FROm superhero order by 나이 limit 1;

-- 나이가 많은 10명
SELECT * FROm superhero order by 나이 desc limit 10;

--  소속회사가 마블인 사람 중 나이가 가장 적은 1명
SELECT * FROm superhero where 소속회사 = '마블'  order by 나이 limit 1 ;

-- N 번째 데이터부터 조회 - 기준점을 변경(OFFSET)
-- 검색 기준점: OFFSET + 1 부터
-- 나이가 10번째로 많은 사람
SELECT * FROM superhero ORDER BY 나이 DESC LIMIT 1 OFFSET 9;



---------------- 내일 라이브 내용 예습 ----------------------------
-- 데이터 수 구하기
-- 전체 데이터 수를 구하여라
SELECT COUNT(*) AS COUNT
FROM superhero;

-- 조건문과 함께 활용
-- 직업이 악당인 사람의 수
SELECT COUNT(*) AS COUNT
FROM superhero
WHERE 직업 = '악당';

-- 전체 평균 나이
SELECT AVG(나이) AS 평균나이 FROM superhero;

-- 문자열은 안나옴
SELECT AVG(국적) AS 평균나이 FRom superhero;

-- 마블의 영웅들의 평균나이를 구하여라
SELECT AVG(나이) AS 평균나이
FROM superhero
WHERE 소속회사 = '마블';


--  그룹 별 계산
--  각 소속회사의 평균 나이를 구하여라
SELECT 소속회사, AVG(나이) AS 평균나이
FROM superhero
GROUP BY 소속회사;


-----------------------------230406-------------------------

-- 평균나이 : GROUP BY + AVG의 결과 (소속회사별로 group by 한다음 avg)
-- 평균나이가 40살 이상인 소속회사를 구하여라

-- 소속회사 별로 그룹
-- 40살 이상인 데이터만 조회
-- 평균 계산
SELECT 소속회사, AVG(나이) AS 평균나이
FROM superhero
WHERE 나이 >= 40
group by 소속회사;

-- 그룹화 후에 조건주기(HAVING)
