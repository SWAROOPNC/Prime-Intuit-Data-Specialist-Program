#w overwrites
#append curson on last line
#r+
#w+
import os
print("os.getcwd() ",os.getcwd())  #to get current working directory
#create new file in working directory using Open
#x mode when file not there that file will be created

"""fp =open("B3_File1.txt","x")
fp.close()""" """RUN THIS ONLY FIRST TIME TO CREATE , after that it throws error"""
#saved as fp to ease of open close handling execution

#list all files from
file_list = list(os.listdir())
for files in file_list :
    print(files)
#verify FILE EXISTS
print(os.path.isfile("B3_File1.txt"))
print(os.path.isfile("B3_File2.txt"))

#WITH Statement no need to close specifically , close automatically
#ensures all resources that are tied up with file are released
#create a file for writing in a specific directoey
#w mode , if not exists it create , if exists it writes
with open(r"C:\Users\Admin\Documents\HTML_LEVEL1\B3_File3.txt","w") as fp1 :
    fp1.write("this is first line")
    pass
with open(r"C:\Users\Admin\Documents\HTML_LEVEL1\B3_File3.txt","w") as fp1 :
    fp1.write(3*"This is NEW LINE ")
    pass

#r must be used , consider it as raw string
#now first line erased ,
#w mode re writes from beginning
print(os.listdir(r"C:\Users\Admin\Documents\HTML_LEVEL1"))
B3_File3_path = r"C:\Users\Admin\Documents\HTML_LEVEL1\B3_File3.txt"
print(os.path.exists(B3_File3_path))
with open(B3_File3_path,"r") as fp2 :
    fp2cont = fp2.read()
    print("fp2.read() : ",fp2cont)

with open(B3_File3_path,"w") as fp3 :
    fp3cont = fp3.write("Breaking: India's daily Covid tally further drops with 2,528 cases, new deaths at 149\n lin2 \n lin3")

with open(B3_File3_path, "r") as fp3:
    fp3cont = fp3.read()
print("fp3.read() : " , fp3cont)
with open(B3_File3_path, "r") as file1:
    file1cont = file1.readlines()

#other way of read
fp9 = open(r"C:\Users\Admin\Documents\HTML_LEVEL1\B3_File3.txt")
fp9cont = fp9.read()
print("fp9.read()",fp9cont)
fp9.close()


#access mode x open a file for exclusive creation
#if file already exists , this operation fails with FileException Error
print("______________________________________________________")
#Exception Handling

a = 1

try:
    b = int(input("Please enter an integer to divide a "))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a valid number or number type")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("This prints anyway")


print("______________________________________________________")
try :
    file_path = r"C:\Users\Admin\PycharmProjects\pythonProject1\B3_File4.txt"
    #create file
    with open(file_path,'x') as fp :
        pass
except :
    print("file already exists")
else :
    print("file created")

from datetime import datetime
timenow = datetime.now()
print(datetime.now())
print(("datetime.now()",timenow))

#strftime , create fle ., structure for time
#ccreate file with date as name d-m-y
fname2 = timenow.strftime("%d-%m-%Y-%H-%M-%S.txt")
with open(fname2,'w') as fp6 :
    print("created file in cwd : ",fname2)
#file with 18-03-2022.txt is created in cwd ,


#to create in specific location
fname3 = timenow.strftime("%d-%m-%Y-%H-%M-%S.txt")
with open(r"C:\Users\Admin\Documents\HTML_LEVEL1\\"+fname3,'w') as fp6 :
    print("created file in specific loc  : ",fname3)
#observe HTMLlevel1\\
#double \\

#file open with alternate path
try :
    fp = open(r"C:\Users\Admin\PycharmProjects\pythonProject1\B3_File9.txt")
    print(fp.read())

except :
    print("some thing wrong")
finally:
    print(" this will print anyway")

try :
    fp = open(r"C:\Users\Admin\PycharmProjects\pythonProject1\B3_File9.txt")
    print(fp.read())
except IOError :
    print("File not found check Again")
except :
    print("some thing wrong")
finally:
    print(" this will print anyway")

#append mode
with open(B3_File3_path,"a") as fp3 :
    fp3cont = fp3.write("\n Added Line \n Breaking: India's daily Covid tally further drops with 2,528 cases, new deaths at 149\n lin2 \n lin3")

with open(B3_File3_path,"r") as fp3 :
    fp3cont = fp3.read()
print(fp3cont)
B3_File3_Oldname = r"C:\Users\Admin\Documents\HTML_LEVEL1\B3_File3NewName.txt"
B3_File3_NewName = r"C:\Users\Admin\Documents\HTML_LEVEL1\B3_File3NewName2.txt"

os.rename(B3_File3_Oldname,B3_File3_NewName)

os.remove(r"C:\Users\Admin\Documents\HTML_LEVEL1\18-03-2022-12-33-57.txt")