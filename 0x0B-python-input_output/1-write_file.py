#!/usr/bin/python3
'''Module : write_file '''


def write_file(filename="", text=""):
    '''
    Writes the specified text to the given file.

    Args:
         filename (str): The name of the file.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    '''
    with open(filename, 'w', encoding='utf-8') as f:
       return f.write(text)
