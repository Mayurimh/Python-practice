# line=str(input())
# s=line.upper()
# print(s)

new=[]
while True:
    string=str(input())
    if string:
        new.append(string.upper())
    else:
        break
for sentence in new:
    print(sentence)