# Reading and Writing Binary Files

#The difference between a string and a byte string is that 
# a byte string can contain characters that a string cannot.
# > Using  for images in PDF files
hw1 = "Hello, world!"
hw2 = b"Hello, world!"

print(hw1)
print(hw2)

# > Reading a binary file
my_picture = open("my_picture.png", "rb")
# > Write a Binary File
my_new_picture = open("my_new_picture.png", "wb")

# Read and write the picture byte by byte
# > like copy or move command
for byte in my_picture:
    my_new_picture.write(byte)
