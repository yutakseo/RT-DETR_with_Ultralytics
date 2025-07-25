from ultralytics import RTDETR
import os, sys
from datetime import datetime
today = datetime.today().strftime("%y.%m.%d")

model = RTDETR("/workspace/RT-DETR for construction equipment detection/25.07.22/weights/best.pt",)
model.info()

def image_inference(model, image_path):
    results = model(
        source=image_path,
        project="Custom_RT-DETR",
        name=f"/inference_results/{today}_result",
        show=False,
        save=True
        )
    return None

def video_inference(model, video_path):
    results = model(
        source=video_path,
        project="Custom_RT-DETR",
        name=f"/inference_results/{today}_result",
        stream=False,
        save=True
        )
    return None


#이미지 추론
"""
image_path = "/workspace/datasets"
image_files = [os.path.join(image_path, fname) 
               for fname in os.listdir(image_path) 
               if fname.lower().endswith((".jpg", ".jpeg", ".png"))]

for images in image_files:
    image_inference(model, images)
"""


#영상 추론
video_path = "/workspace/datasets"
image_files = [os.path.join(video_path, fname) 
               for fname in os.listdir(video_path) 
               if fname.lower().endswith((".mp4", ".avi", ".mov"))]

for videos in image_files:
    image_inference(model, videos)