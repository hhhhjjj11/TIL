class MyClass:

    def method(self):
        return 'instance method', self

    @classmethod
    def classmethod(cls):
        return 'class method', cls

    @staticmethod
    def staticmethod():
        return 'static method'


my_class = MyClass()
print(my_class.method())
print()

# 객체 지향의 핵심 4가지
# 추상화 : 코드의 재사용성을 높이고 기능을 확장, 핵심이 되는 공통부분만 추림
# 다형성 : 각자의 특성에 따라 다른 결과 만들기
# 캡슐화 : 데이터 보호하기
# 상속 : 하위 클래스는 상위 클래스에 정의된 속성, 행동

class Professor :
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department


class Person : 
    pass

p1 = Person()
p1._age = 25  # 이거 안됨

print(p1._age) # 이거 안됨

p1.set_age(25)
print(p1.get_age())


# 1. 추상화 - 현실 세계에 있는 것을 얼마나 코드로 잘 표현하느냐
# 2. 상속 - 부모의 속성(변수, 함수 등), 권한 등을 모두 가져와서 재사용
#           - 중복되는 코드 관리
#           - 수정 등 유지보수에서 생산성을 증가시키기 위해
# 3. 다형성 - 같은 이름의 메서드가 다른 동작을 한다는 개념 (덮어쓰기)
# 4. 캡슐화 - 엑세스 권한 
#               -@property
#               -@변수.setter

# 2. 파이썬의 예외처리 ( 에러 처리 )


# 상속의 예시
# 아래와같이 클래스두개를 짜면 중복되는 부분이 생김.
# 이럴 경우 클래스간 상속을 이용하여 만들어 주는 편이 낫다.
class Goblen:
    def __init__(self,hp):
        self.hp = hp
    
    def attack(self):
        print('몽둥이를 휘두른다')

    def avoid(self):
        print('공격을 회피한다')

    
class Stone_Goblen:
    def __init__(self,hp):
        self.hp = hp

    def attack(self):
        print('돌을 던진다')

    def avoid(self):
        print('공격을 회피했다')


# 상속을 이용한 경우 를 보자

class Goblen:
    def __init__(self,hp):
        self.hp = hp
    
    def attack(self):
        print('몽둥이를 휘두른다')

    def avoid(self):
        print('공격을 회피한다')

    
class Stone_Goblen(Goblen):
    # 부모와 다른 동작을 하는 메서드(재정의 - 오버라이딩)
    def __init__(self,hp):
        self.hp = hp

    # 부모와 완전히 동일한 동작을 하는 메서드 - 생략가능
    # def attack(self):
    #     print('돌을 던진다')

    # def avoid(self):
    #     print('공격을 회피했다')

