import yaml


def read_yaml(filename):
    with open("src/config/" + filename + ".yaml", "r") as f:
        return yaml.safe_load(f)
