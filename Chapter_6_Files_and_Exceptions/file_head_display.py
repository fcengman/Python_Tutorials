# This program takes text file names as arguments and prints the first five lines of each text file given.


import sys  # sys to read command line arguments
# sys used to open text file and amend file name with .txt if necessary.
import read_textfile as read


def print_five_lines(file):
    '''This function prints the first five lines of the given text file. 

    Args:
        file (io.TextIOWrapper): A text file.
    '''
    for count in range(1, 6):
        file_line = file.readline()  # Reads next line in text file.

        ''' Prints line to terminal if not empty,'''
        if file_line != "":
            print("{0}: {1}".format(count, file_line), end="")
        else:
            break


def main():
    '''This function executes the program.'''

    print("You have entered {0} arguments.\n".format(len(sys.argv)-1))

    '''Continues if arguments have been included.'''
    if len(sys.argv) > 1:

        '''Iterates over the range of arguments, except for program name argument.'''
        for count in range(1, len(sys.argv)):

            # Adds extention if necessary.
            file_name = read.add_txt(sys.argv[count])
            # Attempts to read text file.
            file = read.open_file(file_name)
            print(type(file))

            '''Prints first five lines if reading files was successful.'''
            if file != False:
                print("The first five lines in \'{0}\' are:".format(
                    file_name))
                print_five_lines(file)
                file.close()

            print("")

    else:
        print("You did not include a filename in the arguments.")


main()  # Executes the program.
