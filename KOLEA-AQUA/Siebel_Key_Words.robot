*** Settings ***
Resource  KOLEA_Key_Words.robot


*** Keywords ***


Logout KOLEA
    Capture Screen
    unselect frame
    wait until element is visible  //li[@id="tb_0"]         ${Wait_10_Sec}
    click element  //li[@id="tb_0"]
    wait until element is visible  //button[@rn='Logout']   ${Wait_10_Sec}
    click element  //button[@rn='Logout']


Should Be KOLEA Sign On Window
    Wait for Sing On Page
    Should Have Hawaii Gov Banner
    Should Have KOLEA Logo
    Should Have Username Field
    Should Have Continue Button

Validate Analytics Logon
    No Operation

Validate CRM Reports Page
    Page Should Have Apply Button

Validate Application Page
    Select iframe
    #Validate Left Active Link To Be     Primary Contact Information
    #We need to use Get Source Key word to convert current page to HTML
    #And use XML library of Robot framework to validate
    Wait For Application Date
    Validate Application Date To Be Today


Open KOLEA Site Map
    From Menu Bar Select Navigate
    Select Site Map
    Wait For Site Map Page

From Menu Bar Select Navigate
    Click Element                   ${Path_Menubar_Navigate}

Select Site Map
    Click Element                   ${Path_Site_Map_Link}


Should Have Hawaii Gov Banner
    Page Should Contain Link        ${Link_Hawaii_Gov}

Should Have KOLEA Logo
    Page Should Contain Image       ${Image_Kolea_Logo}

Should Have Username Field
    Page Should Contain Element     ${Path_KOLEA_Sign_On_Username}

Should Have Continue Button
    Page Should Contain Button      ${Value_Continue}

Validate Application Date To Be Today
    Wait Until Element Is Visible   ${Path_SBL_New_App_Create_Date}         ${Wait_10_Sec}
    Textfield Value Should Be       ${Path_SBL_New_App_Create_Date}         ${Today_mm_dd_ccyy}

Page Should Have Apply Button
    Page Should Contain Button      ${Value_Apply}

Enter User Name
    [Arguments]                     ${Inp_Value_User_Name}=${Siebel_Default_Username}
    Wait Until Element Is Visible   ${Path_KOLEA_Sign_On_Username}                      ${Wait_02_Sec}
    Input Text                      ${Path_KOLEA_Sign_On_Username}                      ${Inp_Value_User_Name}

Enter Password
    [Arguments]                     ${Inp_Value_Password}=${Siebel_Default_Password}
    Input Text                      ${Path_Password_Field}                              ${Inp_Value_Password}

Enter Case Name
    [Arguments]                     ${Inp_Case_Name}
    Input Text                      ${Path_Case_Name}                                   ${Inp_Case_Name}

Enter Primary Contact Information
    [Arguments]     @{varargs}
    Log Many     @{varargs}
    Log Many     ${varargs}
    ${Random_First_Name}=   Get Random First Name
    ${Random_Last_Name}=    Get Random Last Name
    ${Random_Middle_Name}=  Get Random Middle Initial
    Log      ${Random_First_Name}
    ${Inp_First_Name} =     Pop From Dictionary    @{varargs}    First_Name     ${Random_First_Name}
    ${Inp_Last_Name} =      Pop From Dictionary    @{varargs}    Last_Name      ${Random_Last_Name}
    ${Inp_Middle_Name} =    Pop From Dictionary    @{varargs}    Middle_Name    ${Random_Middle_Name}

    ${dict} =    Create Dictionary    ${Value_First_Name}=${Inp_First_Name}
    Set To Dictionary       ${dict}     ${Value_Middle_Name}        ${Inp_Middle_Name}
    Set To Dictionary       ${dict}     ${Value_Last_Name}          ${Inp_Last_Name}
    Enter Primary Contact Name  ${dict}

Enter Primary Contact Name
    [Arguments]         ${Primary_Name}
    ${Primary_First_Name}=      Get From Dictionary     ${Primary_Name}     ${Value_First_Name}
    ${Primary_Middle_Name}=     Get From Dictionary     ${Primary_Name}     ${Value_Middle_Name}
    ${Primary_Last_Name}=       Get From Dictionary     ${Primary_Name}     ${Value_Last_Name}
    Enter Primary Contact First Name    ${Primary_First_Name}
    Enter Primary Contact Middle Name   ${Primary_Middle_Name}
    Enter Primary Contact Last Name     ${Primary_Last_Name}
    Enter Primary Contact Name Suffix

Enter Primary Contact First Name
    [Arguments]                 ${Inp_First_Name}=Default
    Enter Given First Name      ${Inp_First_Name}

Enter Given First Name
    [Arguments]     ${Inp_First_Name}
    Input Text  ${Path_SBL_New_App_First_Name}      ${Inp_First_Name}

Enter Primary Contact Middle Name
    [Arguments]                 ${Random_Mid_Initial}=Default
    Input Text  ${Path_SBL_New_App_Mid_Initial}     ${Random_Mid_Initial}

Enter Primary Contact Last Name
    [Arguments]                 ${Random_Last_Name}=Default
    Input Text  ${Path_SBL_New_App_Last_Name}          ${Random_Last_Name}

Enter Primary Contact Name Suffix
    [Arguments]                 ${Suffixes}=Default
    ${Suffixes}=    Get List Items      ${Path_SBL_New_App_Suffix}
    Select Random From List  ${Path_SBL_New_App_Suffix}     ${Suffixes}


Select Random From List
    [Arguments]     ${Inp_Path}     ${Inp_List}
    ${Choice}=      Get Random Selection From List  ${Inp_List}
    Select From List By Index   ${Inp_Path}     ${Choice}


