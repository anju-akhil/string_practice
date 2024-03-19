#PALINDROME 
text="malayalam"
str=text[::-1]
#print(str)
if text==str:
    print("Palindrome")
else:
    print("Not Palindrome")

#--------------------------------------------------------------------
rev=""
for i in text:
    rev=i+rev
print("Palindrome" if text==rev else "Not Palindrome")