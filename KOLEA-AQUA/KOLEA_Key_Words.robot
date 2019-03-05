*** Settings ***

Variables       Variables.py
Library         SeleniumLibrary
Library         Collections
Library         OperatingSystem
Library         String
Library         ExcelLibrary
Library         FakerLibrary
Library         Variables



*** Keywords ***    


Do Nothing
    No Operation

Open Home Page
    [Arguments]          ${Application}
    Run Keyword If      '${Application}'=='${Value_Siebel}'         Open Siebel Home Page
    Run Keyword If      '${Application}'=='${Value_LifeRay}'        Open LifeRay Home Page
    Run Keyword If      '${Application}'=='${Value_IDM}'            Open IDM Home Page
    Maximize Window

Open Siebel Home Page
    Open Browser         ${URL_Siebel}      ${BROWSER_FireFox}
    Set Selenium Speed  ${Selenium_Speed}


Open LifeRay Home Page

    Open Browser         ${URL_LifeRay}     ${BROWSER_RANDOM}
    Set Selenium Speed   ${Selenium_Speed}
    Wait for LifeRay Home Page
    Validate LifeRay Home Page

Open IDM Home Page

    Open Browser         ${URL_LifeRay}     ${BROWSER_RANDOM}
    Set Selenium Speed   ${Selenium_Speed}
    Wait for LifeRay Home Page
    Validate LifeRay Home Page

Close Browsers
    Capture Screen
    Close All Browsers

Maximize Window
    maximize browser window

Save Session Details
    ${conn_url}  ${session_id}=    Return Driver Props
    ${file_line}=       catenate    ${conn_url} ${session_id}
    Create File     ${CURDIR}/Session.txt   ${file_line}

Get Session Details
    ${file_line}=       Get File            ${CURDIR}/Session.txt
    [Return]  ${file_line}

Capture and Close
    Capture Screen
    Close Browser


Capture Screen
    capture page screenshot


Click OK on Alert
    Handle Alert    timeout=100 s

Click Enter
    [Arguments]                 ${Inp_Path}
    Press Key                   ${Inp_Path}                    \\13


Should Have Button
    [Arguments]     ${Button_Value}
    Page Should Contain Button  ${Button_Value}

Click Button With Name
    [Arguments]     ${Button_Value}
    Click Button    ${Button_Value}

Sleep A Second
    Sleep In Seconds                1

Sleep In Seconds
    [Arguments]          ${time_in_seconds}=${Value_1}
    Sleep                ${time_in_seconds}


Wait For iframe
    Wait Until Element Is Visible   ${Path_iframe}      ${Wait_20_Sec}

Select iframe
    Wait For iframe
    Select Frame                    ${Path_iframe}

########################################################################################################################
###################################                 VALIDATIONS                             ##################################
########################################################################################################################

Validate LifeRay Home Page
    Should Have Image Large KOLEA Logo
    Should Have Button  ${Value_Pre_Assessment}
    Should Have Button  ${Value_Sign_In}
    Should Have Button  ${Value_Apply_Now}
    Should Have Button  ${Value_Register_Now}

Should Have Image Large KOLEA Logo
    Page Should Contain Image       ${URL_Hawaii_Large_Logo}


########################################################################################################################
###################################                 WAITS                             ##################################
########################################################################################################################

	
Wait for LifeRay Home Page
    Wait Until Element Is Visible   ${Path_LifeRay_Home_Page_Footer}                    ${Wait_10_Sec}
