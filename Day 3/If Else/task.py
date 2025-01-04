def main():
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))
    measurement(height)

def measurement(h):
    if h > 120:
        print("You are eligible for a ride")
    else:
        print("You are not eligible for a ride")

main()
