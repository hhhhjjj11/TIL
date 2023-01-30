# ## 객체지향

# ### self
# - 인스턴스 자기자신
# - 

# class Person:
#     def talk(self):
#         print('안녕')

#     def eat(self, food):
#         print(f'{food}를 냠냠')

# person1 = Person()
# person1.talk() 
# person1.eat('피자') 
# person1.eat('치킨')

# class Person:
#     def __init__(self) :
#         print('생성될 때 자동으로 불려요')

# aiden = Person()
# aiden = Person()

# class Person:
#     count=0

#     def __init__(self,name):
#         self.name = name
#         Person.count+=1

#     @classmethod
#     def number_of_populaton(cls):
#         print(f'인구수는 {cls.count}입니다')

# person1 = Person('아이유')
# person2 = Person('이찬혁')


# Person.number_of_populaton()
# person1.number_of_population()
