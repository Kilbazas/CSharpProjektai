# our task is to implement peron coder validator
# what is the first step?
# algorithm steps:
    # 1. read user input
    # 1.1. verify lengh of input 
    # 2. verify first two symbols
    # 2.2. verify if bank number is valid on MOD97
    # 3. verify Bank code
    # 4. verify control number
    # 5. Verify bank name
char_symbol = {'A':'10',
               'B':'11',
               'C':'12',
               'D':'13',
               'E':'14',
               'F':'15',
               'G':'16',
               'H':'17',
               'I':'18',
               'J':'19',
               'K':'20',
               'L':'21',
               'M':'22',
               'N':'23',
               'O':'24',
               'P':'25',
               'Q':'26',
               'R':'27',
               'S':'28',
               'T':'29',
               'U':'30',
               'V':'31',
               'W':'32',
               'X':'33',
               'Y':'34',
               'Z':'35',
               }
def read_iban_number():
    iban_number = input("What is your account number? ")
    iban_number = "".join(iban_number.split())
    iban_number = iban_number.upper()
    return iban_number

def iban_number_lenght_checker(iban_param):
    result = False
    if len(iban_param) == 20:
        result = True
    return result

def iban_symbols_validation(iban_param):
    result = True
    chars = iban_param[0:2]
    numbers = iban_param[2:]
    for x in range(len(numbers)):
        if(ord(numbers[x]) < 48 or ord(numbers[x]) > 57): 
            result = False
            break
    if chars != "LT":
        result = False
    return result

def iban_to_number(iban_param):
    iban_check_code = iban_param[4:] + iban_param[0:2] + '00'
    iban_check_code = list(iban_check_code)
    new_iban_string = ""
    for char in range(len(iban_check_code)):
        if iban_check_code[char] in char_symbol:
            value = char_symbol.get(iban_check_code[char])
            iban_check_code[char] = value 
    for i in range(len(iban_check_code)):
        new_iban_string = new_iban_string + str(iban_check_code[i])
    return new_iban_string

def is_iban_check_numbers_valid(iban_param):
    result = False
    iban_as_number = iban_to_number(iban_param)
    iban_control_numbers = (98 - (int(iban_as_number) % 97))
    if iban_control_numbers < 10:
        Iban_control_numbers = '0'+ str(iban_control_numbers)
    if int(iban_control_numbers) == int(iban_param[2:4]):
        result = True
    return result

def is_iban_valid_mod_formula(iban_param):   
    result = False
    iban_as_number = iban_to_number(iban_param)
    iban_as_number = iban_as_number[:-2] + iban_param[2:4]
    if int(iban_as_number) % 97 == 1:
        result = True
    return result

def is_iban_lithuanian(iban_param):
    result = False 
    if iban_param[0:2] == "LT":
        result = True
    return result

def is_bank_code_valid(iban_param):
    result = False
    if iban_param[4:9]:
        result = True
    return result

def return_bank_name(iban_param):
    result = ""
    bank_id_and_name = {'72900':"Citadelė",
                        '73000':"Swedbank",
                        '40100':"Luminor", 
                        '21400':"Nodea", 
                        '32500':"Revolut", 
                        '70440':"SEB", 
                        '72300':"Medicinos bankas", 
                        '71800':"Šiaulių bankas"}

    if is_bank_code_valid(iban_param) == True:
        result = bank_id_and_name.get(iban_param[4:9], 'Not found')
    return print(result)


#tests
iban = read_iban_number()

if(iban_number_lenght_checker(iban) == False):
    print("Iban is too short or too long")
else:
    print("Personal code is from 20 symbols")
if (is_iban_check_numbers_valid(iban) == False):
    print("Iban check numbers are invalid")
else:
    print("Iban check numbers are valid")
if (iban_symbols_validation(iban) == False):
    print("Something wrong with iban format")
else:
    print("Iban format is validated")
if (is_iban_valid_mod_formula(iban) == False):
    print("Iban number does not compile with 97 mod")
else:
    print("Iban number does work with 97 mod")
if(is_iban_lithuanian(iban) == False):
    print("This is not Lithuanian bank")
else:
    print("It is Lithuanian bank")
if(is_bank_code_valid(iban) == False):
    print("Bank code is not recognisible")
else:
    print("We can find this bank in the list")
return_bank_name(iban)
