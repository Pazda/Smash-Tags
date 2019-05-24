# -*- coding: utf-8 -*-
"""
Created on Thu May 23 18:42:36 2019

@author: Tim
"""

import pysmash
import pickle, csv
from textgenrnn import textgenrnn

areTraining = False

if __name__ == "__main__":
    if areTraining:
        
        tagSet = []
        with open('tags', 'rb') as fp:
            tagSet = pickle.load(fp)
            
        if os.path.isfile( "tags_weights.hdf5" ):
        	os.remove( "tags_weights.hdf5" )
        if os.path.isfile( "tags_vocab.json" ):
        	os.remove( "tags_vocab.json" )
        if os.path.isfile( "tags_config.json" ):
        	os.remove( "tags_config.json" )
            
        textgen = textgenrnn( name='tags' )
        textgen.train_new_model(
        		tagSet,
        		#context_labels = context_labels,
        		num_epochs = 8,
        		gen_epochs = 0,
        		train_size = 0.9,
        		batch_size = 128,
        		rnn_layers = 5,
        		rnn_size = 128,
        		rnn_bidirectional = True,
        		max_length = 7,
        		max_words = 10000,
        		dim_embeddings = 100,
        		dropout = 0.0,
        		word_level = False )
        
    else:
        #Use existing model
        textgen = textgenrnn( weights_path = 'tags_weights.hdf5',
        vocab_path = 'tags_vocab.json',
        config_path = 'tags_config.json' )
        
    generated = textgen.generate( 3000, temperature=0.9, return_as_list=True )
    print(str(generated))
    
    #with open( 'outputs.csv', 'w' ) as outfile:
        #wr = csv.writer( outfile, quoting=csv.QUOTE_ALL )
        #wr.writerow( generated )
    
    #for name in generated:
        #print("[ " + name + " ]")