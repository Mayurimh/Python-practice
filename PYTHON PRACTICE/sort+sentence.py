s = str(input())
line=[x for x in s.split(" ")]
print(" ".join(sorted(list(set(line)))))
# s = str(input())
# words = [word for word in s.split(" ")]
# print (" ".join(sorted(list(set(words)))))