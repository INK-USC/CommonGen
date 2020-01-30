# source ~/.bashrc
INPUT_FILE=~/CommonGen/dataset/final_data/commongen/commongen.test.src_alpha.txt
TRUTH_FILE=~/CommonGen/dataset/final_data/commongen/commongen.test.tgt.txt
PRED_FILE=$1

echo ${INPUT_FILE} 
echo ${TRUTH_FILE}
echo ${PRED_FILE}

echo "Start running ROUGE"

cd ~/CommonGen/methods/unilm-based
~/anaconda3/envs/unilm_env/bin/python unilm/src/gigaword/eval.py --pred ${PRED_FILE}   --gold ${TRUTH_FILE} --perl


echo "BLEU/METER/CIDER/SPICE"
cd ~/CommonGen/evaluation/Traditional/eval_metrics/
~/anaconda3/envs/coco_score/bin/python eval.py --key_file ${INPUT_FILE} --gts_file ${TRUTH_FILE} --res_file ${PRED_FILE}


echo "PivotScore"
cd ~/CommonGen/evaluation/PivotScore
~/anaconda3/envs/pivot_score/bin/python evaluate.py --pred ${PRED_FILE}   --ref ${TRUTH_FILE} --cs ${INPUT_FILE} --cs_str ../../dataset/final_data/commongen/commongen.test.src_cs_str.txt

echo "_________________"
echo "Correct BERTScore"
cd ~/CommonGen/evaluation/BERTScore
CUDA_VISIBLE_DEVICES=7 /home/bill/anaconda3/envs/bert_score/bin/python evaluate.py --pred ${PRED_FILE}   --ref ${TRUTH_FILE} --cs ../../dataset/final_data/commongen/commongen.test.src_alpha.txt
