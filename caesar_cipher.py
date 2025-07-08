def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            if mode == 'encrypt':
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char
    return result

print("=== Caesar Cipher ===")
text = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

output = caesar_cipher(text, shift, mode)
print(f"\nResult: {output}")
