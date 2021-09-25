roll=set(map(int,input().split()))
roll2=set(map(int,input().split()))
common=roll2.intersection(roll)
print(len(common))
