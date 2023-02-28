끝내기=0
words=[]
while 끝내기==0:
    word = input('다음단어:')
    if word=='done':
        끝내기=1
        print('done이 입력되어 끝말잇기를 종료합니다.')
    words.append(word)
    print(words)
    N=len(words)
    틀린사람없음=1
    for i in range (1,N):
        앞=list(words[i-1])
        뒤=list(words[i])
        if 앞[-1] != 뒤[0]:
            print(f'{i+1}번째 사람이 틀렸습니다.')
            끝내기=1
