---
language: english
thumbnail:
---

# SpanBERT large fine-tuned on SQuAD v1

[SpanBERT](https://github.com/facebookresearch/SpanBERT) created by [Facebook Research](https://github.com/facebookresearch) and fine-tuned on [SQuAD 1.1](https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/) for **Q&A** downstream task ([by them](https://github.com/facebookresearch/SpanBERT#finetuned-models-squad-1120-relation-extraction-coreference-resolution)).

## Details of SpanBERT

[SpanBERT: Improving Pre-training by Representing and Predicting Spans](https://arxiv.org/abs/1907.10529)

## Details of the downstream task (Q&A) - Dataset 📚 🧐 ❓

[SQuAD1.1](https://rajpurkar.github.io/SQuAD-explorer/)

## Model fine-tuning 🏋️‍

You can get the fine-tuning script [here](https://github.com/facebookresearch/SpanBERT)

```bash
python code/run_squad.py \
  --do_train \
  --do_eval \
  --model spanbert-large-cased \
  --train_file train-v1.1.json \
  --dev_file dev-v1.1.json \
  --train_batch_size 32 \
  --eval_batch_size 32  \
  --learning_rate 2e-5 \
  --num_train_epochs 4 \
  --max_seq_length 512 \
  --doc_stride 128 \
  --eval_metric f1 \
  --output_dir squad_output \
  --fp16
```

## Results Comparison 📝

|                   | SQuAD 1.1     | SQuAD 2.0  | Coref   | TACRED |
| ----------------------  | ------------- | ---------  | ------- | ------ |
|                         | F1            | F1         | avg. F1 |  F1    |
| BERT (base)             | 88.5*         | 76.5*      | 73.1    |  67.7  |
| SpanBERT (base)         | [92.4*](https://huggingface.co/mrm8488/spanbert-base-finetuned-squadv1)         | [83.6*](https://huggingface.co/mrm8488/spanbert-base-finetuned-squadv2)      | 77.4    |  [68.2](https://huggingface.co/mrm8488/spanbert-base-finetuned-tacred)  |
| BERT (large)            | 91.3          | 83.3       | 77.1    |  66.4  |
| SpanBERT (large)        | **94.6** (this)         | [88.7](https://huggingface.co/mrm8488/spanbert-large-finetuned-squadv2)     | 79.6    |  [70.8](https://huggingface.co/mrm8488/spanbert-large-finetuned-tacred)  |


Note: The numbers marked as * are evaluated on the development sets becaus those models were not submitted to the official SQuAD leaderboard. All the other numbers are test numbers.

## Model in action

Fast usage with **pipelines**:

```python
from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="mrm8488/spanbert-large-finetuned-squadv1",
    tokenizer="SpanBERT/spanbert-large-cased"
)

qa_pipeline({
    'context': "Manuel Romero has been working very hard in the repository hugginface/transformers lately",
    'question': "How has been working Manuel Romero lately?"

})

# Output: {'answer': 'very hard in the repository hugginface/transformers',
 'end': 82,
 'score': 0.327230326857725,
 'start': 31}
```

> Created by [Manuel Romero/@mrm8488](https://twitter.com/mrm8488)

> Made with <span style="color: #e25555;">&hearts;</span> in Spain
