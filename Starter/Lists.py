total = 0
expense = []
numofexpense= int(input("How many units are you entering\n"))
for i in range(numofexpense):
    expense.append(int(input("Enter Units\n")))

total = sum(expense)
print("This is your added unit "+ str(total))