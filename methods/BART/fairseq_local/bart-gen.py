import torch
import sys
from fairseq.models.bart import BARTModel
from tqdm import tqdm 


split = sys.argv[1]

bart = BARTModel.from_pretrained(
    'tmp/saved_models_final/',
    checkpoint_file='checkpoint_best.pt',
    data_name_or_path='commongen-bin'
)

bart.cuda()
bart.eval()
bart.half()
count = 1
bsz = 16
with open('input/%s.src'%split) as source:
    source_lines = source.read().split("\n")
sline = source_lines[0]
slines = [sline]
i = 0
res = []
scores = []
for sline in tqdm(source_lines[1:]):
    if count % bsz == 0:
        with torch.no_grad():
            hypotheses_batch = bart.sample(slines, output_score=True, beam=5, lenpen=0, max_len_b=64, no_repeat_ngram_size=2, min_len=2)

        for hypothesis in hypotheses_batch:
            res.append(hypothesis[0])
            scores.append(hypothesis[1])
            # fout.write(hypothesis + '\n')
            # fout.flush()
        slines = []
        i += 1
        # print(i)
    slines.append(sline.strip())
    count += 1
if slines != []:
    hypotheses_batch = bart.sample(slines, output_score=True, beam=5, lenpen=0, max_len_b=64, no_repeat_ngram_size=2, min_len=2)
    for hypothesis in hypotheses_batch:
        res.append(hypothesis[0])
        scores.append(hypothesis[1])
        # fout.write(hypothesis + '\n')
        # fout.flush()
with open('bart.%s'%split, 'w') as fout:
    fout.write("\n".join(res))

with open('bart.%s.scores'%split, 'w') as fout:
    fout.write("\n".join([str(float(s)) for s in scores]))