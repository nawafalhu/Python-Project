
print("Welcome to the secret auction program.")
bid = {}

def height(bides) :
    max = 0
    winner = None
    for bid in bides : 
        if max < bides[bid] : 
            max = bides[bid]
            winner = bid
    print(f"The winner is {winner} with a bid of ${max}")

while any != "no":
    name = input("What is your name?: ")
    price = int(input("What's your bid?: "))
    bid[name] = price
    any = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
height(bid)


