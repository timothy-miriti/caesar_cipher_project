from colorama import Fore, Style, init
init(autoreset=True)

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"{Style.BRIGHT}Here is the text after encryption: {Fore.GREEN}{cipher_text}")

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"{Style.BRIGHT}Here is the text after decryption: {Fore.GREEN}{plain_text}")

        

wanna_end=False
while not wanna_end:  
    what_to_do = input(f"{Fore.YELLOW}Type 'encrypt' for encryption, type 'decrypt' for decryption:\n ")
    text = input(f"{Fore.MAGENTA}{Style.BRIGHT}Type your message:\n ").lower()
    shift = int(input(f"{Fore.BLUE}{Style.BRIGHT}Type the shift key:\n "))

    if what_to_do == "encrypt":
        encryption(plain_text=text, shift_key=shift)
    elif what_to_do == "decrypt":
        decryption(cipher_text=text, shift_key=shift)
    else:    print(f"{Fore.RED}{Style.BRIGHT}Invalid input. Please type 'encrypt' or 'decrypt'.")
    play_again = input(f"{Fore.YELLOW}Do you want to play again? Type 'yes' or 'no':\n ")
    if play_again.lower() == "no":
        wanna_end = True
        print(f"{Fore.GREEN}{Style.BRIGHT}Thank you for using the Caesar Cipher program. Goodbye!")