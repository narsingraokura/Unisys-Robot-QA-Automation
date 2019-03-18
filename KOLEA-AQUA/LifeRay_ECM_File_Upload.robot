*** Settings ***
Resource    KOLEA_Key_Words.robot    
Resource    LifeRay_Key_Words.robot

   
   

*** Test Cases ***
LifeRayECMUpload
   Open Browser                                 ${URL_ECMUpload}                                                             ${BROWSER_Chrome}
   Maximize window
   
   Click Element                                ${Path_PP_Doc_Upload_Page_What_Does_This_File_Contain}
   Select From List By Index                    ${Path_PP_Doc_Upload_Page_What_Does_This_File_Contain}                        0

   Click Element                                ${Path_PP_Doc_Upload_Page_If_VD_File_Contains}
   Select from list By Index                    ${Path_PP_Doc_Upload_Page_If_VD_File_Contains}                                1
   Click Element                                ${Path_PP_Doc_Upload_Page_If_VD_File_Contains_For}
   Select From List By Index                    ${Path_PP_Doc_Upload_Page_If_VD_File_Contains_For}                            1
   Click Element                                ${Path_PP_Doc_Upload_Page_If_VD_Doc_For_Another_Per_In_This_Case_Yes}     
   
   Click Element                                ${Path_PP_Doc_Upload_Page_VD_If_Yes_File_Contains}
   Select from List By Index                    ${Path_PP_Doc_Upload_Page_VD_If_Yes_File_Contains}                            1
   
   Click Element                                ${Path_PP_Doc_Upload_Page_VD_If_Yes_File_Contains_For}
   Select from List By Index                    ${Path_PP_Doc_Upload_Page_VD_If_Yes_File_Contains_For}                        1
   Choose File                                  ${Path_PP_Doc_Upload_Page_File_Choosen}                                       C://Users//giriganv//Desktop//Unisys-Holidays-2019.PNG
     
   
   # Click Element                                ${Path_PP_Doc_Upload_Page_What_Does_This_File_Contain}
   # Select From List By Index                    ${Path_PP_Doc_Upload_Page_What_Does_This_File_Contain}                         1  
   
   # Click Element                                ${Path_PP_Doc_Upload_Page_Form_Select_The_Form}
   # Select from List By Index                    ${Path_PP_Doc_Upload_Page_Form_Select_The_Form}                                1   

   # Choose File                                  ${Path_PP_Doc_Upload_Page_File_Choosen}                                        C://Users//giriganv//Desktop//Unisys-Holidays-2019.PNG
   
   Click Element                ${Path_PP_Doc_Upload_Page_Terms_And_Conditions}   
   
  
   