Search for KOLEA Analytics

    Wait Until Element Is Visible   ${Path_SiteMap_Filter_Input}
    Sleep In Seconds                5
    input text                      ${Path_SiteMap_Filter_Input}                        ${Value_KOLEA_Analytics}
    press key                       ${Path_SiteMap_Filter_Input}                       \\13
    #Wait For Search Results

From Side Bar Select
    [Arguments]         ${Menu_Selector}
    ${Path_Dynamic}=    catenate    ${Path_SideBar_Prefix}${Menu_Selector}${Path_Suffix}
    Log                 ${Path_Dynamic}
    click link          ${Path_Dynamic}
    #Run Keyword if      '${Menu_Selector}' == '${Value_Cases}'        Wait For Case Search To Appear
    Wait Till The Search Button Appears

Access Change Of Circumstance Deductions
    Wait For Case Menu To Load
    Wait Till The Search Button Appears
    Click On Change Of Circumstance
    Wait Till The Search Button Appears
    Wait Until Element Is Visible   ${Path_Change_Of_Circumstance}  ${Wait_20_Sec}
    mouse over          ${Path_Change_Of_Circumstance}
    Wait Until Element Is Visible   ${Path_Sub_Menu_Deductions}      ${Wait_20_Sec}
    click element       ${Path_Sub_Menu_Deductions}

Add Deduction
    [Arguments]         @{List_Deduction_Details}
    ${Inp_Deduction_Type}=          Get From List   ${List_Deduction_Details}   0
    ${Inp_Deduction_Amount}=        Get From List   ${List_Deduction_Details}   1

    Click New               Deductions
    wait until element is visible  //div[@id='s_vctrl_div']//following::input[@name='Source']   10
    input text    //div[@id='s_vctrl_div']//following::input[@name='Source']  ${Inp_Deduction_Type}
    PRESS KEY  //div[@id='s_vctrl_div']//following::input[@name='Source']   \\9
    press key   //div[@id='s_vctrl_div']//following::input[@name='Amount']  ${Inp_Deduction_Amount}
    press key  //div[@id='s_vctrl_div']//following::input[@name='Amount']   \\13


########################################################################################################################
###################################                 CLICKS                            ##################################
########################################################################################################################

Click on the result
    click element                   ${Path_Search_Result}

Click On Menu DashBoard
    Wait for iframe
    Select iframe
    wait until element is visible   ${Path_Dashboard}                               ${Wait_20_Sec}
    click element                   ${Path_Dashboard}

Click On CRM Reports
    Wait For CRM Reports Link
    Click CRM Reports

Click CRM Reports
    Click Element  //html/body/div[3]/div[2]/div/div[3]/div[4]/div


Click Continue
    Click Element                   ${Path_Signon_Page_Continue_button}
    Wait For Password Page

Click Button Go
    Click Button                    ${Path_Search_Go}
    Wait For Case Search Results
    #Wait Until Element Is Visible  //a[@class='drilldown']  100

Click Enter To Login KOLEA
    Click Enter                     ${Path_Password_Device_Enter}
    Wait For Logging In

Click On First Case Search Result
    Click Link                      ${Path_First_Case_Search_Result}
    Wait Till The Search Button Appears

Click On Change Of Circumstance
    Click Link                      ${Path_Change_Of_Circumstance}
    Wait Till The Search Button Appears

Click New
	[Arguments]	    ${Path_Applet_Name}
	${Path_Dynamic}		catenate    ${Path_Plus_Sign_Prefix}${Path_Applet_Name}${Path_Plus_Sign_Suffix}
	Wait Until Element Is Visible   ${Path_Dynamic}     ${Wait_10_Sec}
	click element       ${Path_Dynamic}

Click On Button
    [Arguments]     ${Inp_Button_Title}
    ${Path_Dynamic}=    catenate  ${Path_Button_Prefix}${Inp_Button_Title}${Path_Suffix}
    click button    ${Path_Dynamic}


########################################################################################################################
###################################                 WAITS                             ##################################
########################################################################################################################


Wait for Sing On Page
    Wait Until Element Is Visible   ${Path_KOLEA_Sign_On_Username}                  ${Wait_02_Sec}

Wait For Password Page
    Wait Until Element Is Visible   ${Path_Password_Field}                          ${Wait_02_Sec}

Wait for Logging In
    Wait Until Element Is Visible   ${Path_Salute_My_Home}                          ${Wait_100_Sec}

Wait For Site Map Page
    Wait Until Element Is Visible   ${Path_SiteMap_Filter_Input}                    ${Wait_20_Sec}

Wait For Search Results
    Wait Until Element Is Visible   ${Path_Search_Result}                           ${Wait_02_Sec}

Wait For Case Search Results
    Wait Until Element Is Visible   ${Path_Case_Search_Result}                      ${Wait_20_Sec}


Wait For CRM Reports Link
    Wait Until Element Is Visible   ${Path_CRM_Reports_Link}                        ${Wait_02_Sec}

Wait For Case Search To Appear
    Wait Until Element Is Visible   ${Path_Case_Search_Go_Button}                   ${Wait_20_Sec}

Wait For Case Menu To Load
    Wait Until Element Is Visible   ${Path_Change_Of_Circumstance}                   ${Wait_20_Sec}

Wait Till The Search Button Appears
    Wait Until Element Is Enabled       ${Path_Search_Button}                       ${Wait_10_Sec}

Wait For Application Date
    Wait Until Element Is Visible   ${Path_SBL_New_App_Create_Date}                   ${Wait_20_Sec}