# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    """
    먼저 아스키 표를 참고하여 대문자리스트bigs와 소문자리스트smalls를 만들고
    chr메서드와 ord메서드를 활용하여 n만큼 뒤에 있는 배열의 항을 불러온다.
    이때 조건문을 이용하여 입력된 단어의 철자가 대문자라면 bigs에서, 소문자라면 smalls에서
    각각 처리하도록 한다.
    """
    bigs =[]
    smalls=[]
    for i in range(65,91):
        bigs.append(chr(i))
    for i in range(97,123):
        smalls.append(chr(i))
    inputs= list(word)
    for i in range(len(inputs)):
        if inputs[i].islower()==True:
            inputs[i]=smalls[(ord(inputs[i])-97+n)%26]  # 102 % 26 = 24
        else:
            inputs[i]=bigs[(ord(inputs[i])-65+n)%26]  # 102 % 26 = 24
    return ''.join(inputs)

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
