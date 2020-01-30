## Automatic Evaluation Metrics for CommonGen

We have intergate all evaluation metric into a single script, and thus we can evaluate each model with all metrics with a commandline as follows (or w/ `bash run_all_eval.sh`). **Please run the installation scripts that are in the readme of each folder (`Traditional`,`BERTScore`, and `PivotScore`).**  Also, please install `ROUGE` following the instructions at `rouge_install_instruction.md`.

```
## ONMT 
bash eval_dev.sh ~/CommonGen/methods/opennmt_based/model_output/commongen_brnn.dev.src_alpha.out > res_files/brnn_dev.res 
bash eval_test.sh ~/CommonGen/methods/opennmt_based/model_output/commongen_brnn.test.src_alpha.out > res_files/brnn_test.res 

bash eval_dev.sh ~/CommonGen/methods/opennmt_based/model_output/commongen_mean.dev.src_alpha.out > res_files/mean_dev.res 
bash eval_test.sh ~/CommonGen/methods/opennmt_based/model_output/commongen_mean.test.src_alpha.out > res_files/mean_test.res 

bash eval_dev.sh ~/CommonGen/methods/opennmt_based/model_output/commongen_transformer.dev.src_alpha.out > res_files/transformer_dev.res 
bash eval_test.sh ~/CommonGen/methods/opennmt_based/model_output/commongen_transformer.test.src_alpha.out > res_files/transformer_test.res 

bash eval_dev.sh ~/CommonGen/methods/opennmt_based/model_output/commongen_settransformer.dev.src_alpha.out > res_files/settransformer_dev.res 
bash eval_test.sh ~/CommonGen/methods/opennmt_based/model_output/commongen_settransformer.test.src_alpha.out > res_files/settransformer_test.res 

## LEVEN 

bash eval_dev.sh ~/CommonGen/methods/fairseq_based/fairseq_local/output/final.leven.alpha.dev.txt > res_files/leven_dev.res 
bash eval_test.sh ~/CommonGen/methods/fairseq_based/fairseq_local/output/final.leven.alpha.test.txt > res_files/leven_test.res 
 

## UNILM

bash eval_dev.sh ~/CommonGen/methods/unilm_based/decoded_sentences/dev/model.10.bin.dev > res_files/unilm_dev.res 
bash eval_test.sh ~/CommonGen/methods/unilm_based/decoded_sentences/test/model.10.bin.test > res_files/unilm_test.res  
```