#!/bin/bash

if [ $# -ne 2 ]; then
    echo "usage: $0 <lang> <path to BPE code>"
    exit 1
fi

l=$1
bpe_code=$2

echo 'Cloning Moses github repository (for tokenization scripts)...'
git clone https://github.com/moses-smt/mosesdecoder.git

echo 'Cloning Subword NMT repository (for BPE pre-processing)...'
git clone https://github.com/rsennrich/subword-nmt.git

if [ $l = "ro" ]; then
    echo 'Downloading Romanian preprocessing scripts...'
    wget -nc https://github.com/rsennrich/wmt16-scripts/raw/master/preprocess/normalise-romanian.py
    wget -nc https://github.com/rsennrich/wmt16-scripts/raw/master/preprocess/remove-diacritics.py
fi

SCRIPTS=mosesdecoder/scripts
TOKENIZER=$SCRIPTS/tokenizer/tokenizer.perl
CLEAN=$SCRIPTS/training/clean-corpus-n.perl
NORM_PUNC=$SCRIPTS/tokenizer/normalize-punctuation.perl
REM_NON_PRINT_CHAR=$SCRIPTS/tokenizer/remove-non-printing-char.perl
BPEROOT=subword-nmt

if [ $l = "ro" ]; then
    perl $NORM_PUNC $l | \
    perl $REM_NON_PRINT_CHAR | \
    python normalise-romanian.py | \
    python remove-diacritics.py | \
    perl $TOKENIZER -threads 8 -a -l $l
    python $BPEROOT/apply_bpe.py -c $bpe_code
else
    perl $NORM_PUNC $l | \
    perl $REM_NON_PRINT_CHAR | \
    perl $TOKENIZER -threads 8 -a -l $l | \
    python $BPEROOT/apply_bpe.py -c $bpe_code
fi
