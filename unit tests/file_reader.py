#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: file_reader.py
# Author: John Doe
# Contact: (xyz@gmail.com)
# Copyright (c) 2020 - 2021 xyz Inc
###

def read_whole_file_as_str(filepath) -> str:
    '''
    Function to read the contents of the text file 

    @ parameters : 
        - filepath str : file location to read from

    @ output :
        - text blob of all the contents 

    @ example: 
        - filepath = 'c:/desktop/John Doe/Text_messages/romeojuliet_chat.txt'
        - output = Ah yes, young love. After all, the fair Juliet is only 21 years old
    '''

    with open(filepath, 'r') as f:
        data = f.read()

    return data


def read_whole_file_as_array(filepath) -> list:
    '''
    Function to read the contents of the text file per line

    @ parameters : 
        - filepath str : file location to read from

    @ output :
        - an array of text per line

    @ example: 
        - filepath = 'c:/desktop/John Doe/Text_messages/romeojuliet_chat.txt'
        - output = [Ah yes, young love,
                     After all, the fair Juliet,
                     is only 21 years old
                     ]
    '''

    with open(filepath, 'r') as f:
        data = f.readlines()

    return data


def check_name_in_line(text_array: list, search_string: str ) -> bool:
    '''
    fucntion to check if the name exist in the text file 

    @ input :
        - text_array : lines read from text file 

    @ output : 
        - instances where the name is identified

    @ example : 
        - text_array = [my name is John Doe, I live in Chicago, Illinois - 60605, I enjoy Football and Hockey]
        - search_string = Chicago
    
        - True as Chicago is present at 2nd line of the array 
    '''
    found_flag = False

    if type(text_array) == list:
        for line in text_array:
            if search_string in line:
                found_flag = True

    else:
        if search_string in text_array:
            found_flag = True

    return found_flag


def main():
    n = 0
    while n != "x":
        try:
            filepath = input('Enter the file location : ') 
            search_value = input(' Enter the string you are looking for ')
            read_nature = input(' Enter 1 to read whole text or 2 to read line by line ')

            if read_nature == '1':
                contents = read_whole_file_as_str(filepath= filepath) 
                print(check_name_in_line(text_array = contents, search_string = search_value))
            else:
                contents = read_whole_file_as_array(filepath= filepath) 
                print(check_name_in_line(text_array = contents, search_string = search_value))

        except Exception as e:
            print(f" ERROR : {e} ")
        
        n = input(' Enter letter x to exit ')


if __name__ == '__main__':
    main()

    
