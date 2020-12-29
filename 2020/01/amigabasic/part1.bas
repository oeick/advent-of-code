DIM SHARED n%     ' number of input lines
DIM SHARED solution&

filename$ = "Shared:input.txt"
CountFileLines(filename$)

PRINT "read"; n%; "lines from "; filename$

DIM SHARED lines(n%)
ReadLines(filename$)

PRINT TIME$; " starting calculation"

SolvePart1(2020)

PRINT TIME$; " finished calculation"
PRINT "solution: "; solution&


' -------- sub routines --------

SUB SolvePart1 (target%) STATIC
  FOR a% = 1 TO n%-1
    FOR b% = a%+1 TO n%
      IF lines(a%) + lines(b%) = target% THEN
        solution& = lines(a%) * lines(b%)
        EXIT SUB
      END IF
    NEXT b%
  NEXT a%  
END SUB

SUB CountFileLines (filename$) STATIC
  OPEN filename$ FOR INPUT AS #1
  n% = 0
  WHILE EOF(1) = 0
    INPUT#1, content
    n% = n% + 1
  WEND
  CLOSE #1
END SUB

SUB ReadLines (filename$) STATIC
  OPEN filename$ FOR INPUT AS #1
  FOR i% = 1 TO n%
    INPUT#1, lines(i%)
  NEXT
  CLOSE #1
END SUB  
