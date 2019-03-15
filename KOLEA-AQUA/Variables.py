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
URL_PCI 				   =		"file:///C:/Users/giriganv/OneDrive%20-%20Unisys/HAWAII_PROJECT/Automation/SmokeTest/Smoke-Test-Suite/Smoke-Test-Suite/Scenario-1-Liferay-Portal/Step7-KOLEA-Public-Portal-Primary-Contact-Info-Page.html"
URL_PADETAILS              =        "file:///C:/Users/giriganv/OneDrive%20-%20Unisys/HAWAII_PROJECT/Automation/SmokeTest/Smoke-Test-Suite/Smoke-Test-Suite/Scenario-1-Liferay-Portal/Step8-KOLEA-Public-Portal-Primary-applicant-Details.html"
URL_HHDETAILS			   =        "file:///C:/Users/giriganv/OneDrive%20-%20Unisys/HAWAII_PROJECT/Automation/SmokeTest/Smoke-Test-Suite/Smoke-Test-Suite/Scenario-1-Liferay-Portal/Step10-KOLEA-Public-Portal-Household-Details.html"

#*****************************************************************************************#
#                                          File Name                                      #
#*****************************************************************************************#
File_Name_LifeRay_Accs     =        'LifeRay_New_Acc'+ "." + 'xlsx'


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
Value_Apply                =        "Apply"
Value_Apply_Now            =        "Apply Now"
Value_Bracket_Closing      =        ")"
Value_Bracket_Opening      =        "("
Value_Cases                =        "Cases"
Value_Comma                =        ","
Value_Continue             =        "Continue"
Value_Double_Quote         =        '"'
Value_Eligible             =        "Eligible"
Value_IDM                  =        "IDM"
Value_Ineligible           =        "Ineligible"
Value_KOLEA_Analytics      =        "KOLEA Analytics"
Value_LifeRay              =        "LifeRay"
Value_None                 =        "None"
Value_Pre_Assessment       =        "Pre-Assessment"
Value_Register_Now         =        "Register Now"
Value_Siebel               =        "Siebel"
Value_Sign_In              =        "Sign In"
Value_Single_Quote         =        "'"
Value_Space                =        " "
Value_Sq_Bracket_Close     =        "]"
Value_Sq_Bracket_Open      =        "["
Value_String_false         =        "false"
Value_String_true          =        "true"
Value_Symbol_At            =        "@"
Value_answer1              =        "answer1"
Value_answer2              =        "answer2"
Value_answer3              =        "answer3"
Value_class                =        "class"
Value_contains             =        "contains"
Value_Default              =        "Default"
Value_div                  =        "div"
Value_emailAddress         =        "emailAddress"
Value_firstName            =        "firstName"
Value_First_Name           =        "First_Name"
Value_id                   =        "id"
Value_input                =        "input"
Value_koleaCACCCancel      =        "koleaCACCCancel"
Value_koleaCreateAccount   =        "koleaCreateAccount"
Value_lastName             =        "lastName"
Value_Middle_Name          =        "Middle_Name"
Value_Last_Name            =        "Last_Name"

Value_password1            =        "password1"
Value_password2            =        "password2"
Value_q1                   =        "q1"
Value_q2                   =        "q2"
Value_q3                   =        "q3"
Value_reEnterEmail         =        "reEnterEmail"
Value_screenName           =        "screenName"
Value_select               =        "select"
Value_str_0                =        "0"
Value_str_1                =        "1"
Value_Suffix               =        "Suffix"

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





############# PrimaryApplicantDetails

Path_LFRY_PAD_Screen_Nav		= "//a/li[text()=' Primary Contact Information ']"
Path_LFRY_PCI_FName_P1		= "//input[@id='firstNameId']"
Path_LFRY_PCI_MName_P1		= "//input[@id='firstNameId']//following::input[@title=' Middle Name '][1]"
Path_LFRY_PCI_LName_P1		= "//input[@id='firstNameId']//following::input[@title=' Last Name '][1]"

Path_LFRY_PCI_SpouseName_If_Married_P1	= "//input[@title=' 5. Name of spouse if married ']"
Path_LFRY_PCI_SSN_P1	= "//input[@id='houseHold.listOfContacts.contact[0].ssn']"

Path_LFRY_PCI_Suffix_P1	= "//select[@title=' Suffix ']"
Path_LFRY_PCI_Suffix_P1_II	= "//select[@title=' Suffix ']/option[2]"

Path_LFRY_PCI_Relation_P1	= "//input[contains(@title,'Relationship to you ?')]"

Path_LFRY_PCI_DOB_P1	= "//input[contains(@title,'Date of birth (mm/dd/yyyy)*')]"
Path_LFRY_PCI_Gender_P1	= "//select[@id='genderSelectId']"
Path_LFRY_PCI_Gender_P1_Male	= "//select[@id='genderSelectId']/option[text()=' Male']"
Path_LFRY_PCI_Gender_P1_Female	= "//select[@id='genderSelectId']/option[text()=' Female']"

Path_LFRY_PCI_P1_Plan_To_File_Federal_Inctx_Rtn_NEXT_Year	= "//select[contains(@title,'Do you plan to file a federal income tax return NEXT YEAR?*')]"
Path_LFRY_PCI_P1_Plan_To_File_Federal_Inctx_Rtn_NEXT_Year_Yes	= "//select[contains(@title,'Do you plan to file a federal income tax return NEXT YEAR?*')]//child::option[text()=' Yes']"
Path_LFRY_PCI_P1_Plan_To_File_Federal_Inctx_Rtn_NEXT_Year_No	= "//select[contains(@title,'Do you plan to file a federal income tax return NEXT YEAR?*')]//child::option[text()=' No']"

Path_LFRY_PCI_P1_Jointly_File_With_Spouse	= "//select[contains(@title,'Will you jointly file with a spouse?*')]"
Path_LFRY_PCI_P1_Jointly_File_With_Spouse_Yes	= "//select[contains(@title,'Will you jointly file with a spouse?*')]//child::option[text()=' Yes']"
Path_LFRY_PCI_P1_Jointly_File_With_Spouse_No	= "//select[contains(@title,'Will you jointly file with a spouse?*')]//child::option[text()=' No']"

Path_LFRY_PCI_P1_Jointly_File_With_Spouse_Yes_Fname	= "//select[contains(@title,'Will you jointly file with a spouse?*')]//following::input[1][@title=' First Name* ']"
Path_LFRY_PCI_P1_Jointly_File_With_Spouse_Yes_Mname	= "//select[contains(@title,'Will you jointly file with a spouse?*')]//following::input[2][@title=' Middle Name ']"
Path_LFRY_PCI_P1_Jointly_File_With_Spouse_Yes_Lname	= "//select[contains(@title,'Will you jointly file with a spouse?*')]//following::input[3][@title=' Last Name ']"

Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtrn	= "//select[contains(@title,'Will you claim any dependents on your tax return?*')]"
Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtrn_Yes	= "//select[contains(@title,'Will you claim any dependents on your tax return?*')]//child::option[text()=' Yes']"
Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtn_No	= "//select[contains(@title,'Will you claim any dependents on your tax return?*')]//child::option[text()=' No']"

Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtn_Yes_Fname	= "//*[@id='DependantTotal']//input[@title=' First Name* ']"
Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtn_Yes_Mname	= "//*[@id='DependantTotal']//input[@title=' Middle Name ']"
Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtn_Yes_Lname		= "//*[@id='DependantTotal']//input[@title=' Last Name ']"

Path_LFRY_PCI_P1_Add_Dependent	= "//input[@id='addDependents']"
Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtn_Add_Dependnt_Fname	= "//*[@id='DependantTotal']//input[@id='taxFirstName1']"
Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtn_Add_Dependnt_Mname	= "//*[@id='DependantTotal']//input[@title='Middle Name']"
Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtn_Add_Dependnt_Lname	= "//*[@id='DependantTotal']//input[@title='Last Name* ']"

Path_LFRY_PCI_P1_Claim_Any_Dependnts_On_Your_Tx_Rtn_Add_Dependt_Remove_Btn	= "//*[@id='DependantTotal']//input[@title='Remove']"

Path_LFRY_PCI_P1_Claimed_As_Dependt_On_someones_Tx_Rtn		= "//select[@id='houseHold.listOfContacts.contact[0].additionalTaxInformation.claimedAsTaxDependentIndicator']"
Path_LFRY_PCI_P1_Claimed_As_Dependt_On_someones_Tx_Rtn_Yes	= "//select[@id='houseHold.listOfContacts.contact[0].additionalTaxInformation.claimedAsTaxDependentIndicator']//following::select[1]//child::option[text()=' Yes']"
Path_LFRY_PCI_P1_Claimed_As_Dependt_On_someones_Tx_Rtn_No	= "//select[@id='houseHold.listOfContacts.contact[0].additionalTaxInformation.claimedAsTaxDependentIndicator']//following::select[1]//child::option[text()=' No']"

