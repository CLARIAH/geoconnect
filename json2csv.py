#! /usr/bin/env python3
import pandas as pd
import json
import sys

def flatten(data, prefix=None):
    if isinstance(data, dict):
        result = {}
        for k, v in data.items():
            result.update(flatten(v, (prefix + '-' if prefix else '') + str(k)))
    elif isinstance(data, list):
        result = {}
        for k, v in enumerate(data):
            result.update(flatten(v, (prefix + '-' if prefix else '') + str(k)))
    else:
        result = {prefix: data}
    return result

def get_dotted_path(path, obj):
    return get_path_as_list(path.split('.'), obj)

def get_path_as_list(path, obj):
    if path:
        return get_path_as_list(path[1:], obj.__getitem__(path[0]))
    return obj

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument(
        'root_iterable',
        help='Dotted path to json array with the main entries, e.g.'
        '`things.features`.')

    args = parser.parse_args()

    with open(args.input_file) as fd:
        data = json.load(fd)

    pd.DataFrame(map(
        flatten,
        get_dotted_path(args.root_iterable, data))
    ).to_csv(sys.stdout)
