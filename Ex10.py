'''

'''
num = int(input("Enter an integer positive number: "))

#Obligamos que el numero sea positivo
while num < 0:
    print("The number is not valid, try again.")
    num = int(input("Enter an integer positive number: "))
if num == 0 or num == 1:
    print("the factorial is 1")

#Realizamos la operación para sacer el factorial.
result = num
mult = num
for i in range(1,num):
    mult -=1
    result = result * mult
print("The factorial is", result)