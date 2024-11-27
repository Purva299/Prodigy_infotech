# Function to encrypt the message
def encrypt(text, shift):
    result = ""
    # Loop through each character in the text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # For spaces and other characters, append them as is
            result += char
    return result

# Function to decrypt the message
def decrypt(text, shift):
    return encrypt(text, -shift)

# Main program
if _name_ == "_main_":
    # Get the user's input
    message = input("Enter the message: ")
    shift_value = int(input("Enter the shift value: "))

    # Encrypt the message
    encrypted_message = encrypt(message, shift_value)
    print(f"Encrypted message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, shift_value)
    print(f"Decrypted message: {decrypted_message}")