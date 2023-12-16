num = int(input("enter any number: "))

f= 0

for i in range(1, num):
    if num ==( i* (i+1)):
        f=1
        break
if f==1:
    print("pronic")
else:
    print("not pronic")