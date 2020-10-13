# Model upload and sharing

Starting with `v2.2.2`, you can now upload and share your fine-tuned models with the community, using the <abbr title="Command-line interface">CLI</abbr> that's built-in to the library.

**First, create an account on [https://huggingface.co/join](https://huggingface.co/join)**. Optionally, join an existing organization or create a new one. Then:

```shell
transformers-cli login
# log in using the same credentials as on huggingface.co
```
Upload your model:
```shell
transformers-cli upload ./path/to/pretrained_model/

# ^^ Upload folder containing weights/tokenizer/config
# saved via `.save_pretrained()`

transformers-cli upload ./config.json [--filename folder/foobar.json]

# ^^ Upload a single file
# (you can optionally override its filename, which can be nested inside a folder)
```

If you want your model to be namespaced by your organization name rather than your username, add the following flag to any command:
```shell
--organization organization_name
```

Your model will then be accessible through its identifier, a concatenation of your username (or organization name) and the folder name above:
```python
"username/pretrained_model"
# or if an org:
"organization_name/pretrained_model"
```

**Please add a README.md model card** to the repo under `model_cards/` with: model description, training params (dataset, preprocessing, hardware used, hyperparameters), evaluation results, intended uses & limitations, etc.

Your model now has a page on huggingface.co/models 🔥

Anyone can load it from code:
```python
tokenizer = AutoTokenizer.from_pretrained("namespace/pretrained_model")
model = AutoModel.from_pretrained("namespace/pretrained_model")
```

List all your files on S3:
```shell
transformers-cli s3 ls
```

You can also delete unneeded files:

```shell
transformers-cli s3 rm …
```
