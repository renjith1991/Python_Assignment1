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

Ans: input()

Q7. What is the default datatype of the value that has been taken as an input using input() function?

Ans: Integer


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
Ans : 1

0 and 0
Ans :0

True and False and True
Ans : False 

1 or 0 or 0
Ans: 1```

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

Ans: 
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
