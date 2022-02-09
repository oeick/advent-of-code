# AmigaBASIC

[Amiga 500](https://en.wikipedia.org/wiki/Amiga_500)

[AmigaBASIC](https://en.wikipedia.org/wiki/AmigaBASIC)


## How

To program with AmigaBASIC on a Windows 10 PC, I use the Amiga Forever emulator 
collection (Value Edition 8), which comes prepared with a ready-to-use 
Workbench 1.3 setup on an emulated Amiga 2000. The setup also includes a shared directory to transfer files between Windows and Workbench (device `Shared:`). So in my basic code I will often load data from a filepath like `Shared:input.txt`. Just save the puzzle input to a file in the shared folder. Surprisingly there has not been any problem reading that file with AmigaBASIC.

Using the save option from the AmigaBASIC file menu produces a file in some binary format, not readable for any Windows tools, as far as I know.
To get the basic listing as an ascii file for my git repository, I use the `save` command with the `A` parameter, to save the basic listing in ascii format in the shared folder.

Information about AmigaBASIC commands:
 - https://archive.org/details/Amiga_BASIC_1985_Commodore
 - http://www.pjhutchison.org/emulation/uae_amigabasic.html