print("Please enter number of coins:")
quarters = int(input("# of quarters: "))
dimes = int(input("# of dimes: "))
nickels = int(input("# of nickels: "))
penniesValue = int(input("# of pennies: "))
quartersValue = int(quarters * 25)
dimesValue = int(dimes * 10)
nickelsValue = int(nickels * 5)
totalCoinValue = int(penniesValue + quartersValue + dimesValue + nickelsValue)
dollarValue = int(totalCoinValue/100)
remainderCoin = (totalCoinValue - (dollarValue * 100))
print("The total is", dollarValue, "dollars and", remainderCoin, "cents" )