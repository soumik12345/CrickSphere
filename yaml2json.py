import yaml
import json
from glob import glob
from tqdm import tqdm
from datetime import datetime, date


def yaml2json(yaml_file: str, json_file: str):

    def default_function(o):
        if isinstance(o, (date, datetime)):
            return o.isoformat()

    with open(yaml_file, 'r') as yaml_in, open(json_file, 'w') as json_out:
        yaml_object = yaml.safe_load(yaml_in)
        json.dump(
            yaml_object, json_out, indent=1,
            default=default_function, sort_keys=True
        )


if __name__ == '__main__':
    yaml_files = glob('./data/all/*')
    for yaml_file in tqdm(yaml_files):
        yaml2json(
            yaml_file,
            yaml_file.replace(
                'all', 'json'
            ).replace(
                'yaml', 'json'
            )
        )
