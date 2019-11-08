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
import nltk
from nltk.stem.snowball import SnowballStemmer
import numpy as np
import spacy
from spacy.attrs import LOWER, POS, ENT_TYPE, IS_ALPHA
from spacy.tokens import Doc
from sys import argv

#path = 'Solverminds_Data/Sample'

def pdf_extract(file, dir_path = 'Solverminds_Data/Sample'):
    text = ""
    with open(join(dir_path, file), 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        for _ in range(0, pdf.getNumPages()):
            page = pdf.getPage(_)
            text += page.extractText()
    return text.strip()
#print(processed)
def process(text):
    processed = text.replace('\n', ' ').replace('\r', '')
    processed = re.sub("\s\s+", " ", processed)
    #processed = re.sub(' +', ' ', processed)
    processed = processed.strip()
    return processed

def remove_tokens_on_match(doc):
    indexes = []
    for index, token in enumerate(doc):
        if(token.pos_ in ('PUNCT', 'SYM')):
            indexes.append(index)
        elif(token.is_stop):
            indexes.append(index)
    np_array = doc.to_array([LOWER, POS, ENT_TYPE, IS_ALPHA])
    np_array = np.delete(np_array, indexes, axis=0)
    doc2 = Doc(doc.vocab, words=[t.text for i, t in enumerate(doc) if i not in indexes])
    doc2.from_array([LOWER, POS, ENT_TYPE, IS_ALPHA], np_array)
    return doc2

def ngram_list(n, word_list, stop_word_list=None):
        """
        Generate ngrams with width n excluding those that are entirely formed of stop words

        Args:
            n (int): i.e. 1, 2, 3...
            word_list (list of str): list of words
            stop_word_list (list of str, Optional): list of words that should be excluded while obtaining
                                                    list of ngrams

        Returns:
            list of str: List of ngrams formed from the given word list except for those that have all their tokes in
                         stop words list
        """
        stop_word_set = set(stop_word_list) if stop_word_list else []
        all_ngrams = nltk.ngrams(word_list, n)
        ngram_list = []
        for ngram in all_ngrams:
            lowered_ngram_tokens = map(lambda token: token.lower(), ngram)
            if any(token not in stop_word_set for token in lowered_ngram_tokens):
                ngram_list.append(' '.join(ngram))
        return ngram_list

def nltk_stems(token_list):
    stems = []
    stemmer = SnowballStemmer("english")
    for token in token_list:
        stems.append(stemmer.stem(token))

    return stems

file_name = argv[1]
n = int(argv[2])

nlp = spacy.load('en_core_web_sm')
text = process(pdf_extract(file_name))
doc = nlp(text)
#print(remove_tokens_on_match(doc))
token_list = []
for token in remove_tokens_on_match(doc):
    token_list.append(token.text)

#print(ngram_list(n, token_list))
print(nltk_stems(token_list))
