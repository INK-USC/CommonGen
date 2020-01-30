import json
import argparse
from bert_score import score

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--pred', default="", type=str)
parser.add_argument('--ref', default="", type=str) 
parser.add_argument('--cs', default="", type=str)
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
    for line in f.readlines():
        concept.append(line.strip())
    

def bert_agreement(pred, ref):
    (P, R, F1), hash_code = score(pred, ref, lang="en", verbose=True, return_hash=True, idf=True)
    # (P_pivot, R_pivot, F1_pivot), _ = score(concept, ref, lang="en", verbose=True, return_hash=True, idf=False)
    print(hash_code)
    # print(f"System level P score: {(P.mean()-P_pivot.mean())*100:.2f}")
    # print(f"System level R score: {(R.mean()-R_pivot.mean())*100:.2f}")
    # print(f"System level F1 score: {(F1.mean()-F1_pivot.mean())*100:.2f}")
    
    print(f"System level P score: {(P.mean())*100:.2f}")
    print(f"System level R score: {(R.mean())*100:.2f}")
    print(f"System level F1 score: {(F1.mean())*100:.2f}")

    (P_pivot, R_pivot, F1_pivot), _ = score(concept, ref, lang="en", verbose=True, return_hash=True, idf=False)
    print(f"Base System level P score: {(P_pivot.mean())*100:.2f}")
    print(f"Base System level R score: {(R_pivot.mean())*100:.2f}")
    print(f"Base System level F1 score: {(F1_pivot.mean())*100:.2f}")
    
bert_agreement(pred, ref)