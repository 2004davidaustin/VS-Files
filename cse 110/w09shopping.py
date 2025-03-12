response = ""
items = []
prices = []
print("\n\n" + "Welcome to the coolest store ever")


#'''

while response != "quit" :
    

    print("\nYou can add an item to your cart, view your cart, remove an item from your cart, check your total, or quit. \n(Add) (View) (Edit) (Remove) (Total) (Quit)")
    response = input("What would you like to do? ").lower()


    if "add" in response : 
        items.append(input("\nWhat did you find to put in your cart? "))
        prices.append(float(input("How much is it? ")))
        print(f"Added '{items[-1]}' to your cart.")


    if "view" in response : 
        if items :
            print("\nHere's what you have so far:")
            for i, item in enumerate(items) :
                print(f"{i+1}. {item}, ${prices[i]}")
                
        else : print("\nYour cart is empty right now.")


    if "edit" in response : 
        change_number = (int(input("\nEnter the number of the item you'd like to edit: ")) - 1)

        while 0 > change_number or change_number > len(items) - 1 : 
                print("That number is outside of the list.")
                change_number = (int(input("\nEnter the number of the item you'd like to edit: ")) - 1)

        change_name = input("What do you want to change it to? ")
        change_price = float(input("What's the new price? "))

        print(f"Changed '{items[change_number]}' for ${prices[change_number]} to '{change_name}' for ${change_price}")

        items[change_number] = change_name
        prices[change_number] = change_price


    if "remove" in response : 
        if items : 
            remove = 0
            remove = (int(input("\nEnter the number of the item you'd like to remove: ")) - 1)

            while 0 > remove or remove > len(items) - 1 : 
                print("That number is outside of the list.")
                remove = (int(input("Enter the number of the item you'd like to remove: ")) - 1)
            
            print(f"Removed '{items[remove]}' from your cart.")
            items.remove(items[remove])
            prices.remove(prices[remove])
        
        else : print("\nYour carty is empty right now.")


    if "total" in response :
        if items : print(f"\nYour current total is ${sum(prices)}")
        else : print("\nYour carty is empty right now.")


    if "quit" in response : print("Have a nice day!\n\n")

#'''
