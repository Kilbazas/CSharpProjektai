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

thousands = {
    "1" : "tūkstantis",
    "2" : "tūkstančiai",
    "3" : "tūkstančių",
    "4" : ""
    }

millions = {
    "1" : "milijonas",
    "2" : "milijonai",
    "3" : "milijonų",
    "4" : ""
}

billions = {
    "1" : "milijardas",
    "2" : "milijardai",
    "3" : "milijardų",
    "4" : ""
}

def number_case(integer):
    integer = int(integer)
    number_as_string = str(integer)
    number_length = len(number_as_string)
    number_value = 0
    number_case = "4"

    if number_length == 4 or number_length == 7: #1000 or 1 000 000
        number_value = number_as_string[0]
        if 1 < int(number_value) < 10:
            number_case = "2"
        else:
            number_case = "1"

    if number_length == 5 or number_length == 8: #10 000 or 10 000 000
        number_value = number_as_string[0:2]
        if 9 < int(number_value) < 21:
            number_case = "3"
        elif int(number_value[1]) == 1 and int(number_value) > 11:
            number_case = "1"
        elif int(number_value) > 10 and number_value[1] != "0" and number_value[1] != "1":
            number_case = "2"
        elif int(number_value) > 10:
            number_case = "3"
    
    if number_length == 9 or number_length == 6:
        number_value = number_as_string[0:3]
        if number_value[1:] == "00" or number_value[2] == "0" or 9 < int(number_value[1:]) < 20:
            number_case = "3"
        elif number_value[1] != "1" and number_value[2] == "1":
            number_case = "1"
        elif int(number_value) > 10 and number_value[1] != "0" and number_value[1] != "1":
            number_case = "2" 

    return number_case


def one_to_hundred_excepted(integer): #1 - 99
    integer = int(integer)
    number_as_string = str(integer)
    number_lenght = len(number_as_string)

    if integer == 0:
        return "nulis"
    if integer < 20:
        return zero_to_twenty.get(number_as_string)
    elif number_as_string[-1] == "0" and number_lenght == 2:
        return decimals.get(number_as_string[0])
    elif 19 < integer < 100:
        return decimals.get(number_as_string[0]) + " " + zero_to_twenty.get(number_as_string[-1])


def hundred_to_thousand_excepted(integer):#100 - 999
    integer = int(integer)
    number_as_string = str(integer)
    number_length = len(number_as_string)
    hundreds_value = "1"
    hundred = integer // 100
    hundred_as_string = str(hundred)

    if integer < 100:
        return one_to_hundred_excepted(integer)

    if int(number_as_string[0]) > 1:
        hundreds_value = "2"

    if integer < 1000:
        if number_as_string[1:] == "00":
            return zero_to_twenty.get(str(hundred)) + " " + hundreds.get(hundreds_value)
        else:
            return zero_to_twenty.get(str(hundred))+ " " + hundreds.get(hundreds_value) + " " + one_to_hundred_excepted(number_as_string[1:])
        
    return "not implemented"


def thousand_to_million_excepted(integer): #1000 - 999999
    integer = int(integer)
    number_as_string = str(integer)
    number_length = len(number_as_string)
    number_case(number_as_string)
    thousands_value = number_case(number_as_string)
    thousand = integer // 1000
    thousand_as_string = str(thousand)
    
    if integer < 1000:
        return hundred_to_thousand_excepted(integer)
    if integer < 10000:
        if number_as_string[1:] == "000":
            return zero_to_twenty.get(number_as_string[0:1]) + " " + thousands.get(thousands_value)
        return zero_to_twenty.get(number_as_string[0:1]) + " " + thousands.get(thousands_value) + " " + hundred_to_thousand_excepted(number_as_string[1:])
    if 9999 < integer < 100000:
        if number_as_string[2:] == "000":
            return hundred_to_thousand_excepted(number_as_string[0:2]) + " " + thousands.get(thousands_value)
        return hundred_to_thousand_excepted(number_as_string[0:2]) + " " + thousands.get(thousands_value) + " " + hundred_to_thousand_excepted(number_as_string[2:])
    if 99999 < integer < 1000000:
        if number_as_string[-4:] == "0000":
            return hundred_to_thousand_excepted(number_as_string[:3]) + " " + thousands.get(thousands_value)
        return hundred_to_thousand_excepted(number_as_string[:3]) + " " + thousands.get(thousands_value) + " " + hundred_to_thousand_excepted(number_as_string[3:])
    
    return "not implemented"

