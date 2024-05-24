"""
THIS LAB:
- Euclid extended
- Bezout Coeficient
- Chinese Remainder
"""

# assume that a,b is input
def euclid_extended(u, v):
    # define coef
    u1, u2, u3 = 1, 0, u
    v1, v2, v3 = 0, 1, v

    # loop until v3 == 0
    while v3 != 0:
        q = u3 // v3
        t1, t2, t3 = u1 - q * v1, u2 - q * v2, u3 - q * v3
        u1, u2, u3 = v1, v2, v3
        v1, v2, v3 = t1, t2, t3

    # u3 = uu1 + vu2 = (u,v)  
    gcd = u3
    return gcd, u1, u2

# Example usage
u = int(input("Enter number: "))
v = int(input("Enter number: "))

gcd, u1, u2 = euclid_extended(u, v)
print(f"GCD of {u}, {v} is {gcd}")

print(f"Coefficients (u1, u2, u3) = ({u1}, {u2}, {gcd}) such that ({u}, {v}) = {gcd} = {u1}*{u} + {u2}*{v}")


# Exercise 2: Chinese Remainder Theorem
def multiply_list_elements(lst):
    """
    Multiplies all elements in a list.
    """
    result = 1
    for num in lst:
        result *= num
    return result

def chinese_remainder(a, m):
    x = 0
    M = multiply_list_elements(m)
    for i in range(len(a)):
        M_i = M/m[i]
        gcd, u1, u2 = euclid_extended(M_i, m[i])
        y_i = u1
        x += a[i] * M_i * y_i 
    return x - (x//M)*M

# Input
# a = [1, 2, 3]
# m = [2, 3, 5]

# Other way
chinese_list = [[1, 2], [2, 3], [3, 5]]
a = [sublist[0] for sublist in chinese_list]
m = [sublist[1] for sublist in chinese_list]

# solution in problem
x = chinese_remainder(a, m)
print(f"Solution for problem is: {x}")



