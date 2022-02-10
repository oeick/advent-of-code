*** Settings ***
Library    String


*** Keywords ***
Solve Part 1
    [Arguments]    ${input}
    ${sequence}    Set Variable    ${input}${input}[0]
    ${length}    Get Length    ${sequence}
    ${sum}    Set Variable    0
    FOR    ${i}    IN RANGE    ${length-1}
        ${this}    Convert To Integer    ${sequence}[${i}]
        ${next}    Convert To Integer    ${sequence}[${i+1}]
        IF    ${this} == ${next}
            ${sum}    Evaluate    ${sum} + ${this}
        END
    END
    [Return]    ${sum}

Solve Part 2
   [Arguments]    ${input}
   ${length}    Get Length    ${input}
   ${second half}    Get Substring    ${input}    ${length/2}    ${length}
   ${sum}    Set Variable    0
   FOR    ${i}    IN RANGE    ${length//2}
       ${this}    Convert To Integer    ${input}[${i}]
       ${next}    Convert To Integer    ${second half}[${i}]
       IF    ${this} == ${next}
           ${sum}    Evaluate    ${sum} + ${this} + ${next}
       END
   END
   [Return]    ${sum}
