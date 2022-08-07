import json
  
# Opening JSON file
f = open('./config/lst_file.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
f.close()  
# Iterating through the json
# list
for i in data['config_data_source']:
    print(i['path'])
    print(i['file_name'])
    print(i['path']+'/'+i['file_name'])
# Closing file
