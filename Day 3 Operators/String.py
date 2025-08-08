# In python anything that you enclose between single or double quotation mark is considered as String. A String is essentially a sequence or array of textual data . Strings are used when working with unicode characters. 
name = "Rakesh"
friend = "Rahul"

print("Hello", name)
meet = "he said \"He wants to meet me.\"" # This is a string with double quotes inside it. The double quotes are escaped with a backslash
print (meet)

meet2 = 'he said "He wants to meet me."'
print(meet2)

meet3 = '''he said,
Hey Rakesh
I'm Good
wants to meet'''
print(meet3) # This is a string with triple quotes. It can span multiple lines. The triple quotes are used

# In python String is likely an array of characters. We can access each character in the string using index. Index starts from 0.
print(name[0]) # prints R
print(name[-1]) # prints h. The negative index starts from the end of the string.

# print(name[6]) # This will throw an error if the index is out of range.

print()
print("Lets use for loop")
for i in name :
    print(i) # prints each character in the string