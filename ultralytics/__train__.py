from ultralytics import RTDETR
from datetime import datetime
today = datetime.today().strftime("%y.%m.%d")


pt_model_path="/workspace/ultralytics/pre-trained models/rtdetr-x.pt"
dataset_path="/workspace/datasets/ITONE_8Classes-constructionEquipments_dataset_refactoring/YOLO/data.yaml"

def trainRTDETR(pt_model_path, dataset_path):
    model = RTDETR(pt_model_path)
    model.info()
    results = model.train(
        model=pt_model_path,
        data=dataset_path, 
        epochs=100,
        batch=16,
        imgsz=640,
        save=True,
        save_period=10,
        device=[0,1],   
        workers=8,
        project="Custom_RT-DETR",
        name=f"{today}_trained_model",
        optimizer="auto",
        val=True,
        plots=True,
        amp=True
    )
    return None

if __name__ == "__main__":
    trainRTDETR(pt_model_path, dataset_path)