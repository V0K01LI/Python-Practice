
# file=open("demo.txt",mode="r") # the file has opened in the read mode but not yet readed
# c=file.read() # the data readed will be stored in c
# print(c)
# file.close()

# ## Instead of Read We are using Readline
# file=open("demo.txt",mode="r") # the file has opened in the read mode but not yet readed
# c=file.readline() # the data readed will be stored in c
# print(c)
# file.close()
# ## when we use readline instead of read it will print only the first line in the whole set of lines or para

# ## use readlines to get all the data in the form of a list
# file=open("demo.txt",mode="r")
# c=file.readlines() # the data readed will be stored in c as a list
# print(c[1])
# file.close() # here in output you will see \n because of the new line

# ## If i need to read only "this is" in the demo.txt
# ## so we can use read and mention num of words
# file=open("demo.txt",mode="r")
# c=file.read(7)
# print(c)
# file.close() # the data readed will be stored in c

## Write mode

# file=open("demo.txt",mode="w")
# file.write("Hello, World!")
# file.close()
## if we use write mode and mention anything in the write function.
## it will override the whole data that is already existing.
## in simple it will remove the whole data and the new data entered through write function will get exist.


## as there is data loss by using w in mode now we will use append = a

# file=open("demo.txt",mode="a")
# file.write("\n Hello, Akash")
# file.close()

## Reading file in r+ mode
# with open("demo.txt",mode="r+") as file:
#     print(file.tell()) ## tell is very helpful file pointer like cursor location in the file
#     print(file.read())
#     print(file.tell())
## here fist tell will be identifying the file pointer where the start location is zero
## In second it will read the file and the pointer will be at the end of the text
## and last tell function gives the end pointer loc of the text
## in w+ we can do both read and write operations so we can use read function together
# c=file.write("this is w+")
## the above command will remove all existing data and create a new line this is w+

## Reading file in w+ mode
# with open("demo.txt",mode="w+") as file:
#     print(file.tell())
#     print(file.read()) ## tell is very helpful file pointer like cursor location in the file
#     print(file.tell())
#     c=file.write("this is w+")
   # file.seek(0) ## seek function is used to move the pointer to the start of the file
## if we do read or write always the pointer will be in zero and also removes the data
# with open("demo.txt",mode="w+") as file:
#     print(file.tell())
#     c=file.write("this is w+")
#     print(file.read()) ## tell is very helpful file pointer like cursor location in the file
#     print(file.tell())
## first write and then read the data

 ## write file in w+ mode
# with open("demo.txt",mode="w+") as file:
#     file.write("New text.")
## simple Trick to remember
# in r+ first do read and then write
# in w+ first do write and the read

## except read we can use other operations to create a file

# with open("sample.txt",mode="w+") as file:
#     pass # as we dont even data i have given pass
## as we gave w+ even though there is no file existing it will automatic create the file with  that name

## seek() is used to chnage the position of the file pointer
## is we use seek(0) and ask tell to know position it will be at 0
## seek will helps to move the pointer

## opening of the file
# fp=open("demo.txt","r")
# print(fp.tell())
# fp.read(2)

# ### print the position og handle or pointer or cursor
# print(fp.tell()) ## value will be 2
# fp.seek(0)  ## i am asking pointer to move back to 0 again
# print(fp.tell()) ## this will give 0

# ## closing file
# fp.close()

file=open("demo.txt",mode="r+")
content=file.read()
v=str(content)
print(v)
f=v.split()
print(f)
f.insert(2,"Akash")
print(file.tell())
file.close()
file=open("demo.txt",mode="w")
print(f)
for i in f:
    file.writelines([i])