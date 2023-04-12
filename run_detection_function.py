import torch


model = torch.hub.load('yolov5', 'custom', path='best1.pt', source='local', device='mps')


async def det(url):
    model.conf = 0.9
    model.iou = 0.2
    results = model(url)
    result = results.pandas().xyxy[0].value_counts('name')
    result_json = result.to_json()
    return result_json


