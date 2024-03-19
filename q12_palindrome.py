#Write a program to check if a string is a palindrome.
text="malayalam"
rev=""
for i in text:
    rev=i+rev
print("Palindrome" if text==rev else "Not palindrome")

text="malayalam"
str=text[::-1]
print("Palindrome" if text==str else "Not palindrome")