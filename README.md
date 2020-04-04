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

###### Translation Results
Translation results are available in translation_results folder for all input data. Please use the below command to translate new       Sanskrit phrase to English phrase. We are assuming you have a text file placed in data folder as data_test.txt.
```
cd nematus
python translate.py -b `batch-size` -v --k `beam-size` --i `input-path` --o `output-path` --m `model-path`
```
Here specify the Source File location, Target file location, Pretrained Model location and the Output/ Prediction File Location.

To compute the BLEU Score, use : 
```
perl data/multi-bleu.perl data/en-sa.sa.test < data/decode.txt
```
