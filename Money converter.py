def opening():
    print("")
    print("====================Conversion rates:====================")
    print("")
    print("GBP - EUR | EUR - GBP | EUR - AUD | AUD - EUR", "\n1.16           0.85           1.47           0.68")
    print("GBP - AUD | AUD - GBP | EUR - JPY | JPY - EUR", "\n1.79            0.55           137.55       0.0073")
    print("GBP - JPY | JPY - GBP | AUD - JPY | JPY - AUD", "\n151.44         0.0066       93.40         0.011")
    print("")
    print("=======================================================")

def main():
    print("")
    print("What currency would you like to convert?")
    currency = input("")
    print("what would you like to convert it to?")
    exchange = input("")
    currency = currency.upper()
    exchange = exchange.upper()
        
    if currency == "GBP" and exchange == "EUR":
        multiplier = float(1.16)
    elif currency == 'EUR' and exchange == 'GBP':
        multiplier = float(0.85)
    elif currency == 'EUR' and exchange == 'AUD':
        multiplier = float(1.47)
    elif currency == 'AUD' and exchange == 'EUR':
        multiplier = float(0.68)
    elif currency == 'GBP' and exchange == 'AUD':
        multiplier = float(1.79)
    elif currency == 'AUD' and exchange == 'GBP':
        multiplier = float(0.55)
    elif currency == 'EUR' and exchange == 'JPY':
        multiplier = float(137.55)
    elif currency == 'JPY' and exchange == 'EUR':
        multiplier = float(0.0073)
    elif currency == 'GBP' and exchange == 'JPY':
        multiplier = float(151.44)
    elif currency == 'JPY' and exchange == 'GBP':
        multiplier = float(0.0066)
    elif currency == 'AUD' and exchange == 'JPY':
        multiplier = float(93.40)
    elif currency == 'JPY' and exchange == 'AUD':
        multiplier = float(0.011)
    else:
        print("This currency was not found. Try again.")
        return True
    
    print("This is the exchange rate for those currencies:")
    print(multiplier)
    print("How many", currency, "would you like to convert?")
    amount = int(input(""))
    print("This is the end result of the conversion:")
    calc = (multiplier * amount)
    print(amount, currency,'is equal to',calc, exchange )
    
    cont = input('Would you like to do another conversion? Y/N \n').upper()
    if cont == "Y":
        return True
    elif cont == "N":
        return False
    else:
        while True:
            cont = input('Would you like to do another conversion? Y/N \n').upper()
            if cont == "Y":
                return True
            elif cont == "N":
                return False
        
while True:       
    opening()
    if main() == False:
        break

