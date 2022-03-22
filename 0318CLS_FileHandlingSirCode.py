import os

# get to know your current working directory
print(os.getcwd())

# Create a new file in the working directory
# We can create a file using the built-in function open()
"""
fp = open('PI_B3_File1.txt', 'x')
fp.close()
"""
# list files from a working directory
print(os.listdir())

# verify file exist in the current directory
print(os.path.isfile('PI_B3_File1.txt'))


# create a text file for writing in a specific directory
with open(r'C:\Users\LENOVO\OneDrive\Desktop\PI_B3_Test2.txt', 'w') as fp:
    fp.write('Hope is a thing with feathers')
    pass
# Using the with statement a file is closed automatically it
# ensures that all the resources that are tied up with the file are released.

# list files a directory
print(os.listdir(r'C:\Users\LENOVO\OneDrive\Desktop'))

# verify file exist
print(os.path.isfile(r'C:\Users\LENOVO\OneDrive\Desktop\PI_B3_Test2.txt'))

# create a file only if it is not present
file_path = r'C:\Users\LENOVO\OneDrive\Desktop\PI_B3_Test3.txt'
if os.path.exists(file_path):
    print('file already exists')
else:
    # create a file
    with open(file_path, 'w') as fp:
        # uncomment if you want empty file
        fp.write('Discipline provides people with rules to live their lives efficiently and effectively')

# The access mode x open a file for exclusive creation.
# If the file already exists, this operation fails with FileExistsError.

# Exception handling in python
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks

try:
    file_path = r'C:\Users\LENOVO\OneDrive\Desktop\PI_B3_Test4.txt'
    # create file
    with open(file_path, 'x') as fp:
        pass
except:
    print('File already exists')

from datetime import datetime
# get current date and time
x = datetime.now()
print(x)
# create a file with date as a name day-month-year
file_name = x.strftime('%d-%m-%Y.txt')
with open(file_name, 'w') as fp:
    print('created', file_name)

# with name as day-month-year-hours-minutes-seconds
file_name_2 = x.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open(file_name_2, 'w') as fp:
    print('created', file_name_2)

# at specified directory
file_name_3 = r"C:\Users\LENOVO\OneDrive\Desktop\\" + x.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open(file_name_3, 'w') as fp:
    print('created', file_name_3)

# Opening the file with absolute path for reading
fp = open(r'C:\Users\LENOVO\OneDrive\Desktop\PI_B3_Test2.txt', 'r')
# read file
print(fp.read())
# Closing the file after reading
fp.close()


# Opening the file with relative path
try:
    fp = open("PI_B3_Test1.txt", "r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("Please check the path.")


# Handling the FileNotFoundError
#fp = open(r'C:\Users\LENOVO\OneDrive\Desktop\reports.txt', 'r')
#print(fp.read())

# We can handle the file not found error inside the try-except block.
try:
    fp = open(r'C:\Users\LENOVO\OneDrive\Desktop\reports.txt', 'r')
    print(fp.read())
    fp.close()
except IOError:
    print("File not found. Please check the path.")
finally:
    print("Exit")

# By calling readline() you can read one line at a time
fp = open(r'C:\Users\LENOVO\OneDrive\Desktop\PI_B3_Test2.txt', 'r')
print(fp.readline())
fp.close()


# open a file for writing new contents into a file using the open()
# function with w as the access mode.

# If the file is already present it will truncate the file, which means
# all the content previously in the file will be deleted, and the new
# content will be added to the file.

fp = open("PI_B3_Test1.txt", "w")
# Writing content
fp.write("New line Prime Intuit")

# Opening the file again for reading the content
fp = open("PI_B3_Test1.txt", "r")

# Reading the contents of the file and closing
print(fp.read())
fp.close()


# We can append some content at the end of the file using the open()
# function by passing the character a as the access mode.
# The cursor will be placed at the end of the file, and
# the new content will get added at the end.

#The difference between this and the write mode is that the file’s
# content will not be truncated or deleted in this mode.

# Open and Append at last
fp = open("PI_B3_Test1.txt", "a")
fp.write(" Added this line by opening the file in append mode ")

# Opening the file again to read
print(fp.read())
fp.close()


# Rename File in Python

#Save an old name and a new name in two separate variables.
old_name = r"C:\Users\LENOVO\OneDrive\Desktop\PI_B3_Test1.txt"
new_name = r"C:\Users\LENOVO\OneDrive\Desktop\PI_B3_Test_new1.txt"

# Renaming the file
os.rename(old_name, new_name)

# Delete (Remove) Files and Directories in Python

# removing a file with relative path
os.remove("B3_File1.txt")

# remove file with absolute path
os.remove(r"C:\Users\LENOVO\OneDrive\Desktop\PI_B3_Test3.txt")
