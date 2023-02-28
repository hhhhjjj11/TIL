# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if len(numbers) == 0 : 
        return 0
    elif len(numbers)==1:
        return (numbers[0]**2) * 3.14
    elif len(numbers)==2 :
        a = int(numbers[0])
        b = int(numbers[1])
        if (a+b)%2 == 1 :
            return a*b*(0.5)
        elif (a+b)%2 == 0 :
            return a*b
    elif len(numbers)>=3 :
        total = sum(numbers)
        avg = total/(len(numbers))
        return(total,avg)


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0