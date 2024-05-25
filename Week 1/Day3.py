from sympy import  factorint
import math

"""
THIS LAB: OOP for prime number: using OOP
- check integer number
- check positive number
- factorize number using sympy
- pseudoprime
- Carmichael number
"""

class NumberTheory:
    def __init__(self, number):
        self.number = self.check_positive(number)

    def check_positive(self, number):
        while True:
            # avoid that the user enter the string,... like that
            try:
                # negative integer
                if(int(number) < 0):
                    print("Error: Please enter a positive integer.")
                    number = int(input("Enter the positive integer: "))
                else:
                    return number
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
                number = -1

    def check_prime(self):
        # the factor not exceeding sqrt of number
        for i in range(2, int(math.sqrt(self.number)) + 1):
            if self.number % i == 0:
                return False
        return True
    
    def factorize_number(self):
        # save into string like "5*1 + 2*1"
        string = ""

        # using function factorint of sympy to get factor
        factor = factorint(self.number)

        # get all keys into dictionary
        for i in factor.keys():
            string += str(i) + "*" + str(factor[i])
            string += "+"

        # not get + in the last
        return string[:-1]
    
    def pseudo_prime(self, base):
        # pseudo prime is composite, so we check composite
        if (not self.check_prime()):
            if((base ** self.number - base) % self.number == 0):
                return True
        return False
    
    def Carmichael_number(self):
        # check composite number
        if (not self.check_prime()):
            factor = factorint(self.number)
            for i in  factor.keys():
                if((self.number-1) % (i-1) != 0):
                    return False
            return True

        
# Create an instance of the class
nt = NumberTheory(10)
nt1 = NumberTheory(-10)
nt2 = NumberTheory("string")


# number 
print(f"You have entered: {nt.number}")
print(f"You have entered: {nt1.number}")
print(f"You have entered: {nt2.number}")



# check prime
nt = NumberTheory(10)
if (nt.check_prime()):
    print(f"Check prime: Prime")
else:
    print(f"Check prime: Composite")

nt = NumberTheory(7)
if (nt.check_prime()):
    print(f"Check prime: Prime")
else:
    print(f"Check prime: Composite")

# factorize the number
nt = NumberTheory(1764)
print(f"Factorize the number: {nt.factorize_number()}")

nt = NumberTheory(23)
print(f"Factorize the number: {nt.factorize_number()}")

# pseudo prime base
nt = NumberTheory(561)
base = int(input("Enter the base: "))
if (nt.pseudo_prime(base)):
    print(f"Pseudo prime {nt.number} base {base}")
else:
    print(f"Not Pseudo prime {nt.number} base {base}")

# carmicheal number
nt = NumberTheory(6601)
if (nt.Carmichael_number()):
    print(f"{nt.number} is Carmecheal number")
else:
    print(f"{nt.number} is not Carmecheal number")
