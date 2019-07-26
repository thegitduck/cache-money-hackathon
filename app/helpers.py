from json import dumps
from yaml import Loader, load
from pathlib import Path


def pretty_print_dict(D):
	print(dumps(D, indent=1))


def get_proj_dir():
    my_path = str(Path.resolve(Path(__file__)))
    return my_path[:my_path.index(__name__)]


def get_vars(target):
  # Get config file variables
  path = get_proj_dir()
  file = f"{path}config.yaml"
  open(file)
  result = load(open(file), Loader=Loader)[target]

  return result