Path_LFRY_PCI_P1_Claimed_As_Dependt_On_someones_Tx_Rtn_Yes_Fname	   = "//input[@id='houseHold.listOfContacts.contact[0].additionalTaxInformation.claimedAsDependentByContact.contactFirstName']"
Path_LFRY_PCI_P1_Claimed_As_Dependt_On_someones_Tx_Rtn_Yes_Mname		= "//input[@id='houseHold.listOfContacts.contact[0].additionalTaxInformation.claimedAsDependentByContact.contactMiddleName']"
Path_LFRY_PCI_P1_Claimed_As_Dependt_On_someones_Tx_Rtn_Yes_Lname		= "//input[@id='houseHold.listOfContacts.contact[0].additionalTaxInformation.claimedAsDependentByContact.contactLastName']"

Path_LFRY_PCI_P1_Chk_If_Tx_Filer_Claimng_You_As_Dependt_Is_Nt_Prt_Of_Hsehold	= "//input[@id='houseHold.listOfContacts.contact[0].additionalTaxInformation.taxFilerNotPartOfHouseholdIndicatorCheckbox']"
Path_LFRY_PCI_P1_How_Are_You_Related_To_Tx_Filer		= "//select[@id='houseHold.listOfContacts.contact[0].additionalTaxInformation.claimedAsDependentByContactRelationShipTypeCode']"
Path_LFRY_PCI_P1_How_Are_You_Related_To_Tx_Filer_Married_To	= "//select[@id='houseHold.listOfContacts.contact[0].additionalTaxInformation.claimedAsDependentByContactRelationShipTypeCode']/option[text()=' Married to']"
Path_LFRY_PCI_P1_Do_You_Need_Health_Coverage_Yes		= "//input[@id='healthCovgReqIndYes']"

Path_LFRY_PCI_P1_Do_You_Need_Health_Coverage_No		= "//input[@id='healthCovgReqIndNo']"

Path_LFRY_PCI_P1_Have_Disability_Tht_Will_last_More_Than_Twelve_Mnths	= "//*[@id='houseHold.listOfContacts.contact[0].phyclPyschHealthConditionIndicator']"
Path_LFRY_PCI_P1_Have_Disability_Tht_Will_last_More_Than_Twelve_Mnths_Yes	= "//select[contains(@title,'Do you have a disability that will last more than twelve (12) months?*')]//child::option[text()=' Yes']"
Path_LFRY_PCI_P1_Have_Disability_Tht_Will_last_More_Than_Twelve_Mnths_No		= "//select[contains(@title,'Do you have a disability that will last more than twelve (12) months?*')]//child::option[text()=' Yes']//child::option[text()=' No']"

Path_LFRY_PCI_P1_Do_You_Currently_Receive_Long_Trm_Care_Nursing_servces 	= "//select[contains(@title,'Do you currently receive long term care nursing services?')]"
Path_LFRY_PCI_P1_You_Curntly_Recve_Lng_Trm_Cre_Nursng_srvcs_Yes_Nursng_Fclty 	= "//select[contains(@title,'Do you currently receive long term care nursing services?')]/option[text()=' Yes, in a nursing facility']"
Path_LFRY_PCI_P1_Have_You_Recvd__Lng_Trm_Cre_Nursng_srvcs_In_Lst_Three_Mnths 	= "//select[contains(@title,'Have you received long term care nursing services in the last three (3) months?')]"
Path_LFRY_PCI_P1_Recvd__Lng_Trm_Cre_Nursng_srvcs_In_Lst_Three_Mnths_Yes		= "//select[contains(@title,'Have you received long term care nursing services in the last three (3) months?')]//child::option[text()=' Yes']"
Path_LFRY_PCI_P1_Recvd__Lng_Trm_Cre_Nursng_srvcs_In_Lst_Three_Mnths_No	 = "//select[contains(@title,'Have you received long term care nursing services in the last three (3) months?')]//child::option[text()=' No']"
Path_LFRY_PCI_P1_Recvd__Lng_Trm_Cre_Nursng_srvcs_In_Lst_Three_Mnths_Yes_From 	= "//select[contains(@title,'Have you received long term care nursing services in the last three (3) months?')]//child::option[text()=' Yes']//following::input[1][@title=' From* ']"
Path_LFRY_PCI_P1_Recvd__Lng_Trm_Cre_Nursng_srvcs_In_Lst_Three_Mnths_Yes_To 	= "//select[contains(@title,'Have you received long term care nursing services in the last three (3) months?')]//child::option[text()=' Yes']//following::input[@title=' To ']"


Path_LFRY_PCI_P1_Do_You_Think_You_Need_Lng_Trm_Cre_Nursng_srvcs_Now 	= "//select[contains(@title,'Do you think you need long term care nursing services now?')]"
Path_LFRY_PCI_P1_Do_You_Think_You_Need_Lng_Trm_Cre_Nursng_srvcs_Now_Yes	 = "//select[contains(@title,'Do you think you need long term care nursing services now?')]//child::option[text()=' Yes']"
Path_LFRY_PCI_P1_Do_You_Think_You_Need_Lng_Trm_Cre_Nursng_srvcs_Now_No 	= "//select[contains(@title,'Do you think you need long term care nursing services now?')]//child::option[text()=' No']"

Path_LFRY_PCI_P1_Do_You_Recve_Supplemental_Security_Income_SSI 	= "//select[contains(@title,'Do you receive Supplemental Security Income (SSI)?')]"
Path_LFRY_PCI_P1_Do_You_Recve_Supplemental_Security_Income_SSI_Yes 	= "//select[contains(@title,'Do you receive Supplemental Security Income (SSI)?')]//child::option[text()=' Yes']"
Path_LFRY_PCI_P1_Do_You_Recve_Supplemental_Security_Income_SSI_No	= "//select[contains(@title,'Do you receive Supplemental Security Income (SSI)?')]//child::option[text()=' No']"

Path_LFRY_PCI_P1_Recvd_Medcl_Srvcs_Past_Ten_Cal_Days_imdt_Prior_date_Of_Appl 	= "//select[contains(@title,'Did you receive any medical services in the past ten (10) calendar days immediately prior to the date of application?')]"
Path_LFRY_PCI_P1_Recvd_Medcl_Srvcs_Past_Ten_Cal_Days_Prior_date_Of_Appl_Yes 	= "//select[contains(@title,'Did you receive any medical services in the past ten (10) calendar days immediately prior to the date of application?')]//child::option[text()=' Yes']"
Path_LFRY_PCI_P1_Recvd_Medcl_Srvcs_Past_Ten_Cal_Days_Prior_date_Of_Appl_No 	= "//select[contains(@title,'Did you receive any medical services in the past ten (10) calendar days immediately prior to the date of application?')]//child::option[text()=' No']"

Path_LFRY_PCI_P1_Recvd_Medcl_Srvcs_Past_Ten_Cal_Days_Prior_date_Of_App_Y_Frm	 = "//select[contains(@title,'Did you receive any medical services in the past ten (10) calendar days immediately prior to the date of application?')]//child::option[text()=' Yes']//following::input[2]"
Path_LFRY_PCI_P1_Recvd_Medcl_Srvcs_Past_Ten_Cal_Days_Prior_date_Of_App_Y_To 	= "//select[contains(@title,'Did you receive any medical services in the past ten (10) calendar days immediately prior to the date of application?')]//following::*[@title=' To* ']"

Path_LFRY_PCI_P1_Are_You_US_Citizen_Or_US_National 	= "//select[contains(@title,'Are you a U.S. citizen or U.S. national?*')]"
Path_LFRY_PCI_P1_Are_You_US_Citizen_Or_US_National_Yes 	= "//select[contains(@title,'Are you a U.S. citizen or U.S. national?*')]//child::option[text()=' Yes']"
Path_LFRY_PCI_P1_Are_You_US_Citizen_Or_US_National_No 	= "//select[contains(@title,'Are you a U.S. citizen or U.S. national?*')]//child::option[text()=' No']"

