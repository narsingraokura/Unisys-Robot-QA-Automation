*** Settings ***
Resource  KOLEA_Key_Words.robot
Resource  LifeRay_Key_Words.robot

*** Test Cases ***                                  Want_Help   Any_ABD     Child_Count     Adult_Count     Babies      Income      Expected

LifeRay App Intake
    [Documentation]     Life ray Application intake.
    ...                 Test driven way of reading from the excel sheet
    [Setup]             Open Home Page  ${Value_LifeRay}
    [Tags]              LifeRay     IDM_Test      App Intake    Excel
	Click Apply Now
	${LifeRay_New_User}=    Enter Account Information
	Log    ${LifeRay_New_User}
	Write LifeRay Account Details To Excel    ${LifeRay_New_User}        
	Capture Screen
	[Teardown]  Close Browser