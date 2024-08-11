text = input("Please enter: ")
n = len(text)
mesage =""
if n > 4 and n < 8:
    result ="It is small"
elif n > 10 and n < 15:
    result = "It is average"
elif n > 15:
    result = "It is big"
print(result)
