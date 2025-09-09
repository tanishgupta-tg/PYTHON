# ==========================================================
# Python Practice Programs (Q1 - Q53)
# With Full Questions + Author info
# ==========================================================

# Q1. Write python code to print hello world.
print("\nQ1:")
print("Hello, World!")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q2. Write python code to demonstrate valid and invalid identifier.
print("\nQ2:")
name = "Alice"
age = 20
_roll_no = 101
print(name, age, _roll_no)
# Invalid examples: 1name, class, roll no (keywords / invalid usage)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q3. Write python code to demonstrate Keywords.
print("\nQ3:")
import keyword
print("Python Keywords:", keyword.kwlist)
print("Total Keywords:", len(keyword.kwlist))
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q4. Write python code to demonstrate indentation.
print("\nQ4:")
x = 10
if x > 5:
    print("x is greater than 5")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q5. Write a python code to demonstrate various types of comments.
print("\nQ5:")
# Single-line comment
"""
This is a multi-line comment written with triple quotes
"""
'''
Another style of multi-line comment
'''
print("Comments demonstrated.")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q6. Write python code to demonstrate input method.
print("\nQ6:")
'''name = input("Enter your name: ")
age = int(input("Enter your age: "))
#print(f"Hello {name}, you are {age} years old.")'''
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q7. Write python code to demonstrate datatypes and variables.
print("\nQ7:")
a=10; b=3.14; c="Python"; d=True
e=[1,2,3]; f=(1,2,3); g={1,2,3}; h={"a":1}
print(type(a),type(b),type(c),type(d),type(e),type(f),type(g),type(h))
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q8. Write python code to demonstrate binary datatypes.
print("\nQ8:")
x = 0b1010
print("Binary literal 0b1010 =", x)
print("Binary of 15 =", bin(15))
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q9. Write python code to demonstrate some of core objects and functions.
print("\nQ9:")
print("len:", len("Python"))
print("max:", max([1,5,3]))
print("min:", min([1,5,3]))
print("abs:", abs(-7))
print("sum:", sum([1,2,3]))
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q10. Write python code to swap value of two variables using all possible ways.
print("\nQ10:")
a, b = 5, 10
print("Before:", a, b)
# Method 1: Temporary variable
temp=a; a=b; b=temp
print("After temp:", a, b)
# Method 2: Tuple unpacking
a, b = b, a
print("After tuple unpacking:", a, b)
# Method 3: Arithmetic operations
a=a+b; b=a-b; a=a-b
print("After arithmetic:", a, b)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q11. Write python code to swap value of three variables using all possible ways.
print("\nQ11:")
a,b,c=1,2,3
print("Before:",a,b,c)
a,b,c=c,a,b
print("After swap:",a,b,c)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q12. Write python code to input name, class, roll no, age and print using formatted print method.
print("\nQ12:")
'''name=input("Enter name: ")
cls=input("Enter class: ")
roll=int(input("Enter roll no: "))
age=int(input("Enter age: "))
print(f"Name:{name}, Class:{cls}, Roll:{roll}, Age:{age}")'''
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q13. Write python code to calculate your age on given date.
print("\nQ13:")
from datetime import date
dob = date(2000,5,20)
given_date = date(2025,8,23)
age= given_date.year-dob.year - ((given_date.month,given_date.day)<(dob.month,dob.day))
print("Age on given date:", age)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q14. Write python code to check whether given year is Leap year or not.
print("\nQ14:")
year = 2024
print("Leap" if (year%4==0 and year%100!=0) or (year%400==0) else "Not Leap")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q15. Write python code to check whether the given number is perfect number or not.
print("\nQ15:")
n=28
print("Perfect" if sum([i for i in range(1,n) if n%i==0])==n else "Not Perfect")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q16. Write python code to check whether the given number is Armstrong number or not.
print("\nQ16:")
n=153
s=sum(int(d)**len(str(n)) for d in str(n))
print("Armstrong" if s==n else "Not Armstrong")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q17. Write python code to check whether the given number is prime or not.
print("\nQ17:")
n=29
print("Prime" if n>1 and all(n%i for i in range(2,int(n**0.5)+1)) else "Not Prime")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q18. Write python code to print all prime, all perfect and all Armstrong number in a given range.
print("\nQ18:")
def is_prime(n): return n>1 and all(n%i for i in range(2,int(n**0.5)+1))
def is_perfect(n): return n==sum(i for i in range(1,n) if n%i==0)
def is_armstrong(n): return n==sum(int(d)**len(str(n)) for d in str(n))
start,end=1,500
print("Primes:",[n for n in range(start,end) if is_prime(n)])
print("Perfect:",[n for n in range(start,end) if is_perfect(n)])
print("Armstrong:",[n for n in range(start,end) if is_armstrong(n)])
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q19. Write python code to print all the leap years from year 1-2025. Also print the total count.
print("\nQ19:")
leaps=[y for y in range(1,2026) if (y%4==0 and y%100!=0) or (y%400==0)]
print(leaps)
print("Total:",len(leaps))
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q20. Write python code to print all the perfect numbers from 1-2025. Also print the total count.
print("\nQ20:")
perfects=[n for n in range(1,2026) if is_perfect(n)]
print(perfects,"Total:",len(perfects))
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q21. Write python code to demonstrate for statement.
print("\nQ21:")
for i in range(5): print(i)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q22. Write python code to demonstrate nested for loop statement.
print("\nQ22:")
for i in range(3):
    for j in range(3):
        print(i,j)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q23. Write python code to demonstrate list comprehensions.
