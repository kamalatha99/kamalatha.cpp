l=[]
n=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    l.append([name,score])
    n.append(score)
n=sorted(list(set(n)))
maxi=n[1]
names=[]
for value in l:
    if maxi==value[1]:
       names.append(value[0])
names.sort()
for i in names: 
    print(i)
        

    
