gino_phrase = input("Please Type in Hello World: ")
user_name = input("Please Enter your Name: ")

if gino_phrase.lower() == "hello world":
    print("Hello World - Hello",user_name)

else:
    while gino_phrase.lower() != "hello world":
        gino_phrase = input("Please Type in Hello World again: ")

        if gino_phrase.lower() == "hello world":
            print("Hello World - Hello", user_name)
        else:
            print("Goodbye World, Goodbye",user_name)

