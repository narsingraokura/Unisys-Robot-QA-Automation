*** Settings ***
#Library     SeleniumLibrary
Resource     KOLEA_Key_Words.robot

*** Variable ***
${File_Name_LifeRay_Accounts}    
${Value_Update_Date}    
${Value_Creation_Date}    
${Value_Session_Id}    
${Value_N}    
${Value_Is_Counselor}    
${Value_Password}    
${Value_User_Name}    
${This_LifeRay_User_Name}
${This_LifeRay_Password}
${LifeRay_Logins}
&{LifeRay_New_User}

*** Keywords ***
    

Click Pre-Assessment
    Click Element                   ${Path_LifeRay_Pre_Assess_Button}
    Select iframe
Click Next
    Wait For Self Assess Page To Appear
    Click Element                   ${Path_Pre_Assess_iframe_Next}
Click Apply Now
    Click Button With Name  ${Value_Apply_Now}
    Wait for Create Account Page
Want Help Paying Health Insurance
    [Arguments]                     ${Answer}
    #Run Keyword if                  ${Answer}   IN  ${Valid_Values_4_Yes}       Need Health Insurance
    ${Present_In_Yes}=              Run Keyword And Return Status   Should Contain  ${Valid_Values_4_Yes}   ${Answer}   ignore_case=True
    ${Present_In_No}=               Run Keyword And Return Status   Should Contain  ${Valid_Values_4_No}    ${Answer}   ignore_case=True
    Run Keyword if                  ${Present_In_Yes}   Need Health Insurance
    Run Keyword if                  ${Present_In_No}    Do Not need Health Insurance
Need Health Insurance
    Wait for Need Health Indicator
    Select From List By Value       ${Path_Need_Health_Indicator}   ${Value_String_True}
Do Not need Health Insurance
    Wait for Need Health Indicator
    Select From List By Value       ${Path_Need_Health_Indicator}   ${Value_String_False}
Any Aged LTC blind or diabled
    [Arguments]                     ${Answer}
    ${Present_In_Yes}=              Run Keyword And Return Status   Should Contain  ${Valid_Values_4_Yes}   ${Answer}   ignore_case=True
    ${Present_In_No}=               Run Keyword And Return Status   Should Contain  ${Valid_Values_4_No}    ${Answer}   ignore_case=True
    Run Keyword if                  ${Present_In_Yes}   Yes ABD
    Run Keyword if                  ${Present_In_No}    No ABD
No ABD
    Select From List By Value       ${Path_Aged_LTC_Blind_Disable}   ${Value_String_True}
Yes ABD
    Select From List By Value       ${Path_Aged_LTC_Blind_Disable}   ${Value_String_False}
Children Aged 18 Or Under
    [Arguments]                     ${Answer}
    Select From List By Value       ${Path_Aged_18_Or_Under}        ${Answer}
Adult Aged 19 or Over
    [Arguments]                     ${Answer}
    Select From List By Value       ${Path_Aged_19_Or_Older}        ${Answer}
Babies Expected
    [Arguments]                     ${Answer}
    Select From List By Value       ${Path_Expected_Child}          ${Answer}
Household monthly income
    [Arguments]                     ${Answer}
    Input Text                      ${Path_Monthly_Income}          ${Answer}
Validate Result
    [Arguments]                     ${Msg_Type}
    Run Keyword if                  '${Msg_Type}' == '${Value_Eligible}'        Validate Result To Be Eligible
    Run Keyword if                  '${Msg_Type}' == '${Value_Ineligible}'      Validate Result To Be Ineligible
Validate Result To Be Eligible
    element should contain          ${Path_Result_Messages}         ${Msg_Eligible}
    Should Have Apply Now Button
    Should Have Logo Of State Of Hawaii
Validate Result To Be Ineligible
    element should contain          ${Path_Result_Messages}         ${Msg_Ineligible}
    Should Have Apply Now Button
    Logo Should Be Market Place
Should Have Logo Of State Of Hawaii
    Page Should Contain Element     ${Path_State_Hawai_Logo}
Logo Should Be Market Place
    Page Should Contain Element     ${Path_Hlth_Ins_Mrkt_Logo}
Should Have Apply Now Button
    Page Should Contain Element     ${Path_Apply_Now}
    
