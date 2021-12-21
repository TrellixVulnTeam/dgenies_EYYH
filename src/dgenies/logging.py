from logging.config import dictConfig
import yaml

with open('src/dgenies/logging.yaml') as f:
    data = yaml.full_load(f)
    dictConfig(data)

