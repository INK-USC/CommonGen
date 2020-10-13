train_src = open('train.src','r',encoding='utf8').readlines()
train_tgt = open('train.tgt','r',encoding='utf8').readlines()

assert(len(train_src) == len(train_tgt))

with open('train.txt','w',encoding='utf8') as writer:
    for i in range(len(train_src)):
        writer.write('[SOS] '+ train_src[i].strip() + ' = ' + train_tgt[i].strip() + ' [EOS]')
        if i != len(train_src) - 1:
            writer.write("\n")




dev_src = open('dev.src','r',encoding='utf8').readlines()
dev_tgt = open('dev.tgt','r',encoding='utf8').readlines()

assert(len(dev_src) == len(dev_tgt))

with open('dev.txt','w',encoding='utf8') as writer:
    for i in range(len(dev_src)):
        writer.write('[SOS] '+ dev_src[i].strip() + ' = ' + dev_tgt[i].strip() + ' [EOS]')
        if i != len(dev_src) - 1:
            writer.write("\n")


## generate dev and test to inference
##########################################################################
test_src = open('test.src','r',encoding='utf8').readlines()

with open("inference_test.txt", "w", encoding="utf8") as writer:
    for i in range(len(test_src)):
        writer.write('[SOS] ' + test_src[i].strip() + ' = ')
        if i != len(test_src) - 1:
            writer.write("\n")


dev_src = open('dev.src','r',encoding='utf8').readlines()

with open("inference_dev.txt", "w", encoding="utf8") as writer:
    for i in range(len(dev_src)):
        writer.write('[SOS] ' + dev_src[i].strip() + ' = ')
        if i != len(dev_src) - 1:
            writer.write("\n")
