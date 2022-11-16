food = [["bananas", 24, 2021], ["crisps", 12, 2021], ["milk", 10, 2019], ["bread", 17, 2021]]

for i in food:
    if i[2] <=2020:
        print(f"{i[0]} is out of date")
    else:
        if i[1] % 2 == 0:
            print(f"{i[0]} is Harry's")
        else:
            print(f"{i[0]} is roomate's")
