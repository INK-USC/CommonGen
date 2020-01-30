export TEXT=input_alpha
python generate.py \
    $TEXT/data-bin \
    --gen-subset valid \
    --task translation_lev \
    --path leven_checkpoints/leven_checkpoints_best.pt \
    --iter-decode-max-iter 15 \
    --beam 5 --remove-bpe \
    --print-step \
    --batch-size 400 &> ./output/leven.alpha.dev.txt

export TEXT=input_alpha
python generate.py \
    $TEXT/data-bin \
    --gen-subset test \
    --task translation_lev \
    --path leven_checkpoints/leven_checkpoints_best.pt \
    --iter-decode-max-iter 9 \
    --beam 5 --remove-bpe \
    --print-step \
    --batch-size 400 &> ./output/leven.alpha.test.txt

export TEXT=input_reason
python generate.py \
    $TEXT/data-bin \
    --gen-subset valid \
    --task translation_lev \
    --path leven_reason_checkpoints/leven_reason_checkpoints_best.pt \
    --iter-decode-max-iter 15 \
    --beam 5 --remove-bpe \
    --print-step \
    --batch-size 400 &> ./output/leven.reason.dev.txt

export TEXT=input_reason
python generate.py \
    $TEXT/data-bin \
    --gen-subset test \
    --task translation_lev \
    --path leven_reason_checkpoints/leven_reason_checkpoints_best.pt \
    --iter-decode-max-iter 9 \
    --beam 5 --remove-bpe \
    --print-step \
    --batch-size 400 &> ./output/leven.reason.test.txt

python ./output/process_output.py