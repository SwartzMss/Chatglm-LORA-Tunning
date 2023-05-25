#coding:utf-8
import argparse
import json
from tqdm import tqdm


def format_example(example: dict) -> dict:
    context = f"{example['instruction']}\n"
    target = example['output']
    return {"Instruction": context, "output": target}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, default="data/alpaca_data.json")
    parser.add_argument("--save_path", type=str, default="data/alpaca_data.jsonl")

    args = parser.parse_args()
    with open(args.data_path,'r', encoding='UTF-8') as f:
        examples = json.load(f)

    with open(args.save_path, 'w') as f:
        for example in tqdm(examples, desc="formatting.."):
            f.write(json.dumps(format_example(example)) + '\n')


if __name__ == "__main__":
    main()
