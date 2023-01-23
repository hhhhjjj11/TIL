T = int(input())

credits=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

for t in range(1,T+1):
    scores=[]
    N, K = map(int,input().split())
    for _ in range(N):
        A, B, C = map(int,input().split())
        score = A * (0.35) + B * (0.45) + C * (0.2)
        scores.append(score)
    
    # scores=[ 점수들.. ]
    srtd_scores=sorted(scores,reverse=True)
    # 디버깅, print(scores)
    # 디버깅, print(srtd_scores)
    scr_K=scores[K-1]
    기준 = int(N/10)
    for item in srtd_scores:
        if scr_K==item:
            index_K=int(srtd_scores.index(item))
            break
    print(f'#{t} {credits[index_K//기준]}')