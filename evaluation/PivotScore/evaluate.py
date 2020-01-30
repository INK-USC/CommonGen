import argparse
import json
import pivot_score

parser = argparse.ArgumentParser()
parser.add_argument('--pred', default="", type=str)
parser.add_argument('--ref', default="", type=str) 
parser.add_argument('--cs', default="../../dataset/final_data/commongen/commongen.dev.src_alpha.txt", type=str)
parser.add_argument('--cs_str', default="../../dataset/final_data/commongen/commongen.dev.src_cs_str.txt", type=str)
args = parser.parse_args()


pred = []
ref = []
concept = []
with open(args.pred) as f:
    for line in f.readlines():
        pred.append(line.strip())
with open(args.ref) as f:
    for line in f.readlines():
        ref.append(line.strip())
with open(args.cs) as f:
    concept = [item.split() for item in f.read().split("\n")]

with open(args.cs_str) as f:
    ori_concepts = [item.split("#") for item in f.read().split("\n")]

def scoring(pred, ref):
    Scores, Coverage, Coverage_POS  = pivot_score.score(pred, ref, concept, ori_concepts, scoring="steiner_tree", parser="spacy", verbose=False)
    print(f"System level Score: {sum(Scores)/len(Scores)*100:.2f}")
    print(f"System level Coverage: {sum(Coverage)/len(Scores)*100:.2f}")
    print(f"System level Coverage_POS: {sum(Coverage_POS)/len(Scores)*100:.2f}")
scoring(pred, ref)