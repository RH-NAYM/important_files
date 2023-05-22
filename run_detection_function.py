# Import Library
import torch
import asyncio
import json
from collections import ChainMap
import math
import pandas as pd 
from collections import OrderedDict

# Load and Adjust Model : 1
Brand_model = torch.hub.load('yolov5', 'custom', path='weights/Model/New94.pt', source='local', device=0)
Brand_model.conf = 0.4
Brand_model.iou = 0.3

# Load and Adjust Model : 2
Count_model = torch.hub.load('yolov5', 'custom', path='weights/Count_Model/countModel86.pt', source='local', device=0)
Count_model.conf = 0.4
Count_model.iou = 0.3

def merge_and_average_dicts(dict1, dict2):
    merged_dict = OrderedDict(dict1)
    common_keys = set(dict1.keys()).intersection(set(dict2.keys()))
    
    for key in dict1.keys():
        if key not in common_keys:
            merged_dict[key] = dict1[key]
    
    for key in dict2.keys():
        if key not in common_keys:
            merged_dict[key] = dict2[key]
    
    for key in common_keys:
        average = math.ceil((dict1[key] + dict2[key]) / 2)
        merged_dict[key] = average
    
    return merged_dict

# Created an Asynchronus Function to perform the detection
async def det(url, sequence):

    # Execute Brand Model
    Brand_loop = asyncio.get_running_loop()
    Brand_result =await Brand_loop.run_in_executor(None, Brand_model, url)
    Brand_result = Brand_result.pandas().xyxy[0].sort_values('xmin')
    Brand_df = pd.DataFrame(Brand_result)
    Brand_sorted_df = pd.DataFrame(Brand_df)
    name_counts = Brand_sorted_df.groupby('name').size().to_dict()
    Brand_result_dict = {}
    for index, row in Brand_sorted_df.iterrows():
        name = row['name']
        Brand_result_dict.update({name:name_counts.get(name, 0)})
    Brand_result_json = json.dumps(Brand_result_dict)
    a = Brand_result_json
    a_dict = json.loads(a)
    dict1 = a_dict
    print("result1: ",dict1)

    # Execute Count Model
    Count_loop = asyncio.get_running_loop()
    Count_result =await Count_loop.run_in_executor(None, Count_model, url)
    Count_result = Count_result.pandas().xyxy[0].sort_values('xmin')
    Count_df = pd.DataFrame(Count_result)
    Count_sorted_df = pd.DataFrame(Count_df)
    name_counts = Count_sorted_df.groupby('name').size().to_dict()
    Count_result_dict = {}
    for index, row in Count_sorted_df.iterrows():
        name = row['name']
        Count_result_dict.update({name:name_counts.get(name, 0)})
    Count_result_json = json.dumps(Count_result_dict)
    b = Count_result_json
    b_dict = json.loads(b)
    dict2 = b_dict
    print("result2: ",dict2)

    # Merging 2 dictionary with the function that was created earlier
    result_dict = merge_and_average_dicts(dict1, dict2)

    # Sequence Detection
    ds = []
    for i in dict1:
        ds +=i
    if ds == sequence:
        sku = ("Valid Sequence")
    else:
        sku = ("Wrong Sequence")

    # Finalise the results    
    result = {'Hair_Care_Items': result_dict, 'Sequence': sku}
    Final_Result = json.dumps(result)
    print("Result Sent to User : ", Final_Result)
    return Final_Result



