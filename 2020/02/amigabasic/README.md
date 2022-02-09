# Advent Of Code 2020 Day 02 with AmigaBASIC

Duration for validating (both parts simultanous) took around 2 minutes.

Difficulties:
 - there is not regex parser in AmigaBASIC
 - there is no function to parse a string into an integer
 - there is no function to count specific characters in a string


### Advent Of Code 2020 Day 03 with AmigaBASIC

Resulting product of part 2 extends 4 byte limit of long integer type in AmigaBASIC.

To calculate the solution product, I used double precision, because this is stored and printed with 16 digits of precision (AmigaBASIC Manual, Reference 8-7).

More information about the binary math used by AmigaBASIC: AmigaBASIC Manual, Appendix D: Internal Representation of Numbers.


*Variable Types*

Trailing declaration characters (default is single precision):

| char | type             | bytes |
| ---- | ---------------- | ----- |
| `%`  | short integer    | 2     |
| `&`  | long integer     | 4     |
| `!`  | single precision | 4     |
| `#`  | double precision | 8     |
| `$`  | String           | 5+    |
