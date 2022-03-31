*** Settings ***
Resource    solver.resource


*** Test Cases ***
Part 1 Example 1a
    ${result}    Solve Part 1    (())
    Should Be Equal As Integers    ${result}    0

Part 1 Example 1b
    ${result}    Solve Part 1    ()()
    Should Be Equal As Integers    ${result}    0

Part 1 Example 2a
    ${result}    Solve Part 1    (((
    Should Be Equal As Integers    ${result}    3

Part 1 Example 2b
    ${result}    Solve Part 1    (()(()(
    Should Be Equal As Integers    ${result}    3

Part 1 Example 3
    ${result}    Solve Part 1    ))(((((
    Should Be Equal As Integers    ${result}    3

Part 1 Example 4a
    ${result}    Solve Part 1    ())
    Should Be Equal As Integers    ${result}    -1

Part 1 Example 4b
    ${result}    Solve Part 1    ))(
    Should Be Equal As Integers    ${result}    -1

Part 1 Example 5a
    ${result}    Solve Part 1    )))
    Should Be Equal As Integers    ${result}    -3

Part 1 Example 5b
    ${result}    Solve Part 1    )())())
    Should Be Equal As Integers    ${result}    -3

Part 2 Example 1a
    ${result}    Solve Part 2    )
    Should Be Equal As Integers    ${result}    1

Part 2 Example 1b
    ${result}    Solve Part 2    ()())
    Should Be Equal As Integers    ${result}    5
