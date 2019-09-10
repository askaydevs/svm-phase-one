from infant_pipe import pdf_extract, process, path, rem_hf_panama, get_body
import pandas as pd
import spacy
import re
from os import listdir
from os.path import isfile, join

nlp = spacy.load('en_core_web_sm')

#uf_text = pdf_extract(path)
#fr_text = process(uf_text)
path = 'Solverminds_Data/Sample'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
#print(onlyfiles)
text = pdf_extract('001.pdf')
#print(text.find('June 19'))
#print(text)
print(get_body(text))
