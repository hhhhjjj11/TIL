-- id, 이름, 직업, 능력, 

-- SQL문 작성 시 주의사항
-- 세미콜론을 기준으로 하나의 SQL문을 판별

-- 새로운 테이블을 생성하기
CREATE TABLE superhero (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    이름 TEXT NOT NULL,
    직업 TEXT NOT NULL,
    능력 TEXT,
    국적 TEXT,
    소속회사 TEXT,
    나이 INTEGER,
    가입날짜 DATE
); 

CREATE TABLE power(
    id INTEGER PRIMARY KEY,
    hero_id INTEGER,
    능력 TEXT,
    -- 외래키 등록 방법
    -- FOREIGN KEY (<필드명>) REFERENCES <테이블명>(<해당테이블PK>)
    -- 사실 지금은 hero  테이블이 없어서 외래키 등록에 오류가 있음
    FOREIGN KEY (hero_id) REFERENCES hero(id)
);

CREATE TABLE job(
    id INTEGER PRIMARY KEY,
    직업 TEXT
);

CREATE TABLE country(
    id INTEGER PRIMARY KEY,
    국적 TEXT
);

CREATE TABLE company(
    id INTEGER PRIMARY KEY,
    소속회사 TEXT
);

CREATE TABLE hero(
    id INTEGER PRIMARY KEY,
    이름 TEXT NOT NULL,
    나이 INTEGER,
    가입날짜 DATE,
    job_id INTEGER,
    country_id INTEGER,
    company_id INTEGER,
    FOREIGN KEY (job_id) REFERENCES job(id),
    FOREIGN KEY (country_id) REFERENCES country(id),
    FOREIGN KEY (company_id) REFERENCES company(id)
);

-- 직업 데이터 삽입하기
INSERT INTO job(직업)
SELECT DISTINCT 직업
FROM superhero;

INSERT INTO country(국적)
SELECT DISTINCT 국적
FROM superhero;

INSERT INTO company(소속회사)
SELECT DISTINCT 소속회사
FROM superhero;


INSERT INTO hero (id, 이름, 나이, 가입날짜,
                job_id, country_id, company_id)
SELECT sh.id, sh.이름, sh.나이, sh.가입날짜,
    CASE
        WHEN sh.직업 = '영웅' THEN 1 ELSE 2
    END AS job_id,
    CASE
        WHEN sh.국적 = '미국' THEN 1
        WHEN sh.국적 = '아스가르드' THEN 2
        WHEN sh.국적 = '러시아' THEN 3
        WHEN sh.국적 = '왜곡의 나라 와칸다' THEN 4
        WHEN sh.국적 = '아틀란티스' THEN 5
        WHEN sh.국적 = '아마조니아' THEN 6
        WHEN sh.국적 = '크립톤' THEN 7
        WHEN sh.국적 = '영국' THEN 8
        WHEN sh.국적 = '애포콜립스' THEN 9
        WHEN sh.국적 = '아즈라엘' THEN 10
        WHEN sh.국적 = '카하지아' THEN 11
        WHEN sh.국적 = '잉글랜드' THEN 12
        WHEN sh.국적 = '스페인' THEN 13
        WHEN sh.국적 = '독일' THEN 14
        WHEN sh.국적 = '캐나다' THEN 15
        WHEN sh.국적 = '완다' THEN 16
        WHEN sh.국적 = '그리스' THEN 17
        WHEN sh.국적 = '케냐' THEN 18
    END AS country_id,
    CASE
        WHEN sh.소속회사 = '마블' THEN 1
        WHEN sh.소속회사 = 'DC' THEN 2
        WHEN sh.소속회사 = '저스티스 리그' THEN 3
    END AS company_id
FROM superhero AS sh;



-- JOIN 을 테스트 하기 위해 랜덤으로 NULL 값을 넣음
UPDATE hero SET 가입날짜 = NULL WHERE id = 10;
UPDATE hero SET 가입날짜 = NULL WHERE id = 20;
UPDATE hero SET 가입날짜 = NULL WHERE id = 25;
UPDATE hero SET job_id = NULL WHERE id = 30;
UPDATE hero SET job_id = NULL WHERE id = 40;
UPDATE hero SET job_id = NULL WHERE id = 50;
UPDATE hero SET company_id = NULL WHERE id = 64;
UPDATE hero SET company_id = NULL WHERE id = 75;
UPDATE hero SET company_id = NULL WHERE id = 88;
UPDATE hero SET country_id = NULL WHERE id = 16;
UPDATE hero SET country_id = NULL WHERE id = 46;
UPDATE hero SET country_id = NULL WHERE id = 57;

-- JOIN : 여러 데이터를 합쳐서 원하는 데이터를 조회하기 --

-- CROSS JOIN
-- 두 테이블 간 가능한 모든 조합을 선택
SELECT * FROM hero, job;

-- INNER JOIN
-- 두 테이블에서 일치하는 값을 가진 행들만 선택
-- SELECT <필드> FROM 테이블1
-- INNER JOIN 테이블2
-- ON 조건
-- 전체 사람들의 id, 이름, 직업을 조회하여라
SELECT hero.id, hero.이름, job.직업
FROM hero
INNER JOIN job
ON hero.job_id = job.id;

-- 똑같은 코드 다른 표현 방식
-- 필드명이 겹치지 않는 부분은 명시하지 않을 수 있다.
SELECT hero.id, 이름, 직업
From hero
LEFT JOIN job
ON hero.job_id = job.id;

-- LEFT JOIN
-- 왼쪽 테이블의 모든 행과 오른쪽 테이블에서 일치하는 값을 가진 행을 선택
-- 일치하는 값이 없는 경우에는 NULL 값을 가짐

-- 똑같은 코드 다른 표현 방식 2
-- 각 테이블에 별칭주기
SELECT A.id, A.이름, B.직업
From hero AS A
LEFT JOIN job AS B
ON A.job_id = B.id;

-- 영웅들의 id, 이름, 능력을 조회하여라
SELECT hero.id, hero.이름, power.능력
From hero 
LEFT JOIN power
ON hero.id = power.hero_id

-- 영웅들의 직업, 소속회사를 조회하여라
SELECT hero.id, hero.이름, job.직업, company.소속회사
FROM hero
left join job
ON hero.job_id = job.id
left join company
ON hero.company_id = company.id;

-- RIGHT JOIN, FULL OUTER JOIN : SQLite는 지원안합니다 우리안씁니다.
-- 실제로도 거의 쓸일 없습니다.


