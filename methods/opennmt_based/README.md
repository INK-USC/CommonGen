## OpenNMT-based Baseline Methods


### Installation
```bash
conda create -n opennmt python=3.6
conda activate opennmt
pip install torch==1.4
cd OpenNMT-py
python setup.py install
pip install oauthlib -U
pip install pyasn1 -U
```

#### Training different models 

```
cd ..
mkdir models
mkdir data
mkdir data/commongen/ 
onmt_preprocess -train_src ../../dataset/final_data/commongen/commongen.train.src_alpha.txt \
                -train_tgt ../../dataset/final_data/commongen/commongen.train.tgt.txt \
                -valid_src ../../dataset/final_data/commongen/commongen.dev.src_alpha.txt \
                -valid_tgt ../../dataset/final_data/commongen/commongen.dev.tgt.txt \
                -save_data data/commongen/CMGN_final \
                -src_seq_length 10 \
                -dynamic_dict \
                -share_vocab \
                -shard_size 100000 \
                -overwrite
```

- BRNN w/ Copy


##### BiRNN
``` 
CUDA_VISIBLE_DEVICES=3 \
onmt_train -save_model models/commongen_brnn \
           -data data/commongen/CMGN_final \
           -copy_attn \
           -global_attention mlp \
           -word_vec_size 128 \
           -rnn_size 128 \
           -layers 2 \
           -encoder_type brnn \
           -train_steps 200000 \
           -max_grad_norm 2 \
           -dropout 0 \
           -batch_size 128 \
           -valid_batch_size 128 \
           -optim adagrad \
           -learning_rate 0.2 \
           -adagrad_accumulator_init 0.1 \
           -reuse_copy_attn \
           -copy_loss_by_seqlength \
           -bridge \
           -seed 777 \
           -world_size 1 \
           -gpu_ranks 0
```

##### Transformer w/ copy


``` 
CUDA_VISIBLE_DEVICES=1 \
onmt_train -data data/commongen/CMGN_final \
           -save_model models/commongen_transformer \
           -layers 1 \
           -rnn_size 128 \
           -word_vec_size 128 \
           -max_grad_norm 0 \
           -optim adam \
           -encoder_type transformer \
           -decoder_type transformer \
           -position_encoding \
           -dropout 0.1 \
           -param_init 0 \
           -warmup_steps 1000 \
           -learning_rate 2 \
           -decay_method noam \
           -label_smoothing 0.1 \
           -adam_beta2 0.998 \
           -batch_size 128 \
           -batch_type tokens \
           -normalization tokens \
           -max_generator_batches 2 \
           -train_steps 200000 \
           -accum_count 4 \
           -share_embeddings \
           -copy_attn \
           -param_init_glorot \
           -world_size 1 \
           -gpu_ranks 0 &
```

##### Mean-encoder w/ copy 
```
CUDA_VISIBLE_DEVICES=2 \
onmt_train -save_model models/commongen_mean \
           -data data/commongen/CMGN_final \
           -copy_attn \
           -global_attention mlp \
           -word_vec_size 128 \
           -rnn_size 128 \
           -layers 1 \
           -encoder_type mean \
           -train_steps 200000 \
           -max_grad_norm 2 \
           -dropout 0. \
           -batch_size 128 \
           -valid_batch_size 128 \
           -optim adagrad \
           -learning_rate 0.15 \
           -adagrad_accumulator_init 0.1 \
           -reuse_copy_attn \
           -copy_loss_by_seqlength \
           -bridge \
           -seed 777 \
           -world_size 1 \
           -gpu_ranks 0
```

##### SetTransformer w/ copy

```
CUDA_VISIBLE_DEVICES=3 \
onmt_train -data data/commongen/CMGN_final \
           -save_model models/commongen_settransformer \
           -layers 1 \
           -rnn_size 128 \
           -word_vec_size 128 \
           -max_grad_norm 0 \
           -optim adam \
           -encoder_type transformer \
           -decoder_type transformer \
           -dropout 0.1 \
           -param_init 0 \
           -warmup_steps 3000 \
           -learning_rate 5 \
           -decay_method noam \
           -label_smoothing 0.1 \
           -adam_beta2 0.998 \
           -batch_size 128 \
           -batch_type tokens \
           -normalization tokens \
           -max_generator_batches 2 \
           -train_steps 200000 \
           -accum_count 4 \
           -share_embeddings \
           -copy_attn \
           -param_init_glorot \
           -world_size 1 \
           -gpu_ranks 0
```



#### Decoding for generating sentences

The below script can be found at `decode_alpha.sh`:

