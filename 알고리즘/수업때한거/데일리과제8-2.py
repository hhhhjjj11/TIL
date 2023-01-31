class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
class Rectangle():
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.가로 = abs(p1.x-p2.x)
        self.세로 = abs(p1.y-p2.y)

    def get_area(self):
        return self.세로*self.가로

    def get_perimeter(self):
        return 2*(self.가로+self.세로)

    def is_square(self):
        if self.세로 == self.가로 :
            return True
        else:
            return False


    # a 변수는 str 타입으로 받는다.
    # 이 메소드는 int 타입의 데이터를 반환한다.
    # 라는 내용의 annotation임
    # 파라미터의 경우는 콜론 찍고 타입써주고
    # 리턴의 경우 콜론전에 화살표랑 타입써주고
    def func(self, a: str) -> int:
        print(a)


# 입력 예시
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())
