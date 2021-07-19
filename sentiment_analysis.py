#python modules
import requests as r
import json 
import nltk as nl
#nl.download('punkt')
#nl.download('averaged_perceptron_tagger')
#with reference from https://sentim-api.herokuapp.com/
def post_request_response_SA(txt):
    URL = 'https://sentim-api.herokuapp.com/api/v1/'
    data={'text':txt}
    headers={'Accept': "application/json", "Content-Type": "application/json"}
    return r.post(URL,data=json.dumps(data),headers=headers).text

#TAG: 'NN' - noun, 'VB' - verb
def extract_specific_tag(txt, tag):
    lines = txt
    # function to test if something is a noun
    is_noun = lambda pos: pos[:2] == tag
    # do the nlp stuff
    tokenized = nl.word_tokenize(lines)
    nouns = [word for (word, pos) in nl.pos_tag(tokenized) if is_noun(pos)] 
    return nouns

#remove repeats in an array 
def removed_repeat_list(contents):
    return_list = []
    for content in contents:
        if content not in return_list:
            return_list.append(content)
    return return_list

#packages data into json
def SA_package_contents_json(txt):
    total_sentiment = json.loads(post_request_response_SA(txt))['result']
    return {'text':txt,'NN':extract_specific_tag(txt, 'NN'),'VB':extract_specific_tag(txt,'VB'),'polarity':total_sentiment['polarity'],'type':total_sentiment['type']}

if __name__ == "__main__":
    print(SA_package_contents_json('''Shafaq News / A reliable local source reported that an ISIS attack on a factory in Heet district, west of al-Anbar Governorate, caused several causalities.

The source told Shafaq News Agency, "Some ISIS terrorists launched an attack on the Haji Lutfi sand factory, east of Heet district, which resulted in the death of two workers in the factory, and the injury of three others."

The source added that the wounded are in critical condition, noting that the local police forces and emergency regiments are now carrying out a searching campaign in the area to arrest the perpetrators.'''))

