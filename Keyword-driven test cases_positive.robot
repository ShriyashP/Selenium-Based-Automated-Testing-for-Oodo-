*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            http://localhost:8069/web/login
${VENDOR_NAME}    Shriyash
${VENDOR_PHONE}   99898

*** Test Cases ***
Create Vendor
    Open Browser    ${URL}    chrome
    Login
    Create Vendor Details
    Close Browser

*** Keywords ***
Login
    Input Text    name:login    admin
    Input Text    name:password    admin
    Click Button    //button[@type='submit']
    Sleep    10s

Create Vendor Details
    Go To    http://localhost:8069/web#cids=1&menu_id=313&action=442&model=lunch.product&view_type=kanban
    Sleep    2s
    Go To   http://localhost:8069/web#cids=1&menu_id=313&action=444&model=lunch.supplier&view_type=kanban
    Sleep    2s
    Click Element   xpath:/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/button
    Sleep   8s
    Input Text   xpath:/html/body/div[1]/div/div[2]/div/div[1]/div/div[3]/table[1]/tbody/tr[1]/td[2]/div/div[1]/div/input   Joe
    Sleep   2s
    Input Text  xpath:/html/body/div[1]/div/div[2]/div/div[1]/div/div[3]/table[2]/tbody/tr[3]/td[2]/input   9076
    Sleep   2s
    Click Element   xpath:/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/button[1]
    Sleep   2s
    Click Element   xpath:/html/body/div[1]/div/div[1]/div[1]/div[1]/ol/li[1]/a
    Sleep   2s