print("\nQ23:")
print([i*i for i in range(10)])
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q24. Write python code to demonstrate index and value enumeration.
print("\nQ24:")
lst=["a","b","c"]
for idx,val in enumerate(lst): print(idx,val)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q25. Write python code to print the following pattern.
print("\nQ25:")
for i in range(1,6): print("*"*i)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q26: Demonstrate multiple inputs separated by spaces

# Take multiple inputs separated by spaces
#inputs = input("Enter multiple values separated by spaces: ").split()

# The inputs list contains strings, print them as is
#print("Input values as strings:", inputs)

# Convert inputs to integers if possible
#int_inputs = list(map(int, inputs))

#print("Input values as integers:", int_inputs)

# Demonstrate accessing individual inputs
#for i, val in enumerate(int_inputs, start=1):
 #   print(f"Input {i}: {val}")

print("This program is executed by Tanish Gupta (0231BCA061)")

# Q27. Write a python code to demonstrate multiple inputs in a list.
print("\nQ27:")
# nums=list(map(int,input("Enter numbers: ").split()))
# print(nums)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q28. Write a python code to demonstrate multiple inputs separated by commas.
print("\nQ28:")
# a,b,c = input("Enter comma values: ").split(",")
# print(a,b,c)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q29. WAP in python to print last digit of a given integer number.
print("\nQ29:")
n=456
print("Last digit:",n%10)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q30. Write a python code to calculate income tax as per given rules.
print("\nQ30:")
income=800000
if income<=250000: tax=0
elif income<=500000: tax=0.05*(income-250000)
elif income<=1000000: tax=0.10*(income-500000)+12500
elif income<=2000000: tax=0.20*(income-1000000)+62500
elif income<=3000000: tax=0.30*(income-2000000)+262500
else: tax=0.40*(income-3000000)+562500
print("Income:",income,"Tax:",tax)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q31. Write a python code to demonstrate continue statement with for loop.
print("\nQ31:")
for i in range(10):
    if i%2==0: continue
    print(i)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q32. Write a python code to demonstrate while loop.
print("\nQ32:")
i=1
while i<=5:
    print(i); i+=1
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q33. Write a python code to demonstrate while string.
print("\nQ33:")
s="Python"; i=0
while i<len(s):
    print(s[i]); i+=1
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q34. Write a python code to demonstrate continue statement with while loop.
print("\nQ34:")
i=0
while i<10:
    i+=1
    if i%2==0: continue
    print(i)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q35. Write a python code to demonstrate break statement with for loop.
print("\nQ35:")
for i in range(10):
    if i==5: break
    print(i)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q36. Write a python code to demonstrate break statement with while loop.
