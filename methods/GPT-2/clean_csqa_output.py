train_output_lines = open('decode_result_train_csqa').readlines()

with open('gpt2.csqa.train','w',encoding='utf8') as writer:
    for line in train_output_lines:
        writer.write(line[line.find('=')+1:line.find('[E')].strip()+'\n')




dev_output_lines = open('decode_result_dev_csqa').readlines()

with open('gpt2.csqa.dev','w',encoding='utf8') as writer:
    for line in dev_output_lines:
        writer.write(line[line.find('=')+1:line.find('[E')].strip()+'\n')

