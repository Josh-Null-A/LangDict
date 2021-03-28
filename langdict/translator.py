import os
import sys
import openpyxl

from . import path_utils
from .backends import *

class Translator:
    def __init__(self, l, p, c, s):
        """
            The Translator class translates words into a target language.
        """

        self.l = l
        self.p = p
        self.c = c

        # If -s is 'google' change the backend
        if s.lower() == 'google':
            self.backend = GoogleBackend(l)
        else:
            self.backend = CambridgeBackend(l)

    def translate(self):
        """
            The main function for the Translator class.

            Starts to webscrape for translations for the given dictionary,
            and places them inside a .xlsx file.
        """

        # Change the systems path to the path of the original .xlsx file
        pathname = path_utils.get_file_path(self.p)
        sys.path.insert(1, pathname)
        os.chdir(sys.path[1])

        # Open a read (r_) and write (w_) xlsxwriter workbook
        r_dictionary = openpyxl.load_workbook(path_utils.get_file_name(self.p))
        if self.c == True:
            w_dictionary = openpyxl.Workbook('dictionary.xlsx')
        else:
            w_dictionary = r_dictionary

        # Get the english words from the dictionary
        english    = self.get_english(r_dictionary)
        print(english)

        # Translate the word into the target language
        translated = self.backend.scrape_translations(english)

        # Put the translated words into a .xlsx workbook
        self.add_translations(w_dictionary, english, translated)

    def get_english(self, dictionary):
        """
            Gets a list of english words from a .xlsx file in each sheet.

            Important:
                It is assumed that the vocab to translate all belongs on the
                'A' column of each sheet.

                It is assumed that is LangDict encouters a cell with no value,
                then the end of the column has been reached. This means you
                should not have empty cells next to vocab you wish to translate.

            Args:
                dictionary -: Workbook :- A dictionary of vocab to translate

            Returns:
                vocab -: dict :- A dict contaning a list of vocab for each sheet
        """

        vocab = {}
        for sheet in dictionary:
            sheet_vocab = []

            for cell in sheet['A']:
                if cell.value is None:
                    break
                sheet_vocab.append(cell.value)

            vocab[sheet.title] = sheet_vocab
        return vocab

    def add_translations(self, dictionary, english, translated):
        pass
