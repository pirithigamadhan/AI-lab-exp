def vacuum(a, b, pos):
    while a == "Dirty" or b == "Dirty":
        if pos == "A":
            if a == "Dirty":
                print("Clean A")
                a = "Clean"
            pos = "B"
        else:
            if b == "Dirty":
                print("Clean B")
                b = "Clean"
            pos = "A"
    print("Both rooms are clean!")

vacuum("Dirty", "Dirty", "A")