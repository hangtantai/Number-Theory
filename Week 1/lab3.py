# import necessary library
import matplotlib.pyplot as plt
import math

# function convert base
def convert_base(num):
    assign = 3
    compare = 0
    value = 0
    ctr = 0
    temp = num  

    #find convert value using while loop
    while(temp > 0):
        value = ((temp%2)*(10**ctr)) + value
        temp = int(temp/2)
        ctr += 1
        compare += 1
        assign += 3
    return value, assign, compare

# test
dec_val = 100
value, assign, compare = convert_base(dec_val)
print(f"Decimal is {dec_val} convert to Binary number is : {value}")
print(f"Assignment: {assign}")
print(f"Comparison: {compare}")

# check assign and compare
assign_list = []
compare_list = []
list_number = [100 * i for i in range(1, 10)]
for i in list_number:
    value, assign, compare = convert_base(i)
    assign_list.append(assign)
    compare_list.append(compare)

# plot
plt.figure(figsize=(10, 6))
plt.plot(list_number, assign_list, label='Gan(N)')
plt.plot(list_number, compare_list, label='Sosanh(N)')
plt.plot(list_number, [1.1* math.log2(N) for N in list_number], label='1.1 * log2(N)')
plt.plot(list_number, [3.3*math.log2(N) + 3.3 for N in list_number], label='3.3*log2(N)')
plt.xlabel('N')
plt.ylabel('Number of assigment')
plt.title('Number of assignment, compare and log2(N)')
plt.legend()
plt.grid(True)
plt.show()
