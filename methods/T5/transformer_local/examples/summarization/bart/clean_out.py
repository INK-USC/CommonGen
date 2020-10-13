test_output_lines = open('test.txt','r',encoding='utf8').readlines()

with open('t5.test','w',encoding='utf8') as writer:
    for line in test_output_lines:
        writer.write(line[:line.find('.')].strip()+'.\n')



val_output_lines = open('val.txt','r',encoding='utf8').readlines()

with open('t5.dev','w',encoding='utf8') as writer:
    for line in val_output_lines:
        writer.write(line[:line.find('.')].strip()+'.\n')
