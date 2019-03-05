*** Settings ***
Resource  KOLEA_Key_Words.robot
Resource  LifeRay_Key_Words.robot
Test Template       LifeRay Self Assessment

*** Test Cases ***                                  Want_Help   Any_ABD     Child_Count     Adult_Count     Babies      Income      Expected
LifeRay Self Assess No Help Single Person              N           Y           0               1               0           10000       Ineligible
LifeRay Self Asses Need Help LTC                       Y           Y           2               2               1           2000        Eligible
LifeRay Self Asses High Income                         Y           Y           0               1               0           10000       Ineligible


LifeRay App Intake
    [Documentation]     Life ray Application intake.
    ...                 Test driven way of reading from the excel sheet
    [Setup]             Open Home Page  ${Value_LifeRay}
    [Tags]              LifeRay     IDM_Test      App Intake    Excel

	Click Apply Now
	Enter Account Information
	Capture Screen
	[Teardown]  close browser



*** Keywords ***

LifeRay Self Assessment
    [Tags]  LifeRay     Smoke_Test      DataDriven
    [Arguments]         ${Want_Help}    ${Any_ABD}      ${Child_Count}  ${Adult_Count}   ${Babies_Count}  ${Income}    ${Expected}

    Open LifeRay Home Page
    Maximize Window
    Click Pre-Assessment
    Click Next
    Capture Screen
    Want Help Paying Health Insurance   ${Want_Help}
    Any Aged LTC blind or diabled       ${Any_ABD}
    Children Aged 18 Or Under           ${Child_Count}
    Adult Aged 19 or Over               ${Adult_Count}
    Babies Expected                     ${Babies_Count}
    Household monthly income            ${Income}
    Capture Screen
    Click Next
    Validate Result                     ${Expected}
    Capture Screen
    close browser
