export PYTORCH_PRETRAINED_BERT_CACHE=tmp/bert-cased-pretrained-cache
DATA_DIR="../../evaluation/csqa/"
EPOCH=$1
MODEL_RECOVER_PATH="tmp/new_finetuned_models/bert_save/model.${EPOCH}.bin"
EVAL_SPLIT=$2

python unilm/src/biunilm/decode_seq2seq.py --bert_model bert-large-cased --new_segment_ids --mode s2s --need_score_traces \
--input_file ${DATA_DIR}/${EVAL_SPLIT}.qac.src --split ${EVAL_SPLIT} \
--model_recover_path ${MODEL_RECOVER_PATH} \
--max_seq_length 64 --max_tgt_length 32 \
--batch_size 12 --beam_size 5 --length_penalty 0 \
--forbid_duplicate_ngrams --forbid_ignore_word "."


cp tmp/new_finetuned_models/bert_save/model.${EPOCH}.bin.${EVAL_SPLIT} decoded_sentences/${EVAL_SPLIT}


