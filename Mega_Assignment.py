## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?

Ans : The language that is capable of creating all types of programs and it is written in the human readle format. 
That's why python called as general purpose and high level programming language.

Q2. Why is Python called a dynamically typed language?

Ans: Python is capable of checking the type of code written during the runtime itself so called dynamically-typed languages.

Q3. List some pros and cons of Python programming language?

Ans : 
pros: 
Simple and easy
Readable
Large Community	
Flexible and Extensible	
Extensive Libraries	
Embeddable	
IOT Opportunities

cons: 
Speed Limitations
High memory consumption
Security
Weak in Mobile Computing and Browsers
Slower than compiled languages
Work Environment


Q4. In what all domains can we use Python?

Ans : 
Web development
Data science
OS development
Scientific programming
Gaming


Q5. What are variable and how can we declare them?

Ans: Variables are the basic unit of storage in a programming language
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.


Q6. How can we take an input from the user in Python?

Ans: using the keyword : input()

Q7. What is the default datatype of the value that has been taken as an input using input() function?

Ans: String

Q8. What is type casting?

Ans : Converting one data type to another data type.

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

Ans: Yes, It is possile to read multiple inputs from input () using  split()
for eg : 
a,b,c = input (“Enter your child age: “).split ()
print(“Enter your elder son’s age: “, a)
print(“Enter your daughter’s age: “, b)
print(“Enter your younger son’s age: “, c)

Q10. What are keywords?

Ans : Keywords are special reserved words that have specific meanings and purposes. 

Q11. Can we use keywords as a variable? Support your answer with reason.

Ans : We cannot use keywords as variable names. It's because keywords have predefined meanings.

Q12. What is indentation? What's the use of indentaion in Python?

Ans : Indentation refers to the spaces at the beginning of a code line.Python uses indentation to indicate a block of code

Q13. How can we throw some output in Python?

Ans : Print()
eg : Print("Welcome to Python")

Q14. What are operators in Python?

Ans:The special symbols that designate that some sort of computation should be performed. 

Q15. What is difference between / and // operators?

Ans: /--> Float division 
    //--> Integer division

Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```

Ans: 
str = "iNeuron"*4
print("Display string = ", str) 


Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

Ans: 
x = int(input("Enter the number :"))
if x%2==0:
    print("The no is even")
else: 
    print("The no is odd")

Q18. What are boolean operator?

Ans : Boolean Operators are simple words (AND, OR, NOT or AND NOT) used as conjunctions to combine or exclude keywords in a search


Q19. What will the output of the following?
```
1 or 0
Ans: True

0 and 0
Ans: False

True and False and True
Ans : False

1 or 0 or 0
```
Ans: True

Q20. What are conditional statements in Python?

Ans : 
Python supports the usual logical conditions from mathematics:
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

Q21. What is use of 'if', 'elif' and 'else' keywords?

Ans:These are conditional statements that provide you with the decision making that is required when you want to execute code based on a particular condition


Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

Ans : 
age = int(input("Enter the Age :"))
if age>=18:
    print("I can vote !!!")
else: 
    print("I can't vote  !!!")


Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
numbers = [12, 75, 150, 180, 145, 525, 50]
sum = 0
for i in numbers: 
  if i % 2 == 0 : 
    sum = sum + i
print("The sum of even no :",sum)    


Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

Ans : 

num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))
num3 = int(input("Enter the number 3:"))
if (num1>=num2) and (num1 >=num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```

Ans : 
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers : 
  if i >150 : 
    if i > 500 :
      break
    continue
  if i % 5 == 0 :
     print(i)

Q26. What is a string? How can we declare string in Python?

Ans : strings in Python are arrays of bytes representing unicode characters
Strings can be created by enclosing characters inside a single quote or double-quotes. 
Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings.

Q27. How can we access the string using its index?

Ans : 
The individual characters in a string can be accessed by specifying the string name followed by a number in square brackets ( [] )
eg : 
string = "Hello World!"
print(string[4])

Q28. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "iNeuron"
```
Ans : string = "Big Data iNeuron"
for i in string[9:len(string)] :
  print(i)

Q29. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "norueNi"
```
string = "Big Data iNeuron"
print(string[16:8:-1])

Q30. Resverse the string given in the above question.

Ans : 
string = "Big Data iNeuron"
print(string[16::-1])

Q31. How can you delete entire string at once?

Ans: 
string = "Big Data iNeuron"
print("String before remove :",string)
string = string.replace("Big Data iNeuron", " ")
print("String After remove :",string)


Q32. What is escape sequence?

Ans: 
An escape sequence is a sequence of characters that, 
when used inside a character or string, does not represent itself but is converted into another character or series of characters

Q33. How can you print the below string?
```
'iNeuron's Big Data Course'
```
Ans: string="'iNeuron's Big Data Course'"
print(string)

