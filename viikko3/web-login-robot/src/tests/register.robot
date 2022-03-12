*** Settings ***
Resource    resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Create User

*** Test Cases ***

Register With Valid Username And Password
# ...
    Set Username   laad
    Set Password    kapton812
    Confirm Password  kapton812
    Submit Register Credentials
    Register Should Succeed


Register With Already Taken Username And Valid Password
    Set Username    Jakke
    Set Password    kapton812
    Confirm Password  kapton812
    Submit Register Credentials
    Register Should Fail With Message  User with username Jakke already exists

Register With Too Short Username And Valid Password
    Set Username    po
    Set Password    kapton812
    Confirm Password  kapton812
    Submit Register Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username    johnson
    Set Password    kapt
    Confirm Password  kapt
    Submit Register Credentials
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username    johnson
    Set Password    laplacian822
    Confirm Password  laplacian811
    Submit Register Credentials
    Register Should Fail With Message  Password and confirmation do not match

Login After Successful Registration
    Set Username   laad
    Set Password    kapton812
    Confirm Password  kapton812
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username    laad
    Set Password    kapton812
    Click Button    Login
    Main Page Should Be Open


Login After Failed Registration
    Set Username    johnson
    Set Password    laplacian822
    Confirm Password  laplacian811
    Submit Register Credentials
    Register Should Fail With Message  Password and confirmation do not match
    Go To Login Page
    Login Page Should Be Open
    Set Username    johsnon
    Set Password    laplacian822
    Click Button    Login
    Login Page Should Be Open
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Go To Register Page and Create User
    Go To Register Page
    Create User  Jakke   kapton812
    Register Page Should Be Open

Confirm Password
    [Arguments]   ${password}
    Input Text  password_confirmation    ${password}

Submit Register Credentials
    Click Button    Register

Register Should Succeed
    Welcome Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Register Should Fail With Message
    [Arguments]   ${message}
    Register Page Should Be Open
    Page Should Contain     ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}