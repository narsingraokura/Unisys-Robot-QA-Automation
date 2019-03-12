#Zen of Variable files
#Avoid dynamic variables
#All variables or functions to be used by scripts starts with character letter
#All functions to start with _
#All variables not to be directly used in the scripts begin with _
#All imports should have an Alias begining with _
#All Lists to begin with LIST__
#All dictionaries to begin with DICT__
import os
import names        as _names
import random       as _random
import string       as _string
import datetime     as _datetime
from datetime import date as _date
from robot.libraries.BuiltIn import BuiltIn

def Return_Driver_Props():
    seLib = BuiltIn().get_library_instance('SeleniumLibrary')

    # the driver is instantiated in the SeleniumLibrary, but not provided publicly, thus accessing it through this py code
    remote_url = seLib.driver.command_executor._url  # for local instance, this is a value in the form 'http://localhost:57856'
    session_id = seLib.driver.session_id

    return remote_url, session_id

def set_driver_session_id(sesion_id):
    """ Sets the sessoin_id of the current driver insance to the provided one. """
    seLib = BuiltIn().get_library_instance('SeleniumLibrary')

    if seLib.driver.session_id != sesion_id:  # this is pretty much guaranteed to be the case
        seLib.driver.close()  # this closes the session's window
        seLib.driver.quit()  # for remote connections (like ours), this deletes the session, but doesn't stop the SE

    # set to the session that's already running
    seLib.driver.session_id = sesion_id

def get_random_browser():
    """

    :return: return once of the browser from 'Chrome', 'IE', 'FireFox'

    """
    browser_list = ["ff", "Chrome"]
    choice = _random.randint(1, 1000000)
    res = choice % len(browser_list)
    return browser_list[res]
    #return 'ie'

def Get_Random_Selection_From_List(inp):
    length = len(inp)
    res = str(_random.randint(0, length-1))
    return res

def Get_Random_First_Name():
    return _names.get_first_name()

def Get_Random_Last_Name():
    #res = 'Automation'
    res = _names.get_last_name()
    return res

def Get_Random_Middle_Initial():
    return _get_random_alphabets_upper(1)

def Get_Random_Email():
    valid_email = _get_random_alphabets(6) + ".automation"
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



#*****************************************************************************************#
#                                           URLs                                          #
#*****************************************************************************************#

URL_Siebel                 =        "https://uat02cm.dhsie.hawaii.gov/epublicsector_enu/"
URL_LifeRay                =        "https://uat02web.dhsie.hawaii.gov/web/kolea/home-page?"
Link_Hawaii_Gov            =        "http://portal.ehawaii.gov/"
URL_Hawaii_Large_Logo      =        "https://uat02web.dhsie.hawaii.gov/hawaiiHIX/images/onegate/logo2.png"

#*****************************************************************************************#
#                                          File Name                                      #
#*****************************************************************************************#
File_Name_LifeRay_Accs     =        'LifeRay_New_Acc'+ "." + 'xlsx'
File_Name_LifeRay_Accounts =        'C:\\Users\\kuraroa\\git\\Unisys-Robot-QA-Automation\\KOLEA-AQUA\\Data_Files\\LifeRay_Users.xlsx'

#*****************************************************************************************#
#                                          Settings                                       #
#*****************************************************************************************#

Wait_02_Sec                =        20
Wait_10_Sec                =        100
Wait_20_Sec                =        200
Wait_100_Sec               =        1000
Wait_5_Min                 =        3000
Selenium_Speed             =        0


#*****************************************************************************************#
#                                          Constants                                      #
#*****************************************************************************************#

