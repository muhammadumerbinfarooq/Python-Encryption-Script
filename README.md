Sure! Here's a well-formatted `README.md` file for your encryption and decryption script:

```markdown
# Caesar Cipher Encryption and Decryption

This Python script provides a simple implementation of the Caesar Cipher for both encryption and decryption of text. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features

- Encrypts text using a specified shift value.
- Decrypts text using the same shift value.
- Handles both uppercase and lowercase letters.
- Preserves non-alphabetic characters (e.g., punctuation, spaces).

## Usage

1. **Encryption**: Enter the text you want to encrypt and the shift value.
2. **Decryption**: The script will automatically decrypt the encrypted text using the same shift value.

## Example

```python
def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift value: "))
    encrypted_text = encrypt(text, shift)
    print("Encrypted text:", encrypted_text)
    decrypted_text = decrypt(encrypted_text, shift)
    print("Decrypted text:", decrypted_text)
```

### Sample Output

```
Enter text to encrypt: Hello, World!
Enter shift value: 3
Encrypted text: Khoor, Zruog!
Decrypted text: Hello, World!
```

## How It Works

- **Encryption**: Each letter in the input text is shifted by the specified number of places. Uppercase and lowercase letters are handled separately to maintain their case.
- **Decryption**: The decryption function uses the same logic as encryption but with a negative shift value to reverse the process.

## Requirements

- Python 3.x

## Running the Script

1. Save the script to a file, e.g., `caesar_cipher.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using Python:

```sh
python caesar_cipher.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

