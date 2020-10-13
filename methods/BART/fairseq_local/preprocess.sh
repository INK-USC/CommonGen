mkdir input
export TEXT=input
cp ../../../dataset/final_data/commongen/commongen.train.src_alpha.txt ./$TEXT/train.src
cp ../../../dataset/final_data/commongen/commongen.train.tgt.txt ./$TEXT/train.tgt
cp ../../../dataset/final_data/commongen/commongen.dev.src_alpha.txt ./$TEXT/dev.src
cp ../../../dataset/final_data/commongen/commongen.dev.tgt.txt ./$TEXT/dev.tgt
cp ../../../dataset/final_data/commongen/commongen.test.src_alpha.txt ./$TEXT/test.src
cp ../../../dataset/final_data/commongen/commongen.test.tgt.txt ./$TEXT/test.tgt

wget -N 'https://dl.fbaipublicfiles.com/fairseq/gpt2_bpe/encoder.json'
wget -N 'https://dl.fbaipublicfiles.com/fairseq/gpt2_bpe/vocab.bpe'
wget -N 'https://dl.fbaipublicfiles.com/fairseq/gpt2_bpe/dict.txt'

for SPLIT in train dev test
do
  for LANG in src tgt
  do
    python -m examples.roberta.multiprocessing_bpe_encoder \
    --encoder-json encoder.json \
    --vocab-bpe vocab.bpe \
    --inputs "./input/$SPLIT.$LANG" \
    --outputs "./input/$SPLIT.bpe.$LANG" \
    --workers 20 \
    --keep-empty;
  done
done

fairseq-preprocess \
  --source-lang "src" \
  --target-lang "tgt" \
  --trainpref "./input/train.bpe" \
  --validpref "./input/dev.bpe" \
  --destdir "./commongen-bin/" \
  --workers 20 \
  --srcdict dict.txt \
  --tgtdict dict.txt