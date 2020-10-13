##########################################################################################################################################
## test
##########################################################################################################################################
## BERT-Gen
bash eval_test.sh ~/CommonGen-plus/methods/BERT-based/bert.test > res_files/bert_based_test.res

## GPT-2
bash eval_test.sh ~/CommonGen-plus/methods/GPT-2/gpt2.test > res_files/gpt2_test.res

## UniLM-v2
bash eval_test.sh ~/CommonGen-plus/methods/UniLM_v2/unilmv2.test > res_files/unilmv2_test.res

### BART
bash eval_test.sh ~/CommonGen-plus/methods/BART/fairseq_local/bart.test > res_files/bart_test.res

## T5-large
bash eval_test.sh ~/CommonGen-plus/methods/T5/transformer_local/examples/summarization/bart/t5.test > res_files/t5_test.res

## T5-base
bash eval_test.sh ~/CommonGen-plus/methods/T5/transformer_local/examples/summarization/bart/t5.test.base > res_files/t5_base_test.res

## T5-large-const
bash eval_test.sh ~/CommonGen-plus/methods/T5-DBA/transformer_local/examples/summarization/bart/t5.cons.test > res_files/t5_const_test.res

## UniLM-v1
bash eval_test.sh ~/CommonGen-plus/methods/unilm_based/decoded_sentences/test/model.10.bin.test > res_files/unilm_test.res



## LEVEN
bash eval_test.sh ~/CommonGen-plus/methods/const-levt/constrained-levt/final.leven.alpha.test.txt > res_files/leven_test.res

## Const LEVEN
bash eval_test.sh ~/CommonGen-plus/methods/const-levt/const-levt.test > res_files/const_leven_test.res


## bRNN
bash eval_test.sh ~/CommonGen-plus/methods/opennmt_based/model_output/commongen_brnn.test.src_alpha.out > res_files/brnn_test.res

## Trans
bash eval_test.sh ~/CommonGen-plus/methods/opennmt_based/model_output/commongen_transformer.test.src_alpha.out > res_files/trans_test.res

## Mean
bash eval_test.sh ~/CommonGen-plus/methods/opennmt_based/model_output/commongen_mean.test.src_alpha.out > res_files/mean_test.res



##########################################################################################################################################
## dev
##########################################################################################################################################
## BERT-Gen
bash eval_dev.sh ~/CommonGen-plus/methods/BERT-based/bert.dev > res_files/bert_based_dev.res

## GPT-2
bash eval_dev.sh ~/CommonGen-plus/methods/GPT-2/gpt2.dev > res_files/gpt2_dev.res

## UniLM-v2
bash eval_dev.sh ~/CommonGen-plus/methods/UniLM_v2/unilmv2.dev > res_files/unilmv2_dev.res

### BART
bash eval_dev.sh ~/CommonGen-plus/methods/BART/fairseq_local/bart.dev > res_files/bart_dev.res

## T5-large
bash eval_dev.sh ~/CommonGen-plus/methods/T5/transformer_local/examples/summarization/bart/t5.dev > res_files/t5_dev.res

## T5-base
bash eval_dev.sh ~/CommonGen-plus/methods/T5/transformer_local/examples/summarization/bart/t5.dev.base > res_files/t5_base_dev.res

## T5-large-const
bash eval_dev.sh ~/CommonGen-plus/methods/T5-DBA/transformer_local/examples/summarization/bart/t5.cons.dev > res_files/t5_const_dev.res

## UniLM-v1
bash eval_dev.sh ~/CommonGen-plus/methods/unilm_based/decoded_sentences/dev/model.10.bin.dev > res_files/unilm_dev.res



## LEVEN
bash eval_dev.sh ~/CommonGen-plus/methods/const-levt/constrained-levt/final.leven.alpha.dev.txt > res_files/leven_dev.res

## Const LEVEN
bash eval_dev.sh ~/CommonGen-plus/methods/const-levt/const-levt.dev > res_files/const_leven_dev.res

## bRNN
bash eval_dev.sh ~/CommonGen-plus/methods/opennmt_based/model_output/commongen_brnn.dev.src_alpha.out > res_files/brnn_dev.res

## Trans
bash eval_dev.sh ~/CommonGen-plus/methods/opennmt_based/model_output/commongen_transformer.dev.src_alpha.out > res_files/trans_dev.res.20000

## Mean
bash eval_dev.sh ~/CommonGen-plus/methods/opennmt_based/model_output/commongen_mean.dev.src_alpha.out > res_files/mean_dev.res.140000