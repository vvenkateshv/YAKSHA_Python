import unittest
import numpy as np
import pandas as pd

# Railway Reservation System

# Preset data for the Railway Reservation System
seat_numbers = np.array([101, 102, 103, 104, 105])  # Seat numbers
ticket_prices = np.array([250, 300, 400, 350, 500])  # Ticket prices for each seat
availability = np.array([True, False, True, False, True])  # Availability status (True means available)
passenger_names = ["John", "Alice", "Bob", "Emma", "David"]  # Reserved passenger names

# Create a DataFrame to manage reservations
df = pd.DataFrame({
    'Seat Number': seat_numbers,
    'Passenger Name': passenger_names,
    'Ticket Price': ticket_prices,
    'Availability': availability
})

# Function 1: Find the total waiting list (count passengers with unavailable seats)
def total_waiting_list(df):
    """
    Count the number of passengers whose seats are unavailable.
    """
    # Count seats where availability is False (unavailable seats)
    waiting_count = len(df[df['Availability'] == False])
    return waiting_count

# Function 2: Find the highest ticket price
def highest_ticket_price(df):
    """
    Identify the seat with the highest ticket price.
    Use df['Ticket Price'].max() to find the maximum value.
    """
    # Find the maximum ticket price
    max_price = df['Ticket Price'].max()
    
    # Find the seat number associated with the highest price
    max_price_row = df[df['Ticket Price'] == max_price]
    seat_number = max_price_row['Seat Number'].iloc[0]
    
    return max_price, seat_number

# Function 3: Find the number of available seats
def available_seats(df):
    """
    Count the number of seats marked as available (Availability == True).
    """
    # Count seats where availability is True
    available_count = len(df[df['Availability'] == True])
    return available_count

# Additional helper functions for better functionality
def display_reservation_data(df):
    """
    Display all reservation data in a formatted table.
    """
    print("\n=== Railway Reservation Data ===")
    print("-" * 60)
    print(f"{'Seat':<6} {'Passenger':<12} {'Price':<8} {'Status':<12}")
    print("-" * 60)
    
    for index, row in df.iterrows():
        status = "Available" if row['Availability'] else "Reserved"
        passenger = row['Passenger Name'] if not row['Availability'] else "N/A"
        print(f"{row['Seat Number']:<6} {passenger:<12} ${row['Ticket Price']:<7} {status:<12}")

def get_available_seats_details(df):
    """
    Get detailed information about available seats.
    """
    available_df = df[df['Availability'] == True]
    return available_df

def get_reserved_seats_details(df):
    """
    Get detailed information about reserved seats.
    """
    reserved_df = df[df['Availability'] == False]
    return reserved_df

def find_cheapest_available_seat(df):
    """
    Find the cheapest available seat.
    """
    available_df = df[df['Availability'] == True]
    if len(available_df) > 0:
        min_price = available_df['Ticket Price'].min()
        cheapest_seat = available_df[available_df['Ticket Price'] == min_price]
        return min_price, cheapest_seat['Seat Number'].iloc[0]
    else:
        return None, None

# Main Execution
def main():
    """
    Execute all functions and display results.
    - Find total waiting list
    - Find the highest ticket price
    - Find the number of available seats
    """
    print("=== Railway Reservation System ===")
    
    # Display all reservation data
    display_reservation_data(df)
    
    # 1. Find total waiting list
    waiting_list_count = total_waiting_list(df)
    print(f"\n=== Waiting List Analysis ===")
    print("-" * 35)
    print(f"Total passengers on waiting list: {waiting_list_count}")
    
    # 2. Find the highest ticket price
    max_price, seat_with_max_price = highest_ticket_price(df)
    print(f"\n=== Highest Ticket Price ===")
    print("-" * 30)
    print(f"Highest ticket price: ${max_price}")
    print(f"Seat number: {seat_with_max_price}")
    
    # 3. Find the number of available seats
    available_count = available_seats(df)
    print(f"\n=== Available Seats ===")
    print("-" * 25)
    print(f"Number of available seats: {available_count}")
    
    # Additional analysis
    print(f"\n=== Additional Analysis ===")
    print("-" * 30)
    
    # Show available seats details
    available_df = get_available_seats_details(df)
    if len(available_df) > 0:
        print("Available seats:")
        for index, row in available_df.iterrows():
            print(f"  • Seat {row['Seat Number']}: ${row['Ticket Price']}")
    
    # Show reserved seats details
    reserved_df = get_reserved_seats_details(df)
    if len(reserved_df) > 0:
        print("\nReserved seats:")
        for index, row in reserved_df.iterrows():
            print(f"  • Seat {row['Seat Number']}: {row['Passenger Name']} - ${row['Ticket Price']}")
    
    # Find cheapest available seat
    cheapest_price, cheapest_seat = find_cheapest_available_seat(df)
    if cheapest_price is not None:
        print(f"\nCheapest available seat: {cheapest_seat} at ${cheapest_price}")
    
    # Summary statistics
    print(f"\n=== Summary Statistics ===")
    print("-" * 30)
    total_seats = len(df)
    total_revenue = df[df['Availability'] == False]['Ticket Price'].sum()
    potential_revenue = df['Ticket Price'].sum()
    occupancy_rate = (total_seats - available_count) / total_seats * 100
    
    print(f"Total seats: {total_seats}")
    print(f"Available seats: {available_count}")
    print(f"Reserved seats: {total_seats - available_count}")
    print(f"Occupancy rate: {occupancy_rate:.1f}%")
    print(f"Current revenue: ${total_revenue}")
    print(f"Potential revenue: ${potential_revenue}")
    
    # Return results for potential further processing
    return {
        'waiting_list_count': waiting_list_count,
        'highest_price': max_price,
        'seat_with_highest_price': seat_with_max_price,
        'available_seats_count': available_count,
        'available_seats_details': available_df,
        'reserved_seats_details': reserved_df,
        'summary': {
            'total_seats': total_seats,
            'occupancy_rate': occupancy_rate,
            'current_revenue': total_revenue,
            'potential_revenue': potential_revenue
        }
    }

# Unit tests for the functions
class TestRailwayReservation(unittest.TestCase):
    
    def setUp(self):
        """Set up test data"""
        self.test_df = pd.DataFrame({
            'Seat Number': [101, 102, 103],
            'Passenger Name': ['John', 'Alice', 'Bob'],
            'Ticket Price': [250, 300, 400],
            'Availability': [True, False, True]
        })
    
    def test_total_waiting_list(self):
        """Test waiting list count function"""
        result = total_waiting_list(self.test_df)
        self.assertEqual(result, 1)  # Only Alice has unavailable seat
    
    def test_highest_ticket_price(self):
        """Test highest ticket price function"""
        max_price, seat_number = highest_ticket_price(self.test_df)
        self.assertEqual(max_price, 400)
        self.assertEqual(seat_number, 103)
    
    def test_available_seats(self):
        """Test available seats count function"""
        result = available_seats(self.test_df)
        self.assertEqual(result, 2)  # John and Bob have available seats

if __name__ == "__main__":
    # Run the main program
    results = main()
    
    # Optionally run unit tests
    print("\n" + "="*50)
    print("Running Unit Tests...")
    print("="*50)
    unittest.main(argv=[''], exit=False, verbosity=2)
