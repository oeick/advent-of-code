# Solutions to Advent of Code puzzles

Programming languages:

- Python: my language at work
- Rust: I would like to learn this language out of private interest
- AmigaBASIC: my first programming language (see below)


## AmigaBASIC

### Why?!

The [Amiga 500](https://en.wikipedia.org/wiki/Amiga_500) was my first computer and [AmigaBASIC](https://en.wikipedia.org/wiki/AmigaBASIC) my first programming language.
I remembered this, while solving programming puzzles and I thought it could be an interesting and nostalgic challenge to try solving those puzzles with AmigaBASIC.

### How?

To program with AmigaBASIC on a Windows 10 PC, I use the Amiga Forever emulator collection (Value Edition 8), which comes prepared with a ready-to-use Workbench 1.3 setup on an emulated Amiga 2000. The setup also includes a shared directory to transfer files between Windows and Workbench (device `Shared:`). So in my basic code I will often load data from a filepath like `Shared:input.txt`. Just save the puzzle input to a file in the shared folder. Surprisingly there has not been any problem reading that file with AmigaBASIC.

Using the save option from the AmigaBASIC file menu produces a file in some binary format, not readable for any Windows tools, as far as I know.
To get the basic listing as an ascii file for my git repository, I use the `save` command with the `A` parameter, to save the basic listing in ascii format in the shared folder.

To help remembering the language I found a pdf of the [AmigaBASIC manual](https://archive.org/details/Amiga_BASIC_1985_Commodore).


### Advent Of Code 2020 Day 01 with AmigaBASIC

The task is simple enough to solve both parts on a modern computer and a modern programming language with non-optimized brute force in less than 1s.

But on an old Amiga with AmigaBASIC it takes far more than that: My emulated Amiga 2000 needs a few seconds brute forcing the first part.

But for the second part it took more than *30 minutes*.

So, now day 1 part 2 has become much more interesting :-)

After some hours of re-writing code I boosted the AmigaBASIC program to solve part two in less than one minute.

The trick is to sort the input and put a conditional break in the inner loop of the brute force code. With sorted input, it took just a few seconds to solve part 2. Unfortunately there is no sorting function in AmigaBASIC, so I had to write it myself. First I tried [insertion sort](https://en.wikipedia.org/wiki/Insertion_sort), because it is easy to implement. It sorted the 200 input numbers in 46s. Then I tried [https://en.wikipedia.org/wiki/Quicksort] and finally it sorted the same list in 7s. I experienced a lot of difficulties to implement und debug quicksort in AmigaBASIC and I was happy when it finally worked correctly.
