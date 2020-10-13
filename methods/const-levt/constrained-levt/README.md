# Constrained-LevT

This repository contains the code for the ACL-20 paper: Lexically Constrained Neural Machine Translation with Levenshtein Transformer. If you use this repository in your work, please cite:

```bibtex
@article{susanto2020lexically,
  title={Lexically Constrained Neural Machine Translation with Levenshtein Transformer},
  author={Susanto, Raymond Hendy and Chollampatt, Shamil and Tan, Liling},
  journal={arXiv preprint arXiv:2004.12681},
  year={2020}
}
```

## Requirements and Installation

* [PyTorch](http://pytorch.org/) version >= 1.2.0
* Python version >= 3.6

```bash
git clone https://github.com/raymondhs/constrained-levt
cd constrained-levt
pip install --editable .
```

## Usage

To replicate the experiments in our paper, you can download our [pretrained models and evaluation sets](https://github.com/raymondhs/constrained-levt/releases) into the root directory of this repository. These models were trained following the [original instructions to train Levenshtein Transformer model](https://github.com/pytorch/fairseq/tree/master/examples/nonautoregressive_translation). To preserve each constraint in the output, use `--preserve-constraint`. For example:

```bash
mkdir -p data-bin
tar -xvzf const_levt_en_de.tgz -C data-bin
cat data-bin/const_levt_en_de/newstest2014-wikt.en \
| python interactive_with_constraints.py \
    data-bin/const_levt_en_de \
    -s en -t de \
    --task translation_lev \
    --path data-bin/const_levt_en_de/checkpoint_best.pt \
    --iter-decode-max-iter 9 \
    --iter-decode-eos-penalty 0 \
    --beam 1 \
    --print-step \
    --batch-size 400 \
    --buffer-size 4000 \
    --preserve-constraint | tee /tmp/gen.out
# ...
# | Translated 3003 sentences (87040 tokens) in 11.5s (261.37 sentences/s, 7575.50 tokens/s)

# Compute term usage rate
cat /tmp/gen.out \
| grep ^H \
| sed 's/^H\-//' \
| sort -n -k 1 \
| cut -f 3 > /tmp/gen.out.sys
python scripts/term_usage_rate.py \
    -i data-bin/const_levt_en_de/newstest2014-wikt.en \
    -s /tmp/gen.out.sys
# Term use rate: 100.000
```

Each input line is tab-separated, where the first column corresponds to the source text and the remaining columns for the constraints. Each constraint is provided in this format: `source|||target`. A preprocessing script (`tokenize.sh`) is provided in case you want to try with your own input. It will run tokenization, BPE segmentation, and additional preprocessing for Romanian. For example:

```bash
echo 'Hello world!' | ./tokenize.sh en data-bin/const_levt_en_de/ende.code
```

## License

The code and models in this repository are licensed under the MIT License. The evaluation datasets are licensed under [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
