*** Settings ***
Resource    resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
# ...
    Input Credentials   laad    kapton812
    Output Should Contain   New user registered

Register With Already Taken Username And Valid Password
    Input Credentials   Jakke   kapton812
    Output Should Contain   User with username Jakke already exists

Register With Too Short Username And Valid Password
    Input Credentials   ja     kapton812
    Output Should Contain   Username and password must contain enough characters

Register With Valid Username and Too Short Password
    Input Credentials  jasper  kel
    Output Should Contain   Username and password must contain enough characters

Register With Valid Username and Long Enough Password Containing Only Letters
    Input Credentials  jasper  kurtosis822

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User    Jakke   kapton812



# ...

#Register With Too Short Username And Valid Password
# ...

#Register With Valid Username And Too Short Password
# ...

#Register With Valid Username And Long Enough Password Containing Only Letters
# ...