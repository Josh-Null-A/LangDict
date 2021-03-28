from .translator import Translator

def main(*args):
    """
        The main function for the langdict package

        This function should be called from the terminal / shell as
        ``` >>> python -m langdict ```
        but can also be imported and used in files.

        If main() is being used inside a file, it should be called as
        ``` main('-l', <target language>, '-p', <path to .xlsx file>) ```

        Arguments:
            *Args -: :- System arguments passed through from the terminal / shell

        Keywords:
            -l -: str :- The target language a dictionary will be translated into
            -p -: str :- A path-name for a .xlsx file containing the dictionary
            -c -: str :- A bool determining if a seperate .xlsx file should be created
            -s -: str :- Ignored by default unless set to 'google', in which case
                         - translations are retrieved from google translate
    """

    l, p = None, None
    c, s = 'false', 'cambridge'

    # Go through *args and find the keyword
    i = 0
    while i < len(args):
        try:
            if args[i] == '-l':
                l = args[i+1]
                i += 1
            elif args[i] == '-p':
                p = args[i+1]
                i += 1
            elif args[i] == '-c':
                c = args[i+1]
                i += 1
            elif args[i] == '-s':
                s = args[i+1]
                i += 1
        except IndexError as e:
            raise ValueError(f'Expected value for {args[i]}')
        i += 1

    # Assert that l & p are not None
    assert l != None and p != None, 'Expected values for -l and -p'

    # Initialize a Translator object and run
    translator = Translator(l, p, c, s)
    translator.translate()
