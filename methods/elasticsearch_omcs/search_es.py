import json
import sys
import argparse
from elasticsearch import Elasticsearch
from tqdm import tqdm


data_path = "../../dataset/final_data/"
parser = argparse.ArgumentParser()
args = parser.parse_args()

train_path = data_path + "commongen.train"
dev_path = data_path + "commongen.dev"
test_path = data_path + "commongen.test"

es = Elasticsearch()

def get_top_k(query, k=100):

    results = es.search(index='omcs', params={"q": query})['hits']['hits'][:k]
    sents = []
    concepts = set(query.split())
    covered_vocab = set()
    for doc in results:
        sent = doc['_source']['doc']['sent']
        sent_vocab = set(sent.lower().replace(".", " ").split())
        if sent_vocab.issubset(covered_vocab):
            continue
        covered_vocab.update(sent_vocab)
        sents.append(sent.replace("Situation:", " "))
        if len(sents) == 10 or concepts.issubset(covered_vocab):
            break
    return sents


def get_query(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
    results = []
    for line in tqdm(lines):
        if not line:
            continue
        item_data = json.loads(line)
        query = item_data["concept_set"].replace("_V", " ").replace("_N", " ").replace("#", " ")
        sents = get_top_k(query)
        item_data["omcs_sents"] = sents
        results.append(json.dumps(item_data))
    return "\n".join(results)

with open(train_path + ".omcs", 'w') as f:
    f.write(get_query(train_path))
with open(dev_path + ".omcs", 'w') as f:
    f.write(get_query(dev_path))
with open(test_path + ".omcs", 'w') as f:
    f.write(get_query(test_path))