Path_LFRY_PCI_P1_If_Nt_US_Citizen_Or_US_National_Hav_Eligble_Immgratn_Status 	= "//div[@id='health_covg']//select[contains(@title,'Are you a U.S. citizen or U.S. national?*')]//following::select[1]"
Path_LFRY_PCI_P1_If_Nt_US_Citizen_Or_US_National_Hav_Eligb_Immgratn_Status_Y 	= "//div[@id='health_covg']//select[contains(@title,'Are you a U.S. citizen or U.S. national?*')]//following::select[1]//child::option[text()=' Yes']"
Path_LFRY_PCI_P1_If_Nt_US_Citizen_Or_US_National_Hav_Eligb_Immgratn_Status_N 	= "//div[@id='health_covg']//select[contains(@title,'Are you a U.S. citizen or U.S. national?*')]//following::select[1]//child::option[text()=' No']"

Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Hav_Eligb_Imig_Sts_Y_Immgtn_Doc_Type 	= "//div[@id='health_covg']//select[@id='ImmgDocType']"
Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Hav_Eligb_Imig_Sts_Y_Status_Type 	= "//div[@id='health_covg']//input[@title=' Status Type ']"
Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Eligb_Imig_Sts_Y_Name_As_On_Imig_Doc 	= "//div[@id='health_covg']//input[@title=' Write your name as it appears on your immigration document ']"
Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Eligb_Imig_Sts_Y_Imig_DType_Visa_AN	= "//input[@id='houseHold.listOfContacts.contact[0].alienNumber']"

Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Eligb_Imig_Sts_Y_Imig_DType_Visa_94	= "//input[@id='houseHold.listOfContacts.contact[0].i94Number']"
Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Eligb_Imig_Sts_Y_Imig_DType_Visa_PN	= "//input[@id='houseHold.listOfContacts.contact[0].passportNumber']"
Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Eligb_Imig_Sts_Y_Imig_DType_Visa_DOE	= "//input[@id='passExpDoe']"

Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Eligb_Imig_Sts_Y_Imig_DType_Visa_OD	= "//input[@id='houseHold.listOfContacts.contact[0].otherImmigrationDocNumber']"
Path_LFRY_PCI_P1_Date_Of_Entry_US_Fnd_Imig_Doc_In_Q13_Dte_Prmnt_Lawfl_Resdnt 	= "//div[@id='health_covg']//input[@id='doe']"
Path_LFRY_PCI_P1_Ctzn_Federtd_Ste_Micronesia_Repblc_Marshall_Islands_Palau_Y	 = "//div[@id='health_covg']//input[@id='fedCtnNewYes']"
Path_LFRY_PCI_P1_Ctzn_Fedrtd_Ste_Micronesia_Rpblc_Mrshl_Islds_Palau_Y_Ctzshp	= "//select[@id='federalState']"
Path_LFRY_PCI_P1_Ctzn_Federtd_Ste_Micronesia_Repblc_Marshall_Islands_Palau_N 	= "//div[@id='health_covg']//input[@id='fedCtnNewNo']"
Path_LFRY_PCI_P1_You_Spouse_Parent_A_Veteran_Or_Actve_Duty_Membr_US_Military 	 = "//div[@id='us_citizen']//following::select[contains(@title, 'Are you, or your spouse or parent a veteran or an active duty member of the US military?')]"
Path_LFRY_PCI_P1_You_Spouse_Parent_A_Veteran_Or_Actve_Duty_Membr_US_Miltry_Y 	= "//div[@id='us_citizen']//following::select[contains(@title, 'Are you, or your spouse or parent a veteran or an active duty member of the US military?')]//child::option[text()=' Yes']"
Path_LFRY_PCI_P1_You_Spouse_Parent_A_Veteran_Or_Actve_Duty_Membr_US_Miltry_N 	= "//div[@id='us_citizen']//following::select[contains(@title, 'Are you, or your spouse or parent a veteran or an active duty member of the US military?')]//child::option[text()=' No']"

Path_LFRY_PCI_P1_You_In_Foster_Care_At_Age18_Or_Older_In_Hawaii 	= "//div[@id='us_citizen']//following::select[contains(@title, 'Were you in foster care at age 18 or older in Hawaii?')]"
Path_LFRY_PCI_P1_You_In_Foster_Care_At_Age18_Or_Older_In_Hawaii_Yes 	= "//div[@id='us_citizen']//following::select[contains(@title, 'Were you in foster care at age 18 or older in Hawaii?')]//child::option[text()=' Yes']"
Path_LFRY_PCI_P1_You_In_Foster_Care_At_Age18_Or_Older_In_Hawaii_No  	= "//div[@id='us_citizen']//following::select[contains(@title, 'Were you in foster care at age 18 or older in Hawaii?')]//child::option[text()=' No']"

Path_LFRY_PCI_P1_Are_You_A_Full_Time_Student	 = "//div[@id='us_citizen']//following::select[contains(@title, 'Are you a full time student?')]"
Path_LFRY_PCI_P1_Are_You_A_Full_Time_Student_Yes  	= "//div[@id='us_citizen']//following::select[contains(@title, 'Are you a full time student?')]//child::option[text()=' Yes']"
Path_LFRY_PCI_P1_Are_You_A_Full_Time_Student_No 	 = "//div[@id='us_citizen']//following::select[contains(@title, 'Are you a full time student?')]//child::option[text()=' No']"

Path_LFRY_PCI_P1_If_Hispanic_Latino_Ethnicity_Check	 = "//div[@id='us_citizen']//following::*[contains(text(), 'If Hispanic/Latino, ethnicity (OPTIONAL - check all that apply')]"
Path_LFRY_PCI_P1_If_Hispanic_Latino_Ethnicity_Chicano_A  	= "//div[@id='us_citizen']//following::*[@id='hawaii.ethnicity.lov.chicanoaCheckbox']"
Path_LFRY_PCI_P1_If_Hispanic_Latino_Ethnicity_Cuban  	= "//div[@id='us_citizen']//following::*[@id='hawaii.ethnicity.lov.cubanCheckbox']"
Path_LFRY_PCI_P1_If_Hispanic_Latino_Ethnicity_Mexican 	= "//div[@id='us_citizen']//following::*[@id='hawaii.ethnicity.lov.mexicanCheckbox']"
Path_LFRY_PCI_P1_If_Hispanic_Latino_Ethnicity_Mexican_American	 = "//div[@id='us_citizen']//following::*[@id='hawaii.ethnicity.lov.mexicanamericanCheckbox']"
Path_LFRY_PCI_P1_If_Hispanic_Latino_Ethnicity_Puerto_Rican	 =  "//div[@id='us_citizen']//following::*[@id='hawaii.ethnicity.lov.puertoricanCheckbox']"
Path_LFRY_PCI_P1_If_Hispanic_Latino_Ethnicity_Other 	= "//div[@id='us_citizen']//following::*[@id='otherEthnicityIndicatorCheckbox']"
Path_LFRY_PCI_P1_If_Hispanic_Latino_Ethnicity_Other_Text	= "//input[@id='houseHold.listOfContacts.contact[0].ethnicity.otherTypeName']"


Path_LFRY_PCI_P1_Race_Check  	= "//div[@id='us_citizen']//following::*[contains(text(), 'Race (OPTIONAL-check all that apply')]"
Path_LFRY_PCI_P1_Race_Check_American_Indian_Or_Alaskan_Native 	= "//div[@id='us_citizen']//following::*[@id='hawaii.race.lov.ameriindioralanatCheckbox']"
Path_LFRY_PCI_P1_Race_Check_Asian_Indian 	= "//div[@id='us_citizen']//following::*[@id='hawaii.race.lov.asianindianCheckbox']"
Path_LFRY_PCI_P1_Race_Check_Black_Or_African_American 	= "//div[@id='us_citizen']//following::*[@id='hawaii.race.lov.blackoraframeCheckbox']"
Path_LFRY_PCI_P1_Race_Check_Chinese 	= "//div[@id='us_citizen']//following::*[@id='hawaii.race.lov.chineseCheckbox']"
Path_LFRY_PCI_P1_Race_Check_Filipino 	= "//div[@id='us_citizen']//following::*[@id='hawaii.race.lov.filipinoCheckbox']"
Path_LFRY_PCI_P1_Race_Check_Guamanian_Or_Chamorro 	= "//div[@id='us_citizen']//following::*[@id='hawaii.race.lov.guamanianorchamorroCheckbox']"
Path_LFRY_PCI_P1_Race_Check_Japanese 	= "//div[@id='us_citizen']//following::*[@id='hawaii.race.lov.japaneseCheckbox']"
Path_LFRY_PCI_P1_Race_Check_Korean 	= "//div[@id='us_citizen']//following::*[@id='hawaii.race.lov.koreanCheckbox']"
Path_LFRY_PCI_P1_Race_Check_Native_Hawaiian 	= "//div[@id='us_citizen']//following::*[@id='hawaii.race.lov.nativehawaiianCheckbox']"
Path_LFRY_PCI_P1_Other_Asian 	= "//div[@id='us_citizen']//following::*[@id='hawaii.race.lov.otherasianCheckbox']"
Path_LFRY_PCI_P1_Other_Pacific_Islander 	= "//div[@id='us_citizen']//following::*[@id='hawaii.race.lov.othpacificCheckbox']"
Path_LFRY_PCI_P1_Samoan 	= "//div[@id='us_citizen']//following::*[@id='hawaii.race.lov.samoanCheckbox']"
Path_LFRY_PCI_P1_Vietnamese 	= "//div[@id='us_citizen']//following::*[@id='hawaii.race.lov..vietnameseCheckbox']"
Path_LFRY_PCI_P1_White 	= "//div[@id='us_citizen']//following::*[@id='hawaii.race.lov.whiteCheckbox']"
Path_LFRY_PCI_P1_Other 	= "//div[@id='us_citizen']//following::*[@id='otherRaceIndicatorCheckbox']"
Path_LFRY_PCI_P1_Other_Text	= "//input[@id='houseHold.listOfContacts.contact[0].race.otherTypeName']"

