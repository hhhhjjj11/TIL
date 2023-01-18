def anagrams(li):

    result = {}

    for words in li:
        anag = ''.join(sorted(words))
        result[anag] = result.get(anag,[]) + [words]
        ''' 
        sorted 함수를 사용하여 단어 구성요소를 정렬시키고, 
        '구분자'.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 
        'abc'의 문자열로 합쳐서 반환하는 특성을 활용하여 도출한 결과값을 
        새로운 dict인 'result'의 'key'값으로 설정해주고, 원래의 단어들을 각 key 값의
        values로 추가해주면 됨. 

        '''

    print(list(result.values()))

li = ['eat','tea','tan','ate','nat','bat']
anagrams(li)

# 빈 객체를 만들고
# 입력배열의 각 아이템들을 재배열