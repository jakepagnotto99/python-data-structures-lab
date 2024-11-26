# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    # Create a list of students
    students = ['Alice', 'Bob', 'Charlie']
    # Assign the second student's name to a variable
    first_student = students[1]
    # Assign the last student's name to a variable
    last_student = students[-1]
    # Return the variables for testing
    return first_student, last_student

# Call the function and print the result
print('Exercise 1:', manage_students())


# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    # Create a tuple of foods
    foods = ('Pizza', 'Burger', 'Pasta')
    # Initialize an empty string
    meal = ''
    # Iterate over the tuple and append each food to meal
    for food in foods:
        meal += food + ' '
    # Return the concatenated string
    return meal.strip()

# Call the function and print the result
print('Exercise 2:', combine_foods())


# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    # Use the same tuple of foods as in the previous exercise
    foods = ('Pizza', 'Burger', 'Pasta')
    # Slice the tuple to get the last two items
    last_two_foods = foods[-2:]
    # Return the sliced tuple
    return last_two_foods

# Call the function and print the result
print('Exercise 3:', slice_foods())


# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”
def hometown_info():
    # Create a dictionary with city, state, and population
    home_town = {
        'city': 'Springfield',
        'state': 'Illinois',
        'population': 116250
    }
    # Create the formatted string
    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"
    # Return the message
    return home_town_message

# Call the function and print the result
print('Exercise 4:', hometown_info())


# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

def list_home_town_items():
    # Create a dictionary for home_town
    home_town = {
        'city': 'Springfield',
        'state': 'Illinois',
        'population': 116250
    }
    # Define an empty list
    home_town_items = []
    # Iterate over the dictionary items and format them into strings
    for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")
    # Return the list
    return home_town_items

# Call the function and print the result
print('Exercise 5:', list_home_town_items())
