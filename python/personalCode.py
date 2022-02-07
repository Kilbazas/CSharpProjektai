# our task is to implement peron coder validator
# what is the first step?
# algorithm steps:
    # 1. read user input
    # 1.1. verify lengh of input (missing)
    # 2. verify man or woman
    # 3. verify is number
    # 4. get birth date
    # 5. verify leaf year
    # 6. verify month
    # 7. verify day
    # 8. verify last number

def personal_code_lenght_checker(person_code_param):
    result = False
    person_code_param = str(person_code_param)
    if len(person_code_param) == 11:
        result = True
    return result

def is_entered_personal_code_is_number(person_code_param):
    result = True
    person_code_param = str(person_code_param)
    for x in range(len(person_code_param)):
        if(ord(person_code_param[x]) < 48 or ord(person_code_param[x]) > 57): 
            result = False
            break
    return result

def get_birth_date_from_personal_code(person_code_param):
    return person_code_param[0:7] 

def is_last_number_is_exeption_for_no_birth_date(person_code_param):
    result = False 
    birth_date = get_birth_date_from_personal_code(person_code_param)
    if birth_date[1:3] == "00" or birth_date[3:5] == "00":
        result = True
    return result

def is_personal_code_exeptional(person_code_param):
    result = False
    input_first_number = person_code_param[0]
    if input_first_number == '9':
        result = True
    return result

def is_entered_personal_code_first_number_valid(person_code_param):
    result = False
    first_number_list = ["1", "2", "3", "4", "5", "6", "9"]
    first_number = person_code_param[0]
    if first_number in first_number_list:
        result = True
    return result

def what_year_is_it(person_code_param):
    year = 5
    birth_date = get_birth_date_from_personal_code(person_code_param)
    input_first_number = birth_date[0]
    if input_first_number == '1' or input_first_number == '2':
        year = "18" + str(birth_date[1:3])
    if input_first_number == '3' or input_first_number == '4':
        year = "19" + str(birth_date[1:3])
    if input_first_number == '5' or input_first_number == '6':
        year = "20" + str(birth_date[1:3])
    return int(year)

def is_entered_personal_code_is_leaf_year(person_code_param):
    result = False
    year = what_year_is_it(person_code_param)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        result = True
    return result

def is_entered_personal_code_month_is_in_range(person_code_param):
    result = False  
    birth_date = get_birth_date_from_personal_code(person_code_param)
    month = birth_date[3:5]
    month = int(month)
    if 0 < month < 13:
        result = True 
    if is_personal_code_exeptional(person_code_param) == True:
        result = True
    if is_last_number_is_exeption_for_no_birth_date(person_code_param) == True:
        result = True 
    return result

def is_entered_personal_code_day_is_in_range(person_code_param):
    result = False  
    birth_date = get_birth_date_from_personal_code(person_code_param)
    days_in_month_list_leaf = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = birth_date[5:7]
    days = int(days)
    month = birth_date[3:5] 
    month = int(month)
    if is_entered_personal_code_is_leaf_year(person_code_param) == True:
        if days <= days_in_month_list_leaf[month - 1]:
            result = True
    if days <= days_in_month_list[month - 1]:
        result = True 
    if is_personal_code_exeptional(person_code_param) == True:
        result = True
    return result

def is_last_number_of_personal_code_is_legit(person_code_param):
    result = False
    input_last_number = person_code_param
    last_number = ((int(input_last_number[0]) * 1 + int(input_last_number[1]) * 2 + int(input_last_number[2]) * 3 + int(input_last_number[3]) * 4 + int(input_last_number[4]) * 5 +
                  int(input_last_number[5]) * 6 + int(input_last_number[6]) * 7 + int(input_last_number[7]) * 8 + int(input_last_number[8]) * 9 + int(input_last_number[9]) * 1)  % 11)
    if last_number == 10:
        last_number = ((int(input_last_number[0]) * 3 + int(input_last_number[1]) * 4 + int(input_last_number[2]) * 5 + int(input_last_number[3]) * 6 + int(input_last_number[4]) * 7 
                       + int(input_last_number[5]) * 8 + int(input_last_number[6]) * 9 + int(input_last_number[7]) * 1 + int(input_last_number[8]) * 2 + int(input_last_number[9]) * 3) % 11)
        if last_number == 10:
            last_number = 0 
    if int(input_last_number[10]) == last_number:
        result = True
    if is_personal_code_exeptional(person_code_param) == True:
        result = True
    return result 

