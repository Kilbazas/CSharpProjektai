months = ["sausis", "vasaris", "kovas", "balandis", "geguze", "birzelis", "liepa", "rugpjutis", "rugsejis", "spalis", "lapkritis", "gruodis"]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def input_number():
    global personalCode
    global personalCodeCharList
    personalCode = input("Ivesk savo asmens koda: ")
    personalCodeCharList = list(personalCode.replace(" ", "") )
    lenght_checker()
    
def lenght_checker():
    if len(personalCodeCharList) != 11:
        print("Neteisingai ivestas asmens kodas: per daug arba per mazai skaitmenu")
        input_number()
    else:    
        return checker()

def checker():
    centuryNumber = int(personalCodeCharList[0])
    birthYear = personalCodeCharList[1] + personalCodeCharList[2]
    birthMonth = personalCodeCharList[3] + personalCodeCharList[4]
    birthDay = personalCodeCharList[5] + personalCodeCharList[6]
    serialNumber = personalCodeCharList[7] + personalCodeCharList[8] + personalCodeCharList[9]
    controlNumber = personalCodeCharList[10]

    def year_checker():
        year_result = ""
        if centuryNumber == 1 or centuryNumber == 2:
            year_result = "18" + str(birthYear)
        if centuryNumber == 3 or centuryNumber == 4:
            year_result = "19" + str(birthYear)
        if centuryNumber == 5 or centuryNumber == 6:
            year_result = "20" + str(birthYear)
            
        return int(year_result)

    def leap_year(year_param):
        return year_param % 4 == 0 and (year_param % 100 != 0 or year_param % 400 == 0)            

    while True:
        if leap_year(year_checker()):
            days[1] = 29
        else:
            print("Vasaris siais metais neturejo 29 dienu")
            return input_number()

        if int(centuryNumber) == 5 or int(centuryNumber) == 6:
            if int(birthYear) > 22:
                print("Negali gimt sitam amziuj ir but vyresnis, nei 22")
                return input_number()

        if int(birthMonth) < 1 or int(birthMonth) > 12:
            print("Neteisingai ivestas menuo")
            return input_number()

        if int(birthDay) > days[int(birthMonth)-1]:
            print("Neteisingai ivesta diena")
            return input_number()

        print(f"Tavo asmens kodas {personalCode} teisingas")
        break


input_number()


#print(int(centuryNumber))
#print(int(birthYear))
#print(int(birthMonth))
#print(int(birthDay))
#print(int(serialNumber))
#print(int(controlNumber))

