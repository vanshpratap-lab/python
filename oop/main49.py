import os

path = r"C:\Users\Hp\Desktop\DEMO"
files = os.listdir(path)
count = 0

for file in files:
    if file.endswith(".png"):
        count += 1
        old_path = os.path.join(path, file)
        new_path = os.path.join(path, f"{count}.png")
        os.rename(old_path, new_path)

print(f"renamed to : {count}")
