*** Settings ***
Resource    KOLEA_Key_Words.robot    
Resource    LifeRay_Key_Words.robot

   
   

*** Test Cases ***
AuthorizedRepresentative
    ${Address}                Address
    ${Street_Address}         Street Address
    ${Apartment_Number}       Building Number
    ${City}                   City
    ${Zip_Code}               Postcode
    ${Phone_Number}           Phone Number
    ${Organization_Name}      Company
    ${Number}                 Int Number
    
   Open Browser                                   ${URL_AuthorizedRep}                                                                ${BROWSER_Chrome}
   Maximize window
   Element Text Should Be                         ${Path_LFRY_AR_Title}                                                               Authorized Representative

    Click Element                                 ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_No}                   
    #Click Element                                 ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Nxt}                 

    Click Element                                 ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y}                 

    Input Text                                    ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_Frst_Name}             ${Random_First_Name}
    Input Text                                    ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_Mdle_Name}             ${Random_Middle_Initial}
    Input text                                    ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_Lst_Name}              ${Random_Last_Name}
    Click Element                                 ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_Suffix}
    Select from List By Index                     ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_Suffix}                5     


    Input Text                                    ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_Addrs_L1}              ${Street_Address} 
    Input Text                                    ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_Aprtmnt}               ${Apartment_Number}




    Input Text                                     ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_City}                 ${City}
    Click Element                                  ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_State}             
    Select From List By Index                      ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_State}                1
    
    Input Text                                     ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_ZCode}                ${Zip_Code}
    Click Element                                  ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_County}         
    Select From List By Index                      ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_County}                1
    Input Text                                     ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_Phone}                ${Phone_Number}
    Input text                                     ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_Orgnztn_Name}         ${Organization_Name}
    Input text                                     ${Path_LFRY_AR_Would_You_Like_To_Include_Authrzd_Reprsntatv_Y_ID_Nmbr}              ${Number}


    #Click Element                                 ${Path_LFRY_AR_Save_And_Exit}               
    #Click Element                                 ${Path_LFRY_AR_Back_Button}                
    #Click Element                                 ${Path_LFRY_AR_Next_Button} 
   
