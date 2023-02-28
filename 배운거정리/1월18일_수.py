# def func1():
#     x = 10

#     def func2():
#         nonlocal x

#         x = 20

#     func2()
#     print(x)

# func1()
# print(x)  # 글로벌스콥에서 x가 없기 때문에 에러가 남.


# 상위 scope에 있는 변수를 수정하고 싶다면 global, nonlocal등을 쓸 수 있지만 쓰지 않는 것을 추천.


li = [1,2,3]
li2= li
li2[0] = 10

def func():
    li = [4,5,6]

func()
print(li)

# Call by Reference vs Call by Value
# Call by Value


# 오후 시작 

# 찜닭

# foods = ['찜닭','김치','콩자반','계란후라이']

# '''
# def 식별자(파라미터):
#     ''''''
#     특정 동잦ㄱ
# '''

# def eat_food(food):
#     '''
#     파라미터로 음식 종류를 받아, "먹는다"를 표현하는 함수
#     '''

# for food in foods:
#     print('수저를 집는다')
#     print(f'{food}을 입에 넣는다')
#     print('냠냠')

#     # 물을 마신다
#     print('뚜껑을 딴다')
#     print('물을 마신다')
#     print('꿀꺽')
#     # 후식을 먹는다

#     # 음료수를 먹는다

# eat_food()

# def have_a_drink():
#     """
#     음료수를 파라미터로 받아, '마신다'를 표현하는 함수
#     """
    
# # 같은 기능을 중복적으로 하는 코드를 

# # 재사용성 = 다시 사용할 수 있는 성질, 쉽게말해서 파라미터 만들어라

# def eat(pre_action, anything, after_action):
#     """
#     무언가를 먹는 것을 표현하는 함수
#     pre_action: 입에 넣기 전 사저농작
    
#     """
#     print(pre_action)
#     print(f'{anything}을 입에 넣는다')
#     print(after_action)

# 입맛이 독특해서 음식을 

# Namespace

# 이름에 따라 구분할 수 있는 범위를 의미

# Local 
# Enclosed
# Global
# Bulit-in

# Global -> (하나의 file)
a= 10


# 예시 1 
# Enclosed
def func():
    a=20

    # Local
    def func2():
        a=30

    func2()

print(a)
func()


# 예시 2
x=0

def func1():
    x=10

    def func2():
        x=20
        print(x)
    func2()
    print(x)


print(x)
func1()

# 0 
# 20
# 10 


# global , nonlocal

# 밖의 영역에서 변수를 가져오 수정하고 싶을 때 쓰는 키워드
#   global, nonlocal(global은 안됨)
def func1():
    global x
    x +=1

    y = 20

count = 0

def func2():
    global count
    print('함수 호출됨')
    count += 1

for _ in range(5):
    func()

print(count)

# nonlocal = 자기 scope말고 바로 한 단계 위 scope의 변수를 불러옴
# global = 이거는 무조건 global scope에 있는 변수 불러오는거

def func1():
    x=10

    def func2():
        x=20

        def func3():
            nonlocal x   # 한단계위에서 x를 불러옴 즉 x=20
            x+=10        # x=30
            print(x)     # x=30

        func3()
        print(x)         # 여기서 주의. func2본문의 x를 func3에서 불러서 30으로 만들었기 때문에
                         # 얘도 30임
    func2()
    print(x)             # 얘는 10임 왜냐면 이 scope에있는 x는 값이 변동된 적이 없음.

func1()