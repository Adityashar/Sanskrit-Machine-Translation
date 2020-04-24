# Sanskrit-Machine-Translation

### Abstract
---


### Project Update
---
##### The Project is completed by implementing Machine Translation in two ways :
1. NMT Through Transformers
2. NMT through Transfer Learning

## 1. For Transfer Learning

### Installation

Clone the repository. (We are assuming you have python version 3.6.x and pip is installed on your linux system)
(Optional)If not, please use the below command, this will create a new environment using conda.

```
conda create -n env python=3.6
conda activate env
```
All dependencies can be installed via:
```
pip install -r requirements.txt
```
NOTE: If you have MemoryError in the install try to use:
```
pip install -r requirements.txt --no-cache-dir
```
Note that Project currently support Tensorflow >= 1.15. We tested it on Tensorflow 1.15.0
By this point, your system should be ready with all dependencies. Please use below command to check PyTorch verion.
```
python -c "import tensorflow; print(tensorflow.__version__)"
```
Output should be your PyTorch version >= 1.15.0
If you still face any issues while installing dependencies for the project, feel free to ping us at our Communication channel.

### Process :

Here we perform Machine Translation on a Low-Resource Language, Sanskrit. For this purpose, the following steps were performed : 

1. We used NEMATUS to train Hi-En NMT Model.
2. This Pretrained Model is used as the base for training our Sa-En Machine Translation Model.

### Training :

#### 1. For English-Hindi NMT Model -
We used the IIT Bombay English-Hindi Corpus consisting of 1.56M parallel lines. The data was tokenized using the IndicNLP tokenizer for hindi and Moses tokenizer for English. The Tokenized data is used for training procedure after applying Byte-pair Encoding using Subword-nmt. Following command was used for training purpose : 
```
python data/build_dictionary.py `hindi_training` `english_training`

python nematus/train.py --source_dataset `training_hindi` --target_dataset `training_english` --dictionaries `hindi_training.json` `english_training.json` --save_freq 30000 --model model.hi-en --model_type transformer --embedding_size 128 --state_size 128 --tie_decoder_embeddings --loss_function per-token-cross-entropy --label_smoothing 0.1 --exponential_smoothing 0.0001 --optimizer adam --adam_beta1 0.9 --adam_beta2 0.98 --adam_epsilon 1e-09 --learning_schedule transformer --maxlen 100 --batch_size 64 --token_batch_size 4096 --valid_source_dataset `validation_hindi` --valid_target_dataset `validation_english` --valid_batch_size 64 --valid_token_batch_size 4096

```
#### 2. For Sanskrit-English NMT Model - 
We used the Sa-en corpus consisting of 6K parallel lines. The data was tokenized using the IndicNLP tokenizer for Sanskrit and Moses tokenizer for English.
```
Sanskrit :
python ./IndicNLP/indicnlp/tokenize/indic_tokenize.py ./data/Sanskrit-English/englishdatasupervised.txt ./data/en-sa.sa.all sa

English :
./data/tokenizer.perl -l en < ./data/Sanskrit-English/englishdatasupervised.txt > ./data/en-sa.en.all
```
The Tokenized data is used for training procedure after applying Byte-pair Encoding using Subword-nmt. Following command was used for training purpose :
```
CUDA_VISIBLE_DEVICES=0 python nematus/train.py --source_dataset data/en-sa.sa.train --target_dataset data/en-sa.en.train --dictionaries data/hindi/train.hi-en.hi.json data/hindi/train.hi-en.en.json --save_freq 20000 --model model.sa-enge --model_type transformer --embedding_size 128 --state_size 128 --tie_decoder_embeddings --loss_function per-token-cross-entropy --label_smoothing 0.1 --exponential_smoothing 0.0001 --optimizer adam --adam_beta1 0.9 --adam_beta2 0.98 --adam_epsilon 1e-09 --learning_schedule transformer --maxlen 200 --batch_size 32 --token_batch_size 2048 --valid_source_dataset data/en-sa.sa.valid --valid_target_dataset data/en-sa.en.valid --valid_freq 5000 --valid_batch_size 32 --valid_token_batch_size 2048 --reload ./Pretrained_Model/model.hi-eng-80000
```

###### Translation Results
Translation results are available in translation_results folder for all input data. Please use the below command to translate new       Sanskrit phrase to English phrase. We are assuming you have a text file placed in data folder as data_test.txt.
```
cd nematus
python translate.py -b 32 -v --k 12 --i ./data/en-sa.sa.test --o ./data/en-out --m ./Pretrained_Model/model.sa-enge-106500
```
Here specify the Source File location, Target file location, Pretrained Model location and the Output/ Prediction File Location.

To compute the BLEU Score, use : 
```
Decoding BPE for Test file and Translated File : 

cat data/en-sa.en.test | sed -E 's/(@@ )|(@@ ?$)//g' > en-sa.en.test.bpe
cat data/en-out | sed -E 's/(@@ )|(@@ ?$)//g' > data/sa-en.out

Calculating BLEU : 

perl data/multi-bleu.perl data/en-sa.en.test.bpe < data/sa-en.out
```
