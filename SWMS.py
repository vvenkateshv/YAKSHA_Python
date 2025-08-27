# Smart Waste Management System

# Preset waste data (Location, Waste Type, Weight in kg)
waste_data = [
    ("Zone A", "Organic", 120),
    ("Zone B", "Plastic", 80),
    ("Zone C", "Electronic", 45),
    ("Zone D", "Metal", 60),
    ("Zone E", "Organic", 95)
]

# Function 1: Calculate total waste by type
def calculate_total_waste_by_type(data):
    """
    Iterate through the data and sum up the total weight for each waste type.
    Store results in a dictionary where the key is the waste type and the value is the total weight.
    """
    waste_summary = {}  # Dictionary to store waste type totals
    
    # Iterate through each waste record
    for location, waste_type, weight in data:
        if waste_type in waste_summary:
            waste_summary[waste_type] += weight
        else:
            waste_summary[waste_type] = weight
    
    return waste_summary

# Function 2: Identify unique waste zones
def unique_waste_zones(data):
    """
    Extract and return a set of unique waste zones from the data.
    """
    zones = set()  # Set to store unique zones
    
    # Extract unique zone locations
    for location, waste_type, weight in data:
        zones.add(location)
    
    return zones

# Function 3: Find heaviest waste location
def find_heaviest_location(data):
    """
    Identify the location with the heaviest waste recorded.
    Use max() to find the location with the highest weight.
    Return the location and its weight.
    """
    if not data:
        return None, 0
    
    # Find the record with maximum weight using max() function
    heaviest_record = max(data, key=lambda x: x[2])  # x[2] is the weight
    heaviest_zone = heaviest_record[0]  # Location
    heaviest_weight = heaviest_record[2]  # Weight
    
    return heaviest_zone, heaviest_weight

# Additional helper function to display waste data
def display_waste_data(data):
    """
    Display all waste data in a formatted table.
    """
    print("\n=== Waste Data Overview ===")
    print("-" * 50)
    print(f"{'Zone':<10} {'Type':<12} {'Weight (kg)':<12}")
    print("-" * 50)
    for location, waste_type, weight in data:
        print(f"{location:<10} {waste_type:<12} {weight:<12}")

# Main Execution
def main():
    """
    Execute all functions and display results.
    - Calculate total waste by type
    - Identify unique waste zones
    - Find the heaviest waste location
    """
    print("=== Smart Waste Management System ===")
    
    # Display raw waste data
    display_waste_data(waste_data)
    
    # 1. Calculate total waste by type
    print("\n=== Total Waste by Type ===")
    waste_totals = calculate_total_waste_by_type(waste_data)
    print("-" * 30)
    for waste_type, total_weight in waste_totals.items():
        print(f"{waste_type:<12}: {total_weight} kg")
    
    # 2. Identify unique waste zones
    print("\n=== Unique Waste Zones ===")
    unique_zones = unique_waste_zones(waste_data)
    print("-" * 25)
    for zone in sorted(unique_zones):  # Sort for better readability
        print(f"• {zone}")
    
    # 3. Find the heaviest waste location
    print("\n=== Heaviest Waste Location ===")
    heaviest_zone, heaviest_weight = find_heaviest_location(waste_data)
    print("-" * 35)
    if heaviest_zone:
        print(f"Zone: {heaviest_zone}")
        print(f"Weight: {heaviest_weight} kg")
    else:
        print("No waste data available")
    
    # Summary statistics
    print("\n=== Summary Statistics ===")
    print("-" * 30)
    total_zones = len(unique_zones)
    total_waste_types = len(waste_totals)
    total_weight = sum(weight for _, _, weight in waste_data)
    average_weight = total_weight / len(waste_data) if waste_data else 0
    
    print(f"Total Zones: {total_zones}")
    print(f"Total Waste Types: {total_waste_types}")
    print(f"Total Weight: {total_weight} kg")
    print(f"Average Weight per Location: {average_weight:.1f} kg")
    
    # Return results for potential further processing
    return {
        'waste_totals': waste_totals,
        'unique_zones': unique_zones,
        'heaviest_location': (heaviest_zone, heaviest_weight),
        'summary': {
            'total_zones': total_zones,
            'total_waste_types': total_waste_types,
            'total_weight': total_weight,
            'average_weight': average_weight
        }
    }

if __name__ == "__main__":
    results = main()
