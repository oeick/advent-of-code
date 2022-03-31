*** Settings ***
Library    OperatingSystem
Resource    solver.resource


*** Task ***
Solve
    ${input}    Get File    ../input.txt
    ${solution 1}    Solve Part 1    ${input}
    ${solution 2}    Solve Part 2    ${input}
    Log    ${solution 1}
    Log    ${solution 2}
