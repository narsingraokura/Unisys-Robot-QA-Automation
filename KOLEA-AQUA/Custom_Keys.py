import random
import names

def _Get_Random_Selection_From_List(inp):
    length = len(inp)
    return random.randint(0, length-1)

def Get_Random_First_Name():
    return names.get_first_name()

def Get_Random_Last_Name():
    res = 'Automation'
    return res

def Get_Random_Middle_Initial():
    return _get_random_alphabets_upper(1)

def Get_Random_Email():
    valid_email = "test.automation"
    valid_domain = "@gmail.com"
    #res = valid_email + '+' + _get_random_alpha_num() + valid_domain
    res = valid_email + _get_random_digits(3) + valid_domain
    return res


def _get_path_4_containing(Node, Attribute, Value):
    Path_Prefix = "//"
    Value_Sq_Bracket_Open = "["
    Value_Sq_Bracket_Close = "]"
    Value_Bracket_Opening = "("
    Value_Bracket_Closing = ")"

    return ''.join([Path_Prefix, Node, Value_Sq_Bracket_Open, 'contains',
                    Value_Bracket_Opening, '@', Attribute, ',',
                    ' ', "'", Value, "'",
                    ')', Value_Sq_Bracket_Close])


def _get_random_alphabets_lower(length=2):
    s = _string.ascii_lowercase

    return ''.join(_random.sample(s,length))

def _get_random_alphabets_upper(length=2):
    s = _string.ascii_uppercase

    return ''.join(_random.sample(s,length))

def _get_random_alphabets(length=2):
    s = _string.ascii_letters

    return ''.join(_random.sample(s,length))

def _get_random_digits(length=2):
    s = _string.digits

    return ''.join(_random.sample(s,length))

def _get_random_punctuation(length=2):
    s = _string.punctuation

    return ''.join(_random.sample(s,length))


def _get_random_alpha_num(length=10):
    s = _string.ascii_lowercase + _string.ascii_uppercase + _string.digits
    res = ''.join(_random.sample(s,length))
    return res


def _randomStringwithDigitsAndSymbols(stringLength=10):
    """Generate a random string of letters, digits and special characters """
    password_characters = _string.ascii_letters + _string.digits + _string.punctuation
    return ''.join(_random.choice(password_characters) for i in range(stringLength))

def _get_strong_password():

    #Password must contain 2 alphabet characters
    #Password must start with alphabet character
    password = ''

    password += _get_random_alphabets(2)

    #Password must contain atleast one lower case letter

    password += _get_random_alphabets_lower(2)

    #Password must contain atleast one numeric character

    password += _get_random_digits(2)

    # Password must contain atleast one lower case letter

    password += _get_random_alphabets_upper(2)

    # Password must contain special characters

    password += _get_random_punctuation(2)

    s = password[2:]
    length = len(s)
    part1 = s[:2]
    part2 = ''.join(_random.sample(s, length))

    password = part1+part2

    return password

def _get_today_mm_dd_ccyy():
    _today = _date.today()
    res = _today.strftime("%m/%d/%Y")
    return res