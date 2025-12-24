# ==========================================================
# Python Practice Programs (Q1 - Q89)
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

# Q54: Write python code to demonstrate string functions
print("\nQ54:")
text = 'hello, world!'
print(text.lower())
print(text.upper())
print(text.title())
print(text.strip())
print(text.replace('world','python'))
print(text.find('world'))
print(text.count('o'))
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q55: Write python code to create menu based calculator
print("\nQ55:")
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

while True:
    print("\nMENU:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator.")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid choice! Please select a valid option.")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q56: Write python code to calculate factorial of the given number using function
print("\nQ56:")
def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q57: Write python code to print Armstrong numbers in a given range
print("\nQ57:")
start = int(input("Enter start value: "))
end = int(input("Enter end value: "))

for num in range(start, end + 1):
    sum = 0
    temp = num
    n = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
    if num == sum:
        print(num)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q58: Write python code to demonstrate decorators with argument.
print("\nQ58:")
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q59: Write python code to demonstrate decorator using functools.wraps
print("\nQ59:")
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper():
        print("Something is happening before function is called ")
        func()
        print("Something is happening after function is called")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q60: Write python code to show use of decorators to add logging to functions
print("\nQ60:")
def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} ended")
        return result
    return wrapper

@log_decorator
def multiply(x, y):
    return x * y

print(multiply(5, 6))
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q61: Write python code to print addition, subtraction, multiplication and transpose of two 3x3 matrices
print("\nQ61:")
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]

