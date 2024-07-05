#!/usr/bin/env bash

DATA_PATH=/p/realai/sneha/cornet2/CorNet/data
DATASET=EUR-Lex-2

python preprocess.py \
--text-path $DATA_PATH/$DATASET/train_texts.txt \
--label-path $DATA_PATH/$DATASET/train_labels.txt \
--vocab-path $DATA_PATH/$DATASET/vocab.npy \
--emb-path $DATA_PATH/$DATASET/emb_init.npy \
--w2v-model $DATA_PATH/glove.840B.300d.gensim

python preprocess.py \
--text-path $DATA_PATH/$DATASET/test_texts.txt \
--label-path $DATA_PATH/$DATASET/test_labels.txt \
--vocab-path $DATA_PATH/$DATASET/vocab.npy