#Path_LFRY_PCI_P1_Current_Job_And_Income_Information 	= "//b[text()='Current Job & Income Information']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Information_Typ_Employment_Employed 	= "//input[@id='employmentTypeEmployed']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Information_Typ_Emplyment_Nt_Emplyd 	= "//input[@id='employmentTypeNotEmployed']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Information_Employer_Name 	= "//input[@id='empName']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Information_PH_Nbr	= "//input[@id='empPhone1']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Information_Address_Line1 	= "//input[@id='addressLine1First']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Information_Apartment_Or_Suite_Nbr 	= "//input[@id='aptOrSuiteFirst']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Information_City 	= "//input[@id='cityFirst']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Information_State 	= "//select[@id='stateFirst']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Zip_Code 	= "//input[@id='zipCodeFirst']"

Path_LFRY_PCI_P1_Current_Job_And_Income_Wages_Tips_Before_Taxes 	= "//input[@id='amount1']"
Path_LFRY_PCI_P1_Current_Job_And_Income_How_Often 	= "//div[@class='addMoreJobs']//following::select[1][@title=' How Often ?* ']"
Path_LFRY_PCI_P1_Current_Job_And_Income_How_Often_Daily 	=  "//div[@class='addMoreJobs']//following::select[1][@title=' How Often ?* ']/option[2]"
Path_LFRY_PCI_P1_Current_Job_And_Income_How_Often_Daily_Days_Wrkd_Each_Week 	= "//div[@class='addMoreJobs']//following::select[1][@title=' How Often ?* ']//following::input[@title=' Number of days worked each week* '][1]"
Path_LFRY_PCI_P1_Current_Job_And_Income_How_Often_Hourly 	= "//div[@class='addMoreJobs']//following::select[1][@title=' How Often ?* ']/option[4]"
Path_LFRY_PCI_P1_Current_Job_And_Incme_How_Oftn_Hourly_Avg_Hrs_Wrkd_Ech_Week 	= "//div[@class='addMoreJobs']//following::input[1][@title=' Average hours worked each week* ']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Income_Start_Date 	= "//div[@class='addMoreJobs']//following::input[1][@title=' Income Start Date ']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Income_End_Date 	= "//div[@class='addMoreJobs']//following::input[1][@title=' Income End Date ']"

Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Button 	= "//input[@type='button' and @value='Add new Jobs']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Emplr_Name 		= "//input[@id='employerNameId1']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_PH_Nbr 	= "//div[@class='addMoreJobs']//following::input[@title='Phone number ']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Address_Line1  	= "//div[@class='addMoreJobs']//following::input[@title='Address Line 1*']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Apartment_Or_Suite_Nbr 	= "//div[@class='addMoreJobs']//following::input[@title='Apartment or suite number']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_City 	= "//div[@class='addMoreJobs']//following::input[@title='City*']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_State 	= "//div[@class='addMoreJobs']//following::select[@title='State*']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Zip_Code 	= "//div[@class='addMoreJobs']//following::input[@title='Zip code*']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Wages_Tips_Before_Taxes 	= "//div[@class='addMoreJobs']//following::input[@title='Wages/tips (before taxes)*']"

Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_How_Often 	=  "//div[@class='addMoreJobs']//following::select[1][@title='How Often ?*']"
Path_LFRY_PCI_P1_Cnt_Jb_And_Incm_Add_New_Jobs_Hw_Oftn_Daily 	= "//div[@class='addMoreJobs']//following::select[1][@title='How Often ?*']/option[2]"
Path_LFRY_PCI_P1_Cnt_Jb_And_Incm_Add_New_Jobs_Hw_Oftn_Daily_Nbr_Hrs_Wrkd 	= "//div[@class='addMoreJobs']//following::select[1][@title='How Often ?*']//following::input[@title='Number of days worked each week*']"
Path_LFRY_PCI_P1_Cnt_Jb_And_Incm_Add_New_Jbs_Hw_Oftn_Hourly	= "//div[@class='addMoreJobs']//following::select[1][@title='How Often ?*']/option[4]"
Path_LFRY_PCI_P1_Cnt_Jb_And_Incm_Add_New_Jbs_Hw_Oftn_Hourly_Avg_Hrs_Wrkd 	= "//div[@class='addMoreJobs']//following::select[1][@title='How Often ?*']//following::input[@title='Average hours worked each week*'][1]"
Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Income_Start_Date 	= "//div[@class='addMoreJobs']//following::input[1][@title='Income Start Date']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Income_End_Date 	= "//div[@class='addMoreJobs']//following::input[1][@title='Income End Date']"

Path_LFRY_PCI_P1_Current_Job_And_Income_In_The_Past_Year_Did_You 	= "//select[@title=' In the past year, did you: ']"
Path_LFRY_PCI_P1_Current_Job_And_Incme_In_The_Past_Year_Did_You_Change_Jobs =   "//select[@title=' In the past year, did you: ']/option[text()=' Change Jobs']"
Path_LFRY_PCI_P1_Current_Job_And_Incme_In_The_Past_Yr_Did_You_None_Of_These = "//select[@title=' In the past year, did you: ']/option[text()=' None of these']"
Path_LFRY_PCI_P1_Current_Job_And_Incme_In_The_Past_Yr_Strt_Wrking_Fewer_Hrs =   "//select[@title=' In the past year, did you: ']/option[text()=' Start working fewer hours']"
Path_LFRY_PCI_P1_Current_Job_And_Incme_InThe_Past_Year_Did_You_Stop_Working 	= "//select[@title=' In the past year, did you: ']/option[text()=' Stop working']"

Path_LFRY_PCI_P1_Current_Job_And_Income_Self_Employed 	= "//input[@id='employmentTypeSelfEmployedCheckbox']"
Path_LFRY_PCI_P1_Current_Job_And_Income_If_Self_Emplyd_Ans_Flwing_Qtns 	= "//b[text()='If self-employed, answer the following questions']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Self_Emplyd_Type_Of_Work 	= "//*[@title=' Type of work* ']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Slf_Empd_Net_Incme_Gt_Paid_Frm_Slf_Emplnt 	= "//*[@title=' How much net income(profits once business expenses are paid) will you get paid from this self-employment this month?* ']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Other_Income_This_Month 	= "//b[text()='OTHER INCOME THIS MONTH']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Othr_Icme_Ths_Mnth_Income_Type 	= "//b[text()='OTHER INCOME THIS MONTH']//following::select[@title=' Income Type* ']"
Path_LFRY_PCI_P1_Cnt_Jb_Incm_Othr_Icme_Ths_Mnth_Income_Type_Alimony_Recvd	= "//b[text()='OTHER INCOME THIS MONTH']//following::select[@title=' Income Type* ']/option[2]"
Path_LFRY_PCI_P1_Current_Job_And_Income_Othr_Icme_Ths_Mnth_Amount 	= "//b[text()='OTHER INCOME THIS MONTH']//following::select[@title=' Income Type* '][1]/following::input[1]"
Path_LFRY_PCI_P1_Current_Job_And_Income_Othr_Icme_Ths_Mnth_How_Often 	= "//b[text()='OTHER INCOME THIS MONTH']//following::select[@title=' How Often ?* '][1]"
Path_LFRY_PCI_P1_Current_Job_And_Income_Othr_Icme_Ths_Mnth_How_Often_Daily 	= "//b[text()='OTHER INCOME THIS MONTH']//following::select[@title=' How Often ?* '][1]/option[2]"

