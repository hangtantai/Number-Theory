"""
THIS LAB: SOME ALGORITHM TO FIND PRIME FACTOR OF INTEGER
- Trial Division
- Pollard Rho
- Pollard Rho Minus 1
- Menu: - time execution - compare 3 algorithm
"""


# import library necessary
import math
import timeit

# function for pollard rho
# find greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

# function: f(x) = x^2 + 1
def mapx(x,n):
    # calculate f(xi) modulo n
    x = (x*x+1) % n
    return x

# class
class FactorInteger:
    def __init__(self, number):
        self.number = number
    
    
    def trial_factorization(self):
        number = self.number
        factors = []

        # Check for divisibility by 2
        while number % 2 == 0:
            number = number // 2
            factors.append(2)

        # Check for divisibility by odd numbers
        for i in range(3, int(math.sqrt(number))+1, 2): 
            while number % i == 0:
                number = number // i
                factors.append(i)
                    
        if number > 2:
            factors.append(number)
        
        return factors
    
    def pollard_rho(self):
        number = self.number
        # initial start point
        x1 = 2
        x2 = 2

        while True:
            # calculate x1
            x1 = mapx(x1,number)

            # calculate x2
            x2 = mapx(mapx(x2,number), number)
            p = gcd(x1-x2,number)

            # this is a prime, not exist factor
            if (p == number):
                return number
            # p is a factor of n
            elif (p!=1):
                return p
            
 
    def polard_rhominus1(self):  
        number = self.number
        # initial base and expo
        a = 2
        i = 2

        while True:
            # fast modulo
            a = (a**i) % number
            d = gcd(a-1, number)

            # factor
            if d > 1:
                return d
            # expo increasement
            i += 1
    
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
                time_trial = timeit.timeit(self.trial_factorization, number=1000)
                time_rho = timeit.timeit(self.pollard_rho, number=1000)
                time_rho_1 = timeit.timeit(self.polard_rhominus1, number=1000)
                result = self.trial_factorization()
                print(f"Number: {self.number}, Trial Factorization: {result} and time execution: {time_trial}")
                result = self.pollard_rho()
                print(f"Number: {self.number}, Pollard Rho: {result} and time execution: {time_rho}")
                result = self.polard_rhominus1()
                print(f"Number: {self.number}, Pollard Rho Minus 1: {result} and time execution: {time_rho_1}")
            elif (press == "2"):
                # Measure the execution times
                time_trial = timeit.timeit(self.trial_factorization, number=1000)
                time_rho = timeit.timeit(self.pollard_rho, number=1000)
                time_rho_1 = timeit.timeit(self.polard_rhominus1, number=1000)

                # Compare
                times = [('Trial Division', time_trial), ('Pollard Rho', time_rho), ('Pollard Rho Minus 1', time_rho_1)]
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


# test case 1
# prime
# nt = FactorInteger(997)
# nt.menu()
# composite
# nt = FactorInteger(998)
# nt.menu()

# # # test case 2
# p, q, r = 10007, 10009, 10037
# number = p * q * r
# nt = FactorInteger(number)
# nt.menu()

# test case 3
number = 1234567
nt = FactorInteger(number)
nt.menu()
