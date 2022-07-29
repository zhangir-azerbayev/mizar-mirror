import os

import datasets
from datasets import load_dataset

files_dir = "mml"

dataset = load_dataset("text", data_dir=files_dir)

print(dataset["train"][0:100])