Q34. What is a list in Python?
Ans: 
Lists are used to store multiple items in a single variable

Q35. How can you create a list in Python?
Ans: 
Lists in Python can be created by just placing the sequence inside the square brackets[]

Q36. How can we access the elements in a list?
Ans: 
To access values in lists, use the square brackets along with the corresponding index. 
for eg: 
list = ["apple", "banana", "cherry"]
print(list[1])

Q37. Write a code to access the word "iNeuron" from the given list.
```
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
``` 
Ans : 
list = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
print(list[4][2])


Q38. Take a list as an input from the user and find the length of the list.

Ans : 

n=int(input("Enter the no of list elements :"))
list1= []
for i in range(0,n):
    element =int(input("Enter the elements :"))
    list1.append(element)
print("The List is:",list1)

Q39. Add the word "Big" in the 3rd index of the given list.
```
lst = ["Welcome", "to", "Data", "course"]
```

Q40. What is a tuple? How is it different from list?

Ans: 
The primary difference between tuples and lists is that tuples are immutable but lists which are mutable. 
Therefore, it is possible to change a list but not a tuple. 
The contents of a tuple cannot change once they have been created in Python due to the immutability of tuples

Q41. How can you create a tuple in Python?

Ans: A tuple in Python can be created by enclosing all the comma-separated elements inside the parenthesis ()
for eg : thistuple = ("apple", "banana", "cherry")
print(thistuple)

Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.

Ans: 
tuplex = ('Hello','welcome') 
print(tuplex)
Tuples are immutable, so you can not add new elements

Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
Ans: yes, we can appedent 2 tuples usinf + 

tuple1 =(1,2,3,4)
tuple2 =(5,6,7,8)
print(tuple1)
print(tuple2)
print(tuple1+tuple2)

Q44. Take a tuple as an input and print the count of elements in it.

Ans : 
m1 = tuple(input('Enter the item to Tuple: ').split())
print("The Tuple elements are : ",m1)
print("The length of Tuple : ",len(m1))


Q45. What are sets in Python?

Ans: Sets are used to store multiple items in a single variable

Q46. How can you create a set?

Ans : Set can be created uisng ()
set1 = set()
set1.add(1)
set1.add(2)
print(set1)

Q47. Create a set and add "iNeuron" in your set.

Ans: 
set1 = set()
set1.add("iNeuron")
print(set1)

Q48. Try to add multiple values using add() function.
Ans : 
set1 = set()
set1.add(1)
set1.add(2)
print(set1)


Q49. How is update() different from add()?

Ans: 
We use add() method to add single value to a set. We use update() method to add sequence values to a set.

Q50. What is clear() in sets?
Ans : The clear() method removes all the elements from a list.

Q51. What is frozen set?

Ans : Frozen set is just an immutable version of a Python set object.

Q52. How is frozen set different from set?
Ans : A frozenset is an unordered and unindexed collection of unique elements.

Q53. What is union() in sets? Explain via code.

Ans :The union() method returns a set that contains all items from the original set, and all items from the specified set(s).
set1={1,2,3,5}
set2={6,7,8,9}
print(set1|set2)

Q54. What is intersection() in sets? Explain via code.

Ans: The intersection() method returns a set that contains the similarity between two or more sets.
set1={1,2,3,5}
set2={6,7,2,5}
print(set1 & set2)

Q55. What is dictionary ibn Python?

Ans : Dictionaries are used to store data values in key:value pairs

Q56. How is dictionary different from all other data structures.

Ans: A dictionary is a general-purpose data structure for storing a group of objects. A dictionary has a set of keys and each key has a single associated value.

Q57. How can we delare a dictionary in Python?

Ans : Dictionaries are written with curly brackets, and have keys and values:
eg: 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

Q58. What will the output of the following?
```
var = {}
print(type(var))
```
Ans : <class 'dict'>

Q59. How can we add an element in a dictionary?

Ans: 
Adding an item to the dictionary is done by using a new index key and assigning a value to it:
for eg: thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict["colour"] = "Red"  # Add value to dict
print(thisdict)


Q60. Create a dictionary and access all the values in that dictionary.

Ans: 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

Q61. Create a nested dictionary and access all the element in the inner dictionary.

Ans: 
family = {
  "child1" : {
    "name" : "Renjith",
    "year" : 1992
  },
  "child2" : {
    "name" : "Minu",
    "year" : 1992
  }
}
print(family)

Q62. What is the use of get() function?

Ans: The get() method returns the value of the item with the specified key.

Q63. What is the use of items() function?
Ans : The items() method is used to return the list with all dictionary keys with values.

Q64. What is the use of pop() function?
Ans : Python list pop() is an inbuilt function in Python that removes and returns the last value from the List or the given index value

Q65. What is the use of popitems() function?
Ans : The popitem() method removes the item that was last inserted into the dictionary


Q66. What is the use of keys() function?

