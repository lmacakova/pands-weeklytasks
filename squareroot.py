

x=float(input("Enter a number: "))
min1=0
max1=x
for i in range(10):
    mid=(min1+max1)/2  #middle value
    res=mid**2       #finding the square of middle value
    if res==x:       #if the middle value is square root program break here
        break        
    elif res>x:      #if the square value of the middle value is more than x then we need to take max value as middle 
    max1=mid
    else:                  #if the square value of the middle value is less than x then we need to take min  value as middle 
    min1=mid
midR=round(mid, 2)gspdreg.galwaymayo@atu.ie
print(midR)