def suma_zodziais(integer): #1 000 000 - 999 999 999
    integer = int(integer)
    number_as_string = str(integer)
    number_length = len(number_as_string)
    number_case(number_as_string)
    millions_value = number_case(number_as_string)
    million = integer // 1000000
    million_as_string = str(million)

    if integer < 1000000:
        return thousand_to_million_excepted(integer)

    if number_length == 7:
        if number_as_string[1:] == "000000":
            return zero_to_twenty.get(number_as_string[0]) + " " + millions.get(millions_value)
        return hundred_to_thousand_excepted(number_as_string[0]) + " " + millions.get(millions_value) + " " + thousand_to_million_excepted(number_as_string[1:])
    elif number_length == 8:
        if number_as_string[2:] == "000000":
            return hundred_to_thousand_excepted(number_as_string[0:2]) + " " + millions.get(millions_value)
        return hundred_to_thousand_excepted(number_as_string[0:2]) + " " + millions.get(millions_value) + " " + thousand_to_million_excepted(number_as_string[2:])
    elif number_length == 9:
        if number_as_string[3:] == "000000":
            return hundred_to_thousand_excepted(number_as_string[0:3]) + " " + millions.get(millions_value)
        return thousand_to_million_excepted(number_as_string[0:3]) + " " + millions.get(millions_value) + " " + thousand_to_million_excepted(number_as_string[3:])

    return "not implemented"

print(suma_zodziais(513121554))

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
if (suma_zodziais(1000) != "vienas tūkstantis"):
    print("failure 1000")
if (suma_zodziais(1001) != "vienas tūkstantis vienas"):
    print("failure 1001")
if (suma_zodziais(1041) != "vienas tūkstantis keturiasdešimt vienas"):
    print("failure 1041")    
if (suma_zodziais(1045) != "vienas tūkstantis keturiasdešimt penki"):
    print("failure 1045")
if (suma_zodziais(1121) != "vienas tūkstantis vienas šimtas dvidešimt vienas"):
    print("failure 1121")
if (suma_zodziais(1131) != "vienas tūkstantis vienas šimtas trisdešimt vienas"):
    print("failure 1131")
if (suma_zodziais(1931) != "vienas tūkstantis devyni šimtai trisdešimt vienas"):
    print("failure 1931")
if (suma_zodziais(2000) != "du tūkstančiai"):
    print("failure 2000")
if (suma_zodziais(2555) != "du tūkstančiai penki šimtai penkiasdešimt penki"):
    print("failure 2555")
if (suma_zodziais(10000) != "dešimt tūkstančių"):
    print("failure 10000")
if (suma_zodziais(11000) != "vienuolika tūkstančių"):
    print("failure 11000")
if (suma_zodziais(11001) != "vienuolika tūkstančių vienas"):
    print("failure 11001")
if (suma_zodziais(14000) != "keturiolika tūkstančių"):
    print("failure 14000")
if (suma_zodziais(20001) != "dvidešimt tūkstančių vienas"):
    print("failure 20001")
if (suma_zodziais(20101) != "dvidešimt tūkstančių vienas šimtas vienas"):
    print("failure 20101")
if (suma_zodziais(50971) != "penkiasdešimt tūkstančių devyni šimtai septyniasdešimt vienas"):
    print("failure 50971")
if (suma_zodziais(51000) != "penkiasdešimt vienas tūkstantis"):
    print("failure 51000")
if (suma_zodziais(51971) != "penkiasdešimt vienas tūkstantis devyni šimtai septyniasdešimt vienas"):
    print("failure 51971")
if (suma_zodziais(81971) != "aštuoniasdešimt vienas tūkstantis devyni šimtai septyniasdešimt vienas"):
    print("failure 81971")
if (suma_zodziais(81511) != "aštuoniasdešimt vienas tūkstantis penki šimtai vienuolika"):
    print("failure 81511")
if (suma_zodziais(82111) != "aštuoniasdešimt du tūkstančiai vienas šimtas vienuolika"):
    print("failure 82111")
if (suma_zodziais(100000) != "vienas šimtas tūkstančių"):
    print("failure 100000")
if (suma_zodziais(100001) != "vienas šimtas tūkstančių vienas"):
    print("failure 100001")
if (suma_zodziais(110001) != "vienas šimtas dešimt tūkstančių vienas"):
    print("failure 110001")
