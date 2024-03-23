import pandas as pd
d= input("Enter the date in form of YYYY-MM-DD: ")
date = pd.to_datetime(d)
print(date.day_name())
if date.day_name() in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")