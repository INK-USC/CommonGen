### Baseline Methods for CommonGen

There are three main kinds of baseline methods of our interest, and they are located in separate folders, namely `opennmt_based` (e.g. bRNN, transformer-based, etc.), `fariseq_based` (Levenshtein transformer), and `unilm_based` (the state-of-the-art bert-based pre-trained text generation model). There is a detailed readme in each folder. Apart from that, `elasticsearch_omcs` contains the code for retrieving the potential relevant sentences from the OMCS corpus, although we found the retrieved sentences are hardly helpful.

#### Related papers:
- _Levenshtein Transformer_ ([Gu et al. NeurIPS 2019](https://arxiv.org/abs/1905.11006)) 
- _Unified Language Model Pre-training for Natural Language Understanding and Generation_ ([Dong et al. NeurIPS 2019](https://arxiv.org/abs/1905.03197 )) 
- _OpenNMT: Open-Source Toolkit for Neural Machine Translation_ ([Klein et al. ACL 2017 (demo)](https://www.aclweb.org/anthology/P17-4012/))