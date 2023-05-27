import json
import importlib_resources


__config = None

ref = importlib_resources.files("terraform_checker").joinpath('config.json')
with ref.open("rb") as fp:
    __config = json.load(fp)

CONFIG = __config
