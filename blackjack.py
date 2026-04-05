import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10] #here 3 time 10 means J,K,Q 

deal=input("Enter Deal to start game:- ")

# Initialize cards correctly using random.choice to allow duplicates (like two Aces)
user_card = [random.choice(cards), random.choice(cards)]
dealer_card = [random.choice(cards), random.choice(cards)]

should_continue=True
while should_continue:
    sum_of_user_card = sum(user_card)
    sum_of_dealer_card = sum(dealer_card)

    # Handle Ace (11) replacing it with 1 if over 21
    if sum_of_user_card > 21 and 11 in user_card:
        user_card.remove(11)
        user_card.append(1)
        sum_of_user_card = sum(user_card)

    print(f"Your cards are: {user_card}, current score: {sum_of_user_card}")
    print(f"Dealer's first card is: {dealer_card[0]}")

    if sum_of_user_card > 21:
        print("You went over. You lose!")
        should_continue = False
    else:
        hit = input("Do you want one more card? 'Yes' or 'No' : ").lower()
        if hit == "yes":
            user_card.append(random.choice(cards))
        else:
            should_continue = False

#  Dealer's turn (only if user hasn't busted)
if sum_of_user_card <= 21:
    # Handle potential two aces in dealer's initial hand
    if sum(dealer_card) > 21 and 11 in dealer_card:
        dealer_card.remove(11)
        dealer_card.append(1)
        
    while sum(dealer_card) < 17:
        dealer_card.append(random.choice(cards))
        if sum(dealer_card) > 21 and 11 in dealer_card:
            dealer_card.remove(11)
            dealer_card.append(1)
            
    sum_of_dealer_card = sum(dealer_card)
    print(f"\nYour final hand: {user_card}, final score: {sum_of_user_card}")
    print(f"Dealer's final hand: {dealer_card}, final score: {sum_of_dealer_card}")

    # Determine Winner
    if sum_of_dealer_card > 21:
        print("Dealer went over. You Win!")
    elif sum_of_dealer_card > sum_of_user_card:
        print("Dealer Wins")
    elif sum_of_user_card > sum_of_dealer_card:
        print("Congratulation You Win!")
    else:
        print("It's a draw!")
