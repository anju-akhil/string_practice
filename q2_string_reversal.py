#STRING REVERSAL
text=input("Enter a text:")
rev=""
for i in text:
    rev=rev+i
print("Palindrome" if text==rev else "Not palindrome")