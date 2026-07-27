# ------READLINES------
# f = open('myfile4.txt', 'r')
# i = 0
# while True:
#     line = f.readline()
#     if not line:
#      break 
#     i = i + 1
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"marks of students {i} in maths is: {m1*2}")
#     print(f"marks of students {i} in english is: {m2*2}")
#     print(f"marks of students {i} in sst is: {m3*2}")

#     print(line)
# ------WRITELINES------
f = open('myfile5.txt' , 'w')
lines = ['line 1\n' , 'line 2\n' , 'line 3\n']
f.writelines(lines)
f.close()