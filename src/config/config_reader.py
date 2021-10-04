import yaml


def read_yaml(filename):
    with open(f"config/{filename}.yaml", "r") as f:
        return yaml.safe_load(f)