Path_LFRY_PCI_P1_Cnt_Jb_Incm_Otr_Icme_Ths_Mnth_Hw_Oftn_Daily_Dys_Wrkd_Ech_Wk 	= "//b[text()='OTHER INCOME THIS MONTH']//following::input[@title=' Number of days worked each week* ']"
Path_LFRY_PCI_P1_Current_Job_And_Income_Othr_Icme_Ths_Mnth_How_Often_Hourly	 = "//b[text()='OTHER INCOME THIS MONTH']//following::select[@title=' How Often ?* '][1]/option[4]"
Path_LFRY_PCI_P1_Cnt_Jb_Incme_Otr_Icme_Hw_Ofn_Hrly_Avg_Hrs_wrkd_ech_Wk = 	"//b[text()='OTHER INCOME THIS MONTH']//following::input[@title=' Average hours worked each week* ']"
Path_LFRY_PCI_P1_Curnt_Jb_And_Incm_Othr_Icme_Ths_Mnth_Hw_Oftn_Incme_Str_Date  	=  "//b[text()='OTHER INCOME THIS MONTH']//following::input[@title=' Income Start Date ']"
Path_LFRY_PCI_P1_Cnt_Job_And_Incme_Othr_Icme_Ths_Mnth_Hw_Oftn_Incme_End_Date 	=  "//b[text()='OTHER INCOME THIS MONTH']//following::input[@title=' Income End Date ']"



Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_Button 	= "//input[@id='addIncome']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_Incme_Type 	= "//b[text()='OTHER INCOME THIS MONTH']//following::select[@title='Income Type*']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_Incme_Type_Alimony_Recvd	= "//b[text()='OTHER INCOME THIS MONTH']//following::select[@title='Income Type*']/option[2]"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_Amount 	= "//b[text()='OTHER INCOME THIS MONTH']//following::input[@title='Amount($)*']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_How_Oftn 	= "//b[text()='OTHER INCOME THIS MONTH']//following::select[@title='How Often ?*'][1]"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_How_Oftn_Daily 	= "//b[text()='OTHER INCOME THIS MONTH']//following::select[@title='How Often ?*'][1]/option[2]"
Path_LFRY_PCI_P1_Cnt_Jb_Incme_Add_Mre_Incm_Hw_Ofn_Daily_Nbr_Days_wrkd_Ech_Wk 	= "//b[text()='OTHER INCOME THIS MONTH']/following::input[@title='Number of days worked each week*']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_How_Oftn_Hourly 	=  "//b[text()='OTHER INCOME THIS MONTH']//following::select[@title='How Often ?*'][1]/option[4]"
Path_LFRY_PCI_P1_Cnt_Jb_Incme_Add_Mre_Incm_Hw_Oftn_Hrly_Avg_Hrs_Wrkd_Ech_Wk 	= "//b[text()='OTHER INCOME THIS MONTH']//following::input[@title='Average hours worked each week*']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_Incme_Str_Date 	= "//b[text()='OTHER INCOME THIS MONTH']/following::input[@title='Income Start Date']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_Incme_End_Date 	= "//b[text()='OTHER INCOME THIS MONTH']/following::input[@title='Income End Date']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_Remove_Button	 = "//b[text()='OTHER INCOME THIS MONTH']//following::input[@type='button' and @value='Remove'][1]"

Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductions 	= "//b[text()='DEDUCTIONS']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Type_Of_Deductn 	= "//b[text()='DEDUCTIONS']//following::select[@title=' Type of deduction* ']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Amount 	= "//b[text()='DEDUCTIONS']//following::input[@title=' Amount($)* ']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_How_Often 	= "//b[text()='DEDUCTIONS']//following::select[@title=' How Often ?* ']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Deductn_Start_Date 	= "//b[text()='DEDUCTIONS']//following::input[@title=' Deduction Start Date ']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Deductn_End_Date 	= "//b[text()='DEDUCTIONS']//following::input[@title=' Deduction End Date ']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Add_More_Deductn_Button 	= "//input[@type='button' and @value='Add more deductions']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Remove_Button 	= "//b[text()='DEDUCTIONS']//following::input[@type='button' and @value='Remove'][1]"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Add_More_Deductn_Type_Of_Deductn 	= "//select[@id='deductionTypeCodeId1']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Add_More_Deductn_Amount 	= "//b[text()='DEDUCTIONS']//following::input[@title='Amount($)*']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Add_More_Deductn_How_Often 	= "//b[text()='DEDUCTIONS']//following::select[@title='How Often ?*']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Add_More_Deductn_Deductn_Start_Date 	= "//b[text()='DEDUCTIONS']//following::input[@title='Deduction Start Date']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Add_More_Deductn_Deductn_End_Date 	= "//b[text()='DEDUCTIONS']//following::input[@title='Deduction End Date']"

Path_LFRY_PCI_P1_Curnt_Job_Incme_Yearly_Income 	= "//b[text()='YEARLY INCOME']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Yearly_Income_Total_Incmr_Ths_Yr 	= "//input[@id='houseHold.listOfContacts.contact[0].currentYearTotalIncome']"
Path_LFRY_PCI_P1_Curnt_Job_Incme_Yearly_Income_Total_Inmce_Tx_Nxt_Yr 	= "//input[@id='houseHold.listOfContacts.contact[0].nextYearExpectedTotalIncome']"

Path_LFRY_PCI_P1_Save_And_Exit 	= "//input[@id='primaryApplicantInfoSaveAndExitId']"
Path_LFRY_PCI_P1_Back 	= "//*[@id='primaryApplicantInfo']//input[@type='button' and @value='Back']"
Path_LFRY_PCI_P1_Next 	= "//input[@id='savePrimForm']"

##########################HouseholdDetails
Path_LFRY_HHD_Add_Person=                    "//input[@id='addDependantButton']"
Path_LFRY_HHD_First_Name_P2=                   "//input[@id='houseHold.listOfContacts.contact[1].firstName']"
Path_LFRY_HHD_Middle_Name_P2=                  "//input[@id='houseHold.listOfContacts.contact[1].middleName']"
Path_LFRY_HHD_Last_Name_P2=                    "//input[@id='houseHold.listOfContacts.contact[1].lastName']"
Path_LFRY_Suffix_P2=                           "//select[@id='houseHold.listOfContacts.contact[1].suffix']"
Path_LFRY_Suffix_P2_Jr=                        "//select[@id='houseHold.listOfContacts.contact[1].suffix']/option[5]"


Path_LFRY_HHD_Relation_Of_P2=                   "//select[@id='houseHold.listOfContacts.contact[1].suffix']/following::select[1]"
Path_LFRY_HH_Date_Of_Birth_P2=                "//input[@id='houseHold.listOfContacts.contact[1].birthDate']"
Path_LFRY_Gender_P2=                          "//select[@id='genderSelectId']"

Path_LFRY_Name_Of_Spouse_P2=                    "//input[@id='houseHold.listOfContacts.contact[1].spouseNameIfMarried']"
Path_LFRY_SSN_P2=                                "//input[@id='houseHold.listOfContacts.contact[1].ssn']"

Path_LFRY_HHD_Does_P2_Live_At_Same_Address=                    "//select[@id='houseHold.listOfContacts.contact[1].primaryApplicantLivingInSameAddressIndicator']"
Path_LFRY_HHD_P2_Lives_Different_Address_Home_Line_1=           "//input[@id='addressLine1First']"
Path_LFRY_HHD_P2_Lives_Different_Address_Home_Apartment=        "//input[@id='aptOrSuiteFirst']"
Path_LFRY_HHD_P2_Lives_Different_Address_Home_City_Name=        "//input[@id='cityFirst']"
Path_LFRY_HHD_P2_Lives_Different_Address_State =                "//select[@id='stateFirst' and @name='houseHold.listOfContacts.contact[1].listOfContactAddresses.contactAddress[0].addressStateName']"
Path_LFRY_HHD_P2_Lives_Different_Address_ZipCode =              "//input[@id='houseHold.listOfContacts.contact[1].listOfContactAddresses.contactAddress[0].addressPostalCode']"
Path_LFRY_HHD_P2_Lives_Different_Address_County =               "//input[@id='houseHold.listOfContacts.contact[1].listOfContactAddresses.contactAddress[0].addressPostalCode']/following::select[1]"         

Path_LFRY_HHD_P2_Lives_Different_Mlng_Address_Line_1=            "//input[@onchange='mailingAddress()' and @id='addressLine1Second']"
Path_LFRY_HHD_P2_Lives_Different_Mlng_Address_Apartment=          "//input[@id='aptOrSuiteSecond']"
Path_LFRY_HHD_P2_Lives_Different_Mlng_Address_CityName=            "//input[@id='citySecond']"
Path_LFRY_HHD_P2_Lives_Different_Mlng_Address_State=               "//select[@id='stateSecond']"
                                                   

