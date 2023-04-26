# import torch
# model = torch.hub.load('yolov5', 'custom', path='best1.pt', source='local', device='mps')
# async def det(url):
#     model.conf = 0.9
#     model.iou = 0.2
#     results = model(url)
#     result = results.pandas().xyxy[0].value_counts('name')
#     result_json = result.to_json()
#     return result_json

import torch
import asyncio
import json
from collections import ChainMap

# Load Model_1:
Banner_model = torch.hub.load('yolov5', 'custom', path='Banner.pt', source='local', device='mps')
Banner_model.conf = 0.9
Banner_model.iou = 0.2

# Load Model_2:
BAT_model = torch.hub.load('yolov5', 'custom', path='BAT.pt', source='local', device='mps')
BAT_model.conf = 0.9
BAT_model.iou = 0.2


# Create Asynchronus Function for Detection:
async def det(url):

    # Execute Banner Model
    Banner_loop = asyncio.get_running_loop()
    Banner_result = await Banner_loop.run_in_executor(None, Banner_model, url)
    Banner_result = Banner_result.pandas().xyxy[0].value_counts('name')
    Banner_out = Banner_result.to_json()
    Banner_result_dict = json.loads(Banner_out)
    # print(Banner_result_dict)

    
    # Execute BAT Model
    BAT_loop = asyncio.get_running_loop()
    BAT_result = await BAT_loop.run_in_executor(None, BAT_model, url)
    BAT_result = BAT_result.pandas().xyxy[0].value_counts('name')
    BAT_out = BAT_result.to_json()
    BAT_result_dict = json.loads(BAT_out)
    # print(BAT_result_dict)


    # Adding Two Model Result
    Combined_result_Dict = { 'Banner': Banner_result_dict,'BAT': BAT_result_dict}
    Final_result_json = json.dumps(Combined_result_Dict)
    print(Final_result_json)

    return Final_result_json








