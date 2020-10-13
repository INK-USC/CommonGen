## Installation 

```
conda create -n pivot_score python=3.6
conda activate pivot_score
pip install spacy
python -m spacy download en
pip install networkx
```


- Example usage for evaluating:
```
python evaluate.py --pred ../../dataset/final_data/commongen.test.human_src   --ref ../../dataset/final_data/commongen.test.human_tgt --cs ../../dataset/final_data/commongen.test.human_cs --cs_str ../../dataset/final_data/commongen.test.human_cs_str
python evaluate.py --pred ../../dataset/final_data/commongen.dev.human_src   --ref ../../dataset/final_data/commongen.dev.human_tgt --cs ../../dataset/final_data/commongen.dev.human_cs --cs_str ../../dataset/final_data/commongen.dev.human_cs_str
```
