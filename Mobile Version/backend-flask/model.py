from keras.models import load_model 
from PIL import Image, ImageOps 
import numpy as np

np.set_printoptions(suppress=True)

SKDModel = load_model(r"./skinDisease_model.h5", compile=False)

SKDClassNames = open(r"./skinDisease_labels.txt", "r").readlines()

HDModel = load_model(r"./hairDisorder_model.h5", compile=False)

HDClassNames = open(r"./hairDisorder_labels.txt", "r").readlines()

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def findSkinDisease(IMG_LOC):

    image = Image.open(IMG_LOC).convert("RGB")

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    prediction = SKDModel.predict(data)
    index = np.argmax(prediction)
    class_name = SKDClassNames[index]
    confidence_score = prediction[0][index]

    return class_name[2:], confidence_score

def findHairDisorder (IMG_LOC):

    image = Image.open(IMG_LOC).convert("RGB")

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    prediction = HDModel.predict(data)
    index = np.argmax(prediction)
    class_name = HDClassNames[index]
    confidence_score = prediction[0][index]


    return class_name[2:], confidence_score
