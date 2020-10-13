# GPT-2


## Installation

```bash
conda create -n gpt2 python=3.7
conda activate gpt2
pip install torch==1.4.0
git clone https://github.com/NVIDIA/apex.git && cd apex && python setup.py install --cuda_ext --cpp_ext
```

Install the repo as a package:
```bash
cd transformers_local ; pip install --editable .
```



## Train and test for GPT-2

- Pre-processing

We process the training data into following format to use GPT-2 to perform seq2seq tasks :

"[SOS] Concept_1 Concept_2 .. Concept_n = output_token_1 output_token_2 ... output_token_n [EOS]"

And inference with a prefix like:

"[SOS] Concept_1 Concept_2 .. Concept_n = "
```bash
cd ..
cp ../../dataset/final_data/commongen/commongen.train.src_alpha.txt train.src
cp ../../dataset/final_data/commongen/commongen.train.tgt.txt train.tg
cp ../../dataset/final_data/commongen/commongen.dev.src_alpha.txt dev.src
cp ../../dataset/final_data/commongen/commongen.dev.tgt.txt dev.tgt
cp ../../dataset/final_data/commongen/commongen.test.src_alpha.txt test.src
python convert_to_gpt2.py
```

- Training

```bash
CUDA_VISIBLE_DEVICES=4 python transformers_local/examples/run_language_modeling.py \
  --output_dir=tmp/new-gpt-2 \
  --model_type=gpt2 \
  --model_name_or_path=gpt2 \
  --do_train \
  --do_eval \
  --evaluate_during_training  \
  --train_data_file=train.txt \
  --eval_data_file=dev.txt \
  --line_by_line \
  --block_size 128 \
  --num_train_epochs 5 \
  --learning_rate 5e-5 \
  --warmup_steps 400 \
  --logging_steps 50 \
  --save_steps 50 \
  --per_gpu_train_batch_size 32 \
  --gradient_accumulation_steps 4 \
  --overwrite_output_dir
```

- Decoding

```bash
# test data
python transformers_local/examples/run_generation_gpt.py \
  --model_type=gpt2 \
  --model_name_or_path=tmp/new-gpt-2/checkpoint-2600 \
  --input_file inference_test.txt \
#  --model_name_or_path=tmp/new-gpt-2/checkpoint-650

# dev data
python transformers_local/examples/run_generation_gpt_backup.py \
  --model_type=gpt2 \
  --model_name_or_path=tmp/new-gpt-2/checkpoint-2600 \
  --input_file inference_dev.txt


# for csqa
#############################################################################
#CUDA_VISIBLE_DEVICES=4 python transformers_local/examples/run_generation_train_csqa_gpt.py \
#  --model_type=gpt2 \
#  --model_name_or_path=tmp/new-gpt-2/checkpoint-2600 \
#  --input_file inference_train_csqa.txt 

#CUDA_VISIBLE_DEVICES=4 python transformers_local/examples/run_generation_dev_csqa_gpt.py \
#  --model_type=gpt2 \
#  --model_name_or_path=tmp/new-gpt-2/checkpoint-2600 \
#  --input_file inference_dev_csqa.txt 

#cp gpt2.csqa.train ../../evaluation/csqa/csqa.train.qac.gpt2.res
#cp gpt2.csqa.dev ../../evaluation/csqa/csqa.dev.qac.gpt2.res
```

- The dev decoding results are saved at "decode_result_dev". The test decoding results are saved at "decode_result". You can run clean_output.py to generate the final output used for evaluation.
```bash
python clean_output.py
```
