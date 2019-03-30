import os
import collections
import random
import gensim

from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(common_texts)]
model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4)
# model.build_vocab(train_corpus)

# def read_corpus(fname, tokens_only=False):
#     with smart_open.smart_open(fname, encoding="iso-8859-1") as f:
#         for i, line in enumerate(f):
#             if tokens_only:
#                 yield gensim.utils.simple_preprocess(line)
#             else:
#                 # For training data, add tags
#                 yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])

# train_corpus = list(read_corpus(lee_train_file))
# test_corpus = list(read_corpus(lee_test_file, tokens_only=True))

