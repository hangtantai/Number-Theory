"""
THIS LAB: Algorithm for check prime
- Rabin Miller
- Trial Division
- Soloway Strassen
"""


import math
import random
import timeit

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1 + 1):
        a_to_power = pow(a, (2**i) * d, n)
        if a_to_power == n-1:
            return True
    return a_to_power == n-1

# exponentiation  
def modulo(base, exponent, mod):  
    x = 1;  
    y = base;  
    while (exponent > 0):  
        if (exponent % 2 == 1):  
            x = (x * y) % mod;  
  
        y = (y * y) % mod;  
        exponent = exponent // 2;  
  
    return x % mod;  
  
# To calculate Jacobian symbol of a 
# given number  
def calculateJacobian(a, n):  
  
    if (a == 0):  
        return 0;# (0/n) = 0  
  
    ans = 1;  
    if (a < 0):  
          
        # (a/n) = (-a/n)*(-1/n)  
        a = -a;  
        if (n % 4 == 3):  
          
            # (-1/n) = -1 if n = 3 (mod 4)  
            ans = -ans;  
  
    if (a == 1):  
        return ans; # (1/n) = 1  
  
    while (a):  
        if (a < 0): 
              
            # (a/n) = (-a/n)*(-1/n)  
            a = -a;  
            if (n % 4 == 3): 
                  
                # (-1/n) = -1 if n = 3 (mod 4)  
                ans = -ans;  
  
        while (a % 2 == 0):  
            a = a // 2;  
            if (n % 8 == 3 or n % 8 == 5):  
                ans = -ans;  
  
        # swap  
        a, n = n, a;  
  
        if (a % 4 == 3 and n % 4 == 3):  
            ans = -ans;  
        a = a % n;  
  
        if (a > n // 2):  
            a = a - n;  
  
    if (n == 1):  
        return ans;  
  
    return 0;  
  
class PrimalityTest:
    def __init__(self, number):
        self.number = self.check_positive_int(number)
    
    def check_positive_int(self, number):
        while True:
            # avoid that the user enter the string,... like that
            try:
                # negative integer
                if(int(number) < 0 or isinstance(number, float) == True):
                    print("Error: Please enter a positive integer.")
                    number = int(input("Enter the positive integer: "))
                else:
                    return number
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
                number = -1
    
    def trial_division(self):
        for i in range(2, int(math.sqrt(self.number)) + 1):
            if (self.number % i == 0):
                return False
        return True
    
    def miller_rabin(self):
        d = self.number - 1
        s = 0
        while d % 2 == 0:
            d >>= 1
            s += 1
        for repeat in range(20):
            a = 0
            while a == 0:
                a = random.randrange(self.number)
            if not miller_rabin_pass(a, s, d, self.number):
                return False
        return True
            

    # To perform the Solovay- Strassen  
    def solowayStrassen(self):  
        if (self.number < 2):  
            return False;  
        if (self.number != 2 and self.number % 2 == 0):  
            return False;  
    
        for i in range(20): 
            
            # Generate a random number a  
            a = random.randrange(self.number - 1) + 1;  
            jacobian = (self.number + calculateJacobian(a, self.number)) % self.number;  
            mod = modulo(a, (self.number - 1) / 2, self.number);  
    
            if (jacobian == 0 or mod != jacobian):  
                return False
        return True
    
    def menu(self):
        print("-"* 50)
        print("MENU: ")
        print("1. Apply each algorithm for number")
        print("2. Compare run execution")
        print("3. Exit")
        print("-"* 50)
        while True: 
            press = input("Enter the application: ")
            if (press == "1"):
                # Measure the execution times
                time_trial = timeit.timeit(self.trial_division, number=1000)
                time_rabin = timeit.timeit(self.miller_rabin, number=1000)
                time_soloway = timeit.timeit(self.solowayStrassen, number=1000)
                result = self.trial_division()
                print(f"Number: {self.number}, Trial Division: {result} and time execution: {time_trial}")
                result = self.miller_rabin()
                print(f"Number: {self.number}, Miller Rabin: {result} and time execution: {time_rabin}")
                result = self.solowayStrassen()
                print(f"Number: {self.number}, Soloway Strassen: {result} and time execution: {time_soloway}")
            elif (press == "2"):
                # Measure the execution times
                time_trial = timeit.timeit(self.trial_division, number=1000)
                time_rabin = timeit.timeit(self.miller_rabin, number=1000)
                time_soloway = timeit.timeit(self.solowayStrassen, number=1000)

                # Compare
                times = [('Trial Division', time_trial), ('Miller Rabin', time_rabin), ('Soloway Strassen', time_soloway)]
                times.sort(key=lambda x: x[1])  # Sort by execution time

                # Print comparison
                for i, (name, time) in enumerate(times):
                    if i == 0:
                        print(f"{name} is the fastest algorithm with a time of {time} seconds.")
                    else:
                        print(f"{name} is slower than {times[i-1][0]} with a time of {time} seconds.")
            else:
                print("Good Bye")
                break
            
    

# # test case 1
# nt = PrimalityTest(997)
# nt.menu()

# # test case 2
# p = 1013
# q = 1031
# number = p*q
# nt = PrimalityTest(number)
# nt.menu()

# test case 3
number = 10000019
nt = PrimalityTest(number)
nt.menu()
