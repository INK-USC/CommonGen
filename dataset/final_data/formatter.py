import json 
import sys
import os
import random 

random.seed(42) 

filenames = ["commongen.train.jsonl", "commongen.dev.jsonl", "commongen.test.jsonl"]

dirpath = "commongen"
if not os.path.exists(dirpath):
    os.mkdir(dirpath)

def split_file(filename):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            data.append(json.loads(line))
    alpha_order_cs_str = []
    ori_cs_str = [] 
    idx_list = []
    idx = 0
    scenes_list = []
    reasons_list = []
    for item in data:
        rand_order  = [word.split('_')[0] for word in item['concept_set'].split('#')]
        random.shuffle(rand_order)
        alpha_order = ' '.join(rand_order)
        scenes = item['scene'] 
        scenes_list += scenes
        ori_cs_str += [item['concept_set']] * len(scenes)
        alpha_order_cs_str += [alpha_order] * len(scenes) 
        idx_list += [str(idx)] * len(scenes)
        idx += 1
    prefix = filename.replace(".jsonl", "")
    with open(dirpath + "/%s.src_alpha.txt"%prefix, 'w', encoding="utf8") as f:
        f.write("\n".join(alpha_order_cs_str)) 
    with open(dirpath + "/%s.cs_str.txt"%prefix, 'w', encoding="utf8") as f:
        f.write("\n".join(ori_cs_str))
    with open(dirpath + "/%s.tgt.txt"%prefix, 'w', encoding="utf8") as f:
        f.write("\n".join(scenes_list))
    with open(dirpath + "/%s.index.txt"%prefix, 'w', encoding="utf8") as f:
        f.write("\n".join(idx_list)) 

for filename in filenames:
    split_file(filename)
