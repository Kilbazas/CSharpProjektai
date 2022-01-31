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
        new_iban_string = new_iban_string + iban_check_code[i]
    return new_iban_string

def is_iban_check_numbers_valid(iban_param):
    result = False
    iban_as_number = int(iban_to_number(iban_param))
    iban_control_numbers = ((98 - iban_as_number) % 97)
    if iban_control_numbers < 10:
        iban_control_numbers = '0'+ str(iban_control_numbers)
    if int(iban_control_numbers) == iban_param[2:4]:
        result = True
    return result

def is_iban_valid_mod_formula(iban_param):   
    result = False
    iban_as_number = iban_to_number(iban_param)
    iban_as_number = iban_as_number[:-2] + iban_param[2:4]
    if int(iban_as_number) % 97 == 1:
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

def verify_iban_number(iban):
    if iban == None:
        return "Input can't be empty."
    if iban == "":
        return "Input can't be empty"
    
    iban = str(iban)
    iban = "".join(iban.split()).upper()
   
    if iban_number_lenght_checker(iban) == False:
        return "Iban is too short or too long."
    if iban_symbols_validation(iban) == False:
        return "There is unexpected symbols in your iban number."
    if is_iban_check_numbers_valid(iban) == False:
        return "Iban check numbers are invalid."
    if is_iban_valid_mod_formula(iban) == False:
        return "Iban is invalid. It didn't pass mod97 algorithm."
    if is_bank_code_valid(iban) == False:
        return "Iban is invalid. There is no bank in Lithuania with this bank code."
    return "valid"

#tests

if verify_iban_number(None) == "valid":
    print("Something is wrong. There is no value entered.")
if verify_iban_number("") == "valid":
    print("Something is wrong. There is zero values entered.")
if verify_iban_number("lt557300010000000036") == False:
    print("Something is wrong. Upper case doesn't work.")
if verify_iban_number("LT55 7300 0100 0000 0036") == False:
    print("Something is wrong. Algorithm does not remove white space.")
if verify_iban_number(int(2129557300010000000036)) == False:
    print("Something is wrong. Algorithm accepts non-string input.")
if verify_iban_number("LT456465") == "valid":
    print("Something is wrong. Iban number is too short.")
if verify_iban_number("LT321321321212123121313132313") == "valid":
    print("Something is wrong. Iban number is too long.")
if verify_iban_number("XS557300010000000036") == "valid":
    print("Something is wrong. Iban number has unexpected symbols.")
if verify_iban_number("LT5573000100000000,6") == "valid":
    print("Something is wrong. Iban has unexpected symbols.")
if verify_iban_number("LT55730A010000000036") == "valid":
    print("Something is wrong. Iban number has unexpected symbols.")
if verify_iban_number("LT507300010000000036") == "Valid":
    print("Something is wrong. Iban check number is invalid.")
if verify_iban_number("LT557300010000000016") == "valid":
    print("Something is wrong. Mod 97 algorithm does not work.")
if verify_iban_number("XS557300010000000036") == "valid":
    print("Something is wrong. Country checker is not working.") #kind of the same test as before
if verify_iban_number("LT557200010000000036") == "valid":
    print("Something is wrong. Bank code identifier do not work.")

print("All tests passed")