BROWSER_Chrome             =        "Chrome"
BROWSER_FireFox            =        "ff"
BROWSER_RANDOM             =        get_random_browser()
Value_0                    =        0
Value_1                    =         1
Value_answer1              =        "answer1"
Value_answer2              =        "answer2"
Value_answer3              =        "answer3"
Value_Apply                =        "Apply"
Value_Apply_Now            =        "Apply Now"
Value_Bracket_Closing      =        ")"
Value_Bracket_Opening      =        "("
Value_Cases                =        "Cases"
Value_class                =        "class"
Value_Comma                =        ","
Value_contains             =        "contains"
Value_Continue             =        "Continue"
Value_Creation_Date        =        "Creation_Date"
Value_Creation_Date        =        "Update_Date"
Value_Default              =        "Default"
Value_div                  =        "div"
Value_Double_Quote         =        '"'
Value_Eligible             =        "Eligible"
Value_emailAddress         =        "emailAddress"
Value_First_Name           =        "First_Name"
Value_firstName            =        "firstName"
Value_id                   =        "id"
Value_IDM                  =        "IDM"
Value_Ineligible           =        "Ineligible"
Value_input                =        "input"
Value_Is_Counselor         =        "Is_Counselor"
Value_KOLEA_Analytics      =        "KOLEA Analytics"
Value_koleaCACCCancel      =        "koleaCACCCancel"
Value_koleaCreateAccount   =        "koleaCreateAccount"
Value_Last_Name            =        "Last_Name"
Value_lastName             =        "lastName"
Value_LifeRay              =        "LifeRay"
Value_Middle_Name          =        "Middle_Name"
Value_None                 =        "None"
Value_N                    =        "N"
Value_Password             =        "Password"
Value_password1            =        "password1"
Value_password2            =        "password2"
Value_Pre_Assessment       =        "Pre-Assessment"
Value_q1                   =        "q1"
Value_q2                   =        "q2"
Value_q3                   =        "q3"
Value_reEnterEmail         =        "reEnterEmail"
Value_Register_Now         =        "Register Now"
Value_screenName           =        "screenName"
Value_select               =        "select"
Value_Session_Id           =        "Session_Id" 
Value_Siebel               =        "Siebel"
Value_Sign_In              =        "Sign In"
Value_Single_Quote         =        "'"
Value_Space                =        " "
Value_Sq_Bracket_Close     =        "]"
Value_Sq_Bracket_Open      =        "["
Value_str_0                =        "0"
Value_str_1                =        "1"
Value_String_false         =        "false"
Value_String_true          =        "true"
Value_Suffix               =        "Suffix"
Value_Symbol_At            =        "@"
Value_User_Name            =        "User_Name"
LIST__Valid_Values_4_Yes    =        [1,"y","yes","true", True]
LIST__Valid_Values_4_No     =         [0,"n","no","false", False]


#*****************************************************************************************#
#                                           Defaults                                      #
#*****************************************************************************************#

Siebel_Default_Username    =        "K036226U"
Siebel_Default_Password    =        "Welcome#3"


#*****************************************************************************************#
#                                           Messages                                      #
#*****************************************************************************************#

Msg_Eligible                =       "Based on the information you provided, it appears that someone in your household may be eligible for zero-cost health insurance coverage"
Msg_Ineligible                =     "Based on the information you provided, you are declining or appear to be ineligible for financial help in paying for coverage."


#*****************************************************************************************#
#                                           Images                                        #
#*****************************************************************************************#

Image_Kolea_Logo                  =  "shi/custom/images/kolea_logo.png"


#*****************************************************************************************#
#                                           Xpaths                                        #
#*****************************************************************************************#

########################LifeRay

Path_LifeRay_Home_Page_Footer     = "//footer[@id='footer']"
Path_LifeRay_Pre_Assess_Button    = "//input[@id='_preassessmentportlet_WAR_hawaiihomeportlet_startPreAssementBtn']"
Path_iframe                       = "//iframe"
Path_Pre_Assess_iframe_Next       = "//input[@title='Next']"
Path_Need_Health_Indicator        = "//select[@name='needHelpIndicator']"
Path_Aged_LTC_Blind_Disable       = "//select[@name='above65Indicator']"
Path_Aged_18_Or_Under             = "//select[@name='aged18OrUnder']"
Path_Aged_19_Or_Older             = "//select[@name='aged19OrOlder']"
Path_Expected_Child               = "//select[@name='expectedChildren']"
Path_Monthly_Income               = "//input[@id='monthlyIncome']"
Path_Result_Messages              = "//div[@id='nomrg']/div/div[2]/p[3]"
Path_Apply_Now                    = "//input[@value='Apply Now']"
Path_Create_Account_Heading       = "//div[@class='heading_create']"
Path_Create_Acc_Security_q1       = _get_path_4_containing(Value_select, Value_id, Value_q1)
Path_Create_Acc_Security_q2       = _get_path_4_containing(Value_select, Value_id, Value_q2)
Path_Create_Acc_Security_q3       = _get_path_4_containing(Value_select, Value_id, Value_q3)
Path_Create_Acc_First_Name        = _get_path_4_containing(Value_input, Value_id, Value_firstName)
Path_Create_Acc_Last_Name         = _get_path_4_containing(Value_input, Value_id, Value_lastName)
Path_Create_Acc_Email             = _get_path_4_containing(Value_input, Value_id, Value_emailAddress)
Path_Create_Acc_reEnter_Email     = _get_path_4_containing(Value_input, Value_id, Value_reEnterEmail)
Path_Create_Acc_Screen_Name       = _get_path_4_containing(Value_input, Value_id, Value_screenName)
Path_Create_Acc_Password1         = _get_path_4_containing(Value_input, Value_id, Value_password1)
Path_Create_Acc_Password2         = _get_path_4_containing(Value_input, Value_id, Value_password2)
Path_Create_Acc_answer1           = _get_path_4_containing(Value_input, Value_id, Value_answer1)
Path_Create_Acc_answer2           = _get_path_4_containing(Value_input, Value_id, Value_answer2)
Path_Create_Acc_answer3           = _get_path_4_containing(Value_input, Value_id, Value_answer3)
Path_Create_Acc_As_Counselor_Yes  = "//input[@type='radio' and @value=1]"
Path_Create_Acc_As_Counselor_No   = "//input[@type='radio' and @value=2]"


