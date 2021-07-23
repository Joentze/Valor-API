#import python modules
import requests as rq
import json
import os
from word_combination import get_dict_from_json

#import dictionary from JSON 
API_JSON = get_dict_from_json('./data/API_collection.json')["API"]

def navigate_to_key(dictionary, key_dir_from_root_list):
    curr_dict = dictionary
    try:    
        for curr_key in key_dir_from_root_list:
            curr_dict = curr_dict[curr_key]
        return curr_dict
    except:
        return "something went wrong!"
    
def process_json_response(JSON_response,KEYS_IN_JSON):
    THIS_JSON = JSON_response.json()
    return_list = []
    for key in KEYS_IN_JSON:
        dir_block = key.split('/')
        return_list.append(navigate_to_key(THIS_JSON,dir_block))
    return return_list

def get_request(api_dict):
    URL =  api_dict['URL']
    FORM_STRING = 'string'
    RESPONSE_TYPE = ['RESPONSE-TYPE']
    response = rq.get(URL + FORM_STRING)
    if RESPONSE_TYPE == "STRING":
        return response
    elif RESPONSE_TYPE == "JSON":
        KEYS_IN_JSON = api_dict['KEYS-IN-JSON']
        return process_json_response(response,KEYS_IN_JSON)

def post_request(api_dict):
    URL =  api_dict['URL']
    RESPONSE_TYPE = api_dict['RESPONSE-TYPE']
    HEADERS = api_dict['HEADERS']
    BODY = api_dict['BODY']
    response = rq.post(URL,data=json.dumps(BODY),headers=HEADERS)
    if RESPONSE_TYPE == "STRING":
        return response
    elif RESPONSE_TYPE == "JSON":
        KEYS_IN_JSON = api_dict['KEYS-IN-JSON']
        return process_json_response(response,KEYS_IN_JSON)
    

def process_api_response(function_name):
    api_dict = API_JSON[function_name]
    request_type = api_dict["REQUEST-TYPE"]
    #accepts two request types get and post for now
    if request_type == "GET":
        return get_request(api_dict)
    elif request_type == "POST":
        print('post request')
        return post_request(api_dict)

if __name__ == "__main__":
    print(process_api_response('GET_SENTIMENT_ANALYSIS_TYPE'))