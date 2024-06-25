*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${LOGIN_URL}    http://localhost:8069/web/login
${VENDOR_URL}    http://localhost:8069/web#cids=1&menu_id=313&action=442&model=lunch.product&view_type=kanban

*** Test Cases ***
Login and Create Vendor
    Open Browser    ${LOGIN_URL}    Chrome
    Maximize Browser Window
    Input Text    name:login    admin
    Input Password    name:password    admin
    Click Button  //*[@id="wrapwrap"]/main/div/form/div[3]/button[1]
    Sleep    10s
    Create Vendor
    [Teardown]    Close Browser

*** Keywords ***
Create Vendor
    Go To    ${VENDOR_URL}
    Sleep    5s
    Click Element    xpath:/html/body/header/nav/div[2]/div[3]/button
    Sleep    5s
    Click Element    xpath:/html/body/header/nav/div[2]/div[3]/div/a[2]
    Sleep    5s
    Click Element    xpath:/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/button
    Sleep    5s
    Click Element    xpath:/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/button[1]
    Sleep   10s
    Wait For Notification

Wait For Notification
    Wait Until Element Is Visible    class=o_notification_manager
    Log    Warning is seen, Test Passed    # Handle the notification
