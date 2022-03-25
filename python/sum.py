
def suma_zodziais(a, b):
    number = a + b
    number = str(number)
    number_lenght = len(number)
    integer = int(number)

    zero_to_twenty = {
        "0" : "nulis",
        "1" : "vienas",
        "2" : "du",
        "3" : "trys",
        "4" : "keturi",
        "5" : "penki",
        "6" : "šeši",
        "7" : "septyni",
        "8" : "aštuoni",
        "9" : "devyni",
        "10" : "dešimt",
        "11" : "vienuolika",
        "12" : "dvylika",
        "13" : "trylika",
        "14" : "keturiolika",
        "15" : "penkiolika",
        "16" : "šešiolika",
        "17" : "septyniolika",
        "18" : "aštuoniolika",
        "19": "devyniolika",
        }

    decimals = {
        "1" : "dešimt",
        "2" : "dvidešimt",
        "3" : "trisdešimt",
        "4" : "keturiasdešimt",
        "5" : "penkiasdešimt",
        "6" : "šešiasdešimt",
        "7" : "septyniasdešimt",
        "8" : "aštuoniasdešimt",
        "9" : "devyniasdešimt",
        }

    hundreds = {
        "1" : "šimtas"
        }

    if integer < 20:
        return zero_to_twenty.get(number)
    elif number[-1] == "0" and number_lenght == 2:
        return decimals.get(number[0])
    elif 19 < integer < 100:
        return decimals.get(number[0]) + " " + zero_to_twenty.get(number[-1])
    elif integer == 100:
        return "vienas šimtas"


if (suma_zodziais(0, 0) != 'nulis'):
    print("0 should be nulis")

if (suma_zodziais(0, 1) != 'vienas'):
    print("failure")

if (suma_zodziais(1, 10) != 'vienuolika'):
    print("failure")

if (suma_zodziais(20, 3) != "dvidešimt trys"):
    print("failure")

if (suma_zodziais(69, 1) != "septyniasdešimt"):
    print("failure")

if (suma_zodziais(70, 2) != "septyniasdešimt du"):
    print("failure")

print("All tests passed!")
