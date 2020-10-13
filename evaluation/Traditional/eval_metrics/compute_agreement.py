import numpy as np
from collections import defaultdict

from bleu.bleu import Bleu
from meteor.meteor import Meteor
from rouge.rouge import Rouge
from cider.cider import Cider
from spice.spice import Spice
import spacy
import sys
import codecs
import argparse
import json
from itertools import combinations
import math



def compute_w(data):
    """ Computes kendall's W from a list of rating lists.
    0 indicates no agreement and 1 indicates unanimous agreement.
    Parameters
    ---------
    data : list
        List of lists with shape (n_items * n_annotators)
    Return
    ---------
    W : float
        Kendall's W [0:1]
    Example
    ---------
    annotations = [
        [1, 1, 1, 2], # item 1
        [2, 2, 2, 3], # item 2
        [3, 3, 3, 1], # item 3
    ]
    # Annotator #4 disagrees with the other annotators
    # Annotators #1, #2, #3 agree
    W = kendall_w(annotations)
    # output: 0.4375
    """

    assert isinstance(data, list), "You must pass a python list,\
        {} found".format(type(data))
    assert all(isinstance(x, list) for x in data), "You must pass a list of\
        python lists as input."  # To test
    assert all(isinstance(x[y], int) for x in data for y in range(len(x))), "You must\
        pass a list of lists of integers."  # To test

    # Number of annotators
    m = len(data[0])
    # Tests
    if not all(len(i) == m for i in data):
        raise ValueError("Items must all have the same number of annotators.\
            At least one sublist of argument 'data' has different length than\
            the first sublist.")
    if m <= 1:
        raise ValueError("Kendall's W is irrevelent for only one annotator,\
            try adding more lists to argument 'data'.")
    if m == 2:
        warnings.warn("Kendall's W is adapted to measure agreement between\
            more than two annotators. The results might not be reliable in\
            this case.", Warning)

    # Number of items
    n = len(data)
    # Tests
    if n <= 1:
        raise ValueError("Kendall's W is irrevelent for only one item,\
            try adding more sublists to argument 'data'.")

    # Sum of each item ranks
    sums = [sum(x) for x in data]
    # Mean of ranking sums
    Rbar = sum(sums) / n
    # Sum of squared deviations from the mean
    S = sum([(sums[x] - Rbar) ** 2 for x in range(n)])

    W = (12 * S) / (m ** 2 * (n ** 3 - n))

    return W

def kendall(x, y):
    assert len(x) == len(y) > 0
    c = 0 #concordant count
    d = 0 #discordant count
    t = 0 #tied count
    for (i, j) in combinations(xrange(len(x)), 2):
        s = (x[i] - x[j]) * (y[i] - y[j])
        if s:
            c += 1
            d += 1
            if s > 0:
                t += 1
            elif s < 0:
                t -= 1
        else:
            if x[i] - x[j]:
                c += 1
            elif y[i] - y[j]:
                d += 1
    return t / math.sqrt(c * d)
'''
annotations = []
for i in range(len(sum_all_1[0])):
    for model in sum_all_1:
        rank_a, rank_b, rank_c = sum_all_1[model][i],sum_all_2[model][i],sum_all_3[model][i]
        annotations.append([rank_a,rank_b,rank_c])
        
W = []
for i in range(len(sum_all_1[0])):
    W.append(compute_w(annotations[i*6:(i+1)*6]))
'''   





nlp = spacy.load("en_core_web_sm")
nlp.pipeline = [('tagger', nlp.tagger)]


def tokenize(dict):
    for key in dict:
        new_sentence_list = []
        for sentence in dict[key]:
            a = ''
            for token in nlp(unicode(sentence)):
                a += token.text
                a += ' '
            new_sentence_list.append(a.rstrip())
        dict[key] = new_sentence_list

    return dict


def evaluator(gts, res):
    eval = {}
    # =================================================
    # Set up scorers
    # =================================================
    print 'tokenization...'
    # Todo: use Spacy for tokenization
    gts = tokenize(gts)
    res = tokenize(res)

    # =================================================
    # Set up scorers
    # =================================================
    print 'setting up scorers...'
    scorers = [
        (Bleu(4), ["Bleu_1", "Bleu_2", "Bleu_3", "Bleu_4"]),
        (Meteor(), "METEOR"),
        # (Rouge(), "ROUGE_L"),
        (Cider(), "CIDEr"),
        (Spice(), "SPICE")
    ]

    # =================================================
    # Compute scores
    # =================================================
    for scorer, method in scorers:
        print 'computing %s score...' % (scorer.method())
        score, scores = scorer.compute_score(gts, res)
        if type(method) == list:
            for sc, scs, m in zip(score, scores, method):
                eval[m] = sc
                print "%s: %0.3f" % (m, sc)
        else:
            eval[method] = score
            print "%s: %0.3f" % (method, score)


