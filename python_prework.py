# Question 1
# Write a function to print “hello_USERNAME!” USERNAME is the input of the function. 
def hello_name(user_name):
    """This is a function that prints hello_USERNAME!"""
    print("hello_" + user_name + "!")

hello_name("USERNAME")
print("\n")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    """Prints all odd numbers between 1-100 and returns nothing"""
    for num in range(1,100,2):
        print(num)
            
first_odds()
print("\n")

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 
def max_num_in_list(b_list):
    """This function takes a list and returns the largest number"""
    return max(b_list)
        
print(max_num_in_list([76, 78, 999, 3677, 10]))
print("\n")

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    """Tests if a year is a leap year"""
    if a_year % 100 == 0 and a_year % 400 == 0:
        return True
    elif a_year % 4 == 0:
        return True
    else:
        return False
          
print(is_leap_year(2024))
print("\n")

# Remember: A leap year is divisible by 4, but not divisible by 100,
# unless it is also divisible by 400
     
# Question 5
# return sorted(a_list) == list(range(min(a_list),max(a_list) +1))
# def is_consecutive(a_list):
#    """Checks if numbers are sequential (Consecutive Numbers going up by 1)"""
#    for num in a_list:
#        if sorted(a_list) == a_list:
#            if range(min(a_list),max(a_list)) == +1:
#                return True                            
#    else:
#       print(False)

# Attempt 1, I gave up

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.
def is_consecutive(a_list):
#    """Checks if numbers are sequential (Consecutive Numbers going up by 1)
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

a_list = [1,2,3,4,5]
print(is_consecutive(a_list))
