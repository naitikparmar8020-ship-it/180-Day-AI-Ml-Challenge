alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']

def ceaser(original_text,shift_number,encode_decode):
    cipher_text=""
    if encode_decode=="decode":
        shift_number *= -1
    for i in original_text:
        if i not in alphabet:
            cipher_text += i
        else:
            shifted_position=alphabet.index(i) + shift_number           
            shifted_position %= len(alphabet) 
            cipher_text+=alphabet[shifted_position]
                
    print(cipher_text)
    

should_continue = True
while should_continue:
    direction=input("type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
    text=input("type a msg :\n")
    shift=int(input("type the shift number\n"))
    ceaser(original_text=text,shift_number=shift,encode_decode=direction)
    
    again=input("do you want to run the caesar cipher again? type 'yes' if you want or say 'no'\n").lower()
    if again == "no":
        should_continue = False
        print("Thank you!!")
