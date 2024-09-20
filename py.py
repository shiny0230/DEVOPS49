from datetime import datetime

def main():
    # Get current year
    current_year = datetime.now().year
    
    # Get user input
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    
    # Calculate birth year
    birth_year = current_year - age
    
    # Output result
    print(f"Hello, {name}! You were born in {birth_year}.")

if __name__ == "__main__":
    main()
