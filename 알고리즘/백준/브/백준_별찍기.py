# 1.

# N= int(input())
# for _ in range (N):
#     for i in range(_):
#         print(' ',end='')

#     for i in range(N-_):
#         print('*',end='')

#     print('')


# 2. 

# N = int(input())
# for i in range(N):
#     #각줄에서
#     for _ in range(N-i-1):
#         print(' ',end='')
#     for _ in range(2*i+1):
#         print('*',end='')

#     print('')
        
#     *
#    ***
#   *****
#  *******
# *********

# 3.
# N=int(input())
# for i in range(N):
#     for _ in range(i):
#         print(' ',end='')
#     for _ in range(2*N-1-2*i):
#         print('*',end='')
#     print('')

# *********
#  *******
#   *****
#    ***
#     *


# 4
# N= int(input())
# for i in range(N):
#     for _ in range(N-i-1):
#         print(' ',end='')
#     for _ in range(2*i+1):
#         print('*',end='')
#     print('')
# for i in range(N-1):
#     for _ in range(i+1):
#         print(' ',end='')
#     for _ in range(2*N-1-2*(i+1)):
#         print('*',end='')
#     print('')


#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *


# 5

# N = int(input())
# for i in range(N):
#     for _ in range(i+1):
#         print('*',end='')
#     for _ in range(2*N-2*(i+1)):
#         print(' ',end='')
#     for _ in range(i+1):
#         print('*',end='')
#     print('')
# for i in range(N-1):
#     for _ in range(N-1-i):
#         print('*',end='')
#     for _ in range(2*(i+1)):
#         print(' ',end='')
#     for _ in range(N-1-i):
#         print('*',end='')
#     print('')

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


# 6

N=int(input())
for i in range(N):
    for _ in range(i):
        print(' ',end='')
    for _ in range(2*N-1-i*2):
        print('*',end='')
    print('')

for i in range(N-1):
    for _ in range(N-2-i):
        print(' ',end='')
    for _ in range(2*(i+1)+1):
        print('*',end='')
    print('')

# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********