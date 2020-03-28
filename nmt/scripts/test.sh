#!/bin/bash

#data_dir = "/home/rlabs/Documents/DualLearning/pytorch-dual-learning"
data_dir="./data"

src="$data_dir/test.sn-en.en"
tgt="$data_dir/test.sn-en.sn"
mdl="./modelSN.iter1000.bin"
txt="./out/ttoutn"

python3 nmt.py --mode test --test_src $src --test_tgt $tgt --load_model $mdl --save_to_file $txt --cuda
