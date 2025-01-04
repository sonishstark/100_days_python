def main():
    number = int(input("Enter an number: "))
    odd_even(number)

def odd_even(n):
    if n % 2 == 0:
        print(f"{n} is an Even number")
    else:
        print(f"{n} is an Odd number")

main()
#check for day 3

