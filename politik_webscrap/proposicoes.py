# -*- coding: utf-8 -*-
"""
@author: Lwz
"""
import json
import requests
from unidecode import unidecode

def decode_names(propositions):
    for i in propositions["dados"]:
        i["ementa"] = unidecode(i["ementa"])

def json_print_file(politic_json_dict={}):
    
    with open("politicians.json",'w') as f:
        json.dump(politic_json_dict, f)

def webscrap_propositions():
    header = {'Content-Type': 'application/json' }
    
    api_url = "https://dadosabertos.camara.leg.br/api/v2/propositions?ordem=ASC&ordenarPor=id"
    n_api_url = ''
    
    response = requests.get(api_url, headers=header)
    
    propositions = { "dados" : []}
    
    while( response.status_code == 200 and ( n_api_url != api_url )):
        json_objt = json.loads(response.content.decode('utf-8'))
        
        for x in json_objt["dados"] : propositions["dados"].append(x)
        #print(json.dumps(json_objt,indent=2))
        #print(json_objt.keys())
        #print(api_url, n_api_url)
        api_url = n_api_url
        
        for i in json_objt["links"]:
            if i["rel"] == "next":
                n_api_url = i["href"]
                response = requests.get(n_api_url, headers=header)
        
                
    if(response.status_code != 200):
        print("Page Resquested Error:", response.status_code, "At url:" , api_url)
        raise
    else:
        for i in propositions["dados"]:
            i["ementa"] = unidecode(i["ementa"])
        print(json.dumps(propositions,indent=2))
        

if __name__ == "__main__":
    webscrap_propositions()