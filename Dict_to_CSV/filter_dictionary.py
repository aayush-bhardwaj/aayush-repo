__author__ = 'Aayush Bhardwaj'

from test_sheet import dict
import json

required_keys=["row_number","test_flag","cloudprofile","deliveryprofile","securityprofile","serverprofile","slaprofile","run_tests"]
dict2=[]
for x in range(len(dict)):
    specific_dict={}
    if 'subtiers' in dict[x].keys():
        continue
    else:
        for y in range(len(required_keys)):
            if required_keys[y] in dict[x].keys():
                specific_dict[required_keys[y]]=dict[x][required_keys[y]]
        dict2.append(specific_dict)
json.dump(dict2, open("new_test_sheet.csv",'w'))
