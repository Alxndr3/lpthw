formatter = "{} {} {} {}"

# In this first case the integers are placed inside the curly braces as values of the variable formatter.
print(formatter.format(1, 2, 3, 4))

# In this case  the strings are placed inside the curly braces as values for the formatted variable formatter.
print(formatter.format("one", "two", "three", "four"))

# In this scenario boolean values are assign to between each pair of curly braces.
print(formatter.format(True, False, True, False))

# In this case four curly braces are placed inside each variable's curly brace pair, printing this way 16 pairs.
print(formatter.format(formatter, formatter, formatter, formatter))

# Again the are put in place of the braces.
print(formatter.format("Eu sou um cordeirinho", "Jesus é o meu pastor", "Sou um feliz menino", "Nos braços do Senhor"))

# the .format(...) is a function
