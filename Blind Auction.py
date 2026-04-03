auc=r'''
                         ___________
                         \         /
                          )_______(
                          ||""""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )""""""""(
                         /__________\
                         `'-------'`
                       .-------------.
                      /_______________\  '''

print(auc)
print("welcome to blind auction")
print("let's start the auction")
bid=[]
should_be = True

while should_be:
  name=input("Enter Your Name:")
  price=int(input("Enter Your Bid Price $ "))
  again=input("If there is any other person who want to Bid For this Auction Yes or NO ").lower()
  if again == "yes":
    print("\n" * 100)
  if again == "no":
    should_be= False

  auction_dict={
      "name": name,
      "price":price
}
  bid.append(auction_dict)

highest_item = max(bid, key=lambda x: x['price'], default=None)

if highest_item:
    print("\n"*100)
    print(f"Congratlation!! Winner is the: {highest_item['name']} with bid  {highest_item['price']} ")
else:
    print("The list is empty!")

