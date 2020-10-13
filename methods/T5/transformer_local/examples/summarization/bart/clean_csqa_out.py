train_output_lines = open('train_csqa.txt','r',encoding='utf8').readlines()

with open('t5.csqa.train','w',encoding='utf8') as writer:
    for line in train_output_lines:
        writer.write(line[:line.find('.')].strip()+'.\n')



val_output_lines = open('val_csqa.txt','r',encoding='utf8').readlines()

with open('t5.csqa.dev','w',encoding='utf8') as writer:
    for line in val_output_lines:
        writer.write(line[:line.find('.')].strip()+'.\n')
