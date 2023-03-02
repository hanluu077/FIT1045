''' 
FIT1045 Python Week 1 

Task: 
- Write a program that reads an integer (assumed non-negative) number of bits 
from the user input and converts this quantity to bits (b), bytes (B), kilobytes (KB) and megabytes (MB). 

Create conversion of 
1 byte = 8 bits.
1 kilobyte = 1024 bytes.
1 megabyte = 1024 kilobytes.
'''

num_of_bits = int(input("number of bits: "))

total_byte = num_of_bits // 8                     # check how many bits can evenly be converted to bytes
remaining_bit = num_of_bits % 8                   # remainder is used for result for BITS 

total_kilobyte = total_byte // 1024               # check how many bytes can be converted to kb
remaining_byte = total_byte % 1024                # Remainder is used for end results for BYTES 

total_megabyte = total_kilobyte // 1024           # check how many bytes can evenly be converted to mb  --> final MB conversion 
remaining_kilobyte = total_kilobyte % 1024        # Remainder is used for end results for KB  

remaining_megabytes = total_megabyte              # refer to line 17

print(num_of_bits,"bits =", remaining_megabytes, "Megabytes", remaining_kilobyte, "Kilobytes", remaining_byte, "Bytes", remaining_bit, "Bits")
