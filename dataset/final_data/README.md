# The dataset and pre-processing scripts

This folder contains the lateset version of the CommonGen dataset (v1.0) and a set of scripts formatting the data for training and testing the baseline models.

## The CommonGen Dataset (v1.0)

There are three files in total:  

- `commongen.train.jsonl`: the training set
- `commongen.dev.jsonl`: the development/validation set
- `commongen.test.jsonl`: the test set.

Each line of the `jsonl` files is a json-format string that can be parsed as a dictionary. There are two main keys for training and testing: `concept_set` and `scene` as well as `reason` (only in dev and test). The value of a `concept-set` item is a string like `apple_N#bag_N#pick_V#put_V#tree_N`, which can be split by the `#` and the part-of-speech tag of each concept is indicated with its suffix `_N` (noun) or `_V` (verb). Each `scene` item is a list of sentences that describe everyday scenarios about the associated concept-set. Additionally, in the devlopment/test set, we provide human-annotated rationales (i.e. a list of sentences for explaining the commonsense knowledge about the specific scene）as the `reason` part.

## Formatting scripts

In order to easily fit the CommonGen dataset with established seq2seq learning frameworks such as OpenNMT and Fariseq, we introduce scripts for transforming the format of the data files. After running `python formatter.py` in this folder, we then can see get files in the `formatted` folder.

- `*.src_alpha.txt` files are used as the inputs for baseline methods.
- `*.tgt.txt` files are used as the outputs for training and testing.
- `*.src_index.txt` files are used for aligning the outputs with the order of original input sets.
- `*.src_cs_str.txt` files are used for checking the coverage of generated outputs.
