str=input("Enter a string:")
words=str.split()
if len(str)>=2:
    word=words[1].upper()
    print("Second word in upper case:",word)
else:
    print("The input must contain minimum of two words:")
    
