user_input = input("please enter your string : ")


def is_palindrome(user_input):
    return user_input == user_input[::-1]

result = is_palindrome(user_input)
print(result)


# HARDCODED VERSION

word = input("please enter your string : ")

def is_palindrome(word):
    n = len(word)
    for i in range (n // 2):
        if word[i] != word[n - 1 - i]:
            return False
        return True
 
result = is_palindrome(word)
print(result)