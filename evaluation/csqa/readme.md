## CSQA with RoBERTa-Large on huggingface

```
CUDA_VISIBLE_DEVICES=0 python ./transformers/examples/multiple-choice/run_multiple_choice.py \
--model_type roberta \
--task_name csqa \
--model_name_or_path roberta-large \
--do_train \
--do_eval \
--do_lower_case \
--data_dir ./original_csqa \
--learning_rate 1e-5 \
--num_train_epochs 5 \
--max_seq_length 80 \
--per_gpu_eval_batch_size=16 \
--per_gpu_train_batch_size=16 \
--gradient_accumulation_steps 1 \
--warmup_steps 150 \
--weight_decay 0.01 \
--max_steps 3000 \
--save_steps 0 \
--adam_epsilon 1e-6 \
--fp16 \
--logging_steps 50 \
--evaluate_during_training \
--overwrite_output \
--seed 42 \
--output_dir /tmp/hg_csqa/roberta_large/original_seed_42/ \
--logging_dir /tmp/hg_csqa/roberta_large/original_seed_42/logs/
```


```
CUDA_VISIBLE_DEVICES=2 python ./transformers/examples/multiple-choice/run_multiple_choice.py \
--model_type roberta \
--task_name csqa \
--model_name_or_path roberta-large \
--do_train \
--do_eval \
--do_lower_case \
--data_dir ./bart_packed \
--learning_rate 1e-5 \
--num_train_epochs 5 \
--max_seq_length 120 \
--per_gpu_eval_batch_size=16 \
--per_gpu_train_batch_size=16 \
--gradient_accumulation_steps 1 \
--warmup_steps 150 \
--weight_decay 0.01 \
--max_steps 3000 \
--save_steps 0 \
--adam_epsilon 1e-6 \
--fp16 \
--logging_steps 50 \
--evaluate_during_training \
--overwrite_output \
--seed 42 \
--output_dir /tmp/hg_csqa/roberta_large/bart_seed_42/ \
--logging_dir /tmp/hg_csqa/roberta_large/bart_seed_42/logs 
```


```
CUDA_VISIBLE_DEVICES=0 python ./transformers/examples/multiple-choice/run_multiple_choice.py \
--model_type roberta \
--task_name csqa \
--model_name_or_path roberta-large \
--do_train \
--do_eval \
--do_lower_case \
--data_dir ./t5_packed \
--learning_rate 1e-5 \
--num_train_epochs 5 \
--max_seq_length 120 \
--per_gpu_eval_batch_size=16 \
--per_gpu_train_batch_size=16 \
--gradient_accumulation_steps 1 \
--warmup_steps 150 \
--weight_decay 0.01 \
--max_steps 3000 \
--save_steps 0 \
--adam_epsilon 1e-6 \
--fp16 \
--logging_steps 50 \
--evaluate_during_training \
--overwrite_output \
--seed 42 \
--output_dir /tmp/hg_csqa/roberta_large/t5_seed_42/ \
--logging_dir /tmp/hg_csqa/roberta_large/t5_seed_42/logs 
```



```
CUDA_VISIBLE_DEVICES=1 python ./transformers/examples/multiple-choice/run_multiple_choice.py \
--model_type roberta \
--task_name csqa \
--model_name_or_path roberta-large \
--do_train \
--do_eval \
--do_lower_case \
--data_dir ./unilm_packed \
--learning_rate 1e-5 \
--num_train_epochs 5 \
--max_seq_length 120 \
--per_gpu_eval_batch_size=16 \
--per_gpu_train_batch_size=16 \
--gradient_accumulation_steps 1 \
--warmup_steps 150 \
--weight_decay 0.01 \
--max_steps 3000 \
--save_steps 0 \
--adam_epsilon 1e-6 \
--fp16 \
--logging_steps 50 \
--evaluate_during_training \
--overwrite_output \
--seed 42 \
--output_dir /tmp/hg_csqa/roberta_large/unilm_seed_42/ \
--logging_dir /tmp/hg_csqa/roberta_large/unilm_seed_42/logs 
```




```
CUDA_VISIBLE_DEVICES=0 python ./transformers/examples/multiple-choice/run_multiple_choice.py \
--model_type roberta \
--task_name csqa \
--model_name_or_path roberta-large \
--do_train \
--do_eval \
--do_lower_case \
--data_dir ./bertbase_packed \
--learning_rate 1e-5 \
--num_train_epochs 5 \
--max_seq_length 120 \
--per_gpu_eval_batch_size=16 \
--per_gpu_train_batch_size=16 \
--gradient_accumulation_steps 1 \
--warmup_steps 150 \
--weight_decay 0.01 \
--max_steps 3000 \
--save_steps 0 \
--adam_epsilon 1e-6 \
--fp16 \
--logging_steps 50 \
--evaluate_during_training \
--overwrite_output \
--seed 42 \
--output_dir /tmp/hg_csqa/roberta_large/bertbase_seed_42/ \
--logging_dir /tmp/hg_csqa/roberta_large/bertbase_seed_42/logs 
```




```
CUDA_VISIBLE_DEVICES=1 python ./transformers/examples/multiple-choice/run_multiple_choice.py \
--model_type roberta \
--task_name csqa \
--model_name_or_path roberta-large \
--do_train \
--do_eval \
--do_lower_case \
--data_dir ./constleven_packed \
--learning_rate 1e-5 \
--num_train_epochs 5 \
--max_seq_length 120 \
--per_gpu_eval_batch_size=16 \
--per_gpu_train_batch_size=16 \
--gradient_accumulation_steps 1 \
--warmup_steps 150 \
--weight_decay 0.01 \
--max_steps 3000 \
--save_steps 0 \
--adam_epsilon 1e-6 \
--fp16 \
--logging_steps 50 \
--evaluate_during_training \
--overwrite_output \
--seed 42 \
--output_dir /tmp/hg_csqa/roberta_large/constleven_seed_42/ \
--logging_dir /tmp/hg_csqa/roberta_large/constleven_seed_42/logs 
```