from ultralytics import YOLO
# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
model.train(data='F:\\computer_vision\\yolo\\config.yaml', epochs=29,   
    optimizer='Adam',
    val=True,
    batch=64,
    imgsz=640)  # train the model
metrics = model.val()  # evaluate model performance on the validation set

# predict on an image
results = model("C://Users//Artyom//Downloads//HGIC_spiders_wolfspider_16x9.jpg")
