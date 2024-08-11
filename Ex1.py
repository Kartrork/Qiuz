text = input("Enter your text: ")
result = " "
if len(text) < 3:
    result = "Small"
elif len(text) <= 8:
    result = "Medium"
elif len(text) > 9:
    result ="Big"
print(result)