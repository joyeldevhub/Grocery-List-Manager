#Going to create a Grocery list manager
# create a empty list to hold the grocery items

grocery_list = []


def display_list():
    print("What would you like to do?")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View your item")
    print("4. Clear your item")
    print("5. exit")

    #Add an Item to the List
    selection = (int(input("Enter the option: ")))
    if selection == 1:
        while True:
            #Enter an item and want to stop the loop, type stop
            item = input("Enter an item (and want to stop the loop, type 'stop'): ")
            if item.lower() == 'stop':
                break
            grocery_list.append(item)
    

    #Remove an Item from the List
    if selection == 2:
        print(grocery_list)
        name = (input("Enter the item name to remove: "))
        if name in grocery_list:
            grocery_list.remove(name)
            print("Entered item has removed from list")
        else: 
            print("Entered item is not in list. Kindly check the list again and proceed.")

    #View the List
    if selection == 3:
        print(grocery_list)
        #for loop with enumerate() method:
        # for list in enumerate(grocery_list):
        #     print(list)
        #If I want to start the list items with number 1:
        for list in enumerate(grocery_list, start=1):
            print(list)

    if selection == 4:
        print(grocery_list)

        #Clear the list items with method of clear()
        grocery_list.clear()


    if selection == 5:
        print("Start purchasing, your list has been ready!!!")
        print(grocery_list)
        exit()




while True:
    display_list()



#Before the project:
# => Function Looping
# => About while looping
# => About enumerate() method

#After the project:
# => I learned how to loop through functions.
# => I gained an understanding of while loops
# => Learned about enumerate method.
# => I worked with conditions.