if (suma_zodziais(111001) != "vienas šimtas vienuolika tūkstančių vienas"):
    print("failure 111001")
if (suma_zodziais(146150) != "vienas šimtas keturiasdešimt šeši tūkstančiai vienas šimtas penkiasdešimt"):
    print("failure 146150")
if (suma_zodziais(214550) != "du šimtai keturiolika tūkstančių penki šimtai penkiasdešimt"):
    print("failure 214550")
if (suma_zodziais(314961) != "trys šimtai keturiolika tūkstančių devyni šimtai šešiasdešimt vienas"):
    print("failure  314961")
if (suma_zodziais(462365) != "keturi šimtai šešiasdešimt du tūkstančiai trys šimtai šešiasdešimt penki"):
    print("failure 462365")
if (suma_zodziais(678753) != "šeši šimtai septyniasdešimt aštuoni tūkstančiai septyni šimtai penkiasdešimt trys"):
    print("failure 678753")
if (suma_zodziais(996411) != "devyni šimtai devyniasdešimt šeši tūkstančiai keturi šimtai vienuolika"):
    print("failure 996411")
if (suma_zodziais(1000001) != 'vienas milijonas vienas'):
    print("failure 1000001")
if (suma_zodziais(1000011) != 'vienas milijonas vienuolika'):
    print("failure 1000011")
if (suma_zodziais(1000023) != "vienas milijonas dvidešimt trys"):
    print("failure 1000023")
if (suma_zodziais(1000070) != "vienas milijonas septyniasdešimt"):
    print("failure 1000070")
if (suma_zodziais(1000099) != "vienas milijonas devyniasdešimt devyni"):
    print("failure 1000099")
if (suma_zodziais(1000100) != "vienas milijonas vienas šimtas"):
    print("failure 1000100")
if (suma_zodziais(1000101) != "vienas milijonas vienas šimtas vienas"):
    print("failure 1000101")
if (suma_zodziais(1000110) != "vienas milijonas vienas šimtas dešimt"):
    print("failure 1000110")
if (suma_zodziais(1000111) != "vienas milijonas vienas šimtas vienuolika"):
    print("failure 1000111")
if (suma_zodziais(1000119) != "vienas milijonas vienas šimtas devyniolika"):
    print("failure 1000119")
if (suma_zodziais(1000120) != "vienas milijonas vienas šimtas dvidešimt"):
    print("failure 1000120")
if (suma_zodziais(1000129) != "vienas milijonas vienas šimtas dvidešimt devyni"):
    print("failure 1000129")
if (suma_zodziais(1000190) != "vienas milijonas vienas šimtas devyniasdešimt"):
    print("failure 1000190")
if (suma_zodziais(1000200) != "vienas milijonas du šimtai"):
    print("failure 1000200")
if (suma_zodziais(1000279) != "vienas milijonas du šimtai septyniasdešimt devyni"):
    print("failure 1000279")
if (suma_zodziais(1000900) != "vienas milijonas devyni šimtai"):
    print("failure 1000900")
if (suma_zodziais(1000999) != "vienas milijonas devyni šimtai devyniasdešimt devyni"):
    print("failure 1000999")
if (suma_zodziais(1001000) != "vienas milijonas vienas tūkstantis"):
    print("failure 1001000")
if (suma_zodziais(1001001) != "vienas milijonas vienas tūkstantis vienas"):
    print("failure 1001001")
if (suma_zodziais(1001041) != "vienas milijonas vienas tūkstantis keturiasdešimt vienas"):
    print("failure 1001041")    
if (suma_zodziais(1001045) != "vienas milijonas vienas tūkstantis keturiasdešimt penki"):
    print("failure 1001045")
if (suma_zodziais(1001121) != "vienas milijonas vienas tūkstantis vienas šimtas dvidešimt vienas"):
    print("failure 1001121")
if (suma_zodziais(1001131) != "vienas milijonas vienas tūkstantis vienas šimtas trisdešimt vienas"):
    print("failure 1001131")
if (suma_zodziais(1001931) != "vienas milijonas vienas tūkstantis devyni šimtai trisdešimt vienas"):
    print("failure 1001931")
if (suma_zodziais(1002000) != "vienas milijonas du tūkstančiai"):
    print("failure 1002000")
if (suma_zodziais(1002555) != "vienas milijonas du tūkstančiai penki šimtai penkiasdešimt penki"):
    print("failure 1002555")
