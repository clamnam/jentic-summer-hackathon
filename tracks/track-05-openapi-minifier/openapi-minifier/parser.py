import yaml
yaml_file = '../examples/simple-spec.yaml'
def parser():

    with open(yaml_file, 'r') as file:
        prime_service = yaml.safe_load(file)
        print(prime_service)
