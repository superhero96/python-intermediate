number_of_items = int(input('plese enter the number:'))


myList=[]


for i in range(number_of_items):
    myNumber = int(input(f'Enter number {i+1}:'))
    myList.append( myNumber)


largest = myList[0]

for item in myList:
    if (item > largest):
        largest = item


print(f'The Largest Number Is {largest}')