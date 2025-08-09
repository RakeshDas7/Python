# a = "Ashis"
# b = "Bishal"
# c = a.count('s')
# print('count of s in Ashis is:', c)

# d = a.split('i')
# print(d)

# e = a.replace('A', 'R')
# print(e)

# f = a.upper()
# print(f)

# g = f.lower()
# print(g)

name = "Ashis,Bishal"
print(name[0]) # A
print(name[0:5]) # Ashis -> including 0 but not 5
print(name[0:]) # Ashis,Bishal
print(name[:len(name)]) # Ashis,Bishal
print(name[6:len(name)]) # Bishal


mango = "Mango"
print("mango is", len(mango), "letter word")
print(mango[:])
print(mango[-3:-1])

nm = "Harry"
print(nm[-4:-2])