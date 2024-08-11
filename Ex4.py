text = input("Enter text: ")
sum =0
for i in range(len(text)):
    if text[i]=="B"or text[i]=="b" or text[i] =="C" or text[i] =="c" or text[i] == "D" or text[i] =="d":
        sum += 1
print("Total",sum)