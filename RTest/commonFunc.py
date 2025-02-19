def verifyChoice(choices, result):
    # Si le numéro sorti est 0, le pari est perdu
    if result == 0:
        return False

    rouges = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    noirs = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}

    conditions = {
        "r": result in rouges,
        "n": result in noirs,
        "p": result % 2 == 0,
        "i": result % 2 == 1,
        "d1": 1 <= result <= 12,
        "d2": 13 <= result <= 24,
        "d3": 25 <= result <= 36,
        "a1": result % 3 == 1,
        "a2": result % 3 == 2,
        "a3": result % 3 == 0,
    }

    # Check if any choice matches the conditions
    return any(conditions.get(choice.lower(), False) for choice in choices) if choices else False


def flatten(l):
    resultat = []
    for element in l:
        if isinstance(element, list):
            resultat.extend(flatten(element))
        else:
            resultat.append(element)
    return resultat