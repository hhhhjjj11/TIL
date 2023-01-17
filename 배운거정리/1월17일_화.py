import random

# 가위바위보 게임 틀 구현

# 필요한 변수 선언 (가위바위보 리스트, 유저/컴퓨터 승 카운트, 판 수)
li = ['가위', '바위', '보']
computer_win_count = 0
user_win_count = 0
draw=0
game = 1
# 반복문 

# 종료하기를 입력하거나, 5판을 하기전까지 무한반복 
while game<=5:
    menu = int(input('메뉴를 입력하세요: (1: 게임하기, 2:종료하기): '))
    # 게임하기   
    if menu == 1:
        print(f'-------------------게임시작----------------------')
        for _ in range(5):
            print(f'---------------------게임 {game}----------------------')
            user=input(f'{li}: ')
            computer=random.choice(li)
            print(f'user: {user}, computer: {computer}')
            if (computer=='보' and user=='바위') or (computer=='바위' and user=='가위') or (computer=='가위' and user=='보'):
                computer_win_count+=1
            elif computer==user:
                draw+=1
            else :
                user_win_count+=1
            print(f'컴퓨터 : {computer_win_count}, 유저 : {user_win_count}, 무승부 : {draw}')
            game+=1

    # 종료하기
    elif menu == 2:
        print('프로그램을 종료합니다')
        break
    # 잘못된 입력 - 안내문 표시 후 다시 반복
    else:
        print('잘못된 입력입니다. 입력을 확인해주세요')

print('-----------------게임이끝났습니다.---------------')
if computer_win_count>user_win_count:
    print('--------------게임결과 : 컴퓨터 승--------------- ')
elif computer_win_count<user_win_count:
    print('----------------게임결과 : 유저 승--------------- ')
else:
    print('----------------게임결과 : 무승부---------------- ')
