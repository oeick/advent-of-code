Hexagon coordinates
===================

Used convention:

 - y axis is aligned south to north
 - x axis is aligned south-west to north-east


Axis orientation:

        y  x
      \ | /
       \|/
        X
       /|\
      / | \
    -x -y


Directions from a single hex field:

             +y
              |
              |         +x
                        /
            \ n  /    /
          nw +--+ ne
            /    \
          -+      +-
            \    /
          sw +--+ se
        /   / s  \
      /
    -x        |
              |
             -y


Example hex field with coordinates:

      /    \    /    \
    -+ -1,2 +--+ 1,1  +--
      \    /    \    /
       +--+ 0,1  +--+ 2,0
      /    \    /    \
    -+ -1,1 +--+ 1,0  +--
      \    /    \    /
       +--+ 0,0  +--+ 2,-1
      /    \    /    \
    -+ -1,0 +--+ 1,-1 +--
      \    /    \    /
