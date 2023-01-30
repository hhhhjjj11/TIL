class Doggy():
    
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self, name, kind, sound) :
        self.name=name
        self.kind=kind
        self.sound=sound
        Doggy.birth_of_dogs+=1
        Doggy.num_of_dogs+=1

    def bark(self):
        print(f'{self.name}는 \"{self.sound}\" 하고 짖습니다!')
    
    def die(self):
        print(f'{self.name}가 고양이별로 떠났습니다 ㅠ')
        Doggy.num_of_dogs-=1

    
    @classmethod
    def get_status(cls):
        print(f'태어난 강아지의 수 : {cls.birth_of_dogs}, 총 강아지의 수 : {cls.num_of_dogs}')


    def __str__(self):
        return f'이름 : {self.name}, 종 : {self.kind}, 울음소리 : {self.sound}'





dog1=Doggy('까까','코리안숏헤어','먀옹~')
dog2=Doggy('쿠키','러시안블루','먀~')
dog3=Doggy('미지의고양이','먼치킨','냥!')
print(dog1)
print(dog2)
print(dog3)
Doggy.get_status()
dog1.bark()
dog3.die()