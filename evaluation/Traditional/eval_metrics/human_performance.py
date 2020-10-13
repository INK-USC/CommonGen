from bleu.bleu import Bleu
from meteor.meteor import Meteor
from rouge.rouge import Rouge
from cider.cider import Cider
from spice.spice import Spice
import spacy
import sys
import codecs
from collections import defaultdict
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--input_file', default="", type=str)
parser.add_argument('--mode', default="human", type=str) # human/oracle
args = parser.parse_args()


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

if __name__=='__main__':

    data_file = args.input_file

    gts = defaultdict(list)
    res = defaultdict(list)

    human_src = []
    human_tgt = []
    human_cs = []
    human_cs_str = []

    with codecs.open(data_file, encoding='utf-8') as f:
        for line in f.readlines():
            item_data = json.loads(line.strip())
            key_str = item_data["concept_set"]
            if args.mode == "human":
                item_data["scene"].sort(key= lambda x:len(x))
                item_data["scene"] = item_data["scene"][:3]
                for i in range(len(item_data["scene"])):
                    for j in range(len(item_data["scene"])):
                        key_str_i_j = key_str + str(i) + str(j)
                        gts[key_str_i_j] = [item_data["scene"][i]]
                        res[key_str_i_j] = [item_data["scene"][j]]
                        human_tgt.append(item_data["scene"][i])
                        human_src.append(item_data["scene"][j])
                        cs = item_data['concept_set'].split("#")
                        cs = [item[:-2] for item in cs]
                        human_cs.append(" ".join(cs))
                        human_cs_str.append(item_data['concept_set'])
            else:
                for j in range(len(item_data["caption_scene"])):
                    key_str_j = key_str + str(j)
                    gts[key_str_j] = item_data["scene"]
                    res[key_str_j] = [item_data["caption_scene"][j]]
    if args.mode == "human":
        with codecs.open(data_file+".human_src", "w", encoding="utf8") as f:
            print "writing " + f.name
            f.write("\n".join(human_src))
        with codecs.open(data_file+".human_tgt", "w", encoding="utf8") as f:
            print "writing " + f.name
            f.write("\n".join(human_tgt))
        with codecs.open(data_file+".human_cs", "w", encoding="utf8") as f:
            print "writing " + f.name
            f.write("\n".join(human_cs))
        with codecs.open(data_file+".human_cs_str", "w", encoding="utf8") as f:
            print "writing " + f.name
            f.write("\n".join(human_cs_str))
    evaluator(gts, res)
