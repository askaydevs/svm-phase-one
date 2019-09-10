#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:26:28 2019

@author: askaydevs (sk_singh18@outlook.com)
"""
import PyPDF2
import os
from os import listdir
from os.path import isfile, join
import re
import spacy
from tika import parser

path = 'Solverminds_Data/Sample'

def pdf_extract(file, dir_path = 'Solverminds_Data/Sample'):
    extract = join(dir_path, file)
    file_data = parser.from_file(extract)
    text = file_data['content'].strip()
    #text = text[73:]
    text = str(text.strip())
    return text
#print(processed)
def process(text):
    processed = re.sub(r'[^\w\s]', ' ', text)
    processed = text.replace('\n', ' ')
    #processed = re.sub(' +', ' ', processed)
    processed = processed.strip()
    return processed

def input_writer():
    if not os.path.exists('test_input.txt'):
        with open('test_input.txt', 'wb') as f:
            f.write(b + processed)
            print("Transformation done successfully!!\n")
        f.close()

def rem_hf_panama(fr_text): # TODO: def rem_hf_hongkong
    fr_text = fr_text.strip()
    return fr_text[172:len(fr_text)-260:1] # This setting is specific to panama documents

def get_body(text):
    #text = rem_hf_panama(text)
    index = []
    for _ in re.findall(' +', text):
        index.append(text.find(_))
    for i in range(0, len(index)):
        if (index[i+1] > index[i]):
            indice = index[i + 1]
            break
        else:
            i += 1
    return text[indice:len(text):1].strip()
