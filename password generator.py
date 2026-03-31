import random 

latters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']
# easy level

print("welcome to password generator")
password = ""
n_latter=int(input("how many latters do you want in your password:"))
for i in range(0,n_latter):
    password+=random.choice(latters)

n_number=int(input("how many numbers do you want in your password:"))
for j in range(0,n_number):
    password+=random.choice(numbers)

n_symbols=int(input("how many symbols do you want in your password:"))
for k in range(0,n_symbols): 
    password+=random.choice(symbols)
print(password)

# hard level by me

print("welcome to password generator")
password = []
n_latter=int(input("how many latters do you want in your password:"))
for i in range(0,n_latter):
    password+=random.choice(latters)
   
n_number=int(input("how many numbers do you want in your password:"))
for j in range(0,n_number):
    password+=random.choice(numbers)

n_symbols=int(input("how many symbols do you want in your password:"))
for k in range(0,n_symbols): 
    password+=random.choice(symbols)
n_password=""

lenght=len(password)
for l in range(0,lenght):
    n_password+=random.choice(password)

print(n_password)
