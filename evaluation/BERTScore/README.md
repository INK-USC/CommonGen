## Installation

```
conda create -n bert_score python=3.6.7
conda activate bert_score
# git clone https://github.com/Tiiiger/bert_score # do once
python -m pip install -U matplotlib
cd bert_score
pip install . 
```

## Example Usage

```
# Get original score
python evaluate.py --pred ../../dataset/final_data/commongen.test.human_src   --ref ../../dataset/final_data/commongen.test.human_tgt --cs ../../dataset/final_data/commongen.test.human_cs 
python evaluate.py --pred ../../dataset/final_data/commongen.dev.human_src   --ref ../../dataset/final_data/commongen.dev.human_tgt --cs ../../dataset/final_data/commongen.dev.human_cs
```
