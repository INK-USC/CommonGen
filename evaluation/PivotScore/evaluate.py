import argparse
import json 
import spacy
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--pred', default="", type=str)
parser.add_argument('--ref', default="", type=str) 
parser.add_argument('--cs', default="../../dataset/final_data/commongen/commongen.dev.src_alpha.txt", type=str)
parser.add_argument('--cs_str', default="../../dataset/final_data/commongen/commongen.dev.src_cs_str.txt", type=str)
args = parser.parse_args()

nlp = spacy.load('en_core_web_sm')
nlp.pipeline = [('tagger', nlp.tagger), ("parser", nlp.parser)]


preds = []
ref = []
concept = []
with open(args.pred) as f:
    for line in f.readlines():
        preds.append(line.strip())
with open(args.ref) as f:
    for line in f.readlines():
        ref.append(line.strip())
with open(args.cs) as f:
    concept_sets = [item.split() for item in f.read().split("\n")]

with open(args.cs_str) as f:
    ori_concepts = [item.split("#") for item in f.read().split("\n")]

def coverage_score(preds, concept_sets):
    covs = []
    for p, cs in tqdm(zip(preds,concept_sets), total=len(preds)):
        cs = set(cs)
        lemmas = set()
        for token in nlp(p):
            lemmas.add(token.lemma_)
        cov = len(lemmas&cs)/len(cs)
        covs.append(cov)
    return sum(covs)/len(covs)

def scoring(preds, ref):

    # Scores, Coverage, Coverage_POS  = pivot_score.score(pred, ref, concept, ori_concepts, scoring="steiner_tree", parser="spacy", verbose=False)
    Coverage = coverage_score(preds, concept_sets)
    # print(f"System level Score: {sum(Scores)/len(Scores)*100:.2f}")
    print(f"System level Coverage: {Coverage*100:.2f}")
    # print(f"System level Coverage_POS: {sum(Coverage_POS)/len(Scores)*100:.2f}")
scoring(preds, ref)