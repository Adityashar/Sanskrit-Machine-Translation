#!/bin/sh

data_dir="./data"
vocab_bin="$data_dir/vocabEN.bin"
train_src="$data_dir/train.sn-en.en"
train_tgt="$data_dir/train.sn-en.sn"
dev_src="$data_dir/valid.sn-en.en"
dev_tgt="$data_dir/valid.sn-en.sn"
test_src="$data_dir/test.sn-en.en"
test_tgt="$data_dir/test.sn-en.sn"

job_name="en-sn"
model_name="model.${job_name}"

python3 nmt.py \
    --cuda \
    --mode train \
    --max_niter 100000 \
    --vocab ${vocab_bin} \
    --save_to ${model_name} \
    --log_every 300 \
    --valid_niter 5000 \
    --valid_metric ppl \
    --save_model_after 1 \
    --beam_size 5 \
    --batch_size 32 \
    --hidden_size 128 \
    --embed_size 128 \
    --uniform_init 0.1 \
    --dropout 0.2 \
    --clip_grad 5.0 \
    --lr_decay 0.5 \
    --train_src ${train_src} \
    --train_tgt ${train_tgt} \
    --dev_src ${dev_src} \
    --dev_tgt ${dev_tgt} \
    --load_model "$1"

