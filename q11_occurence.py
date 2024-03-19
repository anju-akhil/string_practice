#Write a program to count the number of occurrences of a specific character in a string.

str="prograMming"
char=input("Enter a character:")
count=0
for i in str:
    if char==i:
        count+=1
print(count)


# #is occur the character
# str="programming"
# char=input("Enter a character:")
# is_char=False
# for i in str:
#     if char in str:
#         is_char=True

# print(is_char)