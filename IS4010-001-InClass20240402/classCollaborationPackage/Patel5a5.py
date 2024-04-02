#patel5a5
# Name:Akash Patel
# email:patel5a5@mai.uc.edu
# Assignment Number:06
# Due Date:02-22-2024
# Course/Section:IS4010
# Semester/Year:Spring/2024
# Brief Description of the assignment:We are using code from leetcode 
# Anything else that's relevant:


def is_palindrome(x):
    # Convert the integer to a string
    x_str = str(x)
    
    # Check if the string is equal to its reverse
    return x_str == x_str[::-1]

# Example usage
x = 121
print(is_palindrome(x))  # Output: True