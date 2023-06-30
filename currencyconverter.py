with open ("currencyData.txt") as f :
    lines = f.readlines

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict(parsed[0]) == parsed[1]


amount = int(input("Enter amount: \n"))
print("Enter the name of currency available options are: \n")
[print(item) for item in currencydict.keys()]
currency = input("Please enter one values: \n")
print(f"{amount} INR is equal to {amount *float (currencyDict[currency])} {currency}")