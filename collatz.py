number=int(input("Please, enter a positive integer: "))
while number != 1:
        if (number%2)>0:
             number =((3 * number) + 1)
             print(number)
        else:
            number = (number / 2)
            print(number)

print("End of sekvence.")