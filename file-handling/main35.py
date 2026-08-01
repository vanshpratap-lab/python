# READING A FILE 
f = open('myfile.txt2', 'r')
# print(f)
anvi = f.read()
print(anvi)
f.close
# WRITING A FILE 
f = open('myfile2.txt' , 'r')
text = f.read()# f.write('hello, world!')
print(text)
f.close()

with open('myfile2.txt', 'a') as f:
    f.write("hey this is vansh")