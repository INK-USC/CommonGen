## UniLM: The state-of-the-art pre-trained language generation model

## Installation 

```bash
#conda create -n unilm_env python=3.6
#conda activate unilm_env
#conda install pytorch=1.3.0 torchvision cudatoolkit=10.0 -c pytorch -n unilm_env
conda create -n unilm python=3.6
conda activate unilm
pip install torch==1.4.0


# Install Apex
mkdir tmp
cd tmp
git clone https://github.com/NVIDIA/apex.git && cd apex
python setup.py install --cuda_ext --cpp_ext
#pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
cd ../../


# Build

pip install --user tensorboardX six numpy tqdm path.py pandas scikit-learn lmdb pyarrow py-lz4framed methodtools py-rouge pyrouge nltk
python -c "import nltk; nltk.download('punkt')"
pip install -e git://github.com/Maluuba/nlg-eval.git#egg=nlg-eval
cd unilm/src
pip install --user --editable .
cd ../../
```


Download pretrained model https://drive.google.com/open?id=1Zj_nZWO7YffaOInj3Q4SZyn09Mb3In-e and put it in the `tmp` folder.

## Train and test for UniLM 

- Train 
```bash
DATA_DIR=../../dataset/final_data/commongen/; \
OUTPUT_DIR=tmp/new_finetuned_models/; \
MODEL_RECOVER_PATH=tmp/unilmv1-large-cased.bin; \
export PYTORCH_PRETRAINED_BERT_CACHE=tmp/bert-cased-pretrained-cache; \
CUDA_VISIBLE_DEVICES=1,2 python unilm/src/biunilm/run_seq2seq.py --do_train --num_workers 0 \
  --bert_model bert-large-cased --new_segment_ids \
  --data_dir ${DATA_DIR} \
  --src_file commongen.train.src_alpha.txt \
  --tgt_file commongen.train.tgt.txt \
  --output_dir ${OUTPUT_DIR}/bert_save \
  --log_dir ${OUTPUT_DIR}/bert_log \
  --model_recover_path ${MODEL_RECOVER_PATH} \
  --max_seq_length 64 --max_position_embeddings 64 \
  --always_truncate_tail  --max_len_a 64 --max_len_b 64 \
  --mask_prob 0.7 --max_pred 20 \
  --train_batch_size 32 --gradient_accumulation_steps 1 \
  --learning_rate 0.00001 --warmup_proportion 0.1 --label_smoothing 0.1 \
  --num_train_epochs 30 \
#  --fp16 --amp
```
- Inference 

Generate decoded sentences on dev and test on model trained on the 10-th epoch. The generated sentences are under `tmp/decoded_sentences`.
```bash
mkdir decoded_sentences
cd decoded_sentences
mkdir dev
mkdir test
cd ..

# generate on dev dataset
CUDA_VISIBLE_DEVICES=4 bash decode_cs.sh 10 dev 
#CUDA_VISIBLE_DEVICES=0 bash decode_csqa.sh 10 csqa.dev
# generate on test dataset
CUDA_VISIBLE_DEVICES=1 bash decode_cs.sh 10 test 
#CUDA_VISIBLE_DEVICES=0 bash decode_csqa.sh 10 csqa.train
``` 