def compute_agreement(scorer, lines):
    agreements = []
    for human_rank in human_ranks:
        #print(1)
        for idx_line,line in enumerate(lines):
            scores = []
            human_rank_line = []
            for idx,model in enumerate(models):
                gts = {}
                res = {}
                data = json.loads(line)
                key_line, gts_line, res_line = ' '.join(data['input']), data['sentences'][idx][1], data['references'][0]
                key = '#'.join(key_line.rstrip('\n').split(' '))
                if key not in gts:
                    gts[key] = []
                    gts[key].append(gts_line.rstrip('\n'))
                    res[key] = []
                    res[key].append(res_line.rstrip('\n'))

                score, scores_p = scorer.compute_score(gts, res)

                if isinstance(score,list):
                    #BLEU-4
                    scores.append(score[-1])
                else:
                    scores.append(score)
                human_rank_line.append(human_rank[model][idx_line])
            rank = list(np.argsort(-np.array(scores)))
            rank_real = []
            #print scores
            for i in range(len(rank)):
                rank_real.append(rank.index(i))
            #print(scores)
            #print(rank_real)
            try:
                score_tau = kendall(rank_real,human_rank_line)
            except:
                print ""
            else:
                agreements.append(score_tau)
    #print len(agreements)
    return np.mean(agreements)