Path_LFRY_HHD_P2_Lives_Different_Mlng_Address_ZipCode=            "//input[@id='zipCodeSecond']"
Path_LFRY_HHD_P2_Lives_Different_Mlng_Address_County=             "//input[@id='houseHold.listOfContacts.contact[1].listOfContactAddresses.contactAddress[0].addressPostalCode']/following::select[1]"

Path_LFRY_HHD_P2_Plan_Income_Tax_Next_Yr=                        "//select[@id='houseHold.listOfContacts.contact[1].additionalTaxInformation.claimedAsTaxDependentIndicator']/preceding::select[3]"
Path_LFRY_HHD_P2_Plan_Income_Tax_Next_Yr_Yes=                    "//select[@id='houseHold.listOfContacts.contact[1].additionalTaxInformation.claimedAsTaxDependentIndicator']/preceding::select[3]/option[2]"
Path_LFRY_HHD_P2_File_Jointly_With_Spouse=                        "//select[@id='houseHold.listOfContacts.contact[1].jointTaxFilerIndicator']"
Path_LFRY_HHD_P2_File_Jointly_With_Spouse_Yes =                    "//select[@id='houseHold.listOfContacts.contact[1].jointTaxFilerIndicator']/option[2]"
Path_LFRY_HHD_P2_File_Jointly_With_Spouse_Yes_First_Name=            "//input[@id='houseHold.listOfContacts.contact[1].additionalTaxInformation.taxFilerSpouse.contactFirstName']"
Path_LFRY_HHD_P2_File_Jointly_With_Spouse_Yes_Middle_Name=            "//input[@id='houseHold.listOfContacts.contact[1].additionalTaxInformation.taxFilerSpouse.contactMiddleName']"
Path_LFRY_HHD_P2_File_Jointly_With_Spouse_Yes_Last_Name=                "//input[@id='houseHold.listOfContacts.contact[1].additionalTaxInformation.taxFilerSpouse.contactLastName']" 

Path_LFRY_HHD_P2_File_Jointly_With_Spouse_Yes_Claim_dpndnts_On_Tax_Rtrn=        "//select[@id='houseHold.listOfContacts.contact[1].additionalTaxInformation.claimingDependentsIndicator']"
Path_LFRY_HHD_P2_File_Jointly_With_Spouse_Yes_Claim_dpndnts_On_Tax_Rtrn_Yes=    "//select[@id='houseHold.listOfContacts.contact[1].additionalTaxInformation.claimingDependentsIndicator']/option[2]"

Path_LFRY_HHD_P2_File_Jntly_With_Spse_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_Frst_Nam=    "//input[@id='houseHold.listOfContacts.contact[1].additionalTaxInformation.listOfTaxDependents.contact[0].contactFirstName']"
Path_LFRY_HHD_P2_Fle_Jntly_Wth_Spse_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_Mddle_Nam=    "//input[@id='houseHold.listOfContacts.contact[1].additionalTaxInformation.listOfTaxDependents.contact[0].contactMiddleName']"
Path_LFRY_HHD_P2_Fle_Jntly_Wth_Spse_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_Lst_Name=    "//input[@id='houseHold.listOfContacts.contact[1].additionalTaxInformation.listOfTaxDependents.contact[0].contactLastName']"


Path_LFRY_HHD_P2_Fle_Jntly_WSps_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_ADpndnt=            "//input[@id='addDependents']"
Path_LFRY_HHD_P2_Fle_Jntly_WSps_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_ADpndnt_Fst_Nam=    "//input[starts-with(@id,'taxFirstName')]"

Path_LFRY_HHD_P2_Fle_Jntly_WSps_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_ADpndnt_Mdl_Nam=    "//input[starts-with(@id,'taxFirstName')]//following::input[1]"

Path_LFRY_HHD_P2_Fle_Jntly_WSps_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_ADpndnt_Lst_Nam=    "//input[starts-with(@id,'taxFirstName')]//following::input[2]"
Path_LFRY_HHD_P2_Fle_Jntly_WSps_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_ADpndnt_Remove=     "//input[(@value='Remove')]"


Path_LFRY_HHD_P2_Be_Claimed_As_Dependent_On_Someone_Tax_Return =                    "//select[@id='houseHold.listOfContacts.contact[1].additionalTaxInformation.claimedAsTaxDependentIndicator']"
Path_LFRY_HHD_P2_Be_Clmd_As_Dpndnt_On_Someone_Tax_Rtrn_Tax_Filer_First_Name=        "//select[@id='houseHold.listOfContacts.contact[1].additionalTaxInformation.claimedAsTaxDependentIndicator']/option[2]/following::input[1]"
Path_LFRY_HHD_P2_Be_Clmd_As_Dpndnt_On_Someone_Tax_Rtrn_Tax_Filer_Mddle_Name=        "//select[@id='houseHold.listOfContacts.contact[1].additionalTaxInformation.claimedAsTaxDependentIndicator']/option[2]/following::input[2]"
Path_LFRY_HHD_P2_Be_Clmd_As_Dpndnt_On_Someone_Tax_Rtrn_Tax_Filer_Last_Name=        "//select[@id='houseHold.listOfContacts.contact[1].additionalTaxInformation.claimedAsTaxDependentIndicator']/option[2]/following::input[3]"

Path_LFRY_HHD_P2_Be_Claimed_As_Dependent_Not_Part_Of_Household=                    "//input[@class='aui-field-input aui-field-input-choice doNotSetRequired claimedAsTaxDependentValidator' and @value='true']"
Path_LFRY_HHD_P2_B_Clmd_As_Dpndnt_Nt_Part_Of_Hhold_And_Hw_Rltd_To_Tax_Filr=          "//Select[@id='houseHold.listOfContacts.contact[1].additionalTaxInformation.claimedAsDependentByContactRelationShipTypeCode']"

Path_LFRY_HHD_Is_P2_Pregnant=                                                        "//select[@id='houseHold.listOfContacts.contact[1].listOfMedicalConditions.medicalCondition[0].medicalConditionIndicator']"
Path_LFRY_HHD_Is_P2_Pregnant_Yes_Hw_Mny_Babies_Are_Expctd_Durng_Prgnancy=            "//select[@title=' How many babies are expected during this pregnancy?* ']"
Path_LFRY_HHD_Is_P2_Pregnant_Yes_Expected_Due_Date=                                 "//input[@title=' Expected Due Date* ']"

Path_LFRY_HHD_P2_Needs_Health_Coverage_No=                                        "//input[@id='healthCovgReqIndNo']"

Path_LFRY_HHD_P2_Needs_Health_Coverage_Yes=                                    "//input[@id='healthCovgReqIndYes']"
Path_LFRY_HHD_P2_Have_Disability_Last_More_Than_Twelve_Months=                "//select[@id='houseHold.listOfContacts.contact[1].phyclPyschHealthConditionIndicator']"

Path_LFRY_HHD_P2_Hv_Dsblty_Lst_Mre_Thn_Twlv_Mnths_Ys_Crntly_Rcv_LTrm_CSrvcs=     "//select[@id='houseHold.listOfContacts.contact[1].currentLTCStatus']"

Path_LFRY_HHD_P2_Received_LTerm_Care_Nursing_Services_In_Three_Months=           "//select[@id='houseHold.listOfContacts.contact[1].receivedLongTermCareServiceInPast3MonthsIndicator']"
Path_LFRY_HHD_P2_Received_LTerm_Care_Nursing_Services_In_Three_Months_Ys_Frm=        "//input[@id='houseHold.listOfContacts.contact[1].receivedLongTermCareServiceFromDate']"
Path_LFRY_HHD_P2_Received_LTerm_Care_Nursing_Services_In_Three_Months_Yes_To=        "//input[@id='houseHold.listOfContacts.contact[1].receivedLongTermCareServiceToDate']"
Path_LFRY_HHD_P2_Think_Need_LTerm_Care_Nursing_Services_Now=                         "//select[@id='houseHold.listOfContacts.contact[1].requiredNursingFacilitiesIndicator']"
Path_LFRY_HHD_P2_Receive_SSI=                                                       "//select[@id='houseHold.listOfContacts.contact[1].receivingSSIIndicator']"

