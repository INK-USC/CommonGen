# UniLM V2


## Installation

```bash
conda create -n unilmv2 python=3.7
conda activate unilmv2
pip install torch==1.4.0
git clone https://github.com/NVIDIA/apex.git && cd apex && python setup.py install --cuda_ext --cpp_ext
cd ..
```

The following Python package need to be installed:
```bash
pip install --user methodtools py-rouge pyrouge nltk
python -c "import nltk; nltk.download('punkt')"
git clone https://github.com/NVIDIA/apex.git && cd apex && python setup.py install --cuda_ext --cpp_ext
```

Prepare data:
```bash
python prepare_data.py
```


Install the repo as a package:
```bash
cd unilm/s2s-ft ; pip install --editable .
```



## Train and test for UniLM V2

- Training

```bash
# path of training data
# folder used to save fine-tuned checkpoints
# folder used to cache package dependencies
TRAIN_FILE=../../commongen.train.json
OUTPUT_DIR=../../tmp/finetuned_models
CACHE_DIR=../../tmp/transformer_package_cache

export CUDA_VISIBLE_DEVICES=3
python -m torch.distributed.launch --nproc_per_node=1 run_seq2seq.py \
  --train_file ${TRAIN_FILE} --output_dir ${OUTPUT_DIR} \
  --model_type unilm --model_name_or_path unilm1.2-base-uncased \
  --do_lower_case --fp16 --fp16_opt_level O2 --max_source_seq_length 64 --max_target_seq_length 64 \
  --per_gpu_train_batch_size 32 --gradient_accumulation_steps 1 \
  --learning_rate 3e-5 --num_warmup_steps 500 --num_training_epochs 30 --cache_dir ${CACHE_DIR}
```

- Decoding

```bash
# path of the fine-tuned checkpoint
#MODEL_PATH=tmp/finetuned_models/ckpt-1500
MODEL_PATH=../../tmp/finetuned_models/ckpt-63177
SPLIT=test
# input file that you would like to decode
INPUT_JSON=../../commongen.${SPLIT}.json

export CUDA_VISIBLE_DEVICES=2
export OMP_NUM_THREADS=4
export MKL_NUM_THREADS=4

python new_decode_seq2seq.py \
  --fp16 --model_type unilm --tokenizer_name unilm1.2-base-uncased --input_file ${INPUT_JSON} --split ${SPLIT} --do_lower_case \
  --model_path ${MODEL_PATH} --max_seq_length 128 --max_tgt_length 64 --batch_size 8 --beam_size 5 \
  --length_penalty 0 --forbid_duplicate_ngrams --mode s2s --forbid_ignore_word "."

SPLIT=dev
INPUT_JSON=../../commongen.${SPLIT}.json
python new_decode_seq2seq.py \
  --fp16 --model_type unilm --tokenizer_name unilm1.2-base-uncased --input_file ${INPUT_JSON} --split ${SPLIT} --do_lower_case \
  --model_path ${MODEL_PATH} --max_seq_length 128 --max_tgt_length 64 --batch_size 8 --beam_size 5 \
  --length_penalty 0 --forbid_duplicate_ngrams --mode s2s --forbid_ignore_word "."
```

- The decoding results are saved at `${MODEL_PATH}.${SPLIT}` (eg ../../tmp/finetuned_models/ckpt-1500.test) .
```bash
mv ../../tmp/finetuned_models/ckpt-63177.test ../../unilmv2.test
mv ../../tmp/finetuned_models/ckpt-63177.dev ../../unilmv2.dev
```
