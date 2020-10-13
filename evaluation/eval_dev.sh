# source ~/.bashrc
INPUT_FILE=~/CommonGen-plus/dataset/final_data/commongen/commongen.dev.src_alpha.txt
TRUTH_FILE=~/CommonGen-plus/dataset/final_data/commongen/commongen.dev.tgt.txt
PRED_FILE=$1

echo ${INPUT_FILE} 
echo ${TRUTH_FILE}
echo ${PRED_FILE}

echo "Start running ROUGE"

cd ~/CommonGen-plus/methods/unilm_based
~/anaconda3/envs/unilm_env/bin/python unilm/src/gigaword/eval.py --pred ${PRED_FILE}   --gold ${TRUTH_FILE} --perl


echo "BLEU/METER/CIDER/SPICE"
cd ~/CommonGen/evaluation/Traditional/eval_metrics/
~/anaconda3/envs/coco_score/bin/python eval.py --key_file ${INPUT_FILE} --gts_file ${TRUTH_FILE} --res_file ${PRED_FILE}


echo "Coverage"
cd ~/CommonGen-plus/evaluation/PivotScore
~/anaconda3/envs/pivot_score/bin/python evaluate.py --pred ${PRED_FILE}   --ref ${TRUTH_FILE} --cs ${INPUT_FILE} --cs_str ../../dataset/final_data/commongen/commongen.dev.cs_str.txt



