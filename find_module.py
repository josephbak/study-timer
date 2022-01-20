# importing random module
import beepy

# importing the os module
import os

# storing the path of modules file
# in variable file_path
file_path = beepy.__file__

# storing the directory in dir variable
dir = os.path.dirname(file_path)

# printing the directory
print(dir)