# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:48:41 2022

@author: tazma
"""

# Caesar Cipher
'''
The cat sat on the mat

the cipher displaces the letters by a predetermined number.
Create an encryption and decryption function.
'''

def caesar_encrypt(text, num):
    '''
    Parameters
    ----------
    text : str
        the unencrypted phrase
    num : int
        the number of letters to shift for cypher

    Returns
    -------
    output : str
        the original text but with letters shifted

    TO DO:
    ------
    1. account for numbers or punctuation
    2. modulo is the better way to handle out of index problems
    '''
    print(f'Original Text: {text}')
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    enc_text = []
    un_text = text.lower().split()
    # print(f"un_text = {un_text}")
    
    for word in un_text:
        enc_word = ''
        for let in word:
            x = alpha.index(let)
            if x+num <= 25:
                enc_word += alpha[x+num]
            else:
                x = x+num - 25
                enc_word += alpha[x]
        enc_text.append(enc_word)
    output = ' '.join(enc_text)
    print(f'Encrypted Text: {output}')
    
    