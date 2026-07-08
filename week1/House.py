name = input("What's your name?")
match name:
    case "Dexter" | "Rita" | "Doakes":
        print("Miami")
    case "Harrison":
        print("New York")
    case _:
        print("Who?")