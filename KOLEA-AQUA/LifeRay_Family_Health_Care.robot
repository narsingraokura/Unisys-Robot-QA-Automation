*** Settings ***
Resource    KOLEA_Key_Words.robot    
Resource    LifeRay_Key_Words.robot

   
   

*** Test Cases ***
FamilyHealthCare
    ${Policy_Name_P3}        Name
    ${Policy_Name_P4}        Name
    ${Policy_Name_P5}        Name
    ${Policy_Number_P3}      Random Policy Number
    ${Policy_Number_P4}      Random Policy Number
    ${Policy_Number_P5}      Random Policy Number
    
      
   Open Browser                   ${URL_FHC}          ${BROWSER_Chrome}
   Maximize window
    
   Select Checkbox                ${Path_LFRY_FHC_Yes_If_Yes_Answer_The_Follng_Que}
   Click Element                  ${Path_LFRY_FHC_Is_P3_Enrld_In_Hlth_Cvrg_Now_If_Yes}
   Click Element                  ${Path_LFRY_FHC_P3_Type_Of_Coverage} 
   Select From List By Index      ${Path_LFRY_FHC_P3_Type_Of_Coverage}                                                1
   Input Text                     ${Path_LFRY_FHC_P3_Policy_Name}                                                     ${Policy_Name_P3}
   Input Text                     ${Path_LFRY_FHC_P3_Policy_Number}                                                   ${Policy_Number_P3}        
   Input Text                     ${Path_LFRY_FHC_P3_Policy_Start_Date}                                               ${Today_mm_dd_ccyy}
   Input Text                     ${Path_LFRY_FHC_P3_Policy_End_Date}                                                 ${Today_mm_dd_ccyy}
   Click Element                  ${Path_LFRY_FHC_P3_Includes_Medical_Care_If_Yes}     
   Click Element                  ${Path_LFRY_FHC_P3_Includes_Dental_Care_If_Yes}    
   Click Element                  ${Path_LFRY_FHC_P3_Includes_Vision_Care_If_Yes}     
   Click Element                  ${Path_LFRY_FHC_P3_Is_This_A_Limited_Benefit_Plan_If_Yes}
    
   
   Click Element                   ${Path_LFRY_FHC_P3_Add_Coverage} 
   Click Element                   ${Path_LFRY_FHC_P3_Add_Coverage_Type_Of_Coverage}
   Select From List By Index       ${Path_LFRY_FHC_P3_Add_Coverage_Type_Of_Coverage}                                   1
   Input Text                      ${Path_LFRY_FHC_P3_Add_Coverage_Policy_Name}                                        ${Policy_Name_P3}
   Input Text                      ${Path_LFRY_FHC_P3_Add_Coverage_Policy_Number}                                      ${Policy_Number_P3}
   Input Text                      ${Path_LFRY_FHC_P3_Add_Coverage_Policy_Start_Date}                                  ${Today_mm_dd_ccyy}
   Input Text                      ${Path_LFRY_FHC_P3_Add_Coverage_Policy_End_Date}                                    ${Today_mm_dd_ccyy}     
   Click Element                   ${Path_LFRY_FHC_P3_Add_Coverage_Includes_Medical_Care_If_Yes} 
   Click Element                   ${Path_LFRY_FHC_P3_Add_Coverage_Includes_Dental_Care_If_Yes}
   Click Element                   ${Path_LFRY_FHC_P3_Add_Coverage_Includes_Vision_Care_If_Yes}
   Click Element                   ${Path_LFRY_FHC_P3_Add_Coverage_Is_This_A_Limited_Benefit_Plan_If_Yes} 
   # Click Element                 ${Path_LFRY_P3_FHC_Remove_Coverage}                   
   
   Click Element                    ${Path_LFRY_FHC_Is_P4_Enrld_In_Hlth_Cvrg_Now_If_Yes}
   Click Element                    ${Path_LFRY_FHC_P4_Type_Of_Coverage}
   Select From List By Index        ${Path_LFRY_FHC_P4_Type_Of_Coverage}                                               3
   Input Text                       ${Path_LFRY_FHC_P4_Policy_Name}                                                    ${Policy_Name_P4}
   Input Text                       ${Path_LFRY_FHC_P4_Policy_Number}                                                  ${Policy_Number_P4}
   Input Text                       ${Path_LFRY_FHC_P4_Policy_Start_Date}                                              ${Today_mm_dd_ccyy}
   Input Text                       ${Path_LFRY_FHC_P4_Policy_End_Date}                                                ${Today_mm_dd_ccyy}
   Click Element                    ${Path_LFRY_FHC_P4_Includes_Medical_Care_If_Yes}
   Click Element                    ${Path_LFRY_FHC_P4_Includes_Dental_Care_If_Yes}
   Click Element                    ${Path_LFRY_FHC_P4_Includes_Vision_Care_If_Yes}
   Click Element                    ${Path_LFRY_FHC_P4_Is_This_A_Limited_Benefit_Plan_If_Yes}
   
   Click Element                     ${Path_LFRY_FHC_P4_Add_Coverage}
   #Click Element                     ${Path_LFRY_FHC_P4_Add_Coverage_Type_Of_Coverage} 
   Select From List By Index         ${Path_LFRY_FHC_P4_Add_Coverage_Type_Of_Coverage}                                 1
   Input Text                        ${Path_LFRY_FHC_P4_Add_Coverage_Policy_Name}                                      ${Policy_Name_P4}
   Input Text                        ${Path_LFRY_FHC_P4_Add_Coverage_Policy_Number }                                   ${Policy_Number_P4}
   Input Text                        ${Path_LFRY_FHC_P4_Add_Coverage_Policy_Start_Date }                               ${Today_mm_dd_ccyy}
   Input Text                        ${Path_LFRY_FHC_P4_Add_Coverage_Policy_End_Date}                                  ${Today_mm_dd_ccyy}
   Click Element                     ${Path_LFRY_FHC_P4_Add_Coverage_Includes_Medical_Care_If_Yes}
   Click Element                     ${Path_LFRY_FHC_P4_Add_Coverage_Includes_Dental_Care_If_Yes}
   Click Element                     ${Path_LFRY_FHC_P4_Add_Coverage_Includes_Vision_Care_If_Yes}
   Click Element                     ${Path_LFRY_FHC_P4_Add_Coverage_Is_This_A_Limited_Benefit_Plan_If_Yes}
   # Click Element                   ${Path_LFRY_P4_FHC_Remove_Coverage}
   
   Click Element                    ${Path_LFRY_FHC_Is_P5_Enrld_In_Hlth_Cvrg_Now_If_Yes}
   Click Element                    ${Path_LFRY_FHC_P5_Type_Of_Coverage} 
   Select From List By Index        ${Path_LFRY_FHC_P5_Type_Of_Coverage}                                                1
   Input Text                       ${Path_LFRY_FHC_P5_Policy_Name}                                                     ${Policy_Name_P5}
   Input Text                       ${Path_LFRY_FHC_P5_Policy_Number}                                                   ${Policy_Number_P5}
   Input Text                       ${Path_LFRY_FHC_P5_Policy_Start_Date}                                               ${Today_mm_dd_ccyy}
   Input Text                       ${Path_LFRY_FHC_P5_Policy_End_Date}                                                 ${Today_mm_dd_ccyy}
   Click Element                    ${Path_LFRY_FHC_P5_Includes_Medical_Care_If_Yes} 
   Click Element                    ${Path_LFRY_FHC_P5_Includes_Dental_Care_If_Yes} 
   Click Element                    ${Path_LFRY_FHC_P5_Includes_Vision_Care_If_Yes}
   Click Element                    ${Path_LFRY_FHC_P5_Is_This_A_Limited_Benefit_Plan_If_Yes} 
   
   Click Element                    ${Path_LFRY_FHC_P5_Add_Coverage}
   Click Element                    ${Path_LFRY_FHC_P5_Add_Coverage_Type_Of_Coverage}
   Select From List By Index        ${Path_LFRY_FHC_P5_Add_Coverage_Type_Of_Coverage}                                   1
   Input Text                       ${Path_LFRY_FHC_P5_Add_Coverage_Policy_Name}                                        ${Policy_Name_P5}
   Input Text                       ${Path_LFRY_FHC_P5_Add_Coverage_Policy_Number}                                      ${Policy_Number_P5}
   Input Text                       ${Path_LFRY_FHC_P5_Add_Coverage_Policy_Start_Date}                                  ${Today_mm_dd_ccyy} 
   Input Text                       ${Path_LFRY_FHC_P5_Add_Coverage_Policy_End_Date}                                    ${Today_mm_dd_ccyy}    
   Click Element                    ${Path_LFRY_FHC_P5_Add_Coverage_Includes_Medical_Care_If_Yes}
   Click Element                    ${Path_LFRY_FHC_P5_Add_Coverage_Includes_Dental_Care_If_Yes}
   Click Element                    ${Path_LFRY_FHC_P5_Add_Coverage_Includes_Vision_Care_If_Yes}                                                                        
   Click Element                    ${Path_LFRY_FHC_P5_Add_Coverage_Is_This_A_Limited_Benefit_Plan_If_Yes}
   #Click Element                   ${Path_LFRY_P5_FHC_Remove_Coverage}        
  
