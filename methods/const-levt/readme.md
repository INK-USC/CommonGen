# Constrained-LevT


## Installation

```bash
# conda install pytorch torchvision cudatoolkit=10.1 -c pytorch
pip install torch==1.4.0 numpy
```

Install apex and the repo as a package:
```bash
git clone https://github.com/NVIDIA/apex.git && cd apex && pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
cd ..
cd constrained-levt
pip install --editable .

```

## Train to get checkpoint

#### Pre-processing
```bash
mkdir input_alpha
export TEXT=input_alpha
cp ../../../dataset/final_data/commongen/commongen.train.src_alpha.txt ./$TEXT/train.src
cp ../../../dataset/final_data/commongen/commongen.train.tgt.txt ./$TEXT/train.tgt
cp ../../../dataset/final_data/commongen/commongen.dev.src_alpha.txt ./$TEXT/dev.src
cp ../../../dataset/final_data/commongen/commongen.dev.tgt.txt ./$TEXT/dev.tgt
cp ../../../dataset/final_data/commongen/commongen.test.src_alpha.txt ./$TEXT/test.src
cp ../../../dataset/final_data/commongen/commongen.test.tgt.txt ./$TEXT/test.tgt
python preprocess.py --joined-dictionary --source-lang src --target-lang tgt --trainpref $TEXT/train --validpref $TEXT/dev --testpref $TEXT/test --destdir $TEXT/data-bin
```

#### Training a model 
```bash
export TEXT=input_alpha
CUDA_VISIBLE_DEVICES=1 python train.py \
    $TEXT/data-bin \
    --save-dir leven_checkpoints \
    --ddp-backend=no_c10d \
    --task translation_lev \
    --criterion nat_loss \
    --arch levenshtein_transformer \
    --noise random_delete \
    --share-all-embeddings \
    --optimizer adam --adam-betas '(0.9,0.98)' \
    --lr 0.0005 --lr-scheduler inverse_sqrt \
    --min-lr '1e-09' --warmup-updates 10000 \
    --warmup-init-lr '1e-07' --label-smoothing 0.1 \
    --dropout 0.3 --weight-decay 0.01 \
    --decoder-learned-pos \
    --encoder-learned-pos \
    --apply-bert-init \
    --log-format 'simple' --log-interval 100 \
    --fixed-validation-seed 7 \
    --max-tokens 1000 \
    --save-interval-updates 10000 \
    --max-update 300000 \
    --fp16 --reset-optimizer
```



## Use checkpoint to decode

- You need to first train a Levenshtein Transformer and place the data-bin file after preprocessing, the test.src, dev.src, and the checkpoint file "checkpoint_best.pt" under const-levt/

- Constrained Decoding
```bash
cd ..
cp -r constrained-levt/input_alpha/data-bin .
cp constrained-levt/leven_checkpoints/checkpoint_best.pt .
cp constrained-levt/input_alpha/test.src .
cp constrained-levt/input_alpha/dev.src .

export SPLIT=test
python prepare.py $SPLIT

cat $SPLIT.const.src \
| CUDA_VISIBLE_DEVICES=1 python constrained-levt/interactive_with_constraints.py \
    data-bin \
    -s src -t tgt \
    --task translation_lev \
    --path ./checkpoint_best.pt \
    --iter-decode-max-iter 15 \
    --iter-decode-eos-penalty 0 \
    --beam 1 \
    --print-step \
    --batch-size 400 \
    --buffer-size 4000 \
    --preserve-constraint | tee ./$SPLIT.out

cat ./$SPLIT.out \
| grep ^H \
| sed 's/^H\-//' \
| sort -n -k 1 \
| cut -f 3 > ./const-levt.$SPLIT

# also inference using dev data
export SPLIT=dev
python prepare.py $SPLIT

cat $SPLIT.const.src \
| CUDA_VISIBLE_DEVICES=1 python constrained-levt/interactive_with_constraints.py \
    data-bin \
    -s src -t tgt \
    --task translation_lev \
    --path ./checkpoint_best.pt \
    --iter-decode-max-iter 15 \
    --iter-decode-eos-penalty 0 \
    --beam 1 \
    --print-step \
    --batch-size 400 \
    --buffer-size 4000 \
    --preserve-constraint | tee ./${SPLIT}.out

cat ./${SPLIT}.out \
| grep ^H \
| sed 's/^H\-//' \
| sort -n -k 1 \
| cut -f 3 > ./const-levt.$SPLIT
```
- The decoding results are saved at "./const-levt.$SPLIT".




- Also can do origin leven decoding
```bash
cd constrained-levt
export TEXT=input_alpha
CUDA_VISIBLE_DEVICES=6 python generate.py \
    $TEXT/data-bin \
    --gen-subset test \
    --task translation_lev \
    --path ../checkpoint_best.pt \
    --iter-decode-max-iter 9 \
    --beam 5 --remove-bpe \
    --print-step \
    --batch-size 25 &> ./output/leven.alpha.test.txt

CUDA_VISIBLE_DEVICES=6 python generate.py \
    $TEXT/data-bin \
    --gen-subset valid \
    --task translation_lev \
    --path ../checkpoint_best.pt \
    --iter-decode-max-iter 9 \
    --beam 5 --remove-bpe \
    --print-step \
    --batch-size 25 &> ./output/leven.alpha.dev.txt


python ./output/process_output.py
```
- The decoding results are saved at final.leven.alpha.test.txt and final.leven.alpha.dev.txt