if __name__=='__main__':
    model_index = {"Leven-Const": 0, "GPT-2": 1, "BERT-Gen": 2, "UniLM": 3, "BART": 4, "T5": 5}
    inversed_model_index = dict(map(reversed, model_index.items()))
    pairs_list = []

    with open("model_pairs.tsv") as f:
        for line in f.readlines():
            line = line.strip()
            if line != "":
                pairs_list.append((model_index[line.split("\t")[0]], model_index[line.split("\t")[1]]))

    # print(len(pairs_list))

    
    sum_all_1 = defaultdict(lambda: [0]*100)
    sum_all_2 = defaultdict(lambda: [0]*100)
    sum_all_3 = defaultdict(lambda: [0]*100)
    sum_all_4 = defaultdict(lambda: [0]*100)
    sum_all_5 = defaultdict(lambda: [0]*100)

    with open("human_eval_1.tsv") as f:
        index = 0
        group_count = 0
        group = False
        comparsions_better_than_me = defaultdict(list)
        idx = 0
        for line in f.readlines():
            line = line.strip()
            if group:
                if group_count == 15:
                    group_count = 0
                    group = False
                    continue

                model_pair = pairs_list[index]
                data = line.split("\t")
                s1 = data[0]
                s2 = data[1]
                score = float(data[2])
                flag = False
                if score > 0.5:
                    better, worse = model_pair[0], model_pair[1] 
                    flag = True
                elif score < 0.5:
                    worse, better = model_pair[0], model_pair[1]
                    flag = True
                if flag:
                    comparsions_better_than_me[inversed_model_index[worse]].append(inversed_model_index[better])
                index += 1
                group_count += 1
            else:
                if line.startswith("Concept set:"):
                    concept_set = line.strip().replace("Concept set:", "").split()
                if line.startswith("Reference:"):
                    group = True
                    # print(comparsions_better_than_me)
                    for model in model_index:
                        rank = len(comparsions_better_than_me.get(model, [])) 
                        #print(idx)
                        sum_all_1[model][idx] = rank
                    idx += 1
                    comparsions_better_than_me = defaultdict(list)
                    
    with open("human_eval_2.tsv") as f:
        index = 0
        group_count = 0
        group = False
        comparsions_better_than_me = defaultdict(list)
        idx = 0
        for line in f.readlines():
            line = line.strip()
            if group:
                if group_count == 15:
                    group_count = 0
                    group = False
                    continue

                model_pair = pairs_list[index]
                data = line.split("\t")
                s1 = data[0]
                s2 = data[1]
                score = float(data[2])
                flag = False
                if score > 0.5:
                    better, worse = model_pair[0], model_pair[1] 
                    flag = True
                elif score < 0.5:
                    worse, better = model_pair[0], model_pair[1]
                    flag = True
                if flag:
                    comparsions_better_than_me[inversed_model_index[worse]].append(inversed_model_index[better])
                index += 1
                group_count += 1
            else:
                if line.startswith("Concept set:"):
                    concept_set = line.strip().replace("Concept set:", "").split()
                if line.startswith("Reference:"):
                    group = True
                    # print(comparsions_better_than_me)
                    for model in model_index:
                        rank = len(comparsions_better_than_me.get(model, [])) 
                        #print(idx)
                        sum_all_2[model][idx] = rank
                    idx += 1
                    comparsions_better_than_me = defaultdict(list)
                    
                    
    with open("human_eval_3.tsv") as f:
        index = 0
        group_count = 0
        group = False
        comparsions_better_than_me = defaultdict(list)
        idx = 0
        for line in f.readlines():
            line = line.strip()
            if group:
                if group_count == 15:
                    group_count = 0
                    group = False
                    continue

                model_pair = pairs_list[index]
                data = line.split("\t")
                s1 = data[0]
                s2 = data[1]
                score = float(data[2])
                flag = False
                if score > 0.5:
                    better, worse = model_pair[0], model_pair[1] 
                    flag = True
                elif score < 0.5:
                    worse, better = model_pair[0], model_pair[1]
                    flag = True
                if flag:
                    comparsions_better_than_me[inversed_model_index[worse]].append(inversed_model_index[better])
                index += 1
                group_count += 1
            else:
                if line.startswith("Concept set:"):
                    concept_set = line.strip().replace("Concept set:", "").split()
                if line.startswith("Reference:"):
                    group = True
                    # print(comparsions_better_than_me)
                    for model in model_index:
                        rank = len(comparsions_better_than_me.get(model, [])) 
                        #print(idx)
                        sum_all_3[model][idx] = rank
                    idx += 1
                    comparsions_better_than_me = defaultdict(list)

    with open("human_eval_4.tsv") as f:
        index = 0
        group_count = 0
        group = False
        comparsions_better_than_me = defaultdict(list)
        idx = 0
        for line in f.readlines():
            line = line.strip()
            if group:
                if group_count == 15:
                    group_count = 0
                    group = False
                    continue

                model_pair = pairs_list[index]
                data = line.split("\t")
                s1 = data[0]
                s2 = data[1]
                score = float(data[2])
                flag = False
                if score > 0.5:
                    better, worse = model_pair[0], model_pair[1] 
                    flag = True
                elif score < 0.5:
                    worse, better = model_pair[0], model_pair[1]
                    flag = True
                if flag:
                    comparsions_better_than_me[inversed_model_index[worse]].append(inversed_model_index[better])
                index += 1
                group_count += 1
            else:
                if line.startswith("Concept set:"):
                    concept_set = line.strip().replace("Concept set:", "").split()
                if line.startswith("Reference:"):
                    group = True
                    # print(comparsions_better_than_me)
                    for model in model_index:
                        rank = len(comparsions_better_than_me.get(model, [])) 
                        #print(idx)
                        sum_all_4[model][idx] = rank
                    idx += 1
                    comparsions_better_than_me = defaultdict(list)

    with open("human_eval_5.tsv") as f:
        index = 0
        group_count = 0
        group = False
        comparsions_better_than_me = defaultdict(list)
        idx = 0
        for line in f.readlines():
            line = line.strip()
            if group:
                if group_count == 15:
                    group_count = 0
                    group = False
                    continue

                model_pair = pairs_list[index]
                data = line.split("\t")
                s1 = data[0]
                s2 = data[1]
                score = float(data[2])
                flag = False
                if score > 0.5:
                    better, worse = model_pair[0], model_pair[1] 
                    flag = True
                elif score < 0.5:
                    worse, better = model_pair[0], model_pair[1]
                    flag = True
                if flag:
                    comparsions_better_than_me[inversed_model_index[worse]].append(inversed_model_index[better])
                index += 1
                group_count += 1
            else:
                if line.startswith("Concept set:"):
                    concept_set = line.strip().replace("Concept set:", "").split()
                if line.startswith("Reference:"):
                    group = True
                    # print(comparsions_better_than_me)
                    for model in model_index:
                        rank = len(comparsions_better_than_me.get(model, [])) 
                        #print(idx)
                        sum_all_5[model][idx] = rank
                    idx += 1
                    comparsions_better_than_me = defaultdict(list)
                    
        gts = {}
        res = {}

    human_ranks = [sum_all_1,sum_all_2,sum_all_3,sum_all_4,sum_all_4]
    models = ['Leven-Const','GPT-2','BERT-Gen','UniLM','BART','T5']
    scorers = [
        (Bleu(4), "Bleu_4"),
        (Meteor(), "METEOR"),
        # (Rouge(), "ROUGE_L"),
        (Cider(), "CIDEr"),
        (Spice(), "SPICE")
    ]
    #scorers = [Bleu(4),Meteor(),Cider(),Spice()]

    with codecs.open('human_eval.jsonl', encoding='utf-8') as f:
        lines = f.readlines()
    for scorer,method in scorers:
        agg = compute_agreement(scorer,lines)
        print "The averaged Kendall's tau of %s with 5 human annotators is %s" % (method,str(agg))
        


