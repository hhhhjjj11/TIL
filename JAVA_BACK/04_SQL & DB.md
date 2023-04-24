# MySQL

## JOIN
- 둘 이상의 테이블에서 데이터를 뽑아서 보기 위해 사용
### JOIN 종류
1. INNER JOIN : 조인 조건에 해당하는 칼럼 값이 양쪽테이블에 모두 존재 하는 경우에만 조회 
2. OUTER JOIN : 조인 조건에 해당하는 칼럼 값이 한 쪽 테이블에만 존재 하더라도 조회 기준 테이블에 따라 LEFT OUTER JOIN, RIGHT OUTER JOIN으로 구분 

### JOIN사용하기
- JOIN쓸 때 , 양쪽 테이블에 다 있는 컬럼은 앞에 테이블붙여서 써줘야함. 안그러면 에러남 
- 예) 테이블.컬럼

### OUTER JOIN
- 둘 중 하나에 어떤 컬럼이 반드시 존재하지 않더라도 데이터를 조회
- 레프트 라이트 있음
- 언제필요?
   - inner join으로 안되는 경우 -> null값 인경우

### SELF JOIN
- 같은 테이블끼리 비교해서 데이터 뽑아내고 싶을때 
- 예 )

### 비 동등 조인
- 조인조건이 table의 PK, FK 등으로 정확히 일치하는 것이 아닐 때 사용

# 서브쿼리
- SQL문 안에 있는 SQL문
- 반드시 괄호( ) 로 감싸서 사용한다.
- 단일 행 또는 다중 행 비교 연산자와 함께 사용 가능.

## 서브쿼리의 필요성
- 예를들어, 
1. 부서 테이블이 있고, 사원 테이블이있다.
2. 사번이7788인 사원의 부서이름이 뭔지 뽑아내고 싶다.
3. 서브쿼리를 쓰지 않으면, 아래와 같이 "JOIN을 이용해서" 쓸 수 있다.
```sql
SELECT d.dname
FROM emp e, dept d
WHERE e.deptno = d.deptno
AND e.empno = 7788;
```
4. 이것은 모든테이블의 데이터를 다 가져와서 전부 조인시킨다음에 다시 조건을 이용해서 걸러서 가져오는 식임.
5. 뭔가 비효율적인데?

### 다르게생각해보자
1. 조인을 사용하지 않고 다음과 같은 방식으로 찾아낼 수는 없을까?
2. 우선, 사원번호가 7788인 사원의 부서넘버(X라 하자)를  찾은다음에 
3. 부서테이블에서 부서넘버가 X인 부서의 이름을 뽑는다.
```sql
SELECT deptno
FROM emp
WHERE empno = 7788;
```

```sql
SELECT dname
FROM dept
WHERE deptno = 20;
```

### 서브쿼리를 쓰면 가능해요!!
```sql
SELECT dname
FROM dept
WHERE deptno = ( SELECT deptno
                               FROM emp
                               WHERE empno = 7788 );

```

### 예시들
1. 매니저 이름이 'KING'인 사원의 사번, 이름, 부서번호, 업무조회
```sql
SELECT empno, ename, deptno, job
FROM emp
WHERE mgr = ( SELECT empno FRM emp WHERE ename = 'KING' );
```

2. 7566 사원보다 급여를 많이 받는 사원의 이름, 급여를 조회
```sql
SELECT ename, sal
FROM emp
WHERE sal > ( SELECT sal FROM emp WHERE empno = 7766 );
```

3. 20번 부서의 평균 급여보다 급여가 많은 사원의 사번, 이름, 업무, 급여 조회
```sql
SELECT empno, ename, job, sa
FROM emp
WHERE sal > ( SELECT avg(sal) FROM emp WHERE deptno = 20 ) ;
```

4. 업무가 'TURNER'와 같고, 사번이 7934인 직우너보다 급여가 많은 사원의 사번, 이름, 업무를 조회
```sql
SELECT empno, ename, job
FROM emp
WHERE job = ( SELECT job FROM emp WHERE ename = 'TURNER' ) 
AND sal > ( SELECT sal FROM emp WHERE empno = 7934 );
```

## IN, ANY, ALL 연산자 -> 다중 행 반환
### 사용 예
1. 업무가 'SALESMAN'인 직원들 중 최소 한 명 이상보다 많은 급여를 받는 사원의 이름, 급여, 업무를 조회
```sql
SELECT ename, sal, job
FROM emp
WHERE sal > ANY ( SELECT sal FROM emp WHERE job = 'SALESMAN') 
AND job != 'SALESMAN' ;
```
- 다중행이란 ANY절이 여러명있다 이말임

2. 업무가 'SALESMAN'인 모든 직원보다 급여(커미션포함)를 많이 받는 사원의 이름, 급여, 업무, 입사일, 부서번호 조회
```sql
SELECT ename, sal, job, hiredate, deptno
FROM emp
WHERE sal > ALL (SELECT sal + IFNULL(COMM,0) FROM emp WHERE job = 'SALESMAN')
AND job != 'SALESMAN';
```
3. 직원이 최소 한 명이라도 근무하는 부서의 부서번호, 부서이름, 위치
```sql
SELECT deptno, dname, loc
FROM dept
WHERE deptno in ( SELECT DISTINCT deptno FROM emp) ;
```
- DISTINCT 키워드를 이용해 중첩되는 행은 제거
- in 다중행에 하나라도 일치하면 조회, =ANY와 같다.

## 서브쿼리 - 다중열
- 이번엔 컬럼 두개 이상 반환하는 경우를 의미.
- 순서쌍으로 괄호로 묶어서 처리가능
- 예를들어, 아래 두 SQL은 의미상 동일, 동일한 방식으로 처리됨
```sql
SELECT * FROM t1 WHERE ( column1, column2 ) = (1,1)
SELECT * FROM t1 WHERE column1 = 1 AND column = 2;
```
### 예
1. 이름이 FORD인 사원과 매니저 및 부서가 같은 사원의 이름, 매니저 번호, 부서번호를 조회
```sql
SELECT ename, mgr, deptno
FROM emp
WHERE (mgr, deptno) = (SELECT mgr, deptno FROM emp WHERE ename = 'FORD')
AND ename <> 'FORD';
```
- <> 는 != 와 같음

## 상호연관 서브 쿼리
- 서브쿼리에서는 메인쿼리에서 사용하는 테이블과 컬럼을 참조할 수있음.
- 반대로 메인에서는 서브꺼 못함
- 이처럼 외부쿼리에 있는 테이블에 대한 참조를 하는 서브 쿼리를 상호연관 서브쿼리라고 함
### 예
1. 소속 부서의 평균 급여보다 많은 급여를 받는 사원의 이름, 급여, 부서번호, 입사일, 업무 조회
```sql
SELECT ename, sal, deptno, hiredate, job
FROM emp e
WHERE sal > ( SELECT AVG(sal) FROM emp WHERE deptno = e.deptno );
```
- 서브쿼리에서 emp테이블을 참조하고있음.
- 또 e.deptno 필드를 참조하고있음

## 서브쿼리 - 인라인 뷰 
- FROM 절에서 사용되는 서브쿼리

## 서브쿼리 - 스칼라 서브 쿼리
- 하나의 행에서 하나의 컬럼 값만 반환하는 서브 쿼리
```sql
SELECT ename, deptno, sal,
(SELECT AVG(sal) FROM emp WHERE deptno = e.deptno ) as avgsal FROM emp e;
```

