# Solutions to Advent of Code puzzles

To practice writing readable, maintainable and testable code, I use the 
exercises from [Advent of Code](https://adventofcode.com/).

Programming languages:

- Python: my first language at work
  - [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
  - [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- Java: my second language at work
- Rust: I would like to learn this language out of private interest
- AmigaBASIC: my first programming language (see below)


## AmigaBASIC

### Why?!

The [Amiga 500](https://en.wikipedia.org/wiki/Amiga_500) was my first computer
and [AmigaBASIC](https://en.wikipedia.org/wiki/AmigaBASIC) my first programming
language.
I remembered this, while solving programming puzzles and I thought it could be 
an interesting and nostalgic challenge to try solving those puzzles with 
AmigaBASIC.

### How?

To program with AmigaBASIC on a Windows 10 PC, I use the Amiga Forever emulator 
collection (Value Edition 8), which comes prepared with a ready-to-use 
Workbench 1.3 setup on an emulated Amiga 2000. The setup also includes a shared directory to transfer files between Windows and Workbench (device `Shared:`). So in my basic code I will often load data from a filepath like `Shared:input.txt`. Just save the puzzle input to a file in the shared folder. Surprisingly there has not been any problem reading that file with AmigaBASIC.

Using the save option from the AmigaBASIC file menu produces a file in some binary format, not readable for any Windows tools, as far as I know.
To get the basic listing as an ascii file for my git repository, I use the `save` command with the `A` parameter, to save the basic listing in ascii format in the shared folder.

Information about AmigaBASIC commands:
 - https://archive.org/details/Amiga_BASIC_1985_Commodore
 - http://www.pjhutchison.org/emulation/uae_amigabasic.html


### Advent Of Code 2020 Day 01 with AmigaBASIC

The task is simple enough to solve both parts on a modern computer and a modern programming language with non-optimized brute force in less than 1s.

But on an old Amiga with AmigaBASIC it takes far more than that: My emulated Amiga 2000 needs a few seconds brute forcing the first part.

But for the second part it took more than *30 minutes*.

So, now day 1 part 2 has become much more interesting :-)

After some hours of re-writing code I boosted the AmigaBASIC program to solve part two in less than one minute.

The trick is to sort the input and put a conditional break in the inner loop of the brute force code. With sorted input, it took just a few seconds to solve part 2. Unfortunately there is no sorting function in AmigaBASIC, so I had to write it myself. First I tried [insertion sort](https://en.wikipedia.org/wiki/Insertion_sort), because it is easy to implement. It sorted the 200 input numbers in 46s. Then I tried [quicksort](https://en.wikipedia.org/wiki/Quicksort) and finally it sorted the same list in 7s. I experienced a lot of difficulties to implement und debug quicksort in AmigaBASIC and I was happy when it finally worked correctly.

And yes, it's the iterative version of quicksort, because sub routines in AmigaBASIC don't allow recursion.


### Advent Of Code 2020 Day 02 with AmigaBASIC

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
