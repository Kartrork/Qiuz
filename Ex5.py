text = input("Enter text: ")
position =0
for i in range(len(text)):
    if i%2==0:
        position+=1
print(position)
