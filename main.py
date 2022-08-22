#creating list
grocery_list = []

#function to add item
def adding_item(myList, action):
    myList.append(action)
    return myList

#function to edit item
def editing_item(action):
    global grocery_list
    if action in grocery_list:
      new = input("What would you like to replace " + action + " with?: ")
      grocery_list.insert((grocery_list.index(action)), new)
      grocery_list.remove(action)
    else:
      print("")
      print("Item not in list.")

#function to remove item
def removing_item(action):
    grocery_list.remove(action)

#function to display list
def print_list(action):
  print("")
  print("Grocery List:")
  for x in (grocery_list): 
    print("(" + str(grocery_list.index(x) + 1 ) + ")" +(x.capitalize()))

#function to end program
def quit(action):
    print("Thanks for playing")

#intro / instructions
print("Welcome to the Grocery List Program.")
print("")
print("")
print("You can add, edit, remove items from the list.")
print("")
print(
    " (1) Add Item \n (2) Edit Item \n (3) Remove Item \n (4) Print List \n (5) Quit"
)
print("")

#asking user what they want to do
choice = input("What action would you like to preform?: ")
while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
    choice = input("What would you like to do? (Select a #) ")

#checking users input and steps into required function function
while choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
    if choice == ("1"):
        action = input("What item would you like to add?: ").capitalize()
        if action in grocery_list:
          print("That item is already in the list.") 
        else: 
          grocery_list = adding_item(grocery_list, action)
          print("")
        choice = input("What would you like to do? (Select a #) ")
    elif choice == ("2"):
        action = input("What would you like to edit?: ").capitalize()
        editing_item(action)
        print("")
        choice = input("What would you like to do? (Select a #) ")
    elif choice == ("3"):
        action = input("What item would you like to remove?: ").capitalize()
        removing_item(action)
        print("")
        choice = input("What would you like to do? (Select a #) ")
    elif choice == ("4"):
        print_list(action)
        print("")
        choice = input("What would you like to do? (Select a #) ")
    elif choice == ("5"):
        action = input("Would you like to quit? (yes or no): ").lower()
        if action == ("yes"):
          quit(action)
          print("")
          choice = "Brent"
        else:
            choice = input("What would you like to do? (Select a #) ")

#asking user what they wanna do if choice was not valid
while choice != "Brent" and choice!= "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
  choice = input("What would you like to do? (Select a #) ")