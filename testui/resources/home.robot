*** Settings ***
Documentation    A file with reusable keywords and variables for the Home page.
Library          SeleniumLibrary

***Variables***
${TIMEOUT}    2

*** Keywords ***
Open Browser To Home Page
    Open Browser    ${APP_URL}    ${BROWSER}    remote_url=${SELENIUM_HUB}


A Home Page Is Open
    Wait Until Page Contains    Time now is
    ...                         ${TIMEOUT}
    ...                         The Home Page didn't load within ${TIMEOUT} snds.