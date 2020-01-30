import json
from tqdm import tqdm

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch(port=9200, timeout=30)

print(es.indices.create(index='omcs_free_1129', ignore=400))

sent_file_format = "./omcs_{:0>2d}"


def gendata(filename):
    with open(filename, encoding='utf-8') as f:
        for line in tqdm(f.read().split('\n')[1:], desc=filename):
            line = line.split('\t')
            if len(line) < 5 or line[4] != 'en':
                continue
            doc = {"sent":line[1]}
            yield {
                "_index": "omcs",
                "_type": "document",
                "doc": doc,
            }
for i in range(0, 19):
    print("Number:", i)
    bulk(es, gendata(sent_file_format.format(i)))

