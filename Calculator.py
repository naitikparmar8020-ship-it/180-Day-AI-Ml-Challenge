#TODO-1 write out the other 3 functions - substract,multiply and divide
def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

#TODO-2 add these 4 functions into a dictionary as the values,(keys= + * - /)

operation={
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
#TODO-3 use the dictionary operation to perform the calculations multiply 4*8 using dictionary

# multiply=operation["*"]
# print(multiply(4,8))
print("welcome to the Maths world..Let's get start....")
should_be=True
n1=int(input("Enter a first number:-"))
while should_be:

  oprtn=input("which mathematical operation does you have to perform \n for addition--> + \n for substraction -- - \n for multiplication-->* \n for division / \n")

  n2=int(input("Enter a second number:-"))

  n1=operation[oprtn](n1,n2)
  print(f"current sum is: {n1}")
  again=input("do you want to perform operation with your previous result 'Yes' or 'No").lower()

  if again=="yes":
    should_be=True
  elif again=="no":
    should_be=False
  else:
    print("Invalid input. Ending calculation.")
    should_be = False


print(f"final result is {n1}")