def matrix_add(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

def matrix_subtract(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

def matrix_multiply(X, Y):
    result = [[0]*len(Y[0]) for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

def matrix_transpose(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

print("Addition:")
for row in matrix_add(A, B):
    print(row)

print("Subtraction:")
for row in matrix_subtract(A, B):
    print(row)

print("Multiplication:")
for row in matrix_multiply(A, B):
    print(row)

print("Transpose of A:")
for row in matrix_transpose(A):
    print(row)

print("This program is executed by Tanish Gupta (0231BCA061)")

# Q62. Write python code to calculate factorial of a given number using recursive function.
print("\n62:")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
num = int(input("Enter a number to find factorial: "))
print(f"Factorial of {num} is {factorial(num)}")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q63. Write a python code to chain generators
print("\n63:")
def generator1():
    for i in range(1, 4):
        yield i

def generator2():
    for j in range(4, 7):
        yield j

def chain_generators(gen1, gen2):
    yield from gen1()
    yield from gen2()

for value in chain_generators(generator1, generator2):
    print(value, end=" ")
print()
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q64. Write python code to print Fibonacci series up to given input number using both simple function (non-recursive) and recursive function.
print("\n64:")
def fib_non_recursive(n):
    a, b = 0, 1
    fib_series = []
    while a <= n:
        fib_series.append(a)
        a, b = b, a+b
    return fib_series

def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

n = int(input("Enter the limit for Fibonacci series: "))
print("Non-recursive Fibonacci series:")
print(fib_non_recursive(n))

print("Recursive Fibonacci series up to n terms:")
for i in range(n):
    print(fib_recursive(i), end=" ")
print()
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q65. Write python code to demonstrate global variable.
print("\n65:")
x = 100

def global_var_demo():
    global x
    x = x + 50
    print(f"Inside function, x = {x}")

print(f"Before function call, x = {x}")
global_var_demo()
print(f"After function call, x = {x}")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q66. Python code to demonstrate a function.
print("\n66:")
def greet():
    print("Hello, welcome to the function demonstration!")

greet()
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q67. Write python code to demonstrate function with return.
print("\n67:")
def add(a, b):
    return a + b

result = add(5, 3)
print(f"Sum of 5 and 3 is {result}")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q68. Write python code to demonstrate function with default parameter.
print("\n68:")
def greet(name="User"):
    print(f"Hello, {name}!")

greet()
greet("Rakshit")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q69. Write python code to demonstrate function with multiple returns.
print("\n69:")
def arithmetic_ops(a, b):
    sum_ = a + b
    diff = a - b
    product = a * b
    return sum_, diff, product

s, d, p = arithmetic_ops(10, 5)
print(f"Sum={s}, Difference={d}, Product={p}")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q70. Write python code to demonstrate a function which returns list/dictionary.
print("\n70:")
def create_list():
    return [1, 2, 3, 4, 5]

def create_dict():
    return {'name': 'Rakshit', 'roll': '0231BCA210'}

lst = create_list()
dct = create_dict()

print(f"List: {lst}")
print(f"Dictionary: {dct}")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q71. Write a python code to create a simple generator
print("\n71:")
def simple_generator():
    yield "Hello"
    yield "from"
    yield "generator"

for word in simple_generator():
    print(word)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q72. Wap in python to reverse a string without using predefined functions.
print("\n72:")
def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

string = input("Enter a string: ")
print(f"Reversed string: {reverse_string(string)}")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q73. Wap in python to check whether the string is palindrome or not.
print("\n73:")
def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q74. Wap in python to calculate the length of a string without using built-in Len() function.
print("\n74:")
def length_of_string(s):
    count = 0
    for _ in s:
        count += 1
    return count

string = input("Enter a string: ")
print(f"Length of the string is {length_of_string(string)}")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q75. Write a python code to demonstrate global variables with nested function.
print("\n75:")
x = 10

def outer_function():
    global x
    x = 20
    def inner_function():
        global x
        x = 30
        print(f"Inside inner_function: x = {x}")
    inner_function()
    print(f"Inside outer_function: x = {x}")

print(f"Before function call: x = {x}")
outer_function()
print(f"After function call: x = {x}")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q76. Write python code to demonstrate docstring for a function
print("\n76:")
def sample_function():
    """This function prints a welcome message"""
    print("Welcome to the docstring demonstration")

print(sample_function.__doc__)
sample_function()
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q77. Write python code to demonstrate decorator.
print("\n77:")
def decorator_function(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator_function
def say_hello():
    print("Hello!")

say_hello()
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q78. Write a python code to use a generator with a loop.
print("\n78:")
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

for number in count_up_to(5):
    print(number)
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q79. Wap in python to determine Season based on month.
print("\n79:")
def season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid month"

month = int(input("Enter month (1-12): "))
print(f"Season: {season(month)}")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q80. Write python code to use Lambda expressions with map.
print("\n80:")
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared}")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q81. Write python code to perform addition, subtraction, multiplication and transpose of two 3x3 matrix:
# - With NumPy
# - Without NumPy
print("\n81:")
import numpy as np

# With NumPy
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])
print("With NumPy:")
print("Addition:\n", A + B)
print("Subtraction:\n", A - B)
print("Multiplication:\n", A * B)
print("Transpose A:\n", A.T)

# Without NumPy
def matrix_add(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

def matrix_subtract(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

def matrix_multiply(X, Y):
    return [[X[i][j]*Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

def matrix_transpose(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]
print("\nWithout NumPy:")
print("Addition:", matrix_add(A,B))
print("Subtraction:", matrix_subtract(A,B))
print("Multiplication:", matrix_multiply(A,B))
print("Transpose:", matrix_transpose(A))
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q82. Write python code to create a custom module (user-defined module).
print("\n82:")
print("# Create a file named mymodule.py with the following content:")
print("""
def greet(name):
    print(f"Hello, {name}!")
""")
print("# Then use the module by importing it in another script.")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q83. Write python code to use a module.
print("\n83:")
print("# Assuming mymodule.py contains a function greet(name)")
print("import mymodule")
print("mymodule.greet('Rakshit')")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q84. Write python code to import specific function of a module.
print("\n84:")
print("# Assuming mymodule.py contains a function greet(name)")
print("from mymodule import greet")
print("greet('Rakshit')")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q85. Write python code to import all functions from a module.
print("\n85:")
print("# Assuming mymodule.py contains some functions")
print("from mymodule import *")
print("# Now all functions from mymodule can be used directly")
print("greet('Rakshit')")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q86. List and demonstrate various standard library module of python.
print("\n86:")
print("# Some standard Python modules with examples:")
print("import math")
print("print(math.sqrt(16))  # Output: 4.0")
print("import random")
print("print(random.randint(1,10))  # Random integer between 1 and 10")
print("import datetime")
print("print(datetime.datetime.now())  # Current date and time")
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q87. Write python code to define a class create its objects and access the properties in methods of the objects.
print("\n87:")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = Person("Rakshit", 21)
p1.display()
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q88. Write python code to demonstrate method overloading and method overriding.
print("\n88:")
class Calculator:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        else:
            return 0

class AdvancedCalculator(Calculator):
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(10, 20))
print(calc.add(10, 20, 30))

adv_calc = AdvancedCalculator()
print(adv_calc.add(5, 10))
print(adv_calc.add(5, 10, 15))
print("This program is executed by Tanish Gupta (0231BCA061)")

# Q89. Write a python code to demonstrate set comprehension
print("\n89:")
squares = {x*x for x in range(1, 11)}
print(f"Set of squares from 1 to 10: {squares}")
print("This program is executed by Tanish Gupta (0231BCA061)")

