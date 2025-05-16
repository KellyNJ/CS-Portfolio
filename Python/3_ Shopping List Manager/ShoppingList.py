shoppingList = []
def append(number):
    for i in range(number):
        item = input(str(i+1)+". What would you like to add? ").title()
        shoppingList.append(item)
def remove(number):
    for i in range(number):
        item = input(str(i+1)+". What would you like to delete? ").title()
        shoppingList.remove(item)
def showList():
    print(*shoppingList, sep = "\n")
def clearList():
    shoppingList.clear()
while True:
    varLoop = input("\nPress 1 to add an item, 2 to remove an item,\n3 to show the list, 4 to clear, or 5 to exit: ")
    if varLoop == '1':
        number = int(input("\nHow many items would you like to add? "))
        append(number)
    elif varLoop == '2':
        number = int(input("\nHow many items would you like to remove? "))
        remove(number)
    elif varLoop == '3':
        if shoppingList == []:
            print("\nThere is nothing in your shopping list.")
        else:
            print("\nYour list contains:")
            showList()
    elif varLoop == '4':
        if shoppingList == []:
            print("\nThere is nothing in your shopping list to clear.")
        else:
            clearList()
            print("\nThe shopping list has been cleared.")
    elif varLoop == '5':
        exit()
