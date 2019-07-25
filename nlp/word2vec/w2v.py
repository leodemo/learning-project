# encoding=utf-8
# This Program is written by Victor Zhang at 2016-08-01 23:04:21
#
#
import logging
import os

import numpy as np
from gensim.models.word2vec import Word2Vec
from gensim.models.keyedvectors import KeyedVectors


class Word2VecModel():
    def __init__(self):
        # For masking purpose
        self.index2word = {0: 'Nil'}
        self.word2index = {'Nil': 0}
        self.model = None
        self.embedding = None
        self.dicSize = 0
        self.length = 0

    def read_file(self,filename):
        ifile=open(filename,'r')
        st=[]
        for line in ifile:
            at=line.strip().split(' ')
            st.append(at)
        return st


    def train_word2vec_model(self, st):
        # if you wanna train a new model, use train_model()
        if os.path.exists("./models/embedding.txt") and os.path.exists("./models/vocab.txt") and os.path.exists(
                "./models/word2vec.model"):
            self.model = self.load_model()
        else:
            self.model = self.train_model(st)
        return self.model

    def set_dict(self):
        if self.model is not None:
            i = 1
            for word in self.model.index2word:
                self.index2word[i] = word
                self.word2index[word] = i
                i += 1
            # print("i=",i)

    def set_save_dict(self):
        if self.model is not None:
            i = 1
            for word in self.model.wv.index2word:
                self.index2word[i] = word
                self.word2index[word] = i
                i += 1

    def get_index(self, word):
        word = word.lower()
        if word in self.word2index:
            return self.word2index[word]
        else:
            return 0

    def get_seq(self,words):
        return [self.get_index(word) for word in words]

    def get_word(self, index):
        if index in self.index2word:
            return self.index2word[index]
        else:
            return None

    def get_vector_by_index(self, index):
        return self.embedding[index]


    def get_vector(self, word):
        if word in self.word2index:
            return self.embedding[self.word2index[word]]
        else:
            return None

    def get_avg_vector(self,sent):
        isum=np.zeros((self.length))
        cnt=0
        for word in sent.split(' '):
            vec=self.get_vector(word)
            if vec is not None:
                isum+=vec
                cnt+=1
        if cnt!=0:
            isum/=cnt
        return isum


    def get_sen_vector(self, sent):
        return self.get_seq(sent.split(' '))

    def train_model(self, st, size=200, window=5, min_count=5):
        logging.info('Trainning Word2Vec model')
        self.model = Word2Vec(st, size=size, window=window, min_count=min_count)
        self.embedding = self.model.wv.syn0
        self.dicSize, self.length = self.embedding.shape
        zeros=np.zeros((1,self.length))
        self.embedding=np.r_[zeros,self.embedding]

        # print(self.embedding[:5,:])
        # print(type(self.model.index2word))
        # print("Embedding Size",self.embedding.shape)
        self.set_save_dict()
        self.save_model(self.model)
        return self.model

    def save_model(self, model):
        logging.info('Saving Word2Vec model')
        model.wv.save_word2vec_format("./models/word2vec.model",binary=False)
        np.savetxt("./models/embedding.txt", self.embedding)
        ifile = open("./models/vocab.txt", 'w')
        for word in model.wv.index2word:
            ifile.write("%s\n" % (word))
        ifile.close()

    def load_model(self):
        logging.info('Loading Word2Vec model')
        self.model = KeyedVectors.load_word2vec_format("./models/word2vec.model",binary=False)
        self.embedding = np.loadtxt('./models/embedding.txt')
        self.dicSize, self.length = self.embedding.shape
        # print(self.dicSize, self.length)
        self.set_dict()
        return self.model

    def get_embedding(self):
        return self.embedding

    def generate_embed_matrix(self,sequence):
        n,m=sequence.shape
        matrix=np.empty((n,m,self.length))
        # print(matrix.shape)
        for j in range(n):
            vectors=np.empty((m,self.length))
            for i,x in enumerate(sequence[j,:]):
                vectors[i,:]=self.embedding[x,:]
            # print(vectors.shape)
            matrix[j,:,:]=vectors
        # print(matrix)
        return matrix


if __name__ == '__main__':
    # 使用方法：在total.txt中存入分好词的文本，空格隔开、一行一句
    # 在运行文件夹中需要新建名为 models 的文件夹
    st=model.read_file('total.txt')
    model.train_model(st)
