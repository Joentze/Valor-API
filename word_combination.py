#import py modules
import json
from sentiment_analysis import SA_package_contents_json


def get_dict_from_json(file_dir):
    with open(file_dir, 'r') as word_json:
        WORD_MAP=json.load(word_json)
    return WORD_MAP

WORD_MAP = get_dict_from_json('./data/word_map.json')

def return_token_combi(string):
    words = string.split(' ')
    return_combi = []
    all_words = list(WORD_MAP)
    for word in words:
        if word in all_words:
            return_combi.append(WORD_MAP[word.lower().strip()])
    return return_combi



if __name__ == "__main__":
    string = ''
    print(return_token_combi(string))
    print(SA_package_contents_json(string))
