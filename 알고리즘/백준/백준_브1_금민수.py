N = input()
import sys
sys.setrecursionlimit(10**6)

def isKMN(N):
   
    if int(N)<4 :
        return False
    if  N.count('4')+N.count('7') == len(N):
        print(N)
        return 
    else:
        isKMN(str(int(N)-1))

isKMN(N)