Path_LFRY_HHD_P2_Receive_Any_Medical_Srvcs_In_Ten_Clndr_Dys_Imdtly_Prir_To=        "//select[@id='houseHold.listOfContacts.contact[1].listOfEmergencyServicesDetails.emergencyServicesDetail[0].emergencyServicesReceivedInPastTenDaysIndicator']"
Path_LFRY_HHD_P2_Rcv_Any_Mdcl_Srvcs_In_Ten_Clndr_Dys_Imdtly_Prir_To_Ys_Frm=        "//input[@id='houseHold.listOfContacts.contact[1].listOfEmergencyServicesDetails.emergencyServicesDetail[0].emergencyServicesDetailsStartDate']"
Path_LFRY_HHD_P2_Rcv_Any_Mdcl_Srvcs_In_Ten_Clndr_Dys_Imdtly_Prir_To_Ys_To=          "//input[@id='houseHold.listOfContacts.contact[1].listOfEmergencyServicesDetails.emergencyServicesDetail[0].emergencyServicesDetailsEndDate']"


Path_LFRY_HHD_P2_US_Citizen_Or_National=                                        "//select[@id='houseHold.listOfContacts.contact[1].usCitizenOrNationalIndicator']"

Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Has_Elgbl_Imgrtn=              "//select[@id='houseHold.listOfContacts.contact[1].qualifiedNonCitizenStatusIndicator']"

#Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Has_Elgbl_Imgrtn_Ys_Doc=        "//select[@id='ImmgDocType']"

Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Has_Elgbl_Imgrtn_Ys_Doc  = "//div[@id='health_covg']//select[@id='ImmgDocType']"
Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Has_Elgbl_Imgrtn_Ys_SType=        "//select[@id='ImmgDocType']/following::input[1]"
Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Ntnl_Has_Elgbl_Imgrtn_Ys_NAs_On_Imgrtn_Dc=     "//input[@id='houseHold.listOfContacts.contact[1].nameOnImmigrationDoc']"

Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Hs_Elgbl_Imgrtn_Ys_Doc_Vsan=        "//input[@id='houseHold.listOfContacts.contact[1].alienNumber']"
Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Hs_Elgbl_Imgrtn_Ys_Doc_Vsain=      "//input[@id='houseHold.listOfContacts.contact[1].i94Number']"
Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Hs_Elgbl_Imgrtn_Ys_Doc_Vsapn=        "//input[@title=' Passport Number ']"
Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Hs_Elgbl_Imgrtn_Ys_Doc_PEdt=        "//input[@id='passExpDoe']"
Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Hs_Elgbl_Imgrtn_Ys_Doc_ODoc=       "//input[@title=' Other Document # ']"

Path_LFRY_HHD_If_P2_Date_Of_Entry_To_US_On_Immigration_Doc_Listed=                     "//input[@id='doe1']"
Path_LFRY_HHD_Is_P2_Ctzn_Of_Fdrtd_Stats_Of_Micrnsia_Rpblc_Of_Mrshl_Islnds_Ys=         "//input[@id='fedCtnNewYes']"
Path_LFRY_HHD_Is_P2_Citizenship_On_Immigrated_Doc_Listed=                            "//select[@id='federalState']"

Path_LFRY_HHD_Is_P2_Or_Their_Spse_Prnt_A_Vtrn_Or_Actv_Duty_Mmbr_Of_US_Mltry=           "//select[@id='houseHold.listOfContacts.contact[1].honorablyDischargedFromMilitaryIndicator']"

Path_LFRY_HHD_P2_In_Foster_Care_At_Age_Eighteen_Or_Older_In_Hawaii=                   "//select[@id='houseHold.listOfContacts.contact[1].listOfFosterCareDetails.fosterCareDetail[0].fosterCareUnderStateRespAt18Indicator']"

Path_LFRY_HHD_Is_P2_Full_Time_Student=                                               "//select[@id='houseHold.listOfContacts.contact[1].fullTimeStudentIndicator']"
Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity=                                      "//div[@id='health_covg']/table/tbody/tr[10]/td/div"


Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity_Chicano=                               "//input[@id='hawaii.ethnicity.lov.chicanoaCheckbox']"
Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity_Mexican_American=                     "//input[@id='hawaii.ethnicity.lov.mexicanamericanCheckbox']"
Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity_Other=                               "//input[@id='otherEthnicityIndicatorCheckbox']"
Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity_Other_Country=                      "//input[@id='houseHold.listOfContacts.contact[1].ethnicity.otherTypeName']"
Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity_Cuban=                             "//input[@id='hawaii.ethnicity.lov.cubanCheckbox']"
Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity_Puerto_Rican=                     "//input[@id='hawaii.ethnicity.lov.puertoricanCheckbox']"
Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity_Mexican=                         "//input[@id='hawaii.ethnicity.lov.mexicanCheckbox']"

Path_LFRY_HHD_P2_Race=                                                                 "//div[@id='health_covg']/table/tbody/tr[12]/td/div"
Path_LFRY_HHD_P2_Race_American_Indian_Or_Alaskan=                                     "//input[@id='hawaii.race.lov.ameriindioralanatCheckbox']"
Path_LFRY_HHD_P2_Race_Chinese=                                                       "//input[@id='hawaii.race.lov.chineseCheckbox']"
Path_LFRY_HHD_P2_Race_Japanese=                                                     "//input[@id='hawaii.race.lov.japaneseCheckbox']"
Path_LFRY_HHD_P2_Race_Other_Asian=                                                 "//input[@id='hawaii.race.lov.otherasianCheckbox']"
Path_LFRY_HHD_P2_Race_Vietnamese=                                                 "//input[@id='hawaii.race.lov..vietnameseCheckbox']"
Path_LFRY_HHD_P2_Race_Other=                                                     "//input[@id='otherRaceIndicatorCheckbox']"
Path_LFRY_HHD_P2_Race_Other_Country=                                            "//input[@id='houseHold.listOfContacts.contact[1].race.otherTypeName']"

Path_LFRY_HHD_P2_Race_Asian_Indian=                                            "//input[@id='hawaii.race.lov.asianindianCheckbox']"
Path_LFRY_HHD_P2_Race_Filipino=                                               "//input[@id='hawaii.race.lov.filipinoCheckbox']"
Path_LFRY_HHD_P2_Race_Korean=                                                "//input[@id='hawaii.race.lov.koreanCheckbox']"
Path_LFRY_HHD_P2_Race_Other_Pacific_Islander=                               "//input[@id='hawaii.race.lov.othpacificCheckbox']"
Path_LFRY_HHD_P2_Race_White=                                               "//input[@id='hawaii.race.lov.whiteCheckbox']"

Path_LFRY_HHD_P2_Race_Black_Or_African_American=                         "//input[@id='hawaii.race.lov.blackoraframeCheckbox']"
Path_LFRY_HHD_P2_Race_Guamanian_Or_Chamorro=                            "//input[@id='hawaii.race.lov.guamanianorchamorroCheckbox']"
Path_LFRY_HHD_P2_Race_Native_Hawaiian=                                 "//input[@id='hawaii.race.lov.nativehawaiianCheckbox']"
Path_LFRY_HHD_P2_Race_Samoan=                                         "//input[@id='hawaii.race.lov.samoanCheckbox']"

Path_LFRY_HHD_P2_Current_Job_Income_Info=                            "//div[@class='emtype']/b"
Path_LFRY_HHD_P2_Type_Of_Employment_Title=                          "//div[@class='matchTitle']"

Path_LFRY_HHD_P2_Type_Of_Employment_Employed=                             "//input[@id='employmentTypeEmployed']"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Name= 		           "//input[@id='empName']"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Phone= 		          "//input[contains(@id,'empPhone')]"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Address_L1=	         "//input[@id='houseHold.listOfContacts.contact[1].listOfFinancialIncomes.financialIncome[0].employerInformation.employerAddress.addressStreetName1']"

Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Apartment_Number= 	"//input[@id='houseHold.listOfContacts.contact[1].listOfFinancialIncomes.financialIncome[0].employerInformation.employerAddress.addressStreetName2']"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_City= 	           "//input[@id='houseHold.listOfContacts.contact[1].listOfFinancialIncomes.financialIncome[0].employerInformation.employerAddress.addressCityName']"

Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_State= 		            "//select[@class='aui-field-input aui-field-input-select aui-field-input-menu requiredValid' and @id='stateFirst']"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_State_1=	               "//select[@class='aui-field-input aui-field-input-select aui-field-input-menu requiredValid' and @id='stateFirst']/option[1]"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Zip_Code= 	          "//input[@id='zipCodeFirst']"

Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Wages_Tips= 		     "//input[@id='amount1']"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Wages_How_Often= 	"//select[@id='houseHold.listOfContacts.contact[1].listOfFinancialIncomes.financialIncome[0].incomeFrequency']"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Wgs_HOften_Dly_Nodw= 		"//select[@id='houseHold.listOfContacts.contact[1].listOfFinancialIncomes.financialIncome[0].incomeFrequency']/following::input[2]"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Wages_Income_Start_Date= 	"//input[@id='houseHold.listOfContacts.contact[1].listOfFinancialIncomes.financialIncome[0].incomeStartDate']"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Wages_Income_End_Date= 	   "//input[@id='houseHold.listOfContacts.contact[1].listOfFinancialIncomes.financialIncome[0].incomeEndDate']"

Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs=                   "//input[@id='addJob']"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Name=         "//input[contains(@id,'employerNameId')]"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Phone=        "//input[@title='Phone number ']"

Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Address_Line_1= 	   "//input[@title='Phone number ']/following::input[1]"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_suite_number= 	       "//input[@title='Phone number ']/following::input[2]"

Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_City=        	 "//input[@title='Phone number ']/following::input[3]"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_State=          	"//select[@title='State*']"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_State_Hawaii= 	"//select[@title='State*']/following::select[1]"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Zip_Code=          "//input[@title='Phone number ']/following::input[4]"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Wages=              "//select[@title='State*']/following::select[1]/preceding::input[1]"

Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Wges_Hw_Oftn=   "//select[@title='State*']/following::select[1]"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_ANew_Jbs_EWges_HOftn_Dnodw=     "//select[@title='State*']/following::select[1]/following::input[2]"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Wges_Strt_Date=      "//input[@title='Income Start Date']"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Wges_End_Date=      "//input[@title='Income End Date']"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Remove=                "//input[@class='aui-button-input' and @title='Remove']"
Path_LFRY_HHD_P2_Type_Of_Employment_Employed_In_The_Past_Year_Did_P2=             "//select[@id='houseHold.listOfContacts.contact[1].pastYearJobHistory']"