def is_person_isnt_too_old(person_code_param):
    result = False
    year = what_year_is_it(person_code_param)
    if year > 1890:
        result = True
    return result

def is_person_isnt_too_young(person_code_param):
    result = False
    year = what_year_is_it(person_code_param)
    if year < 2023:
        result = True
    return result

def verify_personal_code(personal_code):
    if personal_code == None:
        return "Input can not be empty"
    if personal_code == "":
        return "Input can not be empty"

    personal_code = str(personal_code)
    personal_code = "".join(personal_code.split())

    if personal_code_lenght_checker(personal_code) == False:
        return "Personal code is too short or too long."
    if is_entered_personal_code_is_number(personal_code) == False:
        return "Personal code has unexpected symbols. It must be a number."
    if is_entered_personal_code_first_number_valid(personal_code) == False:
        return "Personal code first number is incorrect."
    if is_entered_personal_code_month_is_in_range(personal_code) == False:
        return "Personal code month is not in range."
    if is_entered_personal_code_day_is_in_range(personal_code) == False:
        return "Personal code day is not in range."
    if is_last_number_of_personal_code_is_legit(personal_code) == False:
        "Personal code is invalid. Last number is not comfirmed."
    if is_person_isnt_too_old(personal_code) == False:
        return "There is no human alive that old..."
    if is_person_isnt_too_young(personal_code) == False:
        return "Come back after your birthday..."

    return "valid"

#tests

if  verify_personal_code(None) == "valid":
    print("Personal code input can not be None.")

if  verify_personal_code("") == "valid":
    print("Personal code input can not be empty.")

if  verify_personal_code("3 9 6 0124 00 40") == "valid": #Logika is not found.
    print("Method join does not work.")

if  verify_personal_code("396012400400") == "valid":
    print("Personal code lenght checker is not working.")

if  verify_personal_code("3960124004") == "valid":
    print("Personal code lenght checker is not working.")

if  verify_personal_code("LT396012400") == "valid":
    print("Personal code symbol checker does not work.")

if  verify_personal_code("79601240040") == "valid":
    print("Personal code first symbol checker does not work.")

if  verify_personal_code("39615240040") == "valid":
    print("Personal code month checker does not work.")

if  verify_personal_code("39600240046") == False:
    print("Personal code month checker does not work. If someone doesn't know birth month case.")

if  verify_personal_code("99600240040") == False:
    print("Personal code month checker does not work. If code starts with 9 case.")

if  verify_personal_code("39601000044") == False:
    print("Personal code day checker does not work. If someone does't know birth day case.")

if  verify_personal_code("39601400040") == "valid":
    print("Personal code day checker does not work. Leaf year case.")

if  verify_personal_code("39602290047") == False:
    print("Personal code day checker does not work. Leaf year case.")

if  verify_personal_code("99601400040") == False:
    print("Personal code day checker does not work. If code starts with 9 case.")

if  verify_personal_code("39601240043") == "valid": #logika is not found
    print("Personal code last number checker does't work.")

if  verify_personal_code("17901240040") == "valid":
    print("Person is too old")

if  verify_personal_code("27901240040") == "valid":
    print("Person is too old")

if  verify_personal_code("59601240040") == "valid":
    print("Person is too young")

if  verify_personal_code("69601240040") == "valid":
    print("Person is too young")

print("All tests passed")
