*** Settings ***
Resource    KOLEA_Key_Words.robot    
Resource    LifeRay_Key_Words.robot
#Resource    LifeRay_Primary_Applicant_Details.robot
   
   

*** Test Cases ***
HouseholdDetails
    ${SSN}            Ssn
    ${Text}           Text
    ${Word}           Word
    ${Inp_User_Name}   catenate    ${Random_First_Name} ${Random_Last_Name} ${Random_Middle_Initial}
    ${Random_Number}    Random Number
    ${Alien_Number}           Random Alien Number
    ${Passport_Number}        Random Passport Number
    ${Int_Number}             Int Number
    ${Number}                 Random Int
    ${Income}                 Random Income
    ${Country}                Country
    ${Phone_Number}           Phone Number
    ${Address}                Address
    ${Street_Address}         Street Address
    ${Apartment_Number}       Building Number
    ${City}                   City
    ${Zip_Code}               Postcode
    
    
    Open Browser                 ${URL_HHDETAILS}           ${BROWSER_Chrome}
    Maximize window
    
    Click Element                ${Path_LFRY_HHD_Add_Person}
    Input Text                   ${Path_LFRY_HHD_First_Name_P2}        ${Random_First_Name}
    Input Text                   ${Path_LFRY_HHD_Middle_Name_P2}       ${Random_Middle_Initial}
    Input Text                   ${Path_LFRY_HHD_Last_Name_P2}         ${Random_Last_Name}
    Click Element                ${Path_LFRY_Suffix_P2}
    Select From List By Index    ${Path_LFRY_Suffix_P2}                4
    
    Click Element                ${Path_LFRY_HHD_Relation_Of_P2}
    Select From List By Index    ${Path_LFRY_HHD_Relation_Of_P2}       1
    Input Text                   ${Path_LFRY_HH_Date_Of_Birth_P2}      ${Today_mm_dd_ccyy}
    Click Element                ${Path_LFRY_Gender_P2}
    Select From List By Index    ${Path_LFRY_Gender_P2}                2
    
    Input Text                   ${Path_LFRY_Name_Of_Spouse_P2}         ${Random_First_Name}
    Input Text                   ${Path_LFRY_SSN_P2}                    ${SSN}
    
    Click Element                                ${Path_LFRY_HHD_Does_P2_Live_At_Same_Address}
    Select From List By Index                    ${Path_LFRY_HHD_Does_P2_Live_At_Same_Address}                             1
    Input Text                                   ${Path_LFRY_HHD_P2_Lives_Different_Address_Home_Line_1}                   ${Street_Address} 
    Input Text                                   ${Path_LFRY_HHD_P2_Lives_Different_Address_Home_Apartment}                ${Apartment_Number}
    Input Text                                   ${Path_LFRY_HHD_P2_Lives_Different_Address_Home_City_Name}                ${City}
    Click Element                                ${Path_LFRY_HHD_P2_Lives_Different_Address_State }
    Select from List By Index                    ${Path_LFRY_HHD_P2_Lives_Different_Address_State }                       0
    Input Text                                   ${Path_LFRY_HHD_P2_Lives_Different_Address_ZipCode }                     ${Zip_Code}
    Click Element                                ${Path_LFRY_HHD_P2_Lives_Different_Address_County }
    Select From List By Index                    ${Path_LFRY_HHD_P2_Lives_Different_Address_County }                      1
    
    Click Element                                ${Path_LFRY_HHD_P2_Plan_Income_Tax_Next_Yr}
    Select From List By Index                    ${Path_LFRY_HHD_P2_Plan_Income_Tax_Next_Yr}                              1
    
    Click Element                                ${Path_LFRY_HHD_P2_File_Jointly_With_Spouse}
    Select From List By Index                    ${Path_LFRY_HHD_P2_File_Jointly_With_Spouse}                             1
    Input Text                                   ${Path_LFRY_HHD_P2_File_Jointly_With_Spouse_Yes_First_Name}              ${Random_First_Name}
    Input Text                                   ${Path_LFRY_HHD_P2_File_Jointly_With_Spouse_Yes_Middle_Name}             ${Random_Middle_Initial}
    Input Text                                   ${Path_LFRY_HHD_P2_File_Jointly_With_Spouse_Yes_Last_Name}               ${Random_Last_Name}
    
    
    Click Element                                ${Path_LFRY_HHD_P2_File_Jointly_With_Spouse_Yes_Claim_dpndnts_On_Tax_Rtrn}
    Select From List By Index                    ${Path_LFRY_HHD_P2_File_Jointly_With_Spouse_Yes_Claim_dpndnts_On_Tax_Rtrn}                                             1
    Input Text                                   ${Path_LFRY_HHD_P2_File_Jntly_With_Spse_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_Frst_Nam}                                         ${Random_First_Name}
    Input Text                                   ${Path_LFRY_HHD_P2_Fle_Jntly_Wth_Spse_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_Mddle_Nam}                                          ${Random_Middle_Initial}
    Input text                                   ${Path_LFRY_HHD_P2_Fle_Jntly_Wth_Spse_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_Lst_Name}                                           ${Random_Last_Name}
    
    Input Text                                   ${Path_LFRY_HHD_P2_Lives_Different_Mlng_Address_Line_1}                                                                ${Street_Address}
    Input Text                                   ${Path_LFRY_HHD_P2_Lives_Different_Mlng_Address_Apartment}                                                             ${Apartment_Number}
    Input Text                                   ${Path_LFRY_HHD_P2_Lives_Different_Mlng_Address_City_Name}                                                             ${City}
    Click Element                                ${Path_LFRY_HHD_P2_Lives_Different_Mlng_Address_State}
    Select From List By Index                    ${Path_LFRY_HHD_P2_Lives_Different_Mlng_Address_State}                                                                 1
    Input Text                                   ${Path_LFRY_HHD_P2_Lives_Different_Mlng_Address_ZipCode}                                                               ${Zip_Code}
    Click Element                                ${Path_LFRY_HHD_P2_Lives_Different_Mlng_Address_County}
    Select From List By Index                    ${Path_LFRY_HHD_P2_Lives_Different_Mlng_Address_County}                                                                1
    Click Element                                ${Path_LFRY_HHD_P2_Fle_Jntly_WSps_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_ADpndnt}        
    Input Text                                   ${Path_LFRY_HHD_P2_Fle_Jntly_WSps_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_ADpndnt_Fst_Nam}                                        ${Random_First_Name}
    Input Text                                   ${Path_LFRY_HHD_P2_Fle_Jntly_WSps_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_ADpndnt_Mdl_Nam}                                        ${Random_Middle_Initial}
    Input Text                                   ${Path_LFRY_HHD_P2_Fle_Jntly_WSps_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_ADpndnt_Lst_Nam}                                        ${Random_Last_Name}
    #Click Element                                ${Path_LFRY_HHD_P2_Fle_Jntly_WSps_Ys_Clm_dpndnts_On_Tx_Rtrn_Ys_ADpndnt_Remove}
    
    Click Element                                ${Path_LFRY_HHD_P2_Be_Claimed_As_Dependent_On_Someone_Tax_Return }
    Select from List By Index                    ${Path_LFRY_HHD_P2_Be_Claimed_As_Dependent_On_Someone_Tax_Return }                                                     1
    
    Input Text                                   ${Path_LFRY_HHD_P2_Be_Clmd_As_Dpndnt_On_Someone_Tax_Rtrn_Tax_Filer_First_Name}                                         ${Random_First_Name}
    Input Text                                   ${Path_LFRY_HHD_P2_Be_Clmd_As_Dpndnt_On_Someone_Tax_Rtrn_Tax_Filer_Mddle_Name}                                         ${Random_Middle_Initial}
    Input Text                                   ${Path_LFRY_HHD_P2_Be_Clmd_As_Dpndnt_On_Someone_Tax_Rtrn_Tax_Filer_Last_Name}                                          ${Random_Last_Name}
    
    Click element                                ${Path_LFRY_HHD_P2_Be_Claimed_As_Dependent_Not_Part_Of_Household}                    
    Click Element                                ${Path_LFRY_HHD_P2_B_Clmd_As_Dpndnt_Nt_Part_Of_Hhold_And_Hw_Rltd_To_Tax_Filr}          
    Select from List By Index                    ${Path_LFRY_HHD_P2_B_Clmd_As_Dpndnt_Nt_Part_Of_Hhold_And_Hw_Rltd_To_Tax_Filr}                                          1
    
    #Sleep                                        2
    # Click Element                                ${Path_LFRY_HHD_Is_P2_Pregnant}  
    # Select From List By Index                    ${Path_LFRY_HHD_Is_P2_Pregnant}                                                                                       1                               
    # Click Element                                ${Path_LFRY_HHD_Is_P2_Pregnant_Yes_Hw_Mny_Babies_Are_Expctd_Durng_Prgnancy}            
    # Select From List By Index                    ${Path_LFRY_HHD_Is_P2_Pregnant_Yes_Hw_Mny_Babies_Are_Expctd_Durng_Prgnancy}                                           1
    # Sleep                                                                                                                                                              2
    # Input text                                   ${Path_LFRY_HHD_Is_P2_Pregnant_Yes_Expected_Due_Date}                                                                 ${Today_mm_dd_ccyy}
    
    Click Element                                ${Path_LFRY_HHD_P2_Needs_Health_Coverage_Yes}                                    
    Click Element                                ${Path_LFRY_HHD_P2_Have_Disability_Last_More_Than_Twelve_Months}                
    Select From List By Index                    ${Path_LFRY_HHD_P2_Have_Disability_Last_More_Than_Twelve_Months}                                                       1
    
    Click Element                                ${Path_LFRY_HHD_P2_Hv_Dsblty_Lst_Mre_Thn_Twlv_Mnths_Ys_Crntly_Rcv_LTrm_CSrvcs}
    Select From List By Index                    ${Path_LFRY_HHD_P2_Hv_Dsblty_Lst_Mre_Thn_Twlv_Mnths_Ys_Crntly_Rcv_LTrm_CSrvcs}                                         1 
    
    Click Element                                ${Path_LFRY_HHD_P2_Received_LTerm_Care_Nursing_Services_In_Three_Months}
    Select From List By Index                    ${Path_LFRY_HHD_P2_Received_LTerm_Care_Nursing_Services_In_Three_Months}                                               1          
    Input Text                                   ${Path_LFRY_HHD_P2_Received_LTerm_Care_Nursing_Services_In_Three_Months_Ys_Frm}                                        ${Today_mm_dd_ccyy} 
    Input text                                   ${Path_LFRY_HHD_P2_Received_LTerm_Care_Nursing_Services_In_Three_Months_Yes_To}                                        ${Today_mm_dd_ccyy}
    
    Click Element                                ${Path_LFRY_HHD_P2_Think_Need_LTerm_Care_Nursing_Services_Now}
    Select From List By Index                    ${Path_LFRY_HHD_P2_Think_Need_LTerm_Care_Nursing_Services_Now}                                                         1
    Click Element                                ${Path_LFRY_HHD_P2_Receive_SSI}
    Select From List By Index                    ${Path_LFRY_HHD_P2_Receive_SSI}                                                                                        1
   
    Click Element                                ${Path_LFRY_HHD_P2_Receive_Any_Medical_Srvcs_In_Ten_Clndr_Dys_Imdtly_Prir_To} 
    Select From List By Index                    ${Path_LFRY_HHD_P2_Receive_Any_Medical_Srvcs_In_Ten_Clndr_Dys_Imdtly_Prir_To}                                          1
    Input Text                                   ${Path_LFRY_HHD_P2_Rcv_Any_Mdcl_Srvcs_In_Ten_Clndr_Dys_Imdtly_Prir_To_Ys_Frm}                                          ${Today_mm_dd_ccyy}  
    Input Text                                   ${Path_LFRY_HHD_P2_Rcv_Any_Mdcl_Srvcs_In_Ten_Clndr_Dys_Imdtly_Prir_To_Ys_To}                                           ${Today_mm_dd_ccyy}  
    
    Click Element                                ${Path_LFRY_HHD_P2_US_Citizen_Or_National}
    Select from List By Index                    ${Path_LFRY_HHD_P2_US_Citizen_Or_National}                                                                             2      
    Click Element                                ${Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Has_Elgbl_Imgrtn}
    Select From List By Index                    ${Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Has_Elgbl_Imgrtn}                                                    1
   
   Click Element                                 ${Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Has_Elgbl_Imgrtn_Ys _Doc}
   Select from List By Index                     ${Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Has_Elgbl_Imgrtn_Ys_Doc}                                             18
   Input Text                                    ${Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Has_Elgbl_Imgrtn_Ys_SType}                                           ${Word}
   Input Text                                    ${Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Ntnl_Has_Elgbl_Imgrtn_Ys_NAs_On_Imgrtn_Dc}                                         ${Inp_User_Name}
   
   Input Text                                    ${Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Hs_Elgbl_Imgrtn_Ys_Doc_Vsan}                                         ${Alien_Number}
   Input Text                                    ${Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Hs_Elgbl_Imgrtn_Ys_Doc_Vsain}                                        ${Int_Number}
   Input Text                                    ${Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Hs_Elgbl_Imgrtn_Ys_Doc_Vsapn}                                        ${Passport_Number}
   Sleep                                         2                                                                                                                               
   Input Text                                    ${Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Hs_Elgbl_Imgrtn_Ys_Doc_PEdt}                                         ${Today_mm_dd_ccyy}
   Input Text                                    ${Path_LFRY_HHD_If_P2_Is_Nt_US_Ctzn_Or_Nt_US_Ntnl_Hs_Elgbl_Imgrtn_Ys_Doc_ODoc}                                         ${Random_Number}
   
   Input Text                                    ${Path_LFRY_HHD_If_P2_Date_Of_Entry_To_US_On_Immigration_Doc_Listed}                                                   ${Today_mm_dd_ccyy}
   Click Element                                 ${Path_LFRY_HHD_Is_P2_Ctzn_Of_Fdrtd_Stats_Of_Micrnsia_Rpblc_Of_Mrshl_Islnds_Ys}        
   Click Element                                 ${Path_LFRY_HHD_Is_P2_Citizenship_On_Immigrated_Doc_Listed}                            
   Select From List By Index                     ${Path_LFRY_HHD_Is_P2_Citizenship_On_Immigrated_Doc_Listed}                                                            1
   Select From List By Index                     ${Path_LFRY_HHD_Is_P2_Citizenship_On_Immigrated_Doc_Listed}                                                            2
   Select From List By Index                     ${Path_LFRY_HHD_Is_P2_Citizenship_On_Immigrated_Doc_Listed}                                                            3
   
   Click Element                                 ${Path_LFRY_HHD_Is_P2_Or_Their_Spse_Prnt_A_Vtrn_Or_Actv_Duty_Mmbr_Of_US_Mltry}
   Select From List By Index                     ${Path_LFRY_HHD_Is_P2_Or_Their_Spse_Prnt_A_Vtrn_Or_Actv_Duty_Mmbr_Of_US_Mltry}                                         1
   
   Click Element                                 ${Path_LFRY_HHD_P2_In_Foster_Care_At_Age_Eighteen_Or_Older_In_Hawaii}
   Select From List By Index                     ${Path_LFRY_HHD_P2_In_Foster_Care_At_Age_Eighteen_Or_Older_In_Hawaii}                                                  2
   
   Click Element                                 ${Path_LFRY_HHD_Is_P2_Full_Time_Student}
   Select From List By Index                     ${Path_LFRY_HHD_Is_P2_Full_Time_Student}                                                                               2
   Element Text Should Be                        ${Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity}                                                                       18. If Hispanic/Latino, ethnicity (OPTIONAL - check all that apply.) 
   
   Click Element                                 ${Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity_Chicano}                              
   Click Element                                 ${Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity_Mexican_American}                    
   Click Element                                 ${Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity_Other}                              
   Input Text                                    ${Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity_Other_Country}                                                         ${Country}
   Click Element                                 ${Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity_Cuban}                             
   Click Element                                 ${Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity_Puerto_Rican}                     
   Click Element                                 ${Path_LFRY_HHD_P2_If_Hispanic_Latino_Ethnicity_Mexican} 
   
   Element Text Should Be                        ${Path_LFRY_HHD_P2_Race}                                                                                               19. Race (OPTIONAL-check all that apply.)
   Click Element                                 ${Path_LFRY_HHD_P2_Race_American_Indian_Or_Alaskan}                                     
   Click Element                                 ${Path_LFRY_HHD_P2_Race_Chinese}                                                       
   Click Element                                 ${Path_LFRY_HHD_P2_Race_Japanese}                                                     
   Click Element                                 ${Path_LFRY_HHD_P2_Race_Other_Asian}                                                 
   Click Element                                 ${Path_LFRY_HHD_P2_Race_Vietnamese}                                                 
   Click Element                                 ${Path_LFRY_HHD_P2_Race_Other}                                                     
   Input Text                                    ${Path_LFRY_HHD_P2_Race_Other_Country}                                                                                  ${Country}                                           

   Click Element                                 ${Path_LFRY_HHD_P2_Race_Asian_Indian}                                            
   Click Element                                 ${Path_LFRY_HHD_P2_Race_Filipino}                                               
   Click Element                                 ${Path_LFRY_HHD_P2_Race_Korean}                                                
   Click Element                                 ${Path_LFRY_HHD_P2_Race_Other_Pacific_Islander}                               
   Click Element                                 ${Path_LFRY_HHD_P2_Race_White}                                               

   Click Element                                 ${Path_LFRY_HHD_P2_Race_Black_Or_African_American}                         
   Click Element                                 ${Path_LFRY_HHD_P2_Race_Guamanian_Or_Chamorro}                            
   Click Element                                 ${Path_LFRY_HHD_P2_Race_Native_Hawaiian}                                 
   Click Element                                 ${Path_LFRY_HHD_P2_Race_Samoan}                                         
   
   Element Text Should Be                        ${Path_LFRY_HHD_P2_Current_Job_Income_Info}                                                                             Current Job & Income Information
   Element Text Should Be                        ${Path_LFRY_HHD_P2_Type_Of_Employment_Title}                                                                            Type of Employment*
   
   
   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed}                             
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Name} 		                                                         ${Random_First_Name}
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Phone} 		                                                         ${Phone_Number}
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Address_L1}	                                                         ${Street_Address}

   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Apartment_Number} 	                                                 ${Apartment_Number}
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_City} 	                                                             ${City}

   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_State} 		            
   Select From List By Index                     ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_State}                                                               0
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Zip_Code} 	                                                         ${Zip_Code}

   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Wages_Tips} 		                                                 ${Random_Number}
   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Wages_How_Often} 	
   Select From List By Index                     ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Wages_How_Often}                                                     1
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Wgs_HOften_Dly_Nodw} 		                                         3
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Wages_Income_Start_Date} 	                                         ${Today_mm_dd_ccyy}
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Emp_Wages_Income_End_Date} 	                                             ${Today_mm_dd_ccyy}
   
   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs}                   
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Name}                                                   ${Random_First_Name}
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Phone}                                                  ${Phone_Number}   
   
   Input text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Address_Line_1} 	                                     ${Street_Address}
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_suite_number} 	                                         ${Apartment_Number}

   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_City}        	                                         ${City}
   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_State}          	
   Select From List By Index                     ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_State}                                                  1
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Zip_Code}                                               ${Zip_Code}
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Wages}                                                  ${Random_Number}

   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Wges_Hw_Oftn}
   Select From List By Index                     ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Wges_Hw_Oftn}                                           1
   Input text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_ANew_Jbs_EWges_HOftn_Dnodw}                                              4
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Wges_Strt_Date}                                         ${Today_mm_dd_ccyy}
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Emp_Wges_End_Date}                                          ${Today_mm_dd_ccyy}
   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_Add_New_Jobs_Remove}
   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_In_The_Past_Year_Did_P2}
   Select From List By Index                     ${Path_LFRY_HHD_P2_Type_Of_Employment_Employed_In_The_Past_Year_Did_P2}                                                 1
   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Self_Employed}                                       
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Self_Employed_Type_Of_Work}                                                       ${Word}
   Input Text                                    ${Path_LFRY_HHD_P2_Tpe_Of_Emplmnt_Slf_Emply_Tpe_Of_Wrk_Hw_Mch_Nt_Incm_Yu_Gt_Pd}                                         ${Random_Number}
   
   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Not_Employed}
   
   Element Text Should Be                        ${Path_LFRY_HHD_P2_Type_Of_Employment_Other_Income_This_Month}                                                          OTHER INCOME THIS MONTH
   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Other_Income_This_Month_Income_Type}
   Select From List By Index                     ${Path_LFRY_HHD_P2_Type_Of_Employment_Other_Income_This_Month_Income_Type}                                              1
   
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Other_Income_This_Month_Income_Amount}                                            ${Income}   
   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Other_Income_This_Mnth_Incm_Amnt_Hw_Oftn} 
   Select From List By Index                     ${Path_LFRY_HHD_P2_Type_Of_Employment_Other_Income_This_Mnth_Incm_Amnt_Hw_Oftn}                                         3      
   Input Text                                    ${Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_This_Mnth_Incm_Avg_Hrs_Wkd_EWeek}                                         ${Number}
   Input Text                                    ${Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_This_Mnth_Incme_Strt_Date}                                                ${Today_mm_dd_ccyy}
   Input Text                                    ${Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_This_Mnth_Incme_End_Date}                                                 ${Today_mm_dd_ccyy}
   
   Click Element                                 ${Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_More_Income_Types}
   Click Element                                 ${Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_More_Income_Types_Othr_Incme}            
   Select From List By Index                     ${Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_More_Income_Types_Othr_Incme}                                         3
    
   Input text                                    ${Path_LFRY_HHD_P2_Tpe_Of_Emplmnt_Othr_Incm_Add_Mre_Incm_Typ_Typ_Amnt}                                                  ${Income}                    
   Click Element                                 ${Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_Mre_Incm_Typs_How_Often}                            
   Select from List By Index                     ${Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_Mre_Incm_Typs_How_Often}                                              1
   Input Text                                    ${Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_Mre_Incm_Typs_NDys_Wkd_EWeek}                                         ${Number}    
   Input Text                                    ${Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_Mre_Incm_Typs_Incme_Strt_Dte}                                         ${Today_mm_dd_ccyy}   
   Input Text                                    ${Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_Mre_Incm_Typs_Incme_End_Dte}                                          ${Today_mm_dd_ccyy}
   #Click Element                                 ${Path_LFRY_HHD_P2_Tpe_Of_Emplymnt_Othr_Incme_Add_Mre_Incm_Remove}                           
   
   
   Element Text Should be                        ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_label}                                                                 DEDUCTIONS
   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Type_Of_Dductn}              
   Select From List By Index                     ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Type_Of_Dductn}                                                        1 
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Amount}                                                                ${Income}
   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Amount_How_Often}
   Select From List By Index                     ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Amount_How_Often}                                                      1
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Deduction_Start_Date}                                                  ${Today_mm_dd_ccyy}
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Deduction_End_Date}                                                    ${Today_mm_dd_ccyy}
   
   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions}                             
   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions_TDduction}                   
   Select From List By Index                     ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions_TDduction}                                               1
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions_Amount}                                                  ${Income}
   Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions_Hw_Oftn}                  
   Select From List By Index                     ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions_Hw_Oftn}                                                 1
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions_Dductn_Strt_Date}                                        ${Today_mm_dd_ccyy}
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions_Dductn_End_Date}                                         ${Today_mm_dd_ccyy}

   #Click Element                                 ${Path_LFRY_HHD_P2_Type_Of_Employment_Deductions_Add_MDductions_Remove}
   
   
   Element Text Should Be                        ${Path_LFRY_HHD_P2_Type_Of_Employment_Yearly_Income_Title}                                                               YEARLY INCOME                                                                  
   Input text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Yearly_Income_Total_Income_This_Year}                                              ${Income}  
   Input Text                                    ${Path_LFRY_HHD_P2_Type_Of_Employment_Yearly_Income_Total_Income_Next_Year}                                              ${Income}
   #Click Element                                 ${Path_LFRY_HHD_P2_Remove_Person_1}                                                             
   #Click Element                                 ${Path_LFRY_HHD_P2_Add_Person_1}                                                                
   #Click Element                                 ${Path_LFRY_HHD_P2_Save_And_Exit}                                                               
   #Click Element                                 ${Path_LFRY_HHD_P2_Save_And_Back}                                                              
   #Click Element                                 ${Path_LFRY_HHD_P2_Save_And_Next}
  