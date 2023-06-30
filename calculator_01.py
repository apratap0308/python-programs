sum = 0
while(True):
     userInput = input("enter the price of item : ")
     if(userInput!= 'q'):
               sum = sum + int(userInput)
               print(f"order total so far: {sum}")
    
     else:
                 print(f"your total bill is {sum}.thanks for shopping") 
     break