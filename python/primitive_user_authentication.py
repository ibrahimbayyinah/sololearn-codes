spam = input("enter your name:\n")

if spam == "joe":
    print("hello joe")
elif spam == "mary":
    while True:
        print("enter a password mary")
        passw = input()
        if passw == "sword":
            break
    print("access granted")
else:
    print("intruder alert!!!!")
