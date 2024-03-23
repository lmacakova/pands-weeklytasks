number=int(input("Please, enter a positive integer: "))
print(number, end=" ")

while number != 1:
        if (number%2)>0:
             number =((3 * number) + 1)
             print(number, end=" ")
             
        else:
            number = (number // 2)
            print(number, end=" ")
print("end")