########################Siebel

Path_KOLEA_Sign_On_Username         =    "//input[@name='userid']"
Path_Signon_Page_Continue_button    =    "//input[@class='loginButton']"
Path_Password_Field                 =    "//input[@name='Bharosa_Password_PadDataField']"
Path_Password_Device_Enter          =    "//area[@title='enter ']"
Path_Salute_My_Home                 =    "//span[@class='siebui-salutation-title']"
Path_Menubar_Navigate               =    "//html/body/div[1]/div/div[1]/div/div[4]/span/li[4]/a"
Path_Site_Map_Link                  =    "//li[@id='ui-id-43']"
Path_SiteMap_Filter_Input           =    "//input[@id='sitemapFilterInput']"
Path_Search_Result                  =    "//a[@id='s_a_230']"
Path_Case_Search_Result             =    "//a[@class='drilldown']"
Path_Dashboard                      =    "//span[@id='dashboard']"
Path_iframe                         =    "//iframe"
Path_CRM_Reports_Link               =    "//html/body/div[3]/div[2]/div/div[3]/div[4]/div"
Path_SideBar_Prefix                 =    "//ul[@class='dynatree-container']//following::*[text()='"
Path_Button_Prefix                  =    "//button[@title='"
Path_Case_Search_Go_Button          =    "//div[@id='s_S_A4_div']//following::button[@title='Search:Go']"
Path_Case_Name                      =    "//input[@aria-label='Case Name']"
Path_Search_Go                      =    "//div[@id='s_S_A4_div']//following::button[@title='Search:Go']"
Path_First_Case_Search_Result       =    "//a[@class='drilldown']"
Path_Change_Of_Circumstance         =    "//div[@id='s_vctrl_div']//following::a[@class='dynatree-title' and ./text()='Change Of Circumstance']"
Path_Sub_Menu_Deductions            =    "//div[@id='s_vctrl_div']//following::a[@class='dynatree-title' and ./text()='Deductions']"
Path_Plus_Sign_Prefix               =    "//button[@title='"
Path_Plus_Sign_Suffix               =    ":New']"
Path_Prefix                         =    "//"
Path_Search_Button                  =    "//span[@class='siebui-icon-tb-executequery ToolbarButtonOn']"
Path_SBL_New_App_Create_Date        =    "//input[@id='caseWorkerCreatedDate']"
Path_SBL_New_App_First_Name         =    "//input[@id='firstNameId']"
Path_SBL_New_App_Mid_Initial        =    "//input[@id='houseHold.listOfContacts.contact[0].middleName']"
Path_SBL_New_App_Last_Name          =    "//input[@id='houseHold.listOfContacts.contact[0].lastName']"
Path_SBL_New_App_Suffix             =    "//select[@id='houseHold.listOfContacts.contact[0].suffix']"


########################Common

Path_Suffix                         =    "']"
Path_State_Hawai_Logo               =    "//div[@class='hawai_logo']"
Path_Hlth_Ins_Mrkt_Logo             =    "//div[@class='popup_bottom_logo']"
Path_Input_Contains_Id              =    "//input[contains(@id, '"


###################### Generated data

Random_First_Name                   =  Get_Random_First_Name()
Random_Middle_Initial               =  Get_Random_Middle_Initial()
Random_Last_Name                    =  Get_Random_Last_Name()
Random_Email                        =  Get_Random_Email()
Random_Password                     =  _get_strong_password()

##################### Dates and times

Today_mm_dd_ccyy                   =    _get_today_mm_dd_ccyy()