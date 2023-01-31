class Nationality():
    # 클래스 변수 영역 (이를 통해 모든 인스턴스가 같은 변수(값)을 공유 할 수 있음)
    # 몇 개의 나라가 생성되었는지 
    cnt=0

    # 초기화(생성자) , 초기에 인스턴스를 생성시 nationality를 입력해주어야 함.
    def __init__(self, nationality, population):
        # 인스턴스 변수 선언
        self.nationality = nationality
        self.population = population
        # 클래스 변수 접근
        Nationality.cnt+=1 # 인스턴스를 만들때마다 클래스변수인 cnt 가 1씩 증가.
    
    # 인스턴스메서드
    #  -> 인스턴스 자체가 가진 데이터를 다룬다.
    # 클래스 변수, 인스턴스 변수 모두 사용가능

    def get_population(self):
        print(f'{self.nationality}-{self.population}')

    
    # 클래스 메서드
    # 클래스 변수만 사용가능한 메서드
    @classmethod
    def get_count(cls):
        print(f'전체 나라 수는 {cls.count}입니다.')

    # 둘 다 아닌 경우
    #  -> 인스턴스 변수, 클래스 변수 모두 사용하지 않는 메서드
    # 변수는 안써도, 문맥상 해당 클래스에 포함된다고 판단될 때
    # static method는 클래스 밖에서 선언해도 전혀 문제 없으며, 동작도 동일하다.
    @staticmethod
    def print_test():
        print('print_test')

    # 매직 메서드 재정의
    # 재정의 : 기존에 있던 함수를 "덮어쓰는" 하는 동작
    # 원래 Nationality 객체가 가지고 있는 __str__ 함수가 아닌,
    # 내가 새로 정의한 __str__ 를 호출한다.

    def __str__(self):
        return '나의 국적은 ' + self.nationality
   
    def __del__(self):
        print('소멸자 호출')

korea_nationality = Nationality("대한민국", 5174)
usa_nationality = Nationality("미국", 33190)
china_nationality = Nationality("중국", 141200)

print(korea_nationality) 
print(usa_nationality)
print(china_nationality)

# 클래스 변수 접근은, 인스턴스, 클래스 모두를 통해 접근 가능.
print(Nationality.cnt)

print(korea_nationality.cnt)
print(usa_nationality.cnt)
print(china_nationality.cnt)


# 매직 메서드 등 모든 객체의 정보 출력
# 매직 메서드 : 특정 상황에 
# print(dir(korea_nationality.__str__()))

# 메모리에서 영영 삭제
del china_nationality

# 메모리에서 china_nationality 변수를 찾을 수 없으니 is not defined 에러 발생
china_nationality.get_population()
Nationality.get_count()