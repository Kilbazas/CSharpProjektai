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



def read_personal_code():
    # write your implementation here
    person_code = input("What is your personal code? ")
    return person_code

def is_entered_personal_code_is_woman_or_man(person_code_param):
    result = 0 # 0 - man, 1 - woman, 2 - wrong
    if person_code_param[0] == '3': 
        result = 0
    if person_code_param[0] == '4':
        result = 1
    if (person_code_param[0] != '3' and person_code_param[0] != "4"):  # this code is wrong 
        result = 2
    return result

def is_entered_personal_code_is_number(person_code_param):
    result = True
    n = len(person_code_param)
    for x in range(n):
        if(ord(person_code_param[x]) < 48 or ord(person_code_param[x]) > 57): # we need to read how to make it more beautiful in Python
            result = False
            break
    return result

def get_birth_date_from_personal_code(person_code_param):
    return person_code_param[1:7] 

def is_entered_personal_code_is_leaf_year(person_code_param):
    result = False
    birth_date = get_birth_date_from_personal_code(person_code_param)
    year = "19"+ str(birth_date[0:2])
    year = int(year)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        result = True
    return result

def is_entered_personal_code_month_is_in_range(person_code_param):
    result = False  
    birth_date = get_birth_date_from_personal_code(person_code_param)
    # implementation goes here
    month = person_code_param[3:5]
    print(month)
    month = int(month)
    if 0 < month < 13:
        result = True  # you do have birth_date 851221 - 12 is your month
    return result # should return true if in range from 1 to 12? Yes

def is_entered_personal_code_day_is_in_range(person_code_param):
    result = False  
    birth_date = get_birth_date_from_personal_code(person_code_param)
    # implementation goes here
    days_in_month_list_leaf = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    days = person_code_param[5:7]
    days = int(days)
    print(days)
    month = person_code_param[3:5] #   person_code_param[3:5] - 1 ? True. Good
    
    month = int(month)
    if is_entered_personal_code_is_leaf_year(person_code_param) == True:
        if days <= days_in_month_list_leaf[month - 1]:
            result = True
    if days <= days_in_month_list[month - 1]:
        result = True 
    return result
#unit tests

personal_code = read_personal_code()

if(is_entered_personal_code_is_woman_or_man(personal_code) == 1):
    print("Woman")
    
if(is_entered_personal_code_is_woman_or_man(personal_code) == 0):
    print("Man")

if(is_entered_personal_code_is_woman_or_man(personal_code) == 2):
    print("Wrong")

if(is_entered_personal_code_is_number(personal_code)):
    print("Number")

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

    
