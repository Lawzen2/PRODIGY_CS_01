def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("> Caesar Cipher Program")
    print(">> Choose an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    
    choice = input(">> Enter your choice (1 or 2): ")
    message = input(">> Enter your message: ")
    shift = int(input(">> Enter the shift value: "))

    if choice == '1':
        result = caesar_encrypt(message, shift)
        print(">> Encrypted message:", result)
    elif choice == '2':
        result = caesar_decrypt(message, shift)
        print(">> Decrypted message:", result)
    else:
        print(">> Invalid choice.")

if __name__ == "__main__":
    main()
