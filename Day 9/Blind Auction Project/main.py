# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)

def highest_bidder(bidders):
    highest_value = max(bidders, key=bidders.get)
    print(f"The highest bidder is {highest_value} with a bid of ${bidders[highest_value]}")


more_bidders = True
bidders ={}
while more_bidders:
    name = input("What is your name?:")
    bid_amount = int(input("What is your bid?:"))
    bidders[name]= bid_amount
    print(bidders)
    other_bidders = input("Are there other bidders? Type 'Yes' or 'No': ").lower()
    if other_bidders == "yes":
        print("\n"*20)
    elif other_bidders == "no":
        more_bidders = False

highest_bidder(bidders)
