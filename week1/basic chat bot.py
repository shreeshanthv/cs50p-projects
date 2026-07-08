message = input("You: ").lower()

match message:
     case "hello":
         print("Bot: Hey there! How are you?")
     case "bye":
          print("Bot: Bye! Good to see you!")
     case _:
          print("Bot: no reply available for this")