if (suma_zodziais(1010000) != "vienas milijonas dešimt tūkstančių"):
    print("failure 1010000")
if (suma_zodziais(1011000) != "vienas milijonas vienuolika tūkstančių"):
    print("failure 1011000")
if (suma_zodziais(1011001) != "vienas milijonas vienuolika tūkstančių vienas"):
    print("failure 1011001")
if (suma_zodziais(1014000) != "vienas milijonas keturiolika tūkstančių"):
    print("failure 1014000")
if (suma_zodziais(1020001) != "vienas milijonas dvidešimt tūkstančių vienas"):
    print("failure 1020001")
if (suma_zodziais(1020101) != "vienas milijonas dvidešimt tūkstančių vienas šimtas vienas"):
    print("failure 1020101")
if (suma_zodziais(1050971) != "vienas milijonas penkiasdešimt tūkstančių devyni šimtai septyniasdešimt vienas"):
    print("failure 1050971")
if (suma_zodziais(1051000) != "vienas milijonas penkiasdešimt vienas tūkstantis"):
    print("failure 1051000")
if (suma_zodziais(1051971) != "vienas milijonas penkiasdešimt vienas tūkstantis devyni šimtai septyniasdešimt vienas"):
    print("failure 1051971")
if (suma_zodziais(1081971) != "vienas milijonas aštuoniasdešimt vienas tūkstantis devyni šimtai septyniasdešimt vienas"):
    print("failure 1081971")
if (suma_zodziais(1081511) != "vienas milijonas aštuoniasdešimt vienas tūkstantis penki šimtai vienuolika"):
    print("failure 1081511")
if (suma_zodziais(1082111) != "vienas milijonas aštuoniasdešimt du tūkstančiai vienas šimtas vienuolika"):
    print("failure 1082111")
if (suma_zodziais(100000) != "vienas šimtas tūkstančių"):
    print("failure 100000")
if (suma_zodziais(1100001) != "vienas milijonas vienas šimtas tūkstančių vienas"):
    print("failure 1100001")
if (suma_zodziais(1110001) != "vienas milijonas vienas šimtas dešimt tūkstančių vienas"):
    print("failure 1110001")
if (suma_zodziais(1111001) != "vienas milijonas vienas šimtas vienuolika tūkstančių vienas"):
    print("failure 1111001")
if (suma_zodziais(1146150) != "vienas milijonas vienas šimtas keturiasdešimt šeši tūkstančiai vienas šimtas penkiasdešimt"):
    print("failure 1146150")
if (suma_zodziais(1214550) != "vienas milijonas du šimtai keturiolika tūkstančių penki šimtai penkiasdešimt"):
    print("failure 1214550")
if (suma_zodziais(1314961) != "vienas milijonas trys šimtai keturiolika tūkstančių devyni šimtai šešiasdešimt vienas"):
    print("failure 1314961")
if (suma_zodziais(1462365) != "vienas milijonas keturi šimtai šešiasdešimt du tūkstančiai trys šimtai šešiasdešimt penki"):
    print("failure 1462365")
if (suma_zodziais(1678753) != "vienas milijonas šeši šimtai septyniasdešimt aštuoni tūkstančiai septyni šimtai penkiasdešimt trys"):
    print("failure 1678753")
if (suma_zodziais(1996411) != "vienas milijonas devyni šimtai devyniasdešimt šeši tūkstančiai keturi šimtai vienuolika"):
    print("failure 1996411")
if (suma_zodziais(2020101) != "du milijonai dvidešimt tūkstančių vienas šimtas vienas"):
    print("failure 2020101")
if (suma_zodziais(84121001) != "aštuoniasdešimt keturi milijonai vienas šimtas dvidešimt vienas tūkstantis vienas"):
    print("failure 84121001")
if (suma_zodziais(100000000) != "vienas šimtas milijonų"):
    print("failure 100000000")
if (suma_zodziais(150000000) != "vienas šimtas penkiasdešimt milijonų"):
    print("failure 150000000")
if (suma_zodziais(154000000) != "vienas šimtas penkiasdešimt keturi milijonai"):
    print("failure 154000000")
if (suma_zodziais(500000000) != "penki šimtai milijonų"):
    print("failure 500000000")
if (suma_zodziais(513121554) != "penki šimtai trylika milijonų vienas šimtas dvidešimt vienas tūkstantis penki šimtai penkiasdešimt keturi"):
    print("failure 513121554")

print("All tests passed!")
