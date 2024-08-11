text = "banana"
isFound = False
for i in range(len(text)):
    if (text[i] =="a" or text[i] == "A") and not isFound:
        print(i)
        isFound = True

