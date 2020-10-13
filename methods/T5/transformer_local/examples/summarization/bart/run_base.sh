export OUTPUT_DIR_NAME=bart_sum
export CURRENT_DIR=${PWD}
#export OUTPUT_DIR=${CURRENT_DIR}/${OUTPUT_DIR_NAME}

# Make output directory if it doesn't exist
#mkdir -p $OUTPUT_DIR

# Add parent directory to python path to access transformer_base.py
export PYTHONPATH="../../":"${PYTHONPATH}"

python finetune.py \
--n_gpu 3 \
--gradient_accumulation_steps=1 \
--warmup_steps 400 \
--data_dir=./commongen \
--model_name_or_path=t5-base \
--num_train_epochs 20 \
--learning_rate=5e-5 \
--train_batch_size=192 \
--eval_batch_size=192 \
--max_source_length=32 \
--max_target_length=32 \
--output_dir=./finetuned_t5_base \
--do_train
