country_info = {
    'AL': [23, 'Albania'],
    'AD': [24, 'Andorra'],
    'AT': [20, 'Austria'],
    'AZ': [28, 'Azerbaijan'],
    'BH': [22, 'Bahrain'],
    'BY': [28, 'Belarus'],
    'BE': [16, 'Belgium'],
    'BA': [20, 'Bosnia and Herzegovina'],
    'BR': [29, 'Brazil'],
    'BG': [22, 'Bulgaria'],
    'CR': [22, 'Costa Rika'],
    'HR': [21, 'Croatia'],
    'CY': [28, 'Cyprus'],
    'CZ': [24,'Czech Republic'],
    'DK': [18, 'Denmark'],
    'DO': [28, 'Dominican Republic'],
    'TL': [23, 'East Timor'],
    'EG': [29, 'Egypt'],
    'SV': [28, 'El Salvador'],
    'EE': [20, 'Estonia'],
    'FO': [18, 'Faroe Islands'],
    'FI': [18, 'Finland'],
    'FR': [27, 'Franace'],
    'GE': [22, 'Georgia'],
    'DE': [22, 'Germany'],
    'GI': [23, 'Gilbraltar'],
    'GR': [27, 'Greece'],
    'GL': [18, 'Greenland'],
    'GT': [28, 'Guatemala'],
    'HU': [28, 'Hungary'],
    'IS': [26, 'Iceland'],
    'IQ': [23, 'Iraq'],
    'IE': [22, 'Ireland'],
    'IL': [23, 'Israel'],
    'IT': [27, 'Italy'],
    'JO': [30, 'Jordan'],
    'KZ': [20, 'Kazachstan'],
    'XK': [20, 'Kosovo'],
    'KW': [30, 'Kuwait'],
    'LV': [21, 'Latvia'],
    'LB': [28, 'Lebanon'],
    'LY': [25, 'Libya'],
    'LI': [21, 'Liechtenstein'],
    'LT': [20, 'Lithuania'],
    'LU': [20, 'Luxembourg'],
    'MK': [19, 'North Macedonia'],
    'MT': [31, 'Malta'],
    'MR': [27, 'Mauritania'],
    'MU': [30, 'Mauritius'],
    'MC': [27, 'Monaco'],
    'MD': [24, 'Moldova'],
    'ME': [22, 'Montenegro'],
    'NL': [18, 'Netherlands'],
    'NO': [15, 'Norway'],
    'PK': [24, 'Pakistan'],
    'PS': [29, 'Palestinian territories'],
    'PL': [28, 'Poland'],
    'PT': [25, 'Portugal'],
    'QA': [29, 'Qatar'],
    'RO': [24, 'Romania'],
    'LC': [32, 'Saint Lucia'],
    'SM': [27, 'San Marino'],
    'ST': [25, 'Sao Tome and Principle'],
    'SA': [24, 'Saudi Arabia'],
    'RS': [22, 'Serbia'],
    'SC': [31, 'Seychelles'],
    'SK': [24, 'Slovakia'],
    'SI': [19, 'Slovenia'],
    'ES': [24, 'Spain'],
    'SD': [18, 'Sudan'],
    'SE': [24, 'Sweden'],
    'CH': [21, 'Switzerland'],
    'TH': [24, 'Tunisia'],
    'TR': [26, 'Turkey'],
    'UA': [29, 'Ukraine'],
    'AE': [23, 'United Arab Emirates'],
    'GB': [22, 'United Kingdom'],
    'VA': [22, 'Vatican City'],
    'VG': [24, 'Virgin Islands, British']
    }

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
    country = iban_param[0:2]
    if len(iban_param) == country_info[country][0]:
        result = True
    return result

def iban_symbols_validation(iban_param):
    result = True
    #chars = iban_param[0:2]
    numbers = iban_param[2:]
    for x in range(len(numbers)):
        if(ord(numbers[x]) < 48 or ord(numbers[x]) > 57): 
            result = False
            break
    #if chars != "LT":
    #    result = False
    return result

def is_iban_check_numbers_valid(iban_param):
    result = False         
    iban_check_code = iban_param[4:] + iban_param[0:2] + '00'
    iban_check_code = list(iban_check_code)
    new_iban_string = ""
    for char in range(len(iban_check_code)):
        if iban_check_code[char] in char_symbol:
            value = char_symbol.get(iban_check_code[char])
            iban_check_code[char] = value 
    for i in range(len(iban_check_code)):
        new_iban_string = new_iban_string + str(iban_check_code[i])

    iban_control_numbers = str(98 - (int(new_iban_string) % 97))

    if iban_control_numbers < 10:
        iban_control_numbers = '0' + str(iban_control_numbers)

    if iban_control_numbers == iban_param[2:4]:
        result = True
    return result

def is_iban_valid_mod_formula(iban_param):           
    iban_check_code = iban_param[4:] + iban_param[0:4]
    iban_check_code = list(iban_check_code)
    new_iban_string = ""
    for char in range(len(iban_check_code)):
        if iban_check_code[char] in char_symbol:
            value = char_symbol.get(iban_check_code[char])
            iban_check_code[char] = value 
    for i in range(len(iban_check_code)):
        new_iban_string = new_iban_string + str(iban_check_code[i])
    if int(new_iban_string) % 97 == 1:
        result = True
    return result

def what_is_the_country(iban_param):
    country = iban_param[0:2]
    countries_name = country_info[country][1]
    result = countries_name
    return result

def is_iban_lithuanian(iban_param):
    result = False 
    
    return result

#def is_lithuanian_bank_code_valid(iban_param):
#    result = False
#    if iban_param[0:2] == "LT":
#        result = True
#    if iban_param[4:9]:
#        result = True
#    return result

#def return_lithuanian_bank_name(iban_param):
#    result = ""
#    bank_id_and_name = {'72900':"Citadelė",
#                        '73000':"Swedbank",
#                        '40100':"Luminor", 
#                        '21400':"Nodea", 
#                        '39200':"Revolut", 
#                        '70440':"SEB", 
#                        '72300':"Medicinos bankas", 
#                        '71800':"Šiaulių bankas"}

#    if is_lithuanian_bank_code_valid(iban_param) == True:
#        result = bank_id_and_name.get(iban_param[4:9], 'Not found')
#    return result

iban = read_iban_number()
