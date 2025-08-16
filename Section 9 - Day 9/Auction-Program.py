# Auction Program

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    
    # Loop through dictionary to find the highest bidder
    for bidder, bid_amount in bidding_dictionary.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"\nThe winner is {winner} with a bid of ${highest_bid}.")


# Store bids
bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    
    # Save the bid
    bids[name] = price
    
    # Ask if more bidders are present
    should_continue = input("Are there other bidders? Type 'yes' or 'no': ").lower()
    
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)  # Clear screen for next bidder