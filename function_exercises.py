# Madlib
def madlib(name, subject):
     return " %s favorite subject is %s " % (name, subject)
result = madlib("Zach", "Math")
print(result)

# C-Temp Conversion
def c_temp_conversion(c):
    return c * 9/5 + 32

def temperature():
    celsius = int(input("Temp in celsius?: "))
    print(c_temp_conversion(celsius))
temperature()

# F-Temp Conversion
def f_temp_conversion(f):
    return f - 32 * 5/9

def temperature():
    fahrenheit = int(input("Temp in fahrenheit?: "))
    print (f_temp_conversion(fahrenheit))
temperature() 

# Is Even
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(23))

# Is Odd
def is_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False
print(is_odd(23))

# Only Evens
def only_evens(number_list):
    new_list = []
    for num in number_list:
        if num % 2 == 0:
            new_list.append(num)
    print(str(new_list))

only_evens([11, 20, 42, 97, 23, 10]) 

# Only Odds
def only_odds(number_list):
    new_list = []
    for num in number_list:
        odd = is_odd(num)
        if odd == True:
            new_list.append(num)
    print(new_list)

only_odds([11, 20, 42, 97, 23, 10])


# MEDIUM TRAINING EXERCISES

# Smallest number
list_of_numbers = [123,456,789]
def find_smallest(list_of_numbers):
    smallest = float("inf") #The inf is signifying the number can be infinity. its a string.
    for number in list_of_numbers:
        if number < smallest:
            smallest = number
    return smallest

print("The smallest number is: " + str(find_smallest(list_of_numbers)))

# Largest number
def find_largest(list_of_numbers):
    largest = 0
    for number in list_of_numbers:
        if number > largest:
            largest = number
    return largest

print(("The largest number is: ") + str(find_largest(list_of_numbers)))

# The Shortest String
def shortest_string(string_list):
    shortest = string_list[0]
    for string in string_list:
        if len(string) < len(shortest):
            shortest = string
    return shortest

print("'" + shortest_string(["Foo", "Their", "Banks"]) + "'" + " is the shortest string.")

# Longest String
def longest_string(string_list):
    longest = string_list[0]
    for string in string_list:
        if len(string) > len(longest):
            longest = string
    return longest

print("'" + longest_string(["Foo", "Their", "Banks"]) + "'" + " is the longest string.")
