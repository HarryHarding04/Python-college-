games = [["Doom Eternal", 50, True], ["Minecraft", 25, False], ["Terraria", 22, False], ["Rainbow Six Seige", 30, True]]
chosen = False

for i in games:
    print(i[0], end=", ")

print()

while chosen == False:
    choice = input("What game would you like to buy? ")
    for i in games:
        if choice == (i[0]):
            print(f"price is £{i[1]}")
            print(f"Is game 18 rated? {i[2]}")
            buy = input("Would you like to purchase? Y/N ")
            if buy == "Y":
                while True:
                    try:
                        num = int(input("How many copies would you like to buy? "))
                    except ValueError:
                        print("Please enter a valid number")
                    else:
                        break
                code = input("Please enter your postcode: ")
                print("Purchase successful!")
                print(num, "copie(s) are being shipped to", code)
                chosen = True
            else:
                print("Take another look ")
