# Sanskrit-Machine-Translation

### Abstract
---


### Project Update
---
##### The Project is completed by implementing Machine Translation in two ways :
1. Supervised MT : Through Transformers
2. Unsupervised MT : Through Dual Learning



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
Note that Project currently support PyTorch >= 1.4
By this point, your system should be ready with all dependencies. Please use below command to check PyTorch verion.
```
python -c "import torch; print(torch.__version__)"
```
Output should be your PyTorch version >= 1.4.0
If you still face any issues while installing dependencies for the project, feel free to ping us at our Communication channel.

#### - For Dual Learning 

For performing MT using deep reinforcement learning, we have trained the following models :
1.	Language model for English
2.	Language model for Sanskrit
3.	Sanskrit - English NMT Model
4.	English - Sanskrit NMT Model

###### Translation Results
Translation results are available in translation_results folder for all input data. Please use the below command to translate new Sumerian phrase to English phrase. We are assuming you have a text file placed in data folder as data_test.txt.
```
cd nmt
./scripts/test.sh *src* *tgt* *mdl* *txt*
```
Here specify the Source File location, Target file location, Pretrained Model location and the Output/ Prediction File Location.

To compute the BLEU Score, use : 
```
perl multi-bleu.perl data/test.de-en.en < out/decode.txt
```
