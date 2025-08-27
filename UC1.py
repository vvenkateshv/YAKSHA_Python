import json

# Sample dataset with 5 cars
car_inventory = [
    {"id": 1, "make": "Toyota", "model": "Camry", "year": 2021, "price": 56500},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2020, "price": 22000},
    {"id": 3, "make": "Ford", "model": "Mustang", "year": 2022, "price": 30000},
    {"id": 4, "make": "Chevrolet", "model": "Cruze", "year": 2019, "price": 18000},
    {"id": 5, "make": "Nissan", "model": "Altima", "year": 2023, "price": 28000}
]

# Function 1: Search cars by budget
def search_by_budget(inventory, max_price):
    """
    Find and return cars that are within the given budget.
    Use list comprehension to filter cars based on price.
    """
    # Filter cars where price is less than or equal to max_price
    filtered_cars = [car for car in inventory if car['price'] <= max_price]
    
    # Display results
    if filtered_cars:
        print(f"\nCars within budget of Rs.{max_price:,}:")
        print("-" * 50)
        for car in filtered_cars:
            print(f"ID: {car['id']}, {car['year']} {car['make']} {car['model']} - Rs.{car['price']:,}")
    else:
        print(f"\nNo cars found within the budget of Rs.{max_price:,}")
    
    return filtered_cars

# Function 2: Save inventory to a file
def save_inventory(inventory, filename="car_inventory.json"):
    """
    Save the car inventory as a JSON file.
    Use json.dump() with indent=4 for readability.
    """
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
    """
    Display all cars in the inventory.
    """
    print("\nAll Available Cars:")
    print("-" * 50)
    for car in inventory:
        print(f"ID: {car['id']}, {car['year']} {car['make']} {car['model']} - Rs.{car['price']:,}")

# Main Execution
def main():
    """
    Call search_by_budget and save_inventory functions.
    - Search for cars under a certain price
    - Save the inventory to a file
    """
    print("=== Car Inventory Management System ===")
    
    # Display all available cars
    display_cars(car_inventory)
    
    # Search for cars under $25,000
    budget_cars = search_by_budget(car_inventory, 25000)
    
    # Save the inventory to a JSON file
    saved_file = save_inventory(car_inventory)
    
    # Additional functionality - show summary
    print(f"\n=== Summary ===")
    print(f"Total cars in inventory: {len(car_inventory)}")
    print(f"Cars within $25,000 budget: {len(budget_cars)}")
    if saved_file:
        print(f"Inventory saved to: {saved_file}")

if __name__ == "__main__":
    main()
