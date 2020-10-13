import argparse
import re


parser = argparse.ArgumentParser(description='Compute term usage rate.')
parser.add_argument('--input', '-i', required=True,
                    help='input file with constraints')
parser.add_argument('--hyp', '-s', required=True,
                    help='hypothesis file')

args = parser.parse_args()


with open(args.input) as fin, open(args.hyp) as fhyp:
    inp = fin.readlines()
    hyp = fhyp.readlines()
    assert len(inp) == len(hyp)
    count = 0
    total = 0
    for i, h in zip(inp, hyp):
        h = h.strip()
        d = i.strip().split('\t')[1:]
        for const in d:
            t = const.split('|||')[1].strip()
            if re.search(r'(\W|^){}(\W|$)'.format(re.escape(t)), h):
                count += 1
            total += 1
    print("Term use rate: {:.3f}".format(count*100/total))
