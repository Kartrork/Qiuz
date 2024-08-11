text = input("Please enter your text now: ")
countA = 0
countB = 0
for i in range(len(text)):
    if text[i] == "A" or text[i] == "a" and text[i]!= "B":
        countA += 1
        countB += 1
print("count letter A and a: ",countA, "and count letter b:",countB)