#Write a program to find the longest word in a string.
text="hello good morning all"
words=text.split(" ")
longest_word = ""
for w in words:
    if len(w) > len(longest_word):
            longest_word = w
print (longest_word)

#longest_word =  max(words, key=len)
#print(longest_word)
