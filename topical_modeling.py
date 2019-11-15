from infant_pipe import pdf_extract, process
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd
import mglearn
import numpy as np
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS

vect = CountVectorizer(ngram_range=(1,1), stop_words='english')
circular_content = process(pdf_extract('001.pdf'))
dtm = vect.fit_transform([circular_content])

#print(pd.DataFrame(dtm.toarray(), columns=vect.get_feature_names()))
print(type(circular_content))
lda = LatentDirichletAllocation(n_components=5)

lda_dtf = lda.fit_transform(dtm)

sorting = np.argsort(lda.components_)[:,::-1]
features = np.array(vect.get_feature_names())
#print(mglearn.tools.print_topics(topics = range(5), feature_names=features, sorting=sorting, topics_per_chunk=5, n_words=10))
#str_circular_content = str(circular_content)
