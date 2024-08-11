text = input("Please enter your text: ")
is_storng_password = False
for i in range(len(text)):
    if text[i] == '@':
        is_storng_password = True
if is_storng_password:
    print("Strong password")
else:
    print("Weak password")