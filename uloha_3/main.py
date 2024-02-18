def is_palindrome(num, radix):
    original_num = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * radix + num % radix
        num //= radix
    return original_num == reversed_num

def next_palindrome(from_num, radix):
    if not 2 <= radix <= 36:
        return 0, None  
    
    current = from_num + 1
    while current < 2**(64)-1:
        if is_palindrome(current, radix):
            return 1, current 
        current += 1
    
    return 0, None 

print("číslo:")
from_num = int(input())
print("v soustavě")
radix = int(input())
success, next_pal = next_palindrome(from_num, radix)
if success:
    print(f"Next palindrome after {from_num} in base {radix} is: {next_pal}")
else:
    print(f"No palindrome found after {from_num} in base {radix}")