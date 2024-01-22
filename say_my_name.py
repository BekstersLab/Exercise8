# Declare all variables used in Python script at the top of the page
first_name = "Rebecca"
first_name_space = "Rebecca "
last_name = "Rootes"
full_name = first_name_space + last_name

# 1 - Added a space by concatenating with speech marks (a bit long winded!)
print(first_name + " " + last_name)

# 2 - Added a space after "Rebecca " so it was included in printed output.
# Negates the need for the quotes around a space for concatenation in previous example
print(first_name_space + last_name)

# 3 - print full_name variable which adds first_name_space and last_name variables together
print(full_name)

# 4- using format method
format_method = "My name is {} {}".format(first_name, last_name)
print(format_method)

# 5 - Rewritten using f-strings (my favourite!). Removes a whole lot of hassle!
print(f"My name is {first_name} {last_name}")

# 6 - Or use the full_name variable which combines first_name and last_name
print(f"My name is {full_name} and this is my first homework!")

