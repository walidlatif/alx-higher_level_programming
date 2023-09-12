#!/usr/bin/python3
'''Module : append_write '''


def append_write(filename="", text=""):
    '''
        Appends a string at the end of a text file

        Args:
            filename (str): The name of the file.
            text (str): The text to be written to the file.

        Returns:
            int: The number of characters written to the file.
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
