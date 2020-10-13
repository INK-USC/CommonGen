test_src = open('csqa.train.qac.src','r',encoding='utf8').readlines()

with open("inference_train_csqa.txt", "w", encoding="utf8") as writer:
    for i in range(len(test_src)):
        writer.write('[SOS] ' + test_src[i].strip() + ' = ')
        if i != len(test_src) - 1:
            writer.write("\n")


dev_src = open('csqa.dev.qac.src','r',encoding='utf8').readlines()

with open("inference_dev_csqa.txt", "w", encoding="utf8") as writer:
    for i in range(len(dev_src)):
        writer.write('[SOS] ' + dev_src[i].strip() + ' = ')
        if i != len(dev_src) - 1:
            writer.write("\n")
