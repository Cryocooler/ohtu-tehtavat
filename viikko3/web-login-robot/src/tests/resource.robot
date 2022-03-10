*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:4000
${BROWSER}  chrome
${DELAY}  0.5 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    #Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Register Page Should Be Open
    Title Should Be  Register

Go To Login Page
    Go To  ${LOGIN URL}

Click Link On Page
    [Arguments]    ${keyword}
    Click Link     ${keyword}

Go To Home Page
    Go To   ${HOME URL}
