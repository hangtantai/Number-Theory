# import necessary libraries
import math

# Function to find the greatest common divisor of two numbers
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

# Function to find the param d in exponential cipher
def mod_inverse(base, modulus):
    gcd, x, _ = extended_gcd(base, modulus)
    if gcd != 1:
        # modular inverse does not exist
        return None
    else:
        return x % modulus

class Cipher:
    def encrypt_caesar(self, plaintext, shift):
        # define ciphertext as an empty string
        ciphertext = ""

        # loop for each character in the plaintext
        for char in plaintext:

            # check if the character is an alphabet
            if char.isalpha():
                # get the ASCII offset based on the case of the character
                ascii_offset = ord('A') if char.isupper() else ord('a')

                # Because ord value is 97-122, so we need to subtract ascii_offset 'a' to normalize it to 0-25
                # then modulo 26 based on the formula, and add the ascii_offset back to use the chr function to convert to character
                encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)

                # append the encrypted character to the ciphertext
                ciphertext += encrypted_char
            
            # if the character is not an alphabet, just append it to the ciphertext, not encrypted
            else:
                ciphertext += char
        return ciphertext

    def decrypt_caesar(self, ciphertext, shift):
        # Basically, the decryption is the same as encryption, but with a negative shift( with this shift = -shift)
        return self.encrypt_caesar(ciphertext, -shift)

    def encrypt_affine(self, plaintext, a, b):
        # define ciphertext as an empty string
        ciphertext = ""

        # loop for each character in the plaintext
        for char in plaintext:

            # check if the character is an alphabet
            if char.isalpha():

                # The same with encrypt_caesar
                ascii_offset = ord('A') if char.isupper() else ord('a')

                # The formula for affine cipher is (a*x + b) mod 26
                encrypted_char = chr(((ord(char) - ascii_offset) * a + b) % 26 + ascii_offset)
                ciphertext += encrypted_char
            
            # if the character is not an alphabet, just append it to the ciphertext, not encrypted
            else:
                ciphertext += char
        return ciphertext

    def decrypt_affine(self, ciphertext, a, b):
        # Modular multiplicative inverse of a
        # pow function, with (number, -1, modulus) is the same as number^-1 mod modulus: inverse of a
        inverse_a = pow(a, -1, 26)  

        # C = aP + b mod 26 => P = a^-1(C - b) mod 26, this shift are (a^-1, -b*a^-1)
        return self.encrypt_affine(ciphertext, inverse_a, -inverse_a * b)

    def encrypt_exponential(self, plaintext, base, modulus):
        # define ciphertext as an empty string
        ciphertext = ""
        
        # remove all spaces from plaintext
        plaintext = plaintext.replace(" ", "")

        # to calculate m param: example 25 -> m = 1, so on
        m = int(math.log10(modulus)) - 1
        
        # split plaintext into blocks of size 2m
        blocks = [plaintext[i:i+m] for i in range(0, len(plaintext), m)]

        # check if last character is one character, add 'X' to make it two characters
        if (len(blocks[-1]) == 1):
            blocks[-1] += 'X'

        # loop for each block in the plaintext
        for block in blocks:
            
            # empty string to store the encrypted block
            encrypted_block = ""

            # loop for each character in the block
            for char in block:
                # check if the character is an alphabet
                if char.isalpha():

                    # The same with encrypt_caesar
                    ascii_offset = ord('A') if char.isupper() else ord('a')

                    # The formula for exponential cipher is (x^base) mod modulus
                    normal_char = ord(char) - ascii_offset

                    # if the encrypted_char is a single digit number, add a leading zero
                    if 0 <= normal_char <= 9:
                        encrypted_block += '0' + str(normal_char)
                    else:
                        encrypted_block += str(normal_char)
                
            # the formula for exponential cipher is (x^base) mod modulus
            encrypted_number = pow(int(encrypted_block), base, modulus)

            # add zeros to the left of the encrypted number if it is less than 2m
            if(len(str(encrypted_number)) < 2*m):
                encrypted_number = "0"*(2*m - len(str(encrypted_number))) + str(encrypted_number)
            ciphertext += str(encrypted_number)
                
        return ciphertext

    def decrypt_exponential(self, ciphertext, base, modulus):
        # define plaintext as an empty string
        plaintext = ""

        # d param
        inverse_base = pow(base, -1, modulus - 1)  

        # to calculate m param
        m = int(math.log10(modulus)) - 1

        # split plaintext into blocks of size 2m
        blocks = [ciphertext[i:i+2*m] for i in range(0, len(ciphertext), 2*m)]

        # loop for each block in the ciphertext
        for block in blocks:
            # perform decryption operation
            decrypted_number = pow(int(block), inverse_base, modulus)

            # add zeros to the left of the decrypted number if it is less than 2m
            if(len(str(decrypted_number)) < 2*m):
                decrypted_number = "0"*(2*m - len(str(decrypted_number))) + str(decrypted_number)
            
            # convert into string
            decrypted_number = str(decrypted_number)
            
            # convert the decrypted number back to characters and append them to the plaintext
            text = ''
            for i in range(0, len(decrypted_number)-1, 2):
                ascii_offset = ord('A')
                text += chr(ascii_offset + int(decrypted_number[i:i+2]))
            plaintext += text
                
        return plaintext

# Create an instance of the class
cipher = Cipher() 
plain_text = "LIFE IS A DREAM"

# # Test case 1
# shift = 3
# encrypt_ceasar = cipher.encrypt_caesar(plain_text, shift)
# print("ENCRYPT CAESAR: ", encrypt_ceasar)

# decrypt_ceasar = cipher.decrypt_caesar(encrypt_ceasar, shift)
# print("DECRYPT CAESAR: ", decrypt_ceasar)

# # Test case 2
# a = 5
# b = 8
# encrypt_affine = cipher.encrypt_affine(plain_text, a, b)
# print("ENCRYPT AFFINE: ", encrypt_affine)

# decrypt_affine = cipher.decrypt_affine(encrypt_affine, a, b)
# print("DECRYPT AFFINE: ", decrypt_affine)


# Test case 3
e = 43
n = 2633
encrypt_exponential = cipher.encrypt_exponential(plain_text, e, n)
print("ENCRYPT EXPONENTIAL: ", encrypt_exponential)

# The way 1: using pow function to calculate d
decrypt_exponential = cipher.decrypt_exponential(encrypt_exponential, e, n)
print("DECRYPT EXPONENTIAL: ", decrypt_exponential)