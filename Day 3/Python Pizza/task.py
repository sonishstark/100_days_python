print("Welcome to Python Pizza Deliveries!")

# Inputs
size = input("What size pizza do you want? S, M, or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# Initialize total
total = 0

# Calculate crust size cost
if size == "S":
    total += 15
elif size == "M":
    total += 20
elif size == "L":
    total += 25
else:
    print("Invalid size selected.")

# Add pepperoni cost
if pepperoni == "Y":
    if size == "S":
        total += 2
    else:  # For M or L
        total += 3

# Add extra cheese cost
if extra_cheese == "Y":
    total += 1

# Output the total
print(f"Your final bill is: ${total}.")





