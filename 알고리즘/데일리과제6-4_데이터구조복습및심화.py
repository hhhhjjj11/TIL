li=input()   #['eat','tea','tan','ate','nat','bat']
length=len(li)  # 6
reslist=[]      
list3=[]
def count(my_list):
    count={}

    for item in my_list:
        count[item]=count.get(item,0)+1
    
    return count

for i in range(length):              # 0~5
    #list(li[i])                      # ['e','a','t']
    list3.append(count(list(li[i])))        # { e:1 , a:1, t:1}

# list = [{ }, { }, { }, { }, { }, { }]
임시리스트=[list3[0]]
for i in range(length):
    if list3[0]==list3[i]:
        임시리스트.append(list[i])
        list3[i]=0  # 임시리스트=[{eat},{tea},{}]
    reslist.append(임시리스트)
    임시리스트=[]
    print(reslist)
    # if list[1] == list[i+1]:
    #     if list[1]=='해결':
    #         continue
    #     reslist.append(임시리스트)
