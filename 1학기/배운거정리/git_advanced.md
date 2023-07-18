# git advanced

## 개념
[Working Directroy]
Untracked  -> 깃허브가 추적하지 않는 파일
- .gitignore

[Staging Area]
Tracked  -> 깃허브가 추적 중인 상태
- $ git add . 를 통해 staging 상태로 만든다.

[Repository]
modified -> 
- $ git commit -m '4월 7일'


기타
## 깃배쉬로 텍스트 파일 만들기
```
$ vi text.txt 
// 깃배쉬로 텍스트 파일 만들기

$ i
// 입력시작

뭐 글자 입력후

// 아래쪽에다가 
$ :wq
// 이러면 저장됨
```

### vim 이란?
 - git bash 가 포함하고 있는 텍스트 에디터
 - vim 크게 네 가지 모드가 존재함
   - Normal 모드
     - vim 실행 시 적용되어 있는 기본 모드
     - 명령어를 입력할 수 있는 모드
       -> 단축키를 활용하여 명령어를 
         u - 이전 명령 취소(undo)
         yy - 현재 줄 복사
         p - 현재 줄 아래에 붙여넣기
         dd - 현재 줄 삭제
         i - insert 모드로 전환 

   - 명령모드
      - Normal 모드에서 ':'(콜론) 입력 시 명령 모드로 접근
      - 파일 저장, 종료, 검색 등 다양한 명령 실행 가능
      - 자주 쓰는 단축키
           :w - 저장
           :q - 종료
           :wq - 저장 후 종료
           :q! - 강제종료
           :wq! - 강제 저장 후 종료
           /문자열 - 현재 커서 아래방향을 검색
           ?찾을문자열 - 현재 커서 기준 윗방향을 검색
                          -> n: 아래방향으로 계속 검색
                          -> N: 위에스 계속 검색
        :set nu (==:set number) - 라인 넘버 보이기
        :set nonu (==:set nonumber) - 라인 넘버 숨기기

 
   - Insert 모드
     - 텍스트를 입력, 수정하는 모드
     - Normal 모드에서 'i', 'a'입력 시 입력 가능
        - i : 현재 커서부터 입력 
        - a: 현재 커서 바로 다음 
   - Visual 모드
       - 드래그 등 마우스를 이용하는 것 처럼 사용가능한 모드


## git restore
  - Working Directory 수정 파일 내용을 이전 커밋 상태로 돌림
  - Tracked 파일들에 대해서만 동작
      -> 한번 이사 커밋을 한 파일들에 대해서 적용
  - 주의 ! 데이터 날아갈 수 있음. 이전 커밋상태로 돌아가기때문에, 커밋 이후 수정한거 날아감.
```
$ git restore text.txt
```
## $ cat text.txt
- 터미널창에서 바로 텍스트파일 내용 볼 수 있음.
```
$ cat text.txt
```

## git add 취소하기
   - root-commit -> 한 번이라도 커밋을 했는지 여부에 따라 명령어가 조금 다름
  - 한번도 커밋을 안 한 파일 : `$ git rm --cached`
  - 한 번이라도 한 파일 : `$ git restore --staged <파일명>`

  - $ git status 를 찍어보면 new file, modified 로 구분되어 표시된다.

## git commit 취소하기
- 직전 commit 수정하기
  - `$ git commit --amend`
      - 새로운 커밋 내용이 있다면 덮어쓰기, 없다면 커밋 메시지만 수정
(이거 살짝 놓침, 구글링해보기.)
- 협업 개발시 사용 지양. 많이 안씀
- commit 



## git reset 
- 특정 커밋으로 돌아가서 작업하자 
- 이후 커밋 내역은 다 지우자
```
$ git reset 커밋ID
```
하고 로그 찍어보면 커밋 없어져잇음
```
$ git log 
```

## git revert
- 특정 버전에 있는 내용을 수정하고 ,
- 이후 커밋은 또 


# branch

## git branch
- 현재 브랜치 목록 조회
```
$ git branch
```

## git branch first
- 브랜치 생성
```
$ git branch first
```
## git switch first
- 현재 사용중인 브랜치 바꾸기
```
$ git switch first
```

## merge
1. 마스터브랜치로 이동한 다음.
2. git merge first 
  - 의미 first브랜치를 현재브랜치(마스터브랜치)로 병합시킨다.

## git branch -d first
- 브랜치 삭제

## git branch -c first
- 생성하고 이동까지 한번에

sd