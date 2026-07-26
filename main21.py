# ----------ONE EXISTING WAY----------
# name = "vansh"
# country = "india"
# print("hey my name is", name, "and i am from", country)
# ---------ANOTHER METHOD-----------
string = "hey my name is {} and i am from {}"
country = "india"
name = "vansh"

# print(string.format(country, name))
print(f"hey my name is {name} and i am from {country}")
print(f"hey my name is {{name}} and i am from {{country}}") #-> this will print the name and country as it is
price = 50.666
txt = f"for only {price:.2f} dollars!"
print(txt)

# num1 = 2
# num2 = 30
# sum = num1*num2
# print(sum)

print(f"{2 * 30}")
