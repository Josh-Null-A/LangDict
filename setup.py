"""
    LangDict
    ========

    Description
    -----------
        LangDict is a python package used as an aide in language acquisition.

        LangDict is used to generate a dictionary of words from English to the user's
        target language. (I.E English > Japanese). These words are stored in a .xlsx file.
        LangDict retrieves translations from https://dictionary.cambridge.org/dictionary/
        A reliable site for a handful of languages.

        Unfortuantly LangDict cannot translate words into target languages that do not
        appear on the cambridge.org website. If the user of this package requires a
        target language that is not present on this website, then the user can specify
        to instead use google translate. (However we don't reccomend this as google
        doesn't do a great job at translating individual words in certain languages)

    Avaliable langauges
    -------------------
        French
        German
        Indonesian
        Italian
        Japanese
        Polish
        Portuguese
        Spanish
        Arabic
        Catalan
        Chinese (Simplified)
        Chinese (Traditional)
        Czech
        Danish
        Korean
        Malay
        Norwegian
        Russian
        Thai
        Turkish
        Vietnamese

    How to use
    ----------
    First make sure you have a .xlsx file containing the words you want to translate
    from English in the first column of each page in the spreadsheet.

    Next, after installing this package using the setup.py file or the python pip
    package, simply run the following command into a terminal.

    ```
        >>> python -m langdict -l <target language> -p <path to .xlsx file>
    ```

    LangDict will then add the translated words to the given .xlsx file. (An
    optional `-c true` tag can be included in the command above to tell landict
    to create a seperate .xlsx file, instead of adding the words to the original.)

"""

from setuptools import setup, find_packages

setup(
        name='LangDict',
        author='Josh Anderson',
        description='LangDict is a python package used as an aide in language acquisition',
        long_description=__doc__,
        version='0.1.0.dev',
        install_requires=['requests>=2.25', 'openpyxl>=3.0'],
        packages=find_packages(),
     )
