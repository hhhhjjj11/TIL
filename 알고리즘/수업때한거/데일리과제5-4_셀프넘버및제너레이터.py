n=int(input())

def fn_d(n):
    n_str = str(n)
    li = list(n_str)
    sum=0
    for item in li:
        sum += int(item)
    result = sum + n
    return result


def is_selfnumber(n):
    """
    1~n까지 중의 자연수i 중에서 fn(i)==n이라면 i가 n의 제너레이터이므로 false반환
    없다며 제너레이터가 없으므로 true반환
    n보다 큰 경우는 따질 필요 없음 n의 제너레이터가 될 수 없으므로 따질 필요 없음.
    """
    for i in range(1,n+1):
        if fn_d(i) == n:
            return False
    return True

print('fn_d(n)',fn_d(n))
print('is_selfnumnber(n)',is_selfnumber(n))