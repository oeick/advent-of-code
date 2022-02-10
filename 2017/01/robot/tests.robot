*** Settings ***
Resource    solver.resource


*** Test Cases ***
Part 1 Example 1
    ${result}    Solve Part 1    1122
    Should Be Equal As Integers    ${result}    3

Part 1 Example 2
    ${result}    Solve Part 1    1111
    Should Be Equal As Integers    ${result}    4

Part 1 Example 3
    ${result}    Solve Part 1    1234
    Should Be Equal As Integers    ${result}    0

Part 1 Example 4
    ${result}    Solve Part 1    91212129
    Should Be Equal As Integers    ${result}    9

Part 2 Example 1
    ${result}    Solve Part 2    1212
    Should Be Equal As Integers    ${result}    6

Part 2 Example 2
    ${result}    Solve Part 2    1221
    Should Be Equal As Integers    ${result}    0

Part 2 Example 3
    ${result}    Solve Part 2    123425
    Should Be Equal As Integers    ${result}    4

Part 2 Example 4
    ${result}    Solve Part 2    123123
    Should Be Equal As Integers    ${result}    12

Part 2 Example 5
    ${result}    Solve Part 2    12131415
    Should Be Equal As Integers    ${result}    4
