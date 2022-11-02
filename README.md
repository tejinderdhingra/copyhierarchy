# copyhierarchy.py

## Python cli tool to copy directory tree from source into destination directory

usage:
`
python3 copyhierarchy.py [-h] -s SRCDIR -d DESTDIR
`

The cli tool validates the inputs and provides the help in case any of the arguments is not provided.

The code does verify if the SRCDIR exists and if it is a directory, it does also verify if the SRCDIR exists inside the DESTDIR or if any of the path is not a directory.

In all the above cases the program does display the respective error message.

The program does copy the directory hierarchy structure of SRCDIR into the DESTDIR only the SRCDIR and DESTDIR are valid directories and if the SRCDIR does not exist inside DESTDIR.

_Note: The directories and files along with the tool are for testing purposes only._
