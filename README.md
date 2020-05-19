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
pip3 install -r requirements.txt
```
NOTE: If you have MemoryError in the install try to use:
```
pip3 install -r requirements.txt --no-cache-dir
```
Note that Project currently support Tensorflow = 1.15. We tested it on Tensorflow 1.15.0
By this point, your system should be ready with all dependencies. Please use below command to check Tensorflow verion.
```
python -c "import tensorflow; print(tensorflow.__version__)"
```
Output should be your Tensorflow version = 1.15.0
If you still face any issues while installing dependencies for the project, feel free to raise issue.

### Process :

Here we perform Machine Translation on a Low-Resource Language, Sanskrit. For this purpose, the following steps were performed : 

1. We used NEMATUS to train Hi-En NMT Model.
2. This Pretrained Model is used as the base for training our Sa-En Machine Translation Model.

### Preprocessing :

#### 1. For English-Hindi NMT Model -
We used the IIT Bombay English-Hindi Corpus consisting of 1.56M parallel lines. The data was tokenized using the IndicNLP tokenizer for hindi and Moses tokenizer for English. 
```
Hindi :
python ./IndicNLP/indicnlp/tokenize/indic_tokenize.py ./data/hi.txt ./data/en-hi.hi.all hi
Output File : /data/en-hi.hi.all 

English :
perl ./data/tokenizer.perl -l en < ./data/en.txt > ./data/en-hi.en.all
Output File : /data/en-hi.en.all 
```
The Tokenized data is used for training procedure after applying Byte-pair Encoding using Subword-nmt. 
```
Hindi :
subword-nmt learn-bpe -s 16000 < ./data/en-hi.hi.all > ./data/hindi_codes    

// hindi_codes file created in the data folder.

subword-nmt apply-bpe -c ./data/hindi_codes < ./data/en-hi.hi.all > ./data/train.hi-en.hi

// train.hi-en.hi file created in the data folder.

English :
subword-nmt learn-bpe -s 16000 < ./data/en-hi.en.all > ./data/eng_codes

// eng_codes file created in the data folder.

subword-nmt apply-bpe -c ./data/eng_codes < ./data/en-hi.en.all > ./data/train.hi-en.en

// train.hi-en.en file created in the data folder.
```

#### 2. For Sanskrit-English NMT Model - 
We used the Sa-en corpus consisting of 6K parallel lines. The data was tokenized using the IndicNLP tokenizer for Sanskrit and Moses tokenizer for English.
```
Sanskrit :
python ./IndicNLP/indicnlp/tokenize/indic_tokenize.py ./data/Sanskrit-English/sanskritdatasupervised.txt ./data/Sanskrit-English/en-sa.sa.all sa

// en-sa.sa.all file created in the data folder.

English :
perl ./data/tokenizer.perl -l en < ./data/Sanskrit-English/englishdatasupervised.txt > ./data/Sanskrit-English/en-sa.en.all

// en-sa.en.all file created in the data folder.
```
The Tokenized data is used for training procedure after applying Byte-pair Encoding using Subword-nmt. 
```
Sanskrit :
subword-nmt learn-bpe -s 4000 < ./data/Sanskrit-English/en-sa.sa.all > ./data/Sanskrit-English/en-sa.sa.codes

// en-sa.sa.codes file created in the data folder.

subword-nmt apply-bpe -c ./data/Sanskrit-English/en-sa.sa.codes < ./data/Sanskrit-English/en-sa.sa.all > ./data/Sanskrit-English/en-sa.sa.bped

// en-sa.sa.bped file created in the data folder.

English :
subword-nmt learn-bpe -s 2000 < ./data/Sanskrit-English/en-sa.en.all > ./data/Sanskrit-English/en-sa.en.codes

// en-sa.en.codes file created in the data folder.

subword-nmt apply-bpe -c ./data/Sanskrit-English/en-sa.en.codes < ./data/Sanskrit-English/en-sa.en.all > ./data/Sanskrit-English/en-sa.en.bped

// en-sa.en.bped file created in the data folder.

Use the following files to split data into train, test and valid :

python data/Sanskrit-English/docen.py

// train.en-sa.en, valid.en-sa.en, test.en-sa.en file created in the data folder.

python data/Sanskrit-English/docsn.py

// train.en-sa.sa, valid.en-sa.sa, test.en-sa.sa file created in the data folder.
```

### Training : 

1. For the Hi-En NMT : 

Firstly concatenated Sn-En and Hi-En parallel data were used to generate dictionary file required in nematus NMT.

```
cat ./data/train.hi-en.hi ./data/Sanskrit-English/en-sa.sa.bped > ./data/train_hindi

// train_hindi file created in the data folder.

cat ./data/train.hi-en.en ./data/Sanskrit-English/en-sa.en.bped > ./data/train_english 

// train_english file created in the data folder.

python data/build_dictionary.py ./data/train_hindi ./data/train_english

// train_english.json, train_hindi.json  file created in the data folder.

```

Following command was used for training purpose, we trained it for 80000 iterations :  
```
python nematus/train.py --source_dataset data/train_hindi --target_dataset data/train_english --dictionaries data/train_hindi.json data/train_english.json --save_freq 30000 --model model.hi-en --model_type transformer --embedding_size 128 --state_size 128 --tie_decoder_embeddings --loss_function per-token-cross-entropy --label_smoothing 0.1 --exponential_smoothing 0.0001 --optimizer adam --adam_beta1 0.9 --adam_beta2 0.98 --adam_epsilon 1e-09 --learning_schedule transformer --maxlen 100 --batch_size 16 --token_batch_size 4096 --valid_source_dataset data/valid.hi-en.hi --valid_target_dataset data/valid.hi-en.en --valid_batch_size 16 --valid_token_batch_size 4096

```
2. For the Sn-En NMT : 

Following command was used for training purpose :
```
CUDA_VISIBLE_DEVICES=0 python nematus/train.py --source_dataset data/en-sa.sa.train --target_dataset data/en-sa.en.train --dictionaries data/train_hindi.json data/train_english.json --save_freq 20000 --model model.sa-en --model_type transformer --embedding_size 128 --state_size 128 --tie_decoder_embeddings --loss_function per-token-cross-entropy --label_smoothing 0.1 --exponential_smoothing 0.0001 --optimizer adam --adam_beta1 0.9 --adam_beta2 0.98 --adam_epsilon 1e-09 --learning_schedule transformer --maxlen 200 --batch_size 32 --token_batch_size 2048 --valid_source_dataset data/en-sa.sa.valid --valid_target_dataset data/en-sa.en.valid --valid_freq 5000 --valid_batch_size 32 --valid_token_batch_size 2048 --reload ./model.hi-en-80000

--reload : location of hi-en model
```

###### Translation Results
Translation results are available in translation_results folder for all input data. Please use the below command to translate new       Sanskrit phrase to English phrase. We are assuming you have a text file placed in data folder as data_test.txt.
```
python nematus/translate.py -b 32 -v -k 12 -i ./data/en-sa.sa.test -o ./data/en-out -m ./Pretrained_Model/model.sa-enge-106500
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
