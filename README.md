 PRODIGY_CS_01 — Caesar Cipher

This repository contains a simple Python script that demonstrates how the Caesar Cipher works. The Caesar Cipher is a basic encryption technique that shifts each letter in a message by a certain number of positions in the alphabet.

Features

- Encrypts messages using a shift value
- Decrypts messages using the same shift
- Supports both uppercase and lowercase letters
- Non-letter characters (punctuation, spaces, etc.) are not affected

How to Run

1. Make sure Python 3 is installed on your system.
2. Clone the repository or download the script.
3. Open a terminal in the project folder and run:

```bash
python3 caesar_cipher.py
```

4. Follow the instructions shown in the terminal.

Example

```
> Caesar Cipher Program
>> Choose an option:
1. Encrypt
2. Decrypt
>> Enter your choice (1 or 2): 1
>> Enter your message: Hello, World!
>> Enter the shift value: 3
>> Encrypted message: Khoor, Zruog!
```

Note

Make sure your script includes the correct entry point:

```python
if __name__ == "__main__":
    main()
```

If it's written like this:

```python
if _name_ == "_main_":
```

…it won't work — those underscores matter.
