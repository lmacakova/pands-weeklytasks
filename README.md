# pands-weeklytasks
## Author: Lucia Macakova
My solutions to the weekly tasks as a student of the program Higher Diploma in Science in Data Analytics, in the module Programming and Scripting:
1. First week: helloworld.py. 
Instructions: To make a python program that displays Hello World! when it is run.
Solution: Print () function [^1] with a message between quotation marks.

2. Second week: bank.py. 
Instructions: 
a) Prompt the user and read in two money amounts (in cents)
b) Add the two amounts
c) Print out the answer in a human-readable format with a euro sign and decimal point between the euro and the cent of the amount.
Solution: Input() function [^1] converting values to integer data types for inputting two amounts in euro cents, add two amounts together and divide the result by 100. Output is printed with print(f'The sum of these is €{newNumber}').

3. Third week: accounts.py
Instructions: Write a python program called accounts.py that reads in a 10-character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
Solution: Input() with the proper message that converts inserted data into strings. Modifying output in print() to cover the first 6 signs of string as Xs and show only the last 4 signs.

4. Fourth week: collatz.py
Instructions: Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.
Solution:  Input() converting data to integer values with the proper message, inputted value is printed by print(). Collatz sequence created and printed by while/if/else loop [^2] finished by 'end' message. Values of sequence are separated by end="" parameter in print().

5. Fifth week: weekday.py
Instructions: Write a program that outputs whether or not today is a weekday.
Solution: Pandas imported as pd. Input that takes string values with proper message. This string is transformed to pandas datetime object by pandas.to_datetime() function [^3]. Datetime object is modified by day_name() method [^4]to the day of the week. If/else statements [^5] that print the message "Yes, unfortunately, today is a weekday." if the date is workday or message "It is the weekend, yay!" if the date is Saturday or Sunday.

6. Sixth week: squareroot.py
Instructions: Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. Create your own sqrt function and do not use the built-in functions x ** .5 or math.sqrt(x).
Solution: Newton method [^6]. First to define function squareroot(n) function with variables a and b., a=0.5*n, b=0.5*(a+n/a). While loop with condition b!=a. If this condition is true, a=b and b=0.5*(a+n/a), and again, till b=a, when value a rounded with round() [^7] to the first decimal number will be returned. Then, Input() converts values as float numbers,  function squareroot() for inserted value, and print(f"The square root of {number} is approx. {squareroot(number)}").

7. Seventh week: es.py
Instructions: Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line. 

Solution: Module sys imported. Try block and except blocks for error handling which can print proper messages [^8]. In try block is the function open() for manipulation with files, that takes the whole file as an argument f with sys.argv[1] [^9]. Variables: file with f.read() [^10], x with file.count('e'), y with file.count('E') [^11] and z with x+y. Try block is finished with print(z) command. The file snow-white.txt is for testing es.py.          

8. Eighth week: plottask.py
Instructions: Write a program called plottask.py that displays:
a) A histogram of a normal distribution of the 1000 values with a mean of 5 and standard deviation of 2. 
b) A plot of the function  h(x)=x3 in the range 0 to 10.
Solution: To import matplotlib.pyplot as plt and numpy as np. Function h(n) which returns n**3. X array with np.arange() [^12] within the proper interval, y array with h(x), and normalThousand array with np.random.normal() [^13]. Histogram for normalThousand and plot for y. 


### Resources
[^1]: https://docs.python.org/3/library/functions.html
[^2]: https://www.w3schools.com/python/python_while_loops.asp
[^3]: https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html
[^4]: https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day_name.html
[^5]: https://www.w3schools.com/python/python_conditions.asp
[^6]: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
[^7]: https://www.w3schools.com/python/ref_func_round.asp
[^8]: https://www.w3schools.com/python/python_try_except.asp
[^9]: https://docs.python.org/3/library/sys.html
[^10]:https://www.w3schools.com/python/ref_file_read.asp
[^11]:https://www.w3schools.com/python/ref_list_count.asp
[^12]:https://numpy.org/doc/stable/reference/generated/numpy.arange.html
[^13]:https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_normal.html

