'''
Write a script that inputs a line of plaintext and a distance value and outputs an encrypted text using a Caesar cipher.

The script should work for any printable characters.

An example of the program input and output is shown below:

Enter a message: Hello world!
Enter the distance value: 4

Lipps${svph%
'''

plain_text = input("Enter messege (must be lowercase): ")
distance = int(input("Enter distance value: "))
code = ""

for letter in plain_text:
    ord_value = ord(letter)
    cipher_value = ord_value + distance
    if cipher_value > (ord("z") + 1):
        cipher_value = ord("a") + distance - \
                       (ord("z") - ord_value + 1)
    code += chr(cipher_value)
print(code)
