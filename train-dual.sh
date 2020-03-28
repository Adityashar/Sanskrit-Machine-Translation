#!/bin/bash

nmtdir=/home/rlabs/Documents/DualLearning/pytorch-dual-learning/nmt
#/data/groups/chatbot/dl_data/wmt16-small
lmdir=/home/rlabs/Documents/DualLearning/pytorch-dual-learning/lm
#/data/groups/chatbot/dl_data/lm
srcdir=/home/rlabs/Documents/DualLearning/pytorch-dual-learning/nmt
#/data/groups/chatbot/dl_data/wmt16-dual

nmtA=$nmtdir/modelSN/model.sn-en.iter10000.bin
nmtB=$nmtdir/modelen/model.en-sn.iter10000.bin

lmA=$lmdir/modelSN.pt
lmB=$lmdir/modelEN.pt
lmA_dict=$lmdir/data/sanskrit/dict.pkl
lmB_dict=$lmdir/data/english/dict.pkl

srcA=$srcdir/data/train.sn-en.sn
srcB=$srcdir/data/train.sn-en.en

saveA="modelSN"
saveB="modelEN"

python3 dual.py \
    --nmt $nmtA $nmtB \
    --lm $lmA $lmB \
    --dict $lmA_dict $lmB_dict \
    --src $srcA $srcB \
    --log_every 5 \
    --save_n_iter 100 \
    --alpha 0.001 \
    --model $saveA $saveB

