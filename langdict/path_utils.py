import os

def get_file_path(pathname):
    """
        Gets the path of a file given a pathname
        (i.e ~/folder/file.txt -> ~/folder/)

        Returns:
            -: str :- The path of the given file name
    """

    # Iterate backwards through the string and locate the last '/'
    i = len(pathname)-1
    while i > 0:
        if pathname[i] == '/':
            return os.path.abspath(pathname[:i+1])
        i -= 1

def get_file_name(pathname):
    """
        Gets the name of a file given a pathname
        (i.e ~/folder/file.txt -> file.txt)

        Returns:
            -: str :- The name of the given file in the pathname
    """

    # Iterate backwards through the string and locate the last '/'
    i = len(pathname)-1
    while i > 0:
        if pathname[i] == '/':
            return os.path.abspath(pathname[i+1:])
        i -= 1
