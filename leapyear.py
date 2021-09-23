year=int(input())
if(year%4==0 and year%100!=0):
    print("hey leap year dude")
elif(year%100==0 and year%400==0):
    print("hey leap year dude")
else:
    print("oh no its not a leap year")
