## Installation 

```

conda create -n coco_score python=2.7
conda activate coco_score
pip install numpy
pip install -U spacy
python -m spacy download en_core_web_sm
bash get_stanford_models.sh
```

- Example: generate scores on baseline models
```

cd eval_metrics
# evaluate on test dataset 
python eval.py --key_file ../../../dataset/final_data/commongen/commongen.test.src_alpha.txt --gts_file ../../../dataset/final_data/commongen/commongen.test.tgt.txt --res_file ../../../methods/unilm_based/decoded_sentences/test/model.10.bin.test
# evaluate on dev dataset
python eval.py --key_file ../../../dataset/final_data/commongen/commongen.dev.src_alpha.txt --gts_file ../../../dataset/final_data/commongen/commongen.dev.tgt.txt --res_file ../../../methods/unilm_based/decoded_sentences/dev/model.10.bin.dev


python eval.py --key_file ../../../dataset/final_data/commongen/commongen.test.src_alpha.txt --gts_file ../../../dataset/final_data/commongen/commongen.test.tgt.txt --res_file ../../../methods/opennmt_based/model_output/commongen.test.src_alpha.out
python eval.py --key_file ../../../dataset/final_data/commongen/commongen.dev.src_alpha.txt --gts_file ../../../dataset/final_data/commongen/commongen.dev.tgt.txt --res_file ../../../methods/opennmt_based/model_output/commongen.dev.src_alpha.out
```



## For Human Bound Performance
```
python human_performance.py --input_file ../../../dataset/final_data/commongen.test
python human_performance.py --input_file ../../../dataset/final_data/commongen.dev
```