str = input().replace("<", " < ").replace(">", " > ").replace("&&", " && ").replace("||", " || ").replace("(", " ( ").replace(")", " ) ")
words = list(str.split())

print(" ".join(words))