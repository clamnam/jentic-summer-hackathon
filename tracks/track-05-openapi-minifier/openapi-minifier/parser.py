import yaml


def parser():
    yaml_file = '../examples/simple-spec.yaml'
    with open(yaml_file, 'r', encoding='utf-8') as f:
        docs = list(yaml.safe_load_all(f))
    for doc in docs:
        print(doc)
