# SEEK () , TELL () , TRUNCATE () METHODS 
# with open('myfile5.txt', 'r') as f:
#     print(type(f))

#     f.seek(10) 

#     print(f.tell())

#     data = f.read(5)
#     print(data)
with open('myfile5.txt', 'w') as f:
    f.write('hello world , this is a program written by me!')
    f.truncate(5)

with open('myfile5.txt', 'r') as f:
    print(f.read(4))