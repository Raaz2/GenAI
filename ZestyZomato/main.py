from prettytable import PrettyTable
from collections import OrderedDict
from colorama import Fore, Style


menu = OrderedDict({})
orders = {}
order_id_counter = 1

#for adding dishesh
def add():
    while True:
        try:
            id = int(input("Enter dish ID: "))
            name = input("Enter dish name: ")
            price = float(input("Enter price: "))
            stock = int(input("Enter quantity: "))
            availablility = "Not Available"
            if int(stock) >= 1:
                availablility = "Available"

            menu[id] = {
            "Name" : name,
            "Price" : price,
            "Stock" :stock,
            "Availability": availablility
            }

            print(f"Dish {name} with ID {id} added to menu.")
            viewMenu()
            break
        except ValueError:
            print("Invalid input. Try again!")

#to remove a dish from menu
def remove():
    id = int(input("Enter the dish ID to remove: "))
    if id in menu:
        name = menu[id]["Name"]
        del menu[id]
        print(f"Dish '{name}' with ID '{id}' removed from the menu.")
        viewMenu()
    else:
        print("Dish not found in the menu.")       


#viewing the menu 
def viewMenu():
    # Create the table
    table = PrettyTable()
    table.field_names = ['Dish ID', 'Dish Name', 'Price', 'Stock','Availability']

    # Add data to the table
    for dish_id, dish_details in menu.items():
        dish_name = dish_details["Name"]
        dish_price = dish_details["Price"]
        dish_stock = dish_details["Stock"]
        dish_availability = dish_details["Availability"]

        # Set color based on availability
        if dish_availability == "Available":
            dish_availability = f"{Fore.GREEN}{dish_availability}{Style.RESET_ALL}"
        else:
            dish_availability = f"{Fore.RED}{dish_availability}{Style.RESET_ALL}"

        table.add_row([dish_id, dish_name, dish_price, dish_stock, dish_availability])

    # Print the table
    print(table)


#taking order from customer
def takeOrder():
    global order_id_counter
    customer_name = input("Enter customer name: ")
    dish_id = int(input("Enter dish ID: "))
    quan = int(input("Enter quantity: "))
    dishes_ordered = []
    if dish_id in menu and menu[dish_id]["Availability"] == "Available":
        dishes_ordered.append(menu[int(dish_id)]["Name"])
        if menu[dish_id]["Stock"] < quan:
            print("Can't order more than" , menu[dish_id]["Stock"])
            return
        else :
            menu[dish_id]["Stock"] = menu[dish_id]["Stock"] - quan
    else:
        print(f"Dish with ID '{dish_id}' is not available. Order cannot be placed.")
        return

    order = {
        "Customer Name": customer_name,
        "Dishes Ordered": dishes_ordered,
        "Status": "Received"
    }
    orders[order_id_counter] = order
    print(f"Order ID: {order_id_counter}")
    order_id_counter += 1
    reviewOrders()

#update order status
def updateOrderStatus():
    order_id = int(input("Enter order ID: "))
    if order_id in orders:
        order = orders[order_id]
        print(f"Current Status: {order['Status']}")
        print("1. Preparing")
        print("2. Ready for Pickup")
        print("3. Delivered")
        option = int(input("Select an option to update the status: "))

        if option == 1:
            order['Status'] = "Preparing"
        elif option == 2:
            order['Status'] = "Ready for Pickup"
        elif option == 3:
            order['Status'] = "Delivered"
        else:
            print("Invalid option selected.")
    else:
        print("Order not found.")


#review orders 
def reviewOrders():
    # Create the table
    table = PrettyTable()
    table.field_names = ['Order ID', 'Customer Name', 'Dishes Ordered', 'Status']

    # Add data to the table
    for order_id, order_details in orders.items():
        customer_name = order_details["Customer Name"]
        dishes_ordered = ', '.join(order_details["Dishes Ordered"])
        status = order_details["Status"]

        table.add_row([order_id, customer_name, dishes_ordered, status])

    # Print the table
    print(table)

def runApp():
    while True:
        print("1. Add dish to menu")
        print("2. Remove dish from menu")
        print("3. Update availability of particular dish")
        print("4. Take order")
        print("5. Update order status")
        print("6. Review all orders")
        print("7. View Menu")
        print("8. Exit")
        
        choice = input("Enter selection: ")
        if choice == "1":
            add()
        elif choice == "2":
            remove()
        elif choice == "3":
            print(choice)
        elif choice == "4":
            takeOrder()
        elif choice == "5":
            updateOrderStatus()
        elif choice == "6":
            reviewOrders()
        elif choice == "7":
            viewMenu()
        elif choice == "8":
            break
        else:
            print("Invalid selection, try again!")

runApp()

print("Thanks for using 'Zomato Chronicles: The Great Food Fiasco App'")
