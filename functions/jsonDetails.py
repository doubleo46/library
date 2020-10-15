"""
    Program to identify the level of each key in a json
"""
import json 
  
# Opening JSON file 
f = open('data.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list 
json_details = {}
def getDetailJson(json_details, data,key, level):
    print("key: ", key)
    for levle1_key,level1_val in data.items(): #D0
        lvl = key + levle1_key
        json_details[lvl] = "Level: " + str(level)
        if (isinstance(level1_val, list)):
            lvl = lvl + "[]"
            for level1_item in level1_val:
                if(isinstance(level1_item, dict)):
                        # level += 1
                        new_key = lvl + "->"
                        json_details = getDetailJson(json_details, level1_item,new_key, level+1)
        elif (isinstance(level1_val, dict)):
            # level += 1
            if key == "":
                new_key = levle1_key + "->" 
            else:
                new_key = key + levle1_key+ "->"
            json_details = getDetailJson(json_details, level1_val,new_key, level+1)
        else:
            pass
            # return json_details

    return json_details
