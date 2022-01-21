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

    
def read_personal_code():
    person_code = input("What is your personal code? ")
    return person_code

def personal_code_lenght_checker(person_code_param):
    result = False
    if len(person_code_param) == 11:
        result = True
    return result

def is_entered_personal_code_is_woman_or_man(person_code_param):
    result = 0 # 0 - man, 1 - woman, 2 - wrong
    if person_code_param[0] == '1' or person_code_param[0] == '3' or person_code_param[0] == '5' : 
        result = 0
    if person_code_param[0] == '2' or person_code_param[0] == '4' or person_code_param[0] == '6':
        result = 1
    if (person_code_param[0] != '1' and person_code_param[0] != '3' and person_code_param[0] != '5' and person_code_param[0] != '2' and person_code_param[0] != '4' and person_code_param[0] != '6'): 
        result = 2
    return result

def is_entered_personal_code_is_number(person_code_param):
    result = True
    n = len(person_code_param)
    for x in range(n):
        if(ord(person_code_param[x]) < 48 or ord(person_code_param[x]) > 57): 
            result = False
            break
    return result

def get_birth_date_from_personal_code(person_code_param):
    return person_code_param[0:7] 

def what_year_is_it(person_code_param):
    birth_date = get_birth_date_from_personal_code(person_code_param)
    input_first_number = birth_date[0]
    if input_first_number == '1' or input_first_number == '2':
        year = "18" + str(birth_date[1:3])
    if input_first_number == '3' or input_first_number == '4':
        year = "19" + str(birth_date[1:3])
    if input_first_number == '5' or input_first_number == '6':
        year = "20" + str(birth_date[1:3])
    year = int(year)
    return year

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
    return result 

def is_last_number_is_exeption_for_no_birth_date(person_code_param):
    result = False 
    birth_date = get_birth_date_from_personal_code(person_code_param)
    if birth_date[1:3] == "00" or birth_date[3:5] == "00":
        result = True
    return result

def is_last_number_is_exeptional(person_code_param):
    result = False
    input_first_number = person_code_param[0]
    if input_first_number == '9':
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


#unit tests

personal_code = read_personal_code()

if(personal_code_lenght_checker(personal_code) == False):
    print("Personal code is too short or too long")
else:
    print("Personal code is from 11 digits")

if(is_entered_personal_code_is_woman_or_man(personal_code) == 1):
    print("Person is woman")
    
if(is_entered_personal_code_is_woman_or_man(personal_code) == 0):
    print("Person is Man")

if(is_entered_personal_code_is_woman_or_man(personal_code) == 2):
    print("Wrong")

if(is_entered_personal_code_is_number(personal_code)):
    print("Personal code is number")

if(is_entered_personal_code_is_number(personal_code) !=  True):
    print("Wrong its not number")

if(is_entered_personal_code_month_is_in_range(personal_code) == True):
   print("Entered personal code month is in range")
else:
   print("Entered personal code month is not in range")
   
if(is_entered_personal_code_day_is_in_range(personal_code) == True):
    print("Entered personal code day is in range")
else:
    print("Entered personal code day is not in range")
if(is_last_number_of_personal_code_is_legit(personal_code) == True):
    print("last number is legit")
else:
    print("last number is not legit")
if(is_last_number_is_exeption_for_no_birth_date(personal_code) == True):
    print("Personal number has an exeption")
else:
    print("There is no exeptions")
if(is_last_number_is_exeptional(personal_code) == True):
    print("Personal code is exeptional")
else:
    print("Personal code is regular")
if(is_person_isnt_too_old(personal_code) == True):
    print("Person isn't too old")
else:
    print("Person is too old")
if(is_person_isnt_too_young(personal_code) == True):
    print("Person isn't too young")
else:
    print("Person is too young")
