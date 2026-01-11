str=input("Enter a string:")
word={}
for char in str:
    if char in word:
        word[char] +=1
    else:
     word[char]=1
print("character frequency:")
for char,count in word.items():
    print(f"{char}:{count}")


    words=input("Enter a line of text:").split(' ')
c={}
for t in words:
    if t in words:
        if t in c:
            c[t] +=1
        else:
            c[t]=1
print(c)

str=input("enter a string:")
if str.endswith("ing"):
    str=str + "ly"
else:
    str=str+ "ing"
print("modified string:",str)


list=input("Enter a list of words seperated by spaces:").split(" ")
longest_length=0
for word in list:
    if len(word)> longest_length:
        longest_length=len(word)
        long_word=word
print("The longest word is",long_word)
print("The length of the longest word is:",longest_length)