Enter Account Information
    [Arguments]             ${Inp_First_Name}=${Random_First_Name}
    ...                     ${Inp_Last_Name}=${Random_Last_Name}
    ...                     ${Inp_Email}=${Random_Email}
    ...                     ${Inp_User_Name}='UserName'
    ...                     ${Inp_password}=${Random_password}
    ...                     ${Inp_answer1}=${Value_answer1}
    ...                     ${Inp_answer2}=${Value_answer2}
    ...                     ${Inp_answer3}=${Value_answer3}
    ${Random_Middle_Name}=  Get Random Middle Initial
    Input Text              ${Path_Create_Acc_First_Name}       ${Inp_First_Name}
    Input Text              ${Path_Create_Acc_Last_Name}        ${Inp_Last_Name}
    Input Text              ${Path_Create_Acc_Email}            ${Inp_Email}
    Input Text              ${Path_Create_Acc_reEnter_Email}    ${Inp_Email}
    ${Inp_User_Name}=   catenate    ${Inp_First_Name}${Inp_Last_Name}${Random_Middle_Name}
    Log                     ${Inp_User_Name}
    Input Text              ${Path_Create_Acc_Screen_Name}      ${Inp_User_Name}
    Input Text              ${Path_Create_Acc_Password1}        ${Inp_password}
    Input Text              ${Path_Create_Acc_Password2}        ${Inp_password}
    Set Suite Variable      ${This_LifeRay_User_Name}           ${Inp_User_Name}
    Set Suite Variable      ${This_LifeRay_Password}            ${Inp_password}
    Log         ${Inp_password}
    Wait For Security Questions
    Select First Option Of Security Question1
    Input Text              ${Path_Create_Acc_answer1}          ${Value_answer1}
    Select First Option Of Security Question2
    Input Text              ${Path_Create_Acc_answer2}          ${Value_answer2}
    Select First Option Of Security Question3
    Input Text              ${Path_Create_Acc_answer3}          ${Value_answer3}
    Select No For Registering As A Counselor
    ${Inp_Q1}=    Get Security Question1
    ${Inp_Q2}=    Get Security Question2
    ${Inp_Q3}=    Get Security Question3
    Click Create Account Button
    Set To Dictionary    ${LifeRay_New_User}    ${Value_First_Name}=${Inp_First_Name}      ${Value_Last_Name}=${Inp_Last_Name}
    Set To Dictionary    ${LifeRay_New_User}    ${Value_Last_Name}=${Inp_Last_Name}        ${Value_emailAddress}=${Inp_Email}
    Set To Dictionary    ${LifeRay_New_User}    ${Value_User_Name}=${Inp_User_Name}        ${Value_Password}=${Inp_password}
    Set To Dictionary    ${LifeRay_New_User}    ${Value_q1}=${Inp_Q1}    ${Value_q2}=${Inp_Q2}    ${Value_q3}=${Inp_Q3}
    Set To Dictionary    ${LifeRay_New_User}    ${Value_answer1}=${Value_answer1}          ${Value_answer2}=${Value_answer2}
    Set To Dictionary    ${LifeRay_New_User}    ${Value_answer3}=${Value_answer3}          ${Value_Is_Counselor}=${Value_N}
    ${Session_id}=    Get Session Id
    Set To Dictionary    ${LifeRay_New_User}    ${Value_Session_Id}=${Session_id}          
    ${Value_Curr_Date}=    Get Current Date       
    Set To Dictionary    ${LifeRay_New_User}    ${Value_Creation_Date}= ${Value_Curr_Date}    ${Value_Update_Date}= ${Value_Curr_Date}
    [Return]    ${LifeRay_New_User}


#######################################################################################################################
    
Write LifeRay Account Details To Excel
    [Arguments]    ${LifeRay_New_User}
    
    Open Excel  ${File_Name_LifeRay_Accounts}
    ${Names}=      Get Sheet Names
    Log     ${Names}  
    Log     ${LifeRay_New_User}
    ${Col}=    Get Column Count    Accounts
    ${Row}=    Get Row Count    Accounts
    Put Number To Cell    Accounts    ${Col}    ${Row}    ${Col}
    ${Inp_User_Name}=    Get From Dictionary    ${LifeRay_New_User}	   ${Value_User_Name}
    Put String To Cell    Accounts    ${Col}    ${Row}    ${Inp_User_Name}
    Save Excel    ${File_Name_LifeRay_Accounts}
    
        
########################################################################################################################
###################################                 Selections                        ##################################
########################################################################################################################
Select First Option Of Security Question1
    Select From List By Index   ${Path_Create_Acc_Security_q1}   ${Value_str_1}
Select First Option Of Security Question2
    Select From List By Index   ${Path_Create_Acc_Security_q2}   ${Value_str_1}
Select First Option Of Security Question3
    Select From List By Index   ${Path_Create_Acc_Security_q3}   ${Value_str_1}
Select No For Registering As A Counselor
    Click Element       ${Path_Create_Acc_As_Counselor_No}

Get Security Question1
    ${res}=    Get Selected List Value       ${Path_Create_Acc_Security_q1}
    [Return]    ${res}
    
Get Security Question2
    ${res}=    Get Selected List Value       ${Path_Create_Acc_Security_q2}
    [Return]    ${res}


Get Security Question3
    ${res}=    Get Selected List Value       ${Path_Create_Acc_Security_q3}
    [Return]    ${res}
    
Click Create Account Button
    Click Button With Name      ${Value_koleaCreateAccount}
########################################################################################################################
###################################                 WAITS                             ##################################
########################################################################################################################
Wait for Create Account Page
    Wait Until Element Is Visible    ${Path_Create_Account_Heading}                     ${Wait_10_Sec}
Wait For Security Questions
    Wait Until Element Is Enabled   ${Path_Create_Acc_Security_q1}                      ${Wait_5_Min}
Wait For Self Assess Page To Appear
    Wait Until Element Is Visible   ${Path_Pre_Assess_iframe_Next}      ${Wait_10_Sec}
Wait for Need Health Indicator
    Wait Until Element Is Visible       ${Path_Need_Health_Indicator}       ${Wait_10_Sec}
