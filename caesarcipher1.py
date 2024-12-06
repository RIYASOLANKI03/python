alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=input(" type 'encode' to encrypt,type 'decode'to decrypt:\n").lower()
text=input("type your message:\n").lower()
shift=int(input("type the shift number:\n "))

def encrypt(original_text,shift_command):
    cipher_text = " "

    for letter in original_text:
        shifted_position=alphabets.index(letter)+shift_command

        shifted_position%=len(alphabets)
        cipher_text += alphabets[shifted_position] 

    print(f"here is the encoded result:{cipher_text}")
encrypt(original_text=text,shift_command=shift)


