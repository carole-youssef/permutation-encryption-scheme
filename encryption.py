#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:37:40 2022

@author: macbook
"""
#task: encrypt a plain text using a key, then use encrypted message and key to decrypt it back to original text
#writing down functions needed to implement task

# this function uses a plain text and key to encrypt a message and produce its cipher text
# it accepts plain text and key as its arguments, and returns a cipher text
# the cipher text is intialised to an empty list
# a for loop is used to go through every character in the plain text
# then, it is mapping the key's element to the plain text's corresponding element... 
# ... and appending that to cipher text list

def encrypt(plain_text, key):
    cipher_text = []  
    for element in plain_text: 
        
        cipher_text.append(key[element])
    return cipher_text 


# creating a find function to return the index of first occurence of each of the element in cipher text 
# it accepts a list and an element/ character, and returns an index
# the index is initialised to 0
# it goes through every character in the list with a for loop
# if character in list is the same as the element (in cipher text), the loop breaks
# if not, then the index is incremented 
# if index is equal to the length of list, then return none

def find (list1, c): 
    i = 0 
        
    for char in list1: 
        if char == c: 
            break 
        else:
            i+=1 
    if i == len(list1):
        return None
    
    return i 

# this function uses a cipher text and key to decrypt the message and produce its plain text 
# it accepts cipher text and key as its arguments, and returns the new plain text
# the new plain text is intialised to an empty list 
# a for loop is used to go through every character in the cipher text  
# then, it's mapping the key's element to the plain text's corresponding element using find function...
# ...and appending that to new plain text list

def decrypt(cipher_text,key): 
    plain_text1 = []          
    for element in cipher_text: 

        plain_text1.append(find(key,element))         
    return plain_text1  
   
    
# function to read the necessary files needed for encrytion and decrytion 
# passing the file name as my arguments, returns file contents
# opening the file for read in binary mode
# reading the contents of the file
# closing file

def read_file(file_name): 

    ThisFile = open(file_name,"rb")
    content = ThisFile.read() 
    
    ThisFile.close() 
    return content 

# writing the contents we need to grab (from the encrypt + decrypt fucntions) to a new file 
# passing the file name and content as my arguments, returns the file
# opening file for write in binary mode
# writing the contents to the file in bytes 
# closing file

def write_file(file_name, content):
    
    ThisFile = open(file_name, "wb") 
    content_enc = bytes(content) 
    ThisFile.write(bytes(content_enc)) 
    
    ThisFile.close() 
    return ThisFile  
    

# this function tests the functions above and checking if the original plain text = the new plain text
# reads the key file
# reads the plain text file
# uses the encrypt function to find the cipher text
# writes the cipher text (the contents) to its corresponding file
# reads the cipher text file  
# uses the decrypt function to find the new plain text - should be equal to original plain text 
# writes the new plain text (the contents) to its corresponding file
# returns the new plain text - just for checking

def test_encryption():  
    key = read_file('key') 
    plain_text = read_file('plain_text') 
    cipher_text = encrypt(plain_text,key) 
    write_file('cipher_text', cipher_text) 
    read_file('cipher_text') 
    plain_text1 = decrypt(cipher_text, key) 
    write_file('plain_text1', plain_text1) 
    
    return read_file('plain_text1') 


# output just to check if program works correctly
print(test_encryption()) 