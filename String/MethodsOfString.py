a = "!!Rakesh !!!!!!!!"
print(len(a)) # Strings are immuatable means we can't change there value 
#

print(a.upper()) # All elements converted into upper case

print(a.lower()) # All elements converted into lower case

print(a.rstrip("!")) # Remove all the elements from right side

print(a.lstrip("!")) # Remove all the elements from left side

print(a.replace("Rakesh", "Happy"))

print(a.split(" ")) # Split the string into list of words

blogHeading = "introduction to js"
print(blogHeading.capitalize()) # Capitalize the first letter of the string and make rest of the string -> Introduction to js

str1 = "Welcome to the console !!!"
print(len(str1))
print(len(str1.center(-7))) 
print(str1.center(50))

b = "Rakesh Rakesh Rakesh"
print(b.count("Rakesh")) # Count the number of times "Rakesh" is i.e. 3

print(str1.startswith("Welcome"))
print(str1.endswith("!!!")) # true 
print(str1.endswith("to", 4, 10)) # true

str1 = "Rakesh is a good boy"
print(str1.find("is")) # gives the index of the first occurrence of "is" i.e. 5
print(str1.find("bad")) # gives -1 because "bad" is not present in the string

#print(str1.index("bad")) # gives ValueError because "bad" is not present in the string
print(str1.index("is")) # gives the index of the first occurrence of "is" i

#alpha numeric string = A-Z, a-z, 0-9
str1 = "Rakesh123"
print(str1.isalnum()) # true

str2 = "Rakesh@123"
print(str2.isalnum()) # false

# alphabates = A-Z, a-z
str3 = "Rakesh"
print(str3.isalpha()) # true

str3 = "Rakesh123"
print(str3.isalpha()) # false

print(str3.islower()) # true

print(str3.isprintable()) # true
str4 = "he is agood by \nand he plays cricket"
print(str4.isprintable()) # false due to "\n"

print(str4.isspace()) #false
str5 = "   "
print(str5.isspace()) # true

str6 = "Rakesh loves to play video game"
print(str6.istitle())
str6 = "Rakesh Loves To Play Video Game"
print(str6.istitle()) # true

print(str6.title())
print(str6.title().istitle())

print(str6.swapcase())