# -*- coding: utf-8 -*- 

def get_value(obj, key):        
    def extract(obj, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, key)
                elif k == key:
                    return v
        elif isinstance(obj, list):
            for item in obj:
                extract(item, key)
        #return v
    results = extract(obj, key)
    return results