Path_LFRY_HHD_P2_Type_Of_Employment_Self_Employed=                                       "//input[@id='employmentTypeSelfEmployedCheckbox']"
Path_LFRY_HHD_P2_Type_Of_Employment_Self_Employed_Type_Of_Work=                         "//input[@id='houseHold.listOfContacts.contact[1].selfEmploymentDetails.selfEmploymentTypeCode']"
Path_LFRY_HHD_P2_Tpe_Of_Emplmnt_Slf_Emply_Tpe_Of_Wrk_Hw_Mch_Nt_Incm_Yu_Gt_Pd=          "//input[@id='houseHold.listOfContacts.contact[1].selfEmploymentDetails.selfEmploymentNetIncomeAmount']"

Path_LFRY_HHD_P2_Type_Of_Employment_Not_Employed=                                    "//input[@id='employmentTypeNotEmployed']"
Path_LFRY_HHD_P2_Type_Of_Employment_Other_Income_This_Month=                        "//b[contains(text(),'OTHER INCOME THIS MONTH')]"
Path_LFRY_HHD_P2_Type_Of_Employment_Other_Income_This_Month_Income_Type=           "//b[contains(text(),'OTHER INCOME THIS MONTH')]/following::select[1]"


Path_LFRY_HHD_P2_Type_Of_Employment_Other_Income_This_Month_Income_Amount=          "//b[contains(text(),'OTHER INCOME THIS MONTH')]/following::select[1]/following::input[1]"
Path_LFRY_HHD_P2_Type_Of_Employment_Other_Income_This_Mnth_Incm_Amnt_Hw_Oftn=      "//input[@id='employmentTypeSelfEmployedCheckbox']/following::select[2]"
Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Other_Incme_This_Mnth_Incm_Amnt_Hw_Oftn_Dly=     "//input[@id='employmentTypeSelfEmployedCheckbox']/following::select[2]/option[2]"
Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Other_Incme_This_Mnth_Incm_NDays_Wkd_EWeek=      "//input[@id='houseHold.listOfContacts.contact[1].listOfOtherIncomes.financialIncome[0].incomeNumberOfDaysWorkedPerWeek']"
Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_This_Mnth_Incm_Amnt_Hw_Oftn_Hrly=     "//input[@id='employmentTypeSelfEmployedCheckbox']/following::select[2]/option[4]"
Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_This_Mnth_Incm_Avg_Hrs_Wkd_EWeek=     "//input[@id='houseHold.listOfContacts.contact[1].listOfOtherIncomes.financialIncome[0].incomeNumberOfHoursWorkedPerWeek']"
Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_This_Mnth_Incme_Strt_Date=           "//input[@id='houseHold.listOfContacts.contact[1].listOfOtherIncomes.financialIncome[0].incomeStartDate']"
Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_This_Mnth_Incme_End_Date=           "//input[@id='houseHold.listOfContacts.contact[1].listOfOtherIncomes.financialIncome[0].incomeEndDate']"

Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_More_Income_Types=              "//input[@title='Add more income types']"
Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_More_Income_Types_Othr_Incme=                       "//b[contains(text(),'OTHER INCOME THIS MONTH')]/following::select[3]"
   
Path_LFRY_HHD_P2_Tpe_Of_Emplmnt_Othr_Incm_Add_Mre_Incm_Typ_Typ_Amnt=                                "//b[contains(text(),'OTHER INCOME THIS MONTH')]/following::select[3]/following::input[1]"

Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_Mre_Incm_Typs_How_Often=                         "//b[contains(text(),'OTHER INCOME THIS MONTH')]/following::select[4]"  
Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_Mre_Incm_Typs_NDys_Wkd_EWeek=                 "//table[@class='app_content_table2 infortbl']/tbody/tr[3]/td[1]/div[3]/span/span/label/following::span[1]/input[1]"

Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_Mre_Incm_Typs_Incme_Strt_Dte=                "//input[@class='aui-button-input requiredValid']/following::input[5]"
Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_Mre_Incm_Typs_Incme_End_Dte=                 "//input[@class='aui-button-input requiredValid']/following::input[6]"

Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_Mre_Incm_Remove=                           "//input[@class='aui-button-input requiredValid']"


Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_label=                         "//b[text()='DEDUCTIONS']"
Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Type_Of_Dductn=               "//select[@id='houseHold.listOfContacts.contact[1].listOfDeductions.deduction[0].deductionTypeCode']"
Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Amount=                     "//select[@id='houseHold.listOfContacts.contact[1].listOfDeductions.deduction[0].deductionTypeCode']/option[2]/following::input[1]"
Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Amount_How_Often=          "//select[@id='houseHold.listOfContacts.contact[1].listOfDeductions.deduction[0].deductionTypeCode']/following::select[1]"

Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Deduction_Start_Date=   "//input[@class='aui-field-input aui-field-input-text makeFieldDisabled clearFieldValues doNotSetRequired GoodDate dateFormatValid hasDatepicker' and @title=' Deduction Start Date ']"
Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Deduction_End_Date=    "//select[@id='houseHold.listOfContacts.contact[1].listOfDeductions.deduction[0].deductionTypeCode']/following::select[1]/following::input[3]"


Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions=                             "//input[@id='addDed']"
Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions_TDduction=                   "//input[@title='Add more income types']/following::select[3]"
Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions_Amount=                    "//input[@title='Add more income types']/following::select[3]/following::input[1]"
Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions_Hw_Oftn=                  "//input[@title='Add more income types']/following::select[4]"
Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions_Dductn_Strt_Date=      "//span[@class='aui-field aui-field-text date_selectorincome']/span/span//input[@title='Deduction Start Date']"
Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions_Dductn_End_Date=      "//input[@title='Add more income types']/following::select[4]/following::input[3]"

Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions_Remove=          "//span[@class='aui-field aui-field-text date_selectorincome']/span/span//input[@title='Deduction Start Date']/following::input[1]"



Path_LFRY_HHD_P2_Type_Of_Employment_Yearly_Income_Title=                       "//b[text()='YEARLY INCOME']"
Path_LFRY_HHD_P2_Type_Of_Employment_Yearly_Income_Total_Income_This_Year=     "//input[@id='houseHold.listOfContacts.contact[1].currentYearTotalIncome']" 
Path_LFRY_HHD_P2_Type_Of_Employment_Yearly_Income_Total_Income_Next_Year=    "//input[@id='houseHold.listOfContacts.contact[1].nextYearExpectedTotalIncome']"
Path_LFRY_HHD_P2_Remove_Person_1=                                           "//input[@id='houseHold.listOfContacts.contact[1].nextYearExpectedTotalIncome']/following::input[1]"
Path_LFRY_HHD_P2_Add_Person_1=                                             "//input[@id='houseHold.listOfContacts.contact[1].nextYearExpectedTotalIncome']/following::input[2]"
Path_LFRY_HHD_P2_Save_And_Exit=                                           "//input[@title='Save & Exit']"
Path_LFRY_HHD_P2_Save_And_Back=                                          "//input[@title='Back']"
Path_LFRY_HHD_P2_Save_And_Next=                                         "//input[@title='Next']"



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



