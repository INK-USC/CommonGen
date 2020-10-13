import spacy
import json
from tqdm import tqdm

nlp = spacy.load('en_core_web_sm')
nlp.pipeline = [("tagger", nlp.tagger)]

blacklist = ["would", "someone", "something", "man", "woman", "boy", "girl", "can", "how", "go", "can", "take", "may", "want", "have", "get", "people", "person", "?", ",", "."]

train_lines = open('dev_rand_split.jsonl').read().split("\n")[:-1]

def get_concepts(sentence, is_q=True):
    if not is_q:
        return sentence.split()

    doc = nlp(sentence)
    concepts = []
    for tok in doc:
        if not tok.is_stop and tok.lemma_.lower() not in blacklist: 
            # print(tok.lemma_,blacklist)
            if tok.pos_ in ["NOUN", "VERB"]:
                concepts.append(tok.lemma_.lower())
    # if concepts == []:    
    #     for tok in doc:
    #         if not tok.is_stop and tok.lemma_.lower() not in blacklist:  
    #             concepts.append(tok.lemma_.lower()) 
    return concepts[:4] 

question_concepts_lines = []
question_answer_concepts_lines = []
question_texts = []
answer_indexs = []
choice_texts = []

for id, line in tqdm(enumerate(train_lines[:]), total=len(train_lines)):
    item = json.loads(line)
    question = item['question']['stem']
    all_question_concepts = [item['question']['question_concept']] + get_concepts(question)
    question_concepts = list(set(all_question_concepts))

    choices = item['question']['choices']
    question_concepts_lines.append(" ".join(question_concepts))
    # if len(question_concepts) <=1: 
    #     continue
    truth_answer = ord(item["answerKey"])-ord("A")
    # break
    answer_indexs.append(str(truth_answer))
    for choice in choices:
        # answer_concepts = get_concepts(choice['text'], is_q=False)
        # writer.write(str(id)+'\t'+choice['label']+'\t'+' '.join(question_concepts+answer_concepts)+'\n')
        qa_concepts = question_concepts + choice['text'].split()
        choice_texts.append(choice['text'])
        question_answer_concepts_lines.append(" ".join(list(set(qa_concepts))))
        question_texts.append(question)
    
#lines = open('concepts.train').readlines()

#with open('concept.train.src','w',encoding='utf8') as writer:
#    for line in lines:
#        writer.write(line.split('\t')[-1])

with open('csqa.dev.qac.src','w',encoding='utf8') as f:
    f.write("\n".join(question_answer_concepts_lines))

with open('csqa.dev.questions','w',encoding='utf8') as f:
    f.write("\n".join(question_texts))

with open('csqa.dev.answers','w',encoding='utf8') as f:
    f.write("\n".join(answer_indexs))

with open('csqa.dev.choices','w',encoding='utf8') as f:
    f.write("\n".join(choice_texts))