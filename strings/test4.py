st = input("enter message:")
words = st.split(" ")
coding = True
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    pass
st = input("enter your message:")
word = st.split()
 
nword = [] 

for w in word: 
    if len(word[0]
        stnew = "fds" + w[1:] + w[0] + "fgu") >= 3: 
        nword.append(stnew)
        print(" ".join(nword))
def encode(text):
    words = text.split()
    nwords = []

    for w in words:
        if len(w) >= 3:
            stnew = "dfs" + w[1:] + w[0] + "khj"
            nwords.append(stnew)

    return " ".join(nwords)

msg = input("Enter message: ")
print(encode(msg))

s = "AI"
b = s.encode()

print(s)
print(b)
print(type(s))
print(type(b))
# nm = "vansh"
# print(nm[-4:-2])