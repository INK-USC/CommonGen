import json
from tqdm import tqdm

model = "constleven"
split = "train"  # train or dev
model_gens = open('csqa.%s.qac.%s.res'%(split, model)).read().split("\n")
data_lines = open('%s_rand_split.jsonl'%split).read().split("\n")[:-1]

assert len(model_gens)/5==len(data_lines)

packed = []
cur_id = 0

# Packed model generation to answers with seperators
for line in tqdm(data_lines[:]):
    item = json.loads(line)  
    for choice_id in range(5): 
        choice = item['question']['choices'][choice_id]["text"]
        # item['question']['choices'][choice_id]["text"] = "CG: " + model_gens[cur_id]  + " </s>  A: " + choice
        item['question']['choices'][choice_id]["CG"] = model_gens[cur_id]
        cur_id += 1
    packed.append(json.dumps(item))


# for line in tqdm(data_lines[:]):
#     item = json.loads(line)  
#     for choice_id in range(5): 
#         # item['question']['choices'][choice_id]["text"] += " | CG: " + model_gens[cur_id] 
#         item['question']['stem'] += " | CG: " + model_gens[cur_id]  
#         cur_id += 1
#     packed.append(json.dumps(item))

open("%s_packed/%s.jsonl"%(model, split.replace("dev", "valid")), "w").write("\n".join(packed))