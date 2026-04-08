name = "Subhasis"
l1 = "SUBBHASIS"
l2 = "subhasis"

print(len(name))
print(name.endswith("sis"))
print(name.startswith("ub"))
print(l1.lower())
print(l2.upper())

text = "hello world"
print(text.replace("world", "Python"))   # hello Python

text1 = "a,b,c"
print(text1.split(","))   # ['a', 'b', 'c']

words = ["hello", "world"]
print(" ".join(words))   # hello world

text2 = "hello"
print(text2.count("l"))   # 2

text2 = "hello"
print(text2.startswith("he"))  # True
print(text2.endswith("lo"))    # True

print("321".isalpha())  # True
print("123".isdigit())    # True

