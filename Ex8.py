while  True:
    letter = input("Please enter your letter: ").strip()
    if letter.lower() == "a":
        print("Found letter A")
        break
    else:
        print("Try again!")