#the purpose of this program is to create a program that utilises one time pads, however using the same pad multiple times to see if
#it can be easily decrypted by an attacker
import secrets
#more secure random key generation

messages = []
with open("your msgs.txt", "r") as f:
    for line in f.readlines():
        msg, nline = line.split("\n")
        messages.append(line)
#use an external text file to prevent people seeing the messages in the code

encrypted_messages = []
key_length = len(max(messages, key = len))
#length of the longest item in list in bytes
key = secrets.token_bytes(key_length)
#generates a random key (in binary form) to encrypt the messages
key_int = int.from_bytes(key, byteorder = "big")
#converts to an integer for easy XORing with the plaintext 
 
for msg in messages:
    binary_msg = int.from_bytes(msg.encode(), byteorder="big")
    #converts the message into binary then an integer
    trunc_key = int.from_bytes(key[:len(msg)], byteorder="big")
    #truncates the key to the length of the message so bitwise xor is correct
    cipher_msg = trunc_key ^ binary_msg
    #XORs the key with the message to produce the ciphertext
    encrypted_messages.append(cipher_msg)

#user input
print("Hello, welcome to this codebreaking exercise. Below are some messages someone stupidly used the same one time pad to encrypt with multiple times:")
for msg in encrypted_messages:
    print(msg)
print("Your goal is to find the key (in integer form) used to encrypt these messages, as well as the original messages. Enter q to give up")

while True:
    attempt = input("Enter key: ")
    try:
        attempt = int(attempt)
    except ValueError:
        if attempt != "q":
            print("Invalid command, enter q to quit or an integer key to guess")
            
    if attempt == "q":
        print(f"The correct key was {key_int}\nThe messages were:")
        for msg in messages:
            print(msg)
        break
    elif attempt == key_int:
        print(f"Correct! {key_int} was the correct key \nThe messages were:")
        for msg in messages:
            print(msg)
        break
    else:
        print("That is incorrect, try again")

