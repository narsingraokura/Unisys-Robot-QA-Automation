*** Settings ***
Resource    KOLEA_Key_Words.robot    
Resource    LifeRay_Key_Words.robot

*** Test Cases ***
PrimaryApplicantDetails
    ${SSN}                    Ssn
    ${Text}                   Text
    ${Word}                   Word
    ${Inp_User_Name}          catenate    ${Random_First_Name} ${Random_Last_Name} ${Random_Middle_Initial}
    ${Random_Number}          Random Number
    ${Alien_Number}           Random Alien Number
    ${Passport_Number}        Random Passport Number
    #${Random_Nine_Four}       Random Nine Four
    ${Int_Number}             Int Number
    ${Number}                 Random Int
    ${Income}                 Random Income
    ${Country}                Country
    ${Phone_Number}           Phone Number
    ${Address}                Address
    ${Apartment_Number}       Building Number
    ${City}                   City
    ${Zip_Code}               Postcode
   Open Browser                 ${URL_PADETAILS}           ${BROWSER_Chrome}
   Maximize window
   
   #Input Text                                              ${Path_SBL_PCI_FName_P1}                                 ${Randome_First_Name}
   #Input Text                                              ${Path_SBL_PCI_MName_P1}                                  ${Random_Middle_Initial}
   #Input Text                                              ${Path_SBL_PCI_LName_P1}                                  ${Random_Last_Name}
   
   Click Element                                             ${Path_LFRY_PCI_Suffix_P1}
   Select From List By Index                                 ${Path_LFRY_PCI_Suffix_P1}                                                         1
   #Input Text                                                 ${Path_SBL_PCI_Relation_P1}
      
   Input Text                                                ${Path_LFRY_PCI_DOB_P1}     ${Today_mm_dd_ccyy}
   Click Element                                             ${Path_LFRY_PCI_Gender_P1}    
   Select From List By Index                                 ${Path_LFRY_PCI_Gender_P1}                                                         1
   
   Input Text                                                ${Path_LFRY_PCI_SpouseName_If_Married_P1}    ${Random_First_Name}
   Input Text                                                ${Path_LFRY_PCI_SSN_P1}                                                              ${SSN}
  
   
    Click Element                                             ${Path_LFRY_PCI_P1_Plan_To_File_Federal_Inctx_Rtn_NEXT_Year}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Plan_To_File_Federal_Inctx_Rtn_NEXT_Year}                        1
    
    Click Element                                             ${Path_LFRY_PCI_P1_Jointly_File_With_Spouse}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Jointly_File_With_Spouse}                                        1    
    Input Text                                                ${Path_LFRY_PCI_P1_Jointly_File_With_Spouse_Yes_Fname}                              ${Random_First_Name}
    Input Text                                                ${Path_LFRY_PCI_P1_Jointly_File_With_Spouse_Yes_Mname}                              ${Random_Middle_Initial}
    Input Text                                                ${Path_LFRY_PCI_P1_Jointly_File_With_Spouse_Yes_Lname}                              ${Random_Last_Name}
    
    Click Element                                             ${Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtrn}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtrn}                                1
    Input Text                                                ${Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtn_Yes_Fname}                       ${Random_First_Name}
    Input Text                                                ${Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtn_Yes_Mname}                       ${Random_Middle_Initial}
    Input Text                                                ${Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtn_Yes_Lname}                       ${Random_Last_Name}
    
    Click Element                                             ${Path_LFRY_PCI_P1_Add_Dependent}
    Input Text                                                ${Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtn_Add_Dependnt_Fname}              ${Random_First_Name} 
    Input Text                                                ${Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtn_Add_Dependnt_Mname}              ${Random_Middle_Initial}
    Input Text                                                ${Path_LFRY_PCI_P1_Claim_Any_Dependt_On_Your_Tx_Rtn_Add_Dependnt_Lname}              ${Random_Last_Name} 
    # Click Button                                            ${Path_LFRY_PCI_P1_Claim_Any_Dependnts_On_Your_Tx_Rtn_Add_Dependt_Remove_Btn} 
    
    Click Element                                             ${Path_LFRY_PCI_P1_Claimed_As_Dependt_On_someones_Tx_Rtn}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Claimed_As_Dependt_On_someones_Tx_Rtn}                             1
    Input Text                                                ${Path_LFRY_PCI_P1_Claimed_As_Dependt_On_someones_Tx_Rtn_Yes_Fname}                   ${Random_First_Name}
    Input Text                                                ${Path_LFRY_PCI_P1_Claimed_As_Dependt_On_someones_Tx_Rtn_Yes_Mname}                   ${Random_Middle_Initial}
    Input Text                                                ${Path_LFRY_PCI_P1_Claimed_As_Dependt_On_someones_Tx_Rtn_Yes_Lname}                   ${Random_Last_Name}
    Select Checkbox                                           ${Path_LFRY_PCI_P1_Chk_If_Tx_Filer_Claimng_You_As_Dependt_Is_Nt_Prt_Of_Hsehold}
    Click Element                                             ${Path_LFRY_PCI_P1_How_Are_You_Related_To_Tx_Filer}  
    Select From List By Index                                 ${Path_LFRY_PCI_P1_How_Are_You_Related_To_Tx_Filer}                                    1
    
    Click Element                                             ${Path_LFRY_PCI_P1_Do_You_Need_Health_Coverage_Yes}     
    Click Element                                             ${Path_LFRY_PCI_P1_Have_Disability_Tht_Will_last_More_Than_Twelve_Mnths}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Have_Disability_Tht_Will_last_More_Than_Twelve_Mnths}               1
    Click Element                                             ${Path_LFRY_PCI_P1_Do_You_Currently_Receive_Long_Trm_Care_Nursing_servces}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Do_You_Currently_Receive_Long_Trm_Care_Nursing_servces}             1
    Click Element                                             ${Path_LFRY_PCI_P1_Have_You_Recvd__Lng_Trm_Cre_Nursng_srvcs_In_Lst_Three_Mnths}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Have_You_Recvd__Lng_Trm_Cre_Nursng_srvcs_In_Lst_Three_Mnths}        1
    Input Text                                                ${Path_LFRY_PCI_P1_Recvd__Lng_Trm_Cre_Nursng_srvcs_In_Lst_Three_Mnths_Yes_From}        ${Today_mm_dd_ccyy} 
    Input Text                                                ${Path_LFRY_PCI_P1_Recvd__Lng_Trm_Cre_Nursng_srvcs_In_Lst_Three_Mnths_Yes_To}          ${Today_mm_dd_ccyy}
    
    Click Element                                             ${Path_LFRY_PCI_P1_Do_You_Think_You_Need_Lng_Trm_Cre_Nursng_srvcs_Now }                        
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Do_You_Think_You_Need_Lng_Trm_Cre_Nursng_srvcs_Now }                 1
    Click Element                                             ${Path_LFRY_PCI_P1_Do_You_Recve_Supplemental_Security_Income_SSI}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Do_You_Recve_Supplemental_Security_Income_SSI}                       1
    
    Click Element                                             ${Path_LFRY_PCI_P1_Recvd_Medcl_Srvcs_Past_Ten_Cal_Days_imdt_Prior_date_Of_Appl}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Recvd_Medcl_Srvcs_Past_Ten_Cal_Days_imdt_Prior_date_Of_Appl}          1
    Input Text                                                ${Path_LFRY_PCI_P1_Recvd_Medcl_Srvcs_Past_Ten_Cal_Days_Prior_date_Of_App_Y_Frm}          ${Today_mm_dd_ccyy} 
    Input Text                                                ${Path_LFRY_PCI_P1_Recvd_Medcl_Srvcs_Past_Ten_Cal_Days_Prior_date_Of_App_Y_To}           ${Today_mm_dd_ccyy}
    
    Click Element                                             ${Path_LFRY_PCI_P1_Are_You_US_Citizen_Or_US_National}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Are_You_US_Citizen_Or_US_National}                                     2
    
    Click Element                                             ${Path_LFRY_PCI_P1_If_Nt_US_Citizen_Or_US_National_Hav_Eligble_Immgratn_Status}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_If_Nt_US_Citizen_Or_US_National_Hav_Eligble_Immgratn_Status}           1
    Click Element                                             ${Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Hav_Eligb_Imig_Sts_Y_Immgtn_Doc_Type}
    Select From List By Value                                 ${Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Hav_Eligb_Imig_Sts_Y_Immgtn_Doc_Type}            Visa 
    
    Input Text                                                ${Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Hav_Eligb_Imig_Sts_Y_Status_Type }               ${Word}
    
    Input Text                                                ${Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Eligb_Imig_Sts_Y_Name_As_On_Imig_Doc}            ${Inp_User_Name}
    Input Text                                                ${Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Eligb_Imig_Sts_Y_Imig_DType_Visa_AN}             ${Alien_Number}
    Input Text                                                ${Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Eligb_Imig_Sts_Y_Imig_DType_Visa_94}             ${Int_Number}
    Input Text                                                ${Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Eligb_Imig_Sts_Y_Imig_DType_Visa_PN}             ${Passport_Number}
    Input Text                                                ${Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Eligb_Imig_Sts_Y_Imig_DType_Visa_DOE}            ${Today_mm_dd_ccyy}
    Input Text                                                ${Path_LFRY_PCI_P1_If_Nt_US_Ctzn_Or_Natnl_Eligb_Imig_Sts_Y_Imig_DType_Visa_OD}             ${Random_Number}    
  
    
    Input Text                                                ${Path_LFRY_PCI_P1_Date_Of_Entry_US_Fnd_Imig_Doc_In_Q13_Dte_Prmnt_Lawfl_Resdnt}             ${Today_mm_dd_ccyy}
    Click Element                                             ${Path_LFRY_PCI_P1_Ctzn_Federtd_Ste_Micronesia_Repblc_Marshall_Islands_Palau_Y}
    Click Element                                             ${Path_LFRY_PCI_P1_Ctzn_Fedrtd_Ste_Micronesia_Rpblc_Mrshl_Islds_Palau_Y_Ctzshp}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Ctzn_Fedrtd_Ste_Micronesia_Rpblc_Mrshl_Islds_Palau_Y_Ctzshp}             1
    Click Element                                             ${Path_LFRY_PCI_P1_Ctzn_Fedrtd_Ste_Micronesia_Rpblc_Mrshl_Islds_Palau_Y_Ctzshp} 
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Ctzn_Fedrtd_Ste_Micronesia_Rpblc_Mrshl_Islds_Palau_Y_Ctzshp}             1   
    Click Element                                             ${Path_LFRY_PCI_P1_You_Spouse_Parent_A_Veteran_Or_Actve_Duty_Membr_US_Military}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_You_Spouse_Parent_A_Veteran_Or_Actve_Duty_Membr_US_Military}             1
    
    Click Element                                             ${Path_LFRY_PCI_P1_You_In_Foster_Care_At_Age18_Or_Older_In_Hawaii}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_You_In_Foster_Care_At_Age18_Or_Older_In_Hawaii}                          1
    
    Click Element                                             ${Path_LFRY_PCI_P1_Are_You_A_Full_Time_Student}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Are_You_A_Full_Time_Student}                                             1
    
    Select Checkbox                                           ${Path_LFRY_PCI_P1_If_Hispanic_Latino_Ethnicity_Chicano_A}
    Select Checkbox                                           ${Path_LFRY_PCI_P1_If_Hispanic_Latino_Ethnicity_Cuban}
    Select Checkbox   	                                      ${Path_LFRY_PCI_P1_If_Hispanic_Latino_Ethnicity_Other}
    Input Text                                                ${Path_LFRY_PCI_P1_If_Hispanic_Latino_Ethnicity_Other_Text}                                 ${Word}
    Select Checkbox                                           ${Path_LFRY_PCI_P1_Race_Check_American_Indian_Or_Alaskan_Native}
    Select Checkbox                                           ${Path_LFRY_PCI_P1_Race_Check_Asian_Indian}
    Select Checkbox                                           ${Path_LFRY_PCI_P1_Other}
    Input Text                                                ${Path_LFRY_PCI_P1_Other_Text}                                                              ${Country}
    
    Click Element                                             ${Path_LFRY_PCI_P1_Current_Job_And_Income_Information_Typ_Employment_Employed}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Information_Employer_Name}                        ${Random_First_Name}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Information_PH_Nbr}                               ${Phone_Number}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Information_Address_Line1}                        ${Address}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Information_Apartment_Or_Suite_Nbr}               ${Apartment_Number}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Information_City}                                 ${City} 
    Click Element                                             ${Path_LFRY_PCI_P1_Current_Job_And_Income_Information_State} 
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Current_Job_And_Income_Information_State}                                0
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Zip_Code}                                         ${Zip_Code}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Wages_Tips_Before_Taxes}                          ${Random_Number}
    Click Element                                             ${Path_LFRY_PCI_P1_Current_Job_And_Income_How_Often} 
    Select From List By Value                                 ${Path_LFRY_PCI_P1_Current_Job_And_Income_How_Often}                                        Daily
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_How_Often_Daily_Days_Wrkd_Each_Week}              ${Random_Number}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Income_Start_Date}                                ${Today_mm_dd_ccyy}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Income_End_Date}                                  ${Today_mm_dd_ccyy}      
    
    Click Element                                             ${Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Button}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Emplr_Name}                          ${Random_First_Name}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_PH_Nbr}                              ${Phone_Number}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Address_Line1}                       ${Address}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Apartment_Or_Suite_Nbr}              ${Apartment_Number}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_City}                                ${City}
    Click Element                                             ${Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_State}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_State}                               0
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Zip_Code}                            ${Zip_Code}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Wages_Tips_Before_Taxes}             ${Random_Number}
    Click Element                                             ${Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_How_Often}
    Select From List By Value                                 ${Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_How_Often}                           Daily
    Input Text                                                ${Path_LFRY_PCI_P1_Cnt_Jb_And_Incm_Add_New_Jobs_Hw_Oftn_Daily_Nbr_Hrs_Wrkd}                 ${Random_Number}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Income_Start_Date}                   ${Today_mm_dd_ccyy}
    Input Text                                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Add_New_Jobs_Income_End_Date}                     ${Today_mm_dd_ccyy}
    Click Element                                             ${Path_LFRY_PCI_P1_Current_Job_And_Income_In_The_Past_Year_Did_You}
    Select From List By Index                                 ${Path_LFRY_PCI_P1_Current_Job_And_Income_In_The_Past_Year_Did_You}                         1            
    

    Select Checkbox                                          ${Path_LFRY_PCI_P1_Current_Job_And_Income_Self_Employed}
    Input Text                                               ${Path_LFRY_PCI_P1_Current_Job_And_Income_Self_Emplyd_Type_Of_Work}                           ${Word}
    Input Text                                               ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Slf_Empd_Net_Incme_Gt_Paid_Frm_Slf_Emplnt}                 ${Random_Number}
    Click Element                                            ${Path_LFRY_PCI_P1_Current_Job_And_Income_Othr_Icme_Ths_Mnth_Income_Type}
    Select From List By Index                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Othr_Icme_Ths_Mnth_Income_Type}                     1
    Input Text                                               ${Path_LFRY_PCI_P1_Current_Job_And_Income_Othr_Icme_Ths_Mnth_Amount}                          ${Random_Number}
    Click Element                                            ${Path_LFRY_PCI_P1_Current_Job_And_Income_Othr_Icme_Ths_Mnth_How_Often}
    Select From List By Index                                ${Path_LFRY_PCI_P1_Current_Job_And_Income_Othr_Icme_Ths_Mnth_How_Often}                        1
    Input Text                                               ${Path_LFRY_PCI_P1_Cnt_Jb_Incm_Otr_Icme_Ths_Mnth_Hw_Oftn_Daily_Dys_Wrkd_Ech_Wk}                ${Random_Number}
    Input Text                                               ${Path_LFRY_PCI_P1_Curnt_Jb_And_Incm_Othr_Icme_Ths_Mnth_Hw_Oftn_Incme_Str_Date}                ${Today_mm_dd_ccyy}
    Input Text                                               ${Path_LFRY_PCI_P1_Cnt_Job_And_Incme_Othr_Icme_Ths_Mnth_Hw_Oftn_Incme_End_Date}                ${Today_mm_dd_ccyy}
                
    
    Click Element                                            ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_Button}
    Click Element                                            ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_Incme_Type}
    Select From List By Index                                ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_Incme_Type}                                1
    Input Text                                               ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_Amount}                                    ${Random_Number}
    Click Element                                            ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_How_Oftn}
    Select From List By Index                                ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_How_Oftn}                                        1
    Input Text   	                                         ${Path_LFRY_PCI_P1_Cnt_Jb_Incme_Add_Mre_Incm_Hw_Ofn_Daily_Nbr_Days_wrkd_Ech_Wk}               ${Random_Number}
    Input Text                                               ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_Incme_Str_Date}                            ${Today_mm_dd_ccyy}
    Input Text                                               ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_Incme_End_Date}                            ${Today_mm_dd_ccyy}
    # Click Element                                          ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Add_More_Income_Remove_Button}                
    
    
    Click Element                                            ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Type_Of_Deductn}
    Select From List By Index                                ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Type_Of_Deductn}                                    1
    Input Text                                               ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Amount}                                             ${Income}
    Click Element                                            ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_How_Often}
    Select From List By Index                                ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_How_Often}                                          1
    Input Text                                               ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Deductn_Start_Date}                                 ${Today_mm_dd_ccyy}
    Input Text                                               ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Deductn_End_Date}                                   ${Today_mm_dd_ccyy}
    
    Click Element                                            ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Add_More_Deductn_Button}             
    Click Element                                            ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Add_More_Deductn_Type_Of_Deductn}
    Select From List By Index                                ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Add_More_Deductn_Type_Of_Deductn}                    1
    Input Text                                               ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Add_More_Deductn_Amount}                             ${Income}
    Click Element                                            ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Add_More_Deductn_How_Often}
    Select From List By Index                                ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Add_More_Deductn_How_Often}                          1
    Input Text                                               ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Add_More_Deductn_Deductn_Start_Date}                 ${Today_mm_dd_ccyy}
    Input Text                                               ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Add_More_Deductn_Deductn_End_Date}                   ${Today_mm_dd_ccyy}
    # Click Element                                          ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Deductn_Remove_Button}                 
    
    Input Text                                               ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Yearly_Income_Total_Incmr_Ths_Yr}                            ${Income}
    Input Text                                               ${Path_LFRY_PCI_P1_Curnt_Job_Incme_Yearly_Income_Total_Inmce_Tx_Nxt_Yr}                         ${Income}
    