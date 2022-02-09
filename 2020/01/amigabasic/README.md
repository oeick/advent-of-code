# Advent Of Code 2020 Day 01 with AmigaBASIC

The task is simple enough to solve both parts on a modern computer and a modern programming language with non-optimized brute force in less than 1s.

But on an old Amiga with AmigaBASIC it takes far more than that: My emulated Amiga 2000 needs a few seconds brute forcing the first part.

But for the second part it took more than *30 minutes*.

So, now day 1 part 2 has become much more interesting :-)

After some hours of re-writing code I boosted the AmigaBASIC program to solve part two in less than one minute.

The trick is to sort the input and put a conditional break in the inner loop of the brute force code. With sorted input, it took just a few seconds to solve part 2. Unfortunately there is no sorting function in AmigaBASIC, so I had to write it myself. First I tried [insertion sort](https://en.wikipedia.org/wiki/Insertion_sort), because it is easy to implement. It sorted the 200 input numbers in 46s. Then I tried [quicksort](https://en.wikipedia.org/wiki/Quicksort) and finally it sorted the same list in 7s. I experienced a lot of difficulties to implement und debug quicksort in AmigaBASIC and I was happy when it finally worked correctly.

And yes, it's the iterative version of quicksort, because sub routines in AmigaBASIC don't allow recursion.