print("\nQ36:")
i=0
while i<10:
    if i==5: break
    print(i); i+=1
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q37. Write a python code to demonstrate try and except.
print("\nQ37:")
try: x=int("abc")
except ValueError: print("Invalid conversion")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q38. Write a python code to demonstrate try and except and else.
print("\nQ38:")
try: x=int("123")
except ValueError: print("Error")
else: print("Success:",x)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q39. Write a python code to demonstrate try and except and finally.
print("\nQ39:")
try: x=int("abc")
except ValueError: print("Error")
finally: print("This always executes")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q40. Write a python code to demonstrate try, except, else and finally.
print("\nQ40:")
try: x=int("123")
except ValueError: print("Error")
else: print("Success:",x)
finally: print("Finished")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q41: Read content of a file using try, except and finally
print("\nQ41:")
filename = "example.txt"  # Specify your file name

try:
    f = open(filename, "r")
    content = f.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print("The specified file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    try:
        f.close()
        print("File closed successfully.")
    except:
        print("File was not opened, so cannot be closed.")
print("This program is executed by Tanish Gupta (0231BCA061)")        

#Q42 write pyhton code to create & modify a list
print("\nQ42:")
my_list= [1,2,3,4,5]
my_list.append(6)
my_list.insert(2,2.5)
print(my_list)
print("This program is executed by Tanish Gupta (0231BCA061)")

#Q42 write pyhton code to create & modify a list
print("\nQ42:")
my_list= [1,2,3,4,5]
my_list.append(6)
my_list.insert(2,2.5)
my_list.remove(4)
print(my_list)
print("This program is executed by Tanish Gupta (0231BCA061)")

#Q43 write python code to demonstrate slicing of the list
print("\nQ43:")
first = my_list[0]
last= my_list[-1]
sub=my_list[1:4]
print('first element',first)
print('last element',last)
print('sliced list',sub)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q44: Use list comprehensions
print("\nQ44:")
# Create a list of squares of numbers 0 to 9
squares = [x ** 2 for x in range(10)]
print("Squares:", squares)

# Create a list of even numbers from 0 to 19
evens = [x for x in range(20) if x % 2 == 0]
print("Even numbers:", evens)

# Create a list of uppercase letters from a given list
letters = ['a', 'b', 'c', 'd']
upper_letters = [ch.upper() for ch in letters]
print("Uppercase letters:", upper_letters)
print("This program is executed by Tanish Gupta (0231BCA061)")

#Q45 write python code to create & access truple
print("\nQ45:")
mytuple=(1,2,3,4)
print(mytuple[0])
print(mytuple[-1])
print("This program is executed by Tanish Gupta (0231BCA061)")

#Q46 write python code to create & access nested truple
print("\nQ46:")
nested=(1,(2,3),4)
print(nested[1][0])
print("This program is executed by Tanish Gupta (0231BCA061)")

#Q47 write python code to demonstrate set operations
print("\nQ47:")
set1={1,2,3}
set2={3,4,5}
union=set1|set2
intersection=set1&set2
defference= set1-set2
print(union)
print(intersection)
print(defference)
print("This program is executed by Tanish Gupta (0231BCA061)")

#Q48 write python code to create and modify a dictionary
print("\nQ48:")
mydict={'name':'Alce','age':25}
mydict['age']=26
mydict['city']='new york'
print(mydict)
print("This program is executed by Tanish Gupta (0231BCA061)")

#Q49 write python code to access and remove dictionary elements
print("\nQ49:")
mydict= {'name':'bob','age':30,'job':'engineer'}
name=mydict.get('name')
mydict.pop('name')
print(name)
print(mydict)
print("This program is executed by Tanish Gupta (0231BCA061)")

#Q50 write python code to iterate through dictionary items
print("\nQ50:")
mydict={'a':1,'b':2,'c':3}
for key, value in mydict.items():
    print(f'{key}:{value}')
print("This program is executed by Tanish Gupta (0231BCA061)")

#Q51 wirte python code to use built-in iterators
print("\nQ51:")
mylist=[1,2,3,4]
it=iter(mylist)
print(next(it))
print(next(it))
print("This program is executed by Tanish Gupta (0231BCA061)")

#Q52 wirte pyhton code to use iterator in a loop
print("\nQ52:")
mylist=[1,2,3,4]
it=iter(mylist)
for item in it:
    print(item)
print("This program is executed by Tanish Gupta (0231BCA061)")

#Q53 wirte python code to create and use custom iterators
print("\nQ53:")
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

rev = Reverse('giraffe')
for char in rev:
    print(char)
print("This program is executed by Tanish Gupta (0231BCA061)")

