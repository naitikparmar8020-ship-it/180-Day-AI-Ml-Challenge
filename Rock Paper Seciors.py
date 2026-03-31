# let's make a game rock paper and seciors
import random
print("Welcome to rock paper and seciors game\n")
print("0 for rock\n1 for paper\n2 for seciors\n")
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")

seciors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

num=int(input("Enter a number:-"))

if num == 0:
    print(rock)
elif num == 1:
    print(paper)
elif num == 2:
    print(seciors)

com=random.randint(0,2)

if com == 0:
    print("Computer Choose Rock"+rock)
elif com==1:
    print("Computer Choose Paper"+paper)
elif com==2:
    print("Computer Choose Seciors"+seciors)


# now it's time to set rule

if (com == 0 and num == 2) or (com == 1 and num == 0) or (com == 2 and num == 1) :
    print("computer wins")
elif (com ==1 and num == 2) or (com == 2 and num == 0) or (com == 0 and num == 1):
    print("You Wins")
else:
    print("you both select same")
