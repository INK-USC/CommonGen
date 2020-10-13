# BART


## Installation

```bash
conda create -n bart python=3.7
conda activate bart
pip install torch===1.4.0
git clone https://github.com/NVIDIA/apex.git && cd apex && python setup.py install --cuda_ext --cpp_ext
```

Install the repo as a package:
```bash
cd ..
cd fairseq_local ; pip install --editable .
```



## Train and test for BART

- Download pre-trained `bart.large` | BART model with 12 encoder and decoder layers | 400M | at [bart.large.tar.gz](https://dl.fbaipublicfiles.com/fairseq/models/bart.large.tar.gz)
```bash
wget https://dl.fbaipublicfiles.com/fairseq/models/bart.large.tar.gz
```

- Pre-processing
```bash
# under fairseq_local
bash preprocess.sh
```

- Training

```bash
TOTAL_NUM_UPDATES=2000  
WARMUP_UPDATES=200      
LR=2e-05
MAX_TOKENS=256
UPDATE_FREQ=4
BART_PATH=./bart.large/model.pt

CUDA_VISIBLE_DEVICES=0,1,2,3 fairseq-train commongen-bin \
    --restore-file $BART_PATH \
    --max-tokens $MAX_TOKENS \
    --save-dir tmp/saved_models_final \
    --save-interval-updates 100 \
    --no-epoch-checkpoints \
    --task translation \
    --source-lang src --target-lang tgt \
    --layernorm-embedding \
    --share-all-embeddings \
    --share-decoder-input-output-embed \
    --reset-optimizer --reset-dataloader --reset-meters \
    --required-batch-size-multiple 1 \
    --arch bart_large \
    --criterion label_smoothed_cross_entropy \
    --label-smoothing 0.1 \
    --dropout 0.1 --attention-dropout 0.1 \
    --weight-decay 0.01 --optimizer adam --adam-betas "(0.9, 0.999)" --adam-eps 1e-08 \
    --clip-norm 0.1 \
    --lr-scheduler polynomial_decay --lr $LR --max-update $TOTAL_NUM_UPDATES --warmup-updates $WARMUP_UPDATES \
    --update-freq $UPDATE_FREQ \
    --skip-invalid-size-inputs-valid-test \
    --find-unused-parameters \
    --fp16 
    # --no-progress-bar
```
6h training on 3 titan 
- Decoding

```bash
CUDA_VISIBLE_DEVICES=3 python bart-gen.py dev
CUDA_VISIBLE_DEVICES=4 python bart-gen.py test
```

- The decoding results are saved at "dev/test.res".


## output ppl of references 
```bash 
CUDA_VISIBLE_DEVICES=3 python bart-ppl.py dev
CUDA_VISIBLE_DEVICES=4 python bart-ppl.py test
```



