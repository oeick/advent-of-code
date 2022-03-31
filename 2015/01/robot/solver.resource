*** Settings ***
Library    String


*** Keywords ***
Solve Part 1
    [Arguments]    ${input}
    ${open parenthesis}    Get Count    ${input}    (
    ${closed parenthesis}    Get Count    ${input}    )
    ${difference}   Evaluate     ${open parenthesis} - ${closed parenthesis}
    [Return]    ${difference}

Solve Part 2
    [Arguments]    ${input}
    ${floor}    Set Variable    ${0}
    ${characters}    Split String To Characters    ${input}
    FOR    ${n}    ${character}    IN ENUMERATE    @{characters}
        IF    '${character}' == '('
            ${floor}    Evaluate    ${floor} + 1
        ELSE
            ${floor}    Evaluate    ${floor} - 1
        END
        Return From Keyword If    ${floor} == -1    ${n + 1}
    END
