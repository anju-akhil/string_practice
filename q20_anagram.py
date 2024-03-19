#Write a program to check if two strings are anagrams.
text="silent"
txt="listen"
s_text=sorted(text)
s_txt=sorted(txt)
print("Anagram" if s_text==s_txt else "Not anagram")