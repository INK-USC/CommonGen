## Fairseq-based Baseline: A case of Levenshtein transformer 

### Prerequisite
* PyTorch version >= 1.2.0
* Python version >= 3.5
* For training new models, you'll also need an NVIDIA GPU and NCCL
* For faster training install NVIDIA's apex library with the --cuda_ext option

### Installation
```bash
#conda create -n fairseq-leven python==3.6.3
#conda activate fairseq-leven
#pip install torch==1.3.1+cu92 torchvision==0.4.2+cu92 -f https://download.pytorch.org/whl/torch_stable.html  --no-cache-dir
conda create -n leven python=3.6
conda activate leven
pip install torch==1.4.0 numpy

git clone https://github.com/NVIDIA/apex.git && cd apex && pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
cd ../fairseq_local/
pip install --editable .
```

### Pre-processing
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


### Training a model 
```bash
export TEXT=input_alpha
CUDA_VISIBLE_DEVICES=0 python train.py \
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
### Generating sentences 

- dev set
```bash
export TEXT=input_alpha
CUDA_VISIBLE_DEVICES=0 python generate.py \
    $TEXT/data-bin \
    --gen-subset valid \
    --task translation_lev \
    --path leven_checkpoints/leven_checkpoints_best.pt \
    --iter-decode-max-iter 15 \
    --beam 5 --remove-bpe \
    --print-step \
    --batch-size 400 &> ./output/leven.alpha.dev.txt 
```

- test set
```bash
export TEXT=input_alpha
#CUDA_VISIBLE_DEVICES=1 python generate.py \
#    $TEXT/data-bin \
#    --gen-subset test \
#    --task translation_lev \
#    --path leven_checkpoints/checkpoint_best.pt \
#    --iter-decode-max-iter 9 \
#    --beam 5 --remove-bpe \
#    --print-step \
#    --batch-size 25 &> ./output/leven.alpha.test.txt
CUDA_VISIBLE_DEVICES=2 python generate.py \
    $TEXT/data-bin \
    --gen-subset test \
    --task translation_lev \
    --path ../../const-levt/checkpoint_best.pt \
    --iter-decode-max-iter 9 \
    --beam 5 --remove-bpe \
    --print-step \
    --batch-size 25 &> ./output/leven.alpha.test.txt
```

#### Post-processing the outputs
```bash
python ./output/process_output.py
```
The final formatted generation results would be `ordered.*.txt` files.