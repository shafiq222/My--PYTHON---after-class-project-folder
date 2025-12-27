number = int(input("enter a nubmer"))
power=int(input("enter a power"))



result=1

for i in range(power):
    result=result * number

print("Result",result)