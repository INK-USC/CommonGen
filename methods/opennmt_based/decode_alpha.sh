onmt_translate -gpu 1 \
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

onmt_translate -gpu 1 \
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


onmt_translate -gpu 1 \
               -batch_size 128 \
               -beam_size 20 \
               -model models/commongen_transformer_step_200000.pt \
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

onmt_translate -gpu 1 \
               -batch_size 128 \
               -beam_size 30 \
               -model models/commongen_transformer_step_200000.pt \
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



onmt_translate -gpu 1 \
               -batch_size 20 \
               -beam_size 20 \
               -model models/commongen_mean_step_200000.pt \
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

onmt_translate -gpu 1 \
               -batch_size 20 \
               -beam_size 20 \
               -model models/commongen_mean_step_200000.pt \
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

onmt_translate -gpu 1 \
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

onmt_translate -gpu 1 \
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