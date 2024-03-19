#Write a program to reverse a string.
str="hello"
rev=""
for i in str:
    rev=i+rev
print(rev)

print(str[::-1])