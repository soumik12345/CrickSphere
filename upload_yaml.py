import json
import yaml
import pymongo
from glob import glob
from tqdm import tqdm
from datetime import date, datetime
from yaml2json import yaml2json


if __name__ == '__main__':
    yaml_files = glob('./data/odis/*.yaml')

    client = pymongo.MongoClient(
        "mongodb+srv://geekyrakshit:qwerty123456@cricket.ndu0h.mongodb.net/test_cricket?retryWrites=true&w=majority"
    )
    database = client["odi_cricket"]
    columns = database['matches']

    for file_name in tqdm(yaml_files):
        yaml2json(file_name, './sample.json')
        with open('./sample.json', 'r') as json_out:
            json_obj = json.loads(json_out.read())
        x = columns.insert(json_obj, check_keys=False)
