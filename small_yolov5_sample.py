import torch

# Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model = torch.hub.load('yolov5', 'custom', path='yolov5/best1.pt', source='local')

# Images
imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images

# Inference
results = model(imgs)

# Results
# results.print()

# results.xyxy[0]  # im1 predictions (tensor)
a = results.pandas().xyxy[0]
print(a)