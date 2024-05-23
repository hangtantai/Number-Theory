# # Exercise 1:


# # using loop
def convert_base(num, original_base, base_convert):
    value = 0
    ctr = 0
    temp = num  

    #find convert value using while loop
    while(temp > 0):
        value = ((temp%base_convert)*(original_base**ctr)) + value
        temp = int(temp/base_convert)
        ctr += 1
    return value

dec_val = 24
print(f"Convert base 1: {convert_base(dec_val, 10, 2)}") 


# using recursive
def convert_base_1(num, base):
    if num >= 1:
        convert_base_1(num // base, base)
        print(num % base, end='')

dec_val = 24
print("Convert base 2:", end ="")
convert_base_1(dec_val, 2) 
print() 


# using loop and store in string
def convert_base_2(num, base):
    store_string = ""
    temp = num

    while(temp > 0):
        remainder = temp % base
        store_string += str(remainder)
        temp //= base
    
    # inserve string
    return store_string[::-1]

dec_val = 24
number = int(convert_base_2(dec_val, 2))
print(f"Convert base 3: {number}")



# thuật toán tìm ước chung lớn nhât
# sử dụng đệ quy

Asume that a is greater than b
def euclid(a,b):
    if b == 0:
        return a
    else:
        r = a % b
        a = b
        b = r
        return euclid(a,b)

a = euclid(5,4)
print(f"Euclid: {a}")

# Exercise 2

def add(a,b):
    # define max_len
    max_len = max(len(a), len(b))

    # fill zero to the same len between 2 numbers
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # result
    result = ""

    # create carry
    carry = 0

    # Traverse the string
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
    
        # Compute the carry.
        carry = 0 if r < 2 else 1
    
    if carry != 0:
        result = '1' + result
    return result



# minus
def minus(a,b):
    # define max_len
    max_len = max(len(a), len(b))

    # fill zero to the same len between 2 numbers
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    # define carry
    carry = 0

    # define result
    result = ""
    # algorithm
    for i in range(max_len - 1, -1, -1):
        r = carry
        if a[i] == "0" and b[i] == "1":
            r -= 1 
        elif a[i] == "1" and b[i] == "0":
            r += 1
        else:
            r -= 0
        result = ('1' if r % 2 != 0 else '0') + result
    
        # Compute the carry.
        carry = -1 if r == -1 or r == -2 else 0
    return result



# # multiply
def multiply(a,b):
    # create list to store 
    list_store = []

    # padding for len of result
    pad = 0

    for i in range(len(b) - 1, -1, -1):
        # Multiply the indicators of b by a
        element = int(b[i]) * int(a) 

        # convert to string
        string = str(element)

        # algorithm
        if element == 0:
            list_store.append(string.ljust(len(a) + pad,'0'))
        else:
            list_store.append(string.ljust(len(string) + pad,'0'))
        pad += 1
    
    # define result is the final of list
    result = list_store[len(list_store)-1]
    for i in range(len(list_store)-2, -1, -1):
        result = add(result,list_store[i])
    return result

# define a, b
a = "10011011"
b = "1110111"



a_dec = convert_base(int(a),2, 10)
b_dec = convert_base(int(b),2, 10)
print(f"a: {a_dec}, b:{b_dec}")
# add
result = add(a,b)
result_dec = convert_base(int(result), 2, 10)
print(f"Add two binary number: {result}")
print(f"Result in base 10: {result_dec}")

# minus
result = minus(a,b)
result_dec = convert_base(int(result), 2, 10)
print(f"Minus two binary number:{result}")
print(f"Result in base 10: {result_dec}")

# multiply
result = multiply(a,b)
result_dec = convert_base(int(result), 2, 10)
print(f"Multiply two binary number:{result}")
print(f"Result in base 10: {result_dec}")