import yaml
from os import getcwd


def read_yaml(filename):
    with open(f"src/config/{filename}.yaml", "r") as f:
        return yaml.safe_load(f)
