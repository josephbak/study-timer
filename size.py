# Python program to explain os.get_terminal_size() method

# importing os module
import os

# Get the size
# of the terminal
size = os.get_terminal_size()

# Print the size
# of the terminal
print(size)

print(type(size.columns))
