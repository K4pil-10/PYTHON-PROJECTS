from logo import logo
print("Welcome to the auction!")
print(logo)

def find_highest_bidder(bidding_dictionary):
    winner= ""
    highest_bid= 0
    for bidder in bidding_dictionary:
        bid_amount= bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid= bid_amount
            winner= bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids= {}
continue_bidding= True
while continue_bidding:
    name = input("What is your name?: ").lower()
    cost = int(input("What is your bid?: $"))
    bids[name] = cost
    should_continue = input("Are there any bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding= False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" *20)
