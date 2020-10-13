
import sys

split = sys.argv[1]

input_lines = open('%s.src'%split).readlines()

with open('%s.const.src'%split,'w',encoding='utf8') as writer:

    for line in input_lines:
        elements = []
        elements.append(line.strip())
        for item in line.strip().split():
            elements.append(item+'|||'+item)
        writer.write('\t'.join(elements)+'\n')

