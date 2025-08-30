import json

# Sample dataset with 5 cars
car_inventory = [
    {"id": 1, "make": "Toyota", "model": "Camry", "year": 2021, "price": 56500},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2020, "price": 22000},
    {"id": 3, "make": "Ford", "model": "Mustang", "year": 2022, "price": 30000},
    {"id": 4, "make": "Chevrolet", "model": "Cruze", "year": 2019, "price": 1800},
    {"id": 5, "make": "Nissan", "model": "Altima", "year": 2023, "price": 28000}
]

# To Search cars by budget
def budget_cars(inventory, maxprice):
    filter_cars = [car for car in inventory if car['price'] <= maxprice]
    if filter_cars:
        print(f"\nCars within budget of Rs.{maxprice:,}:")
        for car in filter_cars:
            print(f"ID: {car['id']}, {car['year']} {car['make']} {car['model']} - Rs.{car['price']:,}")
    else:
        print(f"\nNo cars found within the budget of Rs.{maxprice:,}")
    return filter_cars

# Save inventory to a file
def save_inventory(inventory, filename="car_inventory.json"):
    try:
        with open(filename, 'w') as file:
            json.dump(inventory, file, indent=4)
        print(f"\nInventory successfully saved to {filename}")
        return filename
    except Exception as e:
        print(f"Error saving inventory: {e}")
        return None

# Additional helper function to display all cars
def display_cars(inventory):
    print("\nAll Available Cars:")
    for car in inventory:
        print(f"ID: {car['id']}, {car['year']} {car['model']} - Rs.{car['price']:,}")

def main():
    print("Car Inventory System")
    display_cars(car_inventory)
    # Search for under Rs.25,000
    budgeted_cars = budget_cars(car_inventory, 25000)
    # Save the inventory to a JSON file
    saved_file = save_inventory(car_inventory)
    # Additional functionality - show summary
    print(f"\n---------Summary-------")
    print(f"Total cars: {len(car_inventory)}")
    print(f"Cars within Rs.25,000 : {len(budgeted_cars)}")
    if saved_file:
        print(f"Inventory saved to: {saved_file}")

if __name__ == "__main__":
    main()
