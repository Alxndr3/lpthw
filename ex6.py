types_of_people = 10

# When a variable is put between curly braces in a string the variable is replaced by the variable value when the string is printed.
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

# In this case a variable is assigned with a formated string.
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# The plus sign + is used to place variables side by side.
print(w + e)