Ans: 
The keys() method Return the keys in the dictionary:

Q67. What is the use of values() function?

Ans: The values() method returns the Values in the dictionary:

Q68. What are loops in Python?
Ans: Loops are a sequence of instructions that does a specific set of instructions or 
tasks based on some conditions and continue the tasks until it reaches certain conditions.
eg, for loop, while loop, nested loop

Q69. How many type of loop are there in Python?
Ans: 2 Type of loops. for loop, while loop. 

Q70. What is the difference between for and while loops?
Ans:  
for loop is used when the number of iterations is known, whereas execution is done in the while loop until the statement in the program is proved wrong. 

Q71. What is the use of continue statement?

Ans: The continue statement passes control to the next iteration

Q72. What is the use of break statement?

Ans: The purpose the break statement is to break out of a loop early

Q73. What is the use of pass statement?
Ans:  The pass statement is a null statement which can be used as a placeholder for future code

Q74. What is the use of range() function?

Ans: The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
syntax: range(start, stop, step)

Q75. How can you loop over a dictionary?

Ans: You can loop through a dictionary by using a for loop.

### Coding problems
Q76. Write a Python program to find the factorial of a given number.

Ans : 
num = int(input("Enter the no:"))
result=1
if(num == 1 or num == 0):
 print("The factoril of ",num,"is:",1)
else:
    for i in range(1,num+1):
        result=i*result
        i=i+1
    print("Factorial of",num,'is:',result)


Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100

Ans: 
principal = int(input("Enter the principal amount:"))
rate = int(input("Enter the Rate of Interest:"))
Tenure = int(input("Enter the tenure period:"))
simple_Interest = (principal*rate*Tenure)/100
print("The simple Interest amount is :",simple_Interest)

Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

Ans: 
principal = int(input("Enter the principal amount:"))
rate = int(input("Enter the Rate of Interest:"))
Tenure = int(input("Enter the tenure period:"))
Compound_Interest = principal*((1+rate/100)**Tenure)
print("The Compound Interest amount is :",Compound_Interest)

Q79. Write a Python program to check if a number is prime or not.

Ans: 
num=int(input("Enter the number:"))
count=0
for i in range(1,num):
    if(num % i==0):
        count=count+1
if(count < 2):
    print("The Number entered is prime ")  
else:
    print("The Number entered is not prime ")  

Q80. Write a Python program to check Armstrong Number.

Ans: 
num=input("Enter the number:")
sum=0
for i in range(0,len(num)):
    sum = sum + int(num[i])**len(num)
print("The no entered is:",num)
print("The sum of digits of numbers:",sum)
if(sum == int(num)):
    print("The no is Armstrong")
else:
    print("The no is not Armstrong")


Q81. Write a Python program to find the n-th Fibonacci Number.
Ans: 
num = int(input("Enter the N-th Fibonacci:"))
fib_set = [0,1,1]
for i in range(3,num):
        fib_set.append(fib_set[i-1]+fib_set[i-2])
print("The Fibonacci series :",fib_set)
print("The N-th Fibonacci no :",fib_set[-1])

Q82. Write a Python program to interchange the first and last element in a list.
Ans: 
list1 = input("Enter the List elements separated by space: ").split()
print("List elements before swapping:", list1)
list1[0],list1[-1]=list1[-1],list1[0]
print("List elements after swapping:", list1)

Q83. Write a Python program to swap two elements in a list.

Ans: 
list1 = input("Enter the List elements separated by space: ").split()
print("List elements before swapping:", list1)
a=int(input("Enter the 1st index positions to swap:"))
b=int(input("Enter the 2nd index positions to swap:"))
list1[a],list1[b]=list1[b],list1[a]
print("List elements after swapping:", list1)


Q84. Write a Python program to find N largest element from a list.

Q85. Write a Python program to find cumulative sum of a list.

Q86. Write a Python program to check if a string is palindrome or not.

Q87. Write a Python program to remove i'th element from a string.

Q88. Write a Python program to check if a substring is present in a given string.

Q89. Write a Python program to find words which are greater than given length k.

Q90. Write a Python program to extract unquire dictionary values.

Q91. Write a Python program to merge two dictionary.

Q92. Write a Python program to convert a list of tuples into dictionary.
```
Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
```

Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
```
Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
```

Q94. Write a Python program to get all combinations of 2 tuples.
```
Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
```

Q95. Write a Python program to sort a list of tuples by second item.
```
Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
```

Q96. Write a python program to print below pattern.
```
* 
* * 
* * * 
* * * * 
* * * * * 
```
Q97. Write a python program to print below pattern.
```
    *
   **
  ***
 ****
*****
```

Q98. Write a python program to print below pattern.
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```

Q99. Write a python program to print below pattern.
```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
```

Q100. Write a python program to print below pattern.
```
A 
B B 
C C C 
D D D D 
E E E E E 
