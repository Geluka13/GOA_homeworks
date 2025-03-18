def captianjack(gold_coin):
    ship1 = 150
    ship2 = 200
    ship3 = 250
    ship4 = 300
    ship5 = 350
    if gold_coin == 0:
        return "აჯანყდა ეკიპაჟი"
    user = input("რომელი გემი გინდათ?: ")
    if int(user) == 1 and gold_coin >= 150:
        return "შენ იყიდე 1 გემი"
    if int(user) == 2 and gold_coin >= 200:
        return "შენ იყიდე 2 გემი"
    if int(user) == 3 and gold_coin >= 250:
        return "შენ იყიდე 3 გემი"
    if int(user) == 4 and gold_coin >= 300:
        return "შენ იყიდე 4 გემი"
    if int(user) == 5 and gold_coin >= 350:
        return "შენ იყიდე 5 გემი"
    else:
        return "ეკიპაჟი აჯანყდა"
print(captianjack(250))