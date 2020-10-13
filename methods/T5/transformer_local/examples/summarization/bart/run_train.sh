export OUTPUT_DIR_NAME=bart_sum
export CURRENT_DIR=${PWD}
#export OUTPUT_DIR=${CURRENT_DIR}/${OUTPUT_DIR_NAME}

# Make output directory if it doesn't exist
#mkdir -p $OUTPUT_DIR

# Add parent directory to python path to access transformer_base.py
export PYTHONPATH="../../":"${PYTHONPATH}"

python finetune.py \
--n_gpu 3 \
--gradient_accumulation_steps=32 \
--warmup_steps 400 \
--data_dir=./commongen \
--model_name_or_path=t5-large \
--num_train_epochs 10 \
--learning_rate=2e-5 \
--train_batch_size=2 \
--eval_batch_size=2 \
--max_source_length=32 \
--max_target_length=32 \
--output_dir=./finetuned_t5_large \
--do_train