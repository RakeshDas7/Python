#In python, we can take user input directly by using input() function. This input function gives a return value as String/character hence we have to pas that into a variable and then convert it into integer using int() function.

a = input()
print("My name is : ", a)

b = input("Enter First Number") # 12
c = input("Enter Second Number") # 23
print(b + c) # 1223 This is string concardination
print(int(b) + int(c)) # 35 

d = int(input('enter first number :')) #5
e = int(input('enter second number :')) #8
print(d + e) # 13
