from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import uvicorn
from PIL import Image
import numpy as np
import tensorflow as tf
import io

app = FastAPI()

# 1. Load the model only once
model = tf.keras.models.load_model("model/plant_model.keras")

CLASS_NAMES = ["healthy", "rusty", "powdery"]  # change based on your dataset

# 2. Preprocessing function
def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((256, 256))   # change to your model's input size
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# 3. API endpoint to receive image and predict
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    input_tensor = preprocess_image(image_bytes)

    prediction = model.predict(input_tensor)
    class_id = np.argmax(prediction[0])
    confidence = float(np.max(prediction[0]))

    result = {
        "predicted_class": CLASS_NAMES[class_id],
        "confidence": round(confidence, 4)
    }

    return JSONResponse(result)

# 4. Run server
# uvicorn main:app --reload

