import sys

try:
    with open (sys.argv[1]) as f:        
        file=f.read()
        x=file.count('e')
        y=file.count('E')
        z=x+y          
    print(z)
except FileNotFoundError :
    print("File not found. Please, enter a valid file name.")
except IndexError:
    print("No file name. Please, enter a filename.")
except ValueError:
    print("No text file.")

        
   
