*** Settings ***
Documentation     Test home page
Resource          ../resources/home.robot

*** Test Cases ***
Use Can Open A Home Page
    [Documentation]    User sees the Home page.

    Open Browser To Home Page
    A Home Page Is Open

    [Teardown]    Close Browser
