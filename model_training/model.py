from ultralytics import YOLO
# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model

model.train(
    data='config.yaml', epochs=29,
    optimizer='Adam',
    val=True,
    batch=64,
    imgsz=640,
    weight_path='../model'
    weight_name='model'
)  # train the model

metrics = model.val()  # evaluate model performance on the validation set
