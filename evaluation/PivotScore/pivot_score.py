# The metric function to measure the distance of two sentences, (with a given words),
# based on steiner tree over dependency parses

# conda create -n dep_score python=3.6
# conda activate dep_score
# pip install spacy
# python -m spacy download en
# pip install networkx
# pip install --user -U nltk

import spacy
from itertools import combinations
import networkx as nx
from networkx.algorithms.approximation import steinertree
from tqdm import tqdm

nlp = spacy.load('en_core_web_sm')
nlp.pipeline = [('tagger', nlp.tagger), ("parser", nlp.parser)]


def get_k_hop_links_fast(sent, pivot_words, ori_concepts, k=1):
    if not len(sent):   # an empty sentence 
        return set(), 0, 0
    sent_doc = nlp(sent)
    covered_pivots = set()
    covered_pivot_pos = set()
    edge_set = set()

    def form_synset(token):
        if token.pos_ in ["NOUN", "VERB", "ADP"]:
            return token.lemma_+"_"+token.pos_[0] # "%s.%s.01"%(token.lemma_, token.pos_[0].lower())
        else:
            return token.pos_

    for token in nlp(sent):
        cur_text = token.lemma_
        if cur_text in pivot_words:
            covered_pivots.add(cur_text)
            if token.lemma_+"_"+token.pos_[0] in ori_concepts:
                covered_pivot_pos.add(token.lemma_+"_"+token.pos_[0])
        one_hop_link_text = "%s-(%s)->%s"%(form_synset(token), token.dep_, form_synset(token.head))
        edge_set.add(one_hop_link_text)
        if k>=2 and token.head.dep_!="ROOT":
            two_hop_link_text = "%s-(%s)->%s-(%s)->%s"%(form_synset(token), token.dep_, form_synset(token.head), token.head.dep_, form_synset(token.head.head))
            edge_set.add(two_hop_link_text)
            if k >=3 and token.head.head.dep_!="ROOT":
                three_hop_link_text = "%s-(%s)->%s-(%s)->%s-(%s)->%s"%(form_synset(token), token.dep_, form_synset(token.head), token.head.dep_, form_synset(token.head.head), token.head.head.dep_, form_synset(token.head.head.head))
                edge_set.add(three_hop_link_text)
                if k >=4 and token.head.head.head.dep_!="ROOT":
                    four_hop_link_text = "%s-(%s)->%s-(%s)->%s-(%s)->%s-(%s)->%s"%(form_synset(token), token.dep_, form_synset(token.head), token.head.dep_, form_synset(token.head.head), token.head.head.dep_, form_synset(token.head.head.head), token.head.head.head.dep_, form_synset(token.head.head.head.head))
                    edge_set.add(four_hop_link_text)
                    if k >=5 and token.head.head.head.head.head.dep_!="ROOT":
                        five_hop_link_text = "%s-(%s)->%s-(%s)->%s-(%s)->%s-(%s)->%s-(%s)->%s"%(form_synset(token), token.dep_, form_synset(token.head), token.head.dep_, form_synset(token.head.head), token.head.head.dep_, form_synset(token.head.head.head), token.head.head.head.dep_, form_synset(token.head.head.head.head), token.head.head.head.head.dep_, form_synset(token.head.head.head.head.head))
                        edge_set.add(five_hop_link_text)

            
    final_k_hop_set = set()
    for link_text in edge_set:
        if "punct" in link_text:
            continue
        word_seq = [w.split("-")[0] for w in link_text.split("->")]
        # print(word_seq)
        if word_seq[0] in covered_pivot_pos and word_seq[-1] in covered_pivot_pos:
            final_k_hop_set.add(link_text)
    return final_k_hop_set, len(covered_pivots)/len(pivot_words), len(covered_pivot_pos)/len(pivot_words)


def get_steiner_tree_edges(sent, pivot_words, ori_concepts):
    if not len(sent):
        return set(), 0, 0
    sent = sent[:-1].replace(".", ", and ")+sent[-1] # combine multiple sentences.

    sent_doc = nlp(sent)
    dep_tree = nx.Graph()
    pivot_word_ids = []
    covered_pivots = set()
    covered_pivot_pos = set()
    for token in nlp(sent):
        cur_text = token.lemma_
        if cur_text not in pivot_words:
            cur_text = token.pos_
        else:
            covered_pivots.add(cur_text)
            pivot_word_ids.append(token.i)
            if token.lemma_+"_"+token.pos_[0] in ori_concepts:
                covered_pivot_pos.add(token.lemma_+"_"+token.pos_[0])
        head_text = token.head.lemma_
        if head_text not in pivot_words:
            head_text = token.head.pos_
        dep_tree.add_node(token.i, text=cur_text)
        dep_tree.add_node(token.head.i, text=head_text)
        dep_tree.add_edge(token.i, token.head.i, dep=token.dep_, weight=1)
    if not nx.is_connected(dep_tree):
        # print("not connected: ", sent)
        return set(), len(covered_pivots)/len(pivot_words), len(covered_pivot_pos)/len(pivot_words)
    # Find the minimal subgraph that covers all the given nodes.
    subgraph = steinertree.steiner_tree(dep_tree, pivot_word_ids)
    edge_set = set()
    for n1, n2 in subgraph.edges():
        n1_text = dep_tree.nodes[n1]["text"]
        n2_text = dep_tree.nodes[n2]["text"]
        edge = dep_tree[n1][n2]
        dep = edge["dep"]
        if n1_text > n2_text:
            n1_text, n2_text = n2_text, n1_text
        edge_set.add("%s->%s->%s"%(n1_text, dep, n2_text))
    return edge_set, len(covered_pivots)/len(pivot_words), len(covered_pivot_pos)/len(pivot_words)



def score(candidate, reference, concepts, ori_concepts, parser="spacy", scoring="steiner_tree", verbose=False):
    scores = []
    coverage = []
    coverage_POS = []
        
    for cand, ref, cs, ori_cs in tqdm(zip(candidate, reference, concepts, ori_concepts), total=len(candidate)):

        cur_dep_cand, coverage_cand, coverage_cand_pos = get_k_hop_links_fast(cand, cs, ori_cs, k=5)
        cur_dep_ref, _, _ = get_k_hop_links_fast(ref, cs, ori_cs, k=5)
        print("cur_dep_cand:", cur_dep_cand)
        print("cur_dep_ref:", cur_dep_ref)
        intersect = cur_dep_cand & cur_dep_ref

        if not len(cur_dep_ref):
            continue
            cur_dep_cand = set([token.lemma_ for token in nlp(cand) if token.lemma not in concepts])
            cur_dep_ref = set([token.lemma_ for token in nlp(ref) if token.lemma_ not in concepts])
            intersect = cur_dep_cand & cur_dep_ref
        
        scores.append(len(intersect)/len(cur_dep_ref))
        coverage.append(coverage_cand)
        coverage_POS.append(coverage_cand_pos)
    return scores, coverage, coverage_POS

cand_1 = "A little boy pick some apples from a tree and puts them into a bag."
cand_2 = "Two girls pick some bags from a tree and put apples into them."
ref = "A man picks some apples from a tree and puts them into a bag."
concepts = ["pick", "apple", "tree", "put", "bag"]
ori_concepts = "pick_V#bag_N#tree_N#apple_N#put_V".split("#")
candidate = [cand_1, cand_2]
reference = [ref] * len(candidate)
concepts = [concepts] * len(candidate)
ori_concepts = [ori_concepts] * len(candidate)
print(score(candidate, reference, concepts, ori_concepts, parser="spacy", scoring="steiner_tree", verbose=False))
