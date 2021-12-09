# T5


## Installation

```bash
conda create -n t5 python=3.6
conda activate t5
pip install torch===1.4.0 -f https://download.pytorch.org/whl/torch_stable.html
pip install pytorch-lightning
#conda install pytorch torchvision cudatoolkit=10.1 -c pytorch==1.4.0 -n t5
mkdir tmp
cd tmp
git clone https://github.com/NVIDIA/apex.git && cd apex && python setup.py install --cuda_ext --cpp_ext
```

Install the repo as a package:
```bash
cd transformer_local ; pip install --editable .
```



## Train and test for T5

- Pre-processing

We process the source training data into following format to use T5 to perform seq2seq tasks :

"generate a sentence with: Concept_1 Concept_2 .. Concept_n"
```bash
cd examples/summarization/bart
mkdir commongen
cp ../../../../../../dataset/final_data/commongen/commongen.train.src_alpha.txt commongen/train.source
cp ../../../../../../dataset/final_data/commongen/commongen.val.src_alpha.txt commongen/val.source
cp ../../../../../../dataset/final_data/commongen/commongen.test.src_alpha.txt commongen/test.source
cp ../../../../../../dataset/final_data/commongen/commongen.train.tgt.txt commongen/train.target
cp ../../../../../../dataset/final_data/commongen/commongen.val.tgt.txt commongen/val.target
cp ../../../../../../dataset/final_data/commongen/commongen.test.tgt.txt commongen/test.target
sed -i -e 's/^/generate a sentence with these concepts: /' commongen/*.source 
```

- Training

```bash
CUDA_VISIBLE_DEVICES=0,1,2 bash run_train.sh
#CUDA_VISIBLE_DEVICES=0,1,2,4 bash run_base.sh
```

- Decoding

```bash
CUDA_VISIBLE_DEVICES=4 bash run_gen.sh
```

- The decoding results are saved at "output.txt". You can further clean the output by runing clean_out.py. The final result is stored in t5.test.
```bash
python clean_out.py
```
