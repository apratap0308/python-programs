s = input("Enter the letter")
d=l=0
for c in s:
    if c.isdigit():
      d = d+1
    elif c.isalpha():
      l=l+1
else:
    pass
    print("DIGIT IS:", d)    
    print("LETTER IS:", l)    
