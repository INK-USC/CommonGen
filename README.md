## CommonGen: A Constrained Text Generation Challenge Towards Generative Commonsense Reasoning

**CommonGen** is a new _constrained text generation_ dataset that requires different kinds of commonsense to generate sentences about everyday scenarios, and thus targets **generative commonsense reasoning**. This repo is for tracking the latest dataset, some baseline models and our evaluation scripts. Please check [http://inklab.usc.edu/CommonGen/](http://inklab.usc.edu/CommonGen/) for more details. Note that our [arxiv article](https://arxiv.org/abs/1911.03705) may contain some _outdated_ statistics and information.


<img src="http://inklab.usc.edu/CommonGen/intro.png" width="700">

#### Content

- `dataset/final_data` saves the latest version of the data. We may have updates on the dataset in the future. Please stay tuned.

- `methods` shows some baseline methods with many frameworks such as OpenNMT and Fariseq, as well as UniLM.

- `evaluation` contains the evaluation scripts for a variety of automatic metrics for testing the performance of system predictions against human-written results.


#### Citation


```
@article{lin2019comgen,
    author = {Bill Yuchen Lin and Ming Shen and Wangchunshu Zhou and Pei Zhou and Chandra Bhagavatula and Yejin Choi and Xiang Ren},
    title = {CommonGen: A Constrained Text Generation Challenge for Generative Commonsense Reasoning},
    journal = {Findings of EMNLP},
    year = {2020}
    note = {to appear}
}
```

#### Contact

Feel free to directly email yuchen[dot]lin[at]usc[dot]edu if you have any feedback. 
