# # Snack inventory dictionary
snackInventory = {}

# # Sales records dictionary
salesRecords = {}

# # Function to add a snack to the inventory
def add():
    id = input("Enter snack id: ")
    name = input("Enter snack name: ")
    price = input("Enter snack price: ")
    available = input("Is the snack available? (yes/no): ")

    snackInventory[id] = {
        "name" : name,
        "price" : price,
        "available" : available.lower()
    }
    
    print(f"Snack {name} with ID {id} added to inventory.")

# # Function to remove a snack from the inventory
def remove():
    id = input("Enter the snack ID to remove: ")
    if id in snackInventory:
        name = snackInventory[id]["name"]
        del snackInventory[id]
        print(f"Snack '{name}' with ID '{id}' removed from the inventory.")
    else:
        print("Snack not found in the inventory.")

# Function to update the availability of a snack
def updateAvailability():
    id = input("Enter the snack ID to update availability: ")
    if id in snackInventory:
        availability = input("Set new availability (yes/no): ")
        snackInventory[id]["available"] = availability
        print("Snack availability updated.")
    else:
        print("Snack not found in the inventory.")

# # Function to record a snack sale
def recordSale():
    id = input("Enter the snack ID sold: ")
    if id in snackInventory:
        name = snackInventory[id]["name"]
        if snackInventory[id]["available"]:
            if id in salesRecords:
                salesRecords[id] += 1
            else:
                salesRecords[id] = 1
            print(f"Snack '{name}' sold. Inventory and sales record updated.")
        else:
            print("Snack not available for sale.")
    else:
        print("Snack not found in the inventory.")

# # Function to display the snack inventory
def display():
    print("Snack Inventory:")
    print("----------------")
    if snackInventory:
        for id, snacks in snackInventory.items():
            availability = "Available" if snacks["available"] == "yes" else "Not Available"
            print(f"ID: {id} | Name: {snacks['name']} | Price: {snacks['price']} | Availability: {availability}")
    else:
        print("No snacks in the inventory.")

# # Function to display the sales records
def displaySalesRecord():
    print("Sales Records:")
    print("--------------")
    if salesRecords:
        for id, quantity in salesRecords.items():
            if id in snackInventory:
                name = snackInventory[id]["name"]
                print(f"ID: {id} | Name: {name} | Quantity Sold: {quantity}")
    else:
        print("No sales records available.")

# Main program loop
while True:
    print("Welcome to 'Mumbai Munchies: The Canteen Chronicle'")
    print("1. Add Snack")
    print("2. Remove Snack")
    print("3. Update Snack Avalability")
    print("4. Record Snack Sale")
    print("5. Display Snack Inventory")
    print("6. Display Sales Records")
    print("7. Quit")
    choice = input("Enter selection: ")

    if choice == "1":
        add()
    elif choice == "2":
        remove()
    elif choice == "3":
        updateAvailability()
    elif choice == "4":
        recordSale()
    elif choice == "5":
        display()
    elif choice == "6":
        displaySalesRecord()
    elif choice == "7":
        break
    else:
        print("Invalid selection, Try again!")

print("Thank you for using the Mumbai Munchies Canteen System.")