```
mkdir model_output
onmt_translate -gpu 0 \
               -batch_size 20 \
               -beam_size 20 \
               -model models/commongen_brnn_step_200000.pt \
               -src ../../dataset/final_data/commongen/commongen.dev.src_alpha.txt \
               -output model_output/commongen_brnn.dev.src_alpha.out \
               -min_length 5 \
               -verbose \
               -stepwise_penalty \
               -coverage_penalty summary \
               -beta 5 \
               -length_penalty wu \
               -alpha 0.9 \
               -block_ngram_repeat 1 \
               -dynamic_dict \
               -share_vocab \
               -replace_unk &\

onmt_translate -gpu 3 \
               -batch_size 20 \
               -beam_size 20 \
               -model models/commongen_brnn_step_200000.pt \
               -src ../../dataset/final_data/commongen/commongen.test.src_alpha.txt \
               -output model_output/commongen_brnn.test.src_alpha.out \
               -min_length 5 \
               -verbose \
               -stepwise_penalty \
               -coverage_penalty summary \
               -beta 5 \
               -length_penalty wu \
               -alpha 0.9 \
               -block_ngram_repeat 1 \
               -replace_unk \
               -dynamic_dict \
               -share_vocab &\


onmt_translate -gpu 2 \
               -batch_size 128 \
               -beam_size 20 \
               -model models/commongen_transformer_step_20000.pt \
               -src ../../dataset/final_data/commongen/commongen.dev.src_alpha.txt \
               -output model_output/commongen_transformer.dev.src_alpha.out \
               -min_length 5 \
               -verbose \
               -stepwise_penalty \
               -coverage_penalty summary \
               -beta 5 \
               -length_penalty wu \
               -alpha 0.9 \
               -block_ngram_repeat 1 \
               -replace_unk &\

onmt_translate -gpu 0 \
               -batch_size 128 \
               -beam_size 30 \
               -model models/commongen_transformer_step_20000.pt \
               -src ../../dataset/final_data/commongen/commongen.test.src_alpha.txt \
               -output model_output/commongen_transformer.test.src_alpha.out \
               -min_length 5 \
               -verbose \
               -stepwise_penalty \
               -coverage_penalty summary \
               -beta 5 \
               -length_penalty wu \
               -alpha 0.9 \
               -block_ngram_repeat 1 \
               -replace_unk &\



onmt_translate -gpu 3 \
               -batch_size 20 \
               -beam_size 20 \
               -model models/commongen_mean_step_140000.pt \
               -src ../../dataset/final_data/commongen/commongen.dev.src_alpha.txt \
               -output model_output/commongen_mean.dev.src_alpha.out \
               -min_length 5 \
               -verbose \
               -stepwise_penalty \
               -coverage_penalty summary \
               -beta 5 \
               -length_penalty wu \
               -alpha 0.9 \
               -block_ngram_repeat 1 \
               -replace_unk &\

onmt_translate -gpu 3 \
               -batch_size 20 \
               -beam_size 20 \
               -model models/commongen_mean_step_140000.pt \
               -src ../../dataset/final_data/commongen/commongen.test.src_alpha.txt \
               -output model_output/commongen_mean.test.src_alpha.out \
               -min_length 5 \
               -verbose \
               -stepwise_penalty \
               -coverage_penalty summary \
               -beta 5 \
               -length_penalty wu \
               -alpha 0.9 \
               -block_ngram_repeat 1 \
               -replace_unk &\

onmt_translate -gpu 0 \
               -batch_size 128 \
               -beam_size 20 \
               -model models/commongen_settransformer_step_200000.pt \
               -src ../../dataset/final_data/commongen/commongen.dev.src_alpha.txt \
               -output model_output/commongen_settransformer.dev.src_alpha.out \
               -min_length 5 \
               -verbose \
               -stepwise_penalty \
               -coverage_penalty summary \
               -beta 5 \
               -length_penalty wu \
               -alpha 0.9 \
               -block_ngram_repeat 1 \
               -dynamic_dic -share_vocab \
               -replace_unk &\

onmt_translate -gpu 0 \
               -batch_size 128 \
               -beam_size 20 \
               -model models/commongen_settransformer_step_200000.pt \
               -src ../../dataset/final_data/commongen/commongen.test.src_alpha.txt \
               -output model_output/commongen_settransformer.test.src_alpha.out \
               -min_length 5 \
               -verbose \
               -stepwise_penalty \
               -coverage_penalty summary \
               -beta 5 \
               -length_penalty wu \
               -alpha 0.9 \
               -block_ngram_repeat 1 \
               -dynamic_dic -share_vocab \
               -replace_unk &
```