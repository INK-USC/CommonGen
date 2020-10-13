test_output_lines = open('decode_result').readlines()

with open('new.gpt2.test','w',encoding='utf8') as writer:
    for line in test_output_lines:
        writer.write(line[line.find('=')+1:line.find('[E')].strip()+'\n')


dev_output_lines = open('decode_result_dev').readlines()

with open('new.gpt2.dev','w',encoding='utf8') as writer:
    for line in dev_output_lines:
        writer.write(line[line.find('=')+1:line.find('[E')].strip()+'\n')

