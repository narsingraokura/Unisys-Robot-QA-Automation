*** Settings ***
Resource    KOLEA_Key_Words.robot    
Resource    LifeRay_Key_Words.robot

*** Test Cases ***
ReviewAndDeclareFile
   Open Browser                 ${URL_Review_Declare}                       ${BROWSER_Chrome}
   Maximize window
   Click Element                ${Path_LFR_RS_Yes_Rnew_Elig_Nxt}
   Select From List By Index    ${Path_LFR_RS_Yes_Rnew_Elig_Nxt}            5
   Click Element                ${Path_LFR_RS_Does_Parnt_livng_Out_Hme_No}
   Click Element                ${Path_LFR_RS_Agree_T_C}
   Input Text                   ${Path_LFR_RS_Sign_Prim_App_FName}          ${Random_First_Name}
   Input Text                   ${Path_LFR_RS_Sign_Prim_App_LName}          ${Random_Last_Name} 
   Click Element                ${Path_LFR_RS_Save_Exit_Btn}
   Click Element                ${Path_LFR_RS_Back_Btn}           
   

