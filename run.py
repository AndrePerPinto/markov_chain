'''
Created on 17/02/2019

@author: dinis
'''
from markov_python.cc_markov import MarkovChain

mc = MarkovChain()
mc.add_file("texto.txt")
words_list = mc.generate_text()
words_list = " ".join(words_list)
print (words_list)
