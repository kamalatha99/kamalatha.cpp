n=int(input())
dic={}
for i in range(n):
    name,*line=input().split()#kammi 12.2 13.3 14.2 takes input in this format
    #print(name,line) means......kammi ['12.2', '13.3', '14.2']
    marks=list(map(float,line))
    #print(marks)means....[12.0, 12.2, 13.2]
    print(dic)
    dic[name]=marks
    #print(dic).......{'kammi': [1.2, 2.23, 3.0]}
query_name=input()
values=dic[query_name]
print(format(sum(values)%3,'.2f'))
