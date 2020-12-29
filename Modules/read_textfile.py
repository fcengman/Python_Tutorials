# This module contains functions used for reading text files.

def add_txt(file_name):
    '''This function adds .txt extention if necessary.'''
    if file_name.endswith(".txt"):
        return file_name
    else:
        return file_name + ".txt"


def open_file(file_name):
    '''This function tries to open a text file.'''
    try:
        file = open(file_name, 'r')
    except IOError:
        print("There is no \'{0}\' in this directory.\n".format(file_name))
        return False
    else:
        return file
