dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

piggyBank["quarters"] = int(dollarAmount / .25)
remainder = round((dollarAmount - (piggyBank["quarters"] * .25)), 2)
piggyBank["dimes"] = int(remainder / .10)
remainder = remainder - (piggyBank["dimes"] * .1)
piggyBank["nickels"] = int(remainder / .05)
remainder = remainder - (piggyBank["nickels"] * .05)
piggyBank["pennies"] = round(remainder / .01)

print(piggyBank)
