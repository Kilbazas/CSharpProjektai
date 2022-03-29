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
    "1" : "šimtas",
    "2" : "šimtai"
    }

def one_to_ninety_nine(integer):
    integer = int(integer)
    number = str(integer)
    number_lenght = len(number)

    if integer < 20:
        return zero_to_twenty.get(number)

    elif number[-1] == "0" and number_lenght == 2:
        return decimals.get(number[0])

    elif 19 < integer < 100:
        return decimals.get(number[0]) + " " + zero_to_twenty.get(number[-1])


def suma_zodziais(integer):
    number = str(integer)
    number_lenght = len(number)
    hundreds_value = "1"
    if integer == 0:
        return "nulis"

    if integer > 0 and integer <= 99:
        return one_to_ninety_nine(integer)

    hundred = integer // 100
    teens = integer % 100

    if int(number[0]) > 1:
        hundreds_value = "2"

    if integer <= 999:
        if number[1:] == "00":
            return zero_to_twenty.get(str(hundred)) + " " + hundreds.get(hundreds_value)
        else:
            return zero_to_twenty.get(str(hundred))+ " " + hundreds.get(hundreds_value) + " " + one_to_ninety_nine(number[1:])
        

    return "not implemented"


print(suma_zodziais(999))

if (suma_zodziais(0) != 'nulis'):
    print("0 should be nulis")

if (suma_zodziais(1) != 'vienas'):
    print("failure 1")

if (suma_zodziais(11) != 'vienuolika'):
    print("failure 11")

if (suma_zodziais(23) != "dvidešimt trys"):
    print("failure 23")

if (suma_zodziais(70) != "septyniasdešimt"):
    print("failure 70")

if (suma_zodziais(99) != "devyniasdešimt devyni"):
    print("failure 99")

if (suma_zodziais(100) != "vienas šimtas"):
    print("failure 100")

if (suma_zodziais(101) != "vienas šimtas vienas"):
    print("failure 101")

if (suma_zodziais(110) != "vienas šimtas dešimt"):
    print("failure 110")

if (suma_zodziais(111) != "vienas šimtas vienuolika"):
    print("failure 111")

if (suma_zodziais(119) != "vienas šimtas devyniolika"):
    print("failure 119")

if (suma_zodziais(120) != "vienas šimtas dvidešimt"):
    print("failure 120")

if (suma_zodziais(129) != "vienas šimtas dvidešimt devyni"):
    print("failure 129")

if (suma_zodziais(190) != "vienas šimtas devyniasdešimt"):
    print("failure 190")

if (suma_zodziais(200) != "du šimtai"):
    print("failure 200")

if (suma_zodziais(279) != "du šimtai septyniasdešimt devyni"):
    print("failure 279")

if (suma_zodziais(900) != "devyni šimtai"):
    print("failure 900")

if (suma_zodziais(999) != "devyni šimtai devyniasdešimt devyni"):
    print("failure 999")

print("All tests passed!")
