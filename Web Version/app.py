from flask import Flask, request, render_template ,jsonify, make_response 
import os
from google.api_core import exceptions
import pandas as pd
from keras.models import load_model  
from PIL import Image, ImageOps  
import numpy as np
import google.generativeai as genai

app = Flask(__name__)

UPLOAD_FOLDER = r'C:\Users\Admin\Desktop\All projects\DermOnDemand Project\Web Version\uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


image_files = [os.path.join(UPLOAD_FOLDER, filename) for filename in os.listdir(UPLOAD_FOLDER) if filename.endswith(('.jpg', '.png'))]

@app.route('/')
def index():
    return render_template('darmahtml.html')

@app.route('/upload_skin', methods=['POST'])
def upload():
    if 'imageFile' not in request.files:
        return "No file part"

    file = request.files['imageFile']

    if file.filename == '':
        return "No selected file"

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        print(file)

        final = image_processing(file)

        return render_template('result.html', result=final[0])
    

def image_processing(image_files):
    results = []  

    image = Image.open(image_files)
    np.set_printoptions(suppress=True)
    model = load_model(r"C:\Users\Admin\Desktop\All projects\DermOnDemand Project\Web Version\ML Models\skin_model.h5", compile=False)
    class_names = open(r"C:\Users\Admin\Desktop\All projects\DermOnDemand Project\Web Version\ML Models\skin_label.txt", "r").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image_process = image.convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image_process, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array
    
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    
    result = "Class: " + str(class_name[2:])
    
    results.append(result)  

    print("Confidence Score:", confidence_score)
    return results

@app.route('/upload_hair', methods=['POST'])
def hair():
    if 'imageFile' not in request.files:
        return "No file part"

    file = request.files['imageFile']

    if file.filename == '':
        return "No selected file"

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        final = hair_image_processing(file)

        return render_template('result.html', result=final[0])

def hair_image_processing(file):
    results = []
    image = Image.open(image_files)
    np.set_printoptions(suppress=True)

    model = load_model(r"C:\Users\Admin\Desktop\All projects\DermOnDemand Project\Web Version\ML Models\skin_model.h5", compile=False)

    class_names = open(r"C:\Users\Admin\Desktop\All projects\DermOnDemand Project\Web Version\ML Models\hair_disease_label.txt", "r").readlines()


    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = image.convert("RGB")

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    
    print("Confidence Score:", confidence_score)
    return class_name

@app.route('/doc_recommendation', methods=['POST'])


def doc_recommendation():
    def convert_markdown_to_json(markdown_text):
        doctors_json = {
            'doctors': []
        }
        processed_text = []
        for line in markdown_text.splitlines():
            line = line.strip() 
            if line:
                processed_text.append(line.replace(">", "").replace("*", ""))

        for i in range(0, len(processed_text), 2):
            if i < len(processed_text):
                doctors_json['doctors'].append({
                    'name': processed_text[i],
                    'address': processed_text[i+1] if i+1 < len(processed_text) else ""  # Handle odd length (no address for last name)
                })
        return doctors_json

    location = request.form['location']
    prompt = f"show me the skin doctors nearby {location} with their location address"

    genai.configure(api_key="AIzaSyAcxIh84MuqI7jH6rckbuuJzSOpLN5jHDE")
    model = genai.GenerativeModel('gemini-pro')

    try:
        response = model.generate_content(prompt)
        doctors_json = convert_markdown_to_json(response.text)
        print(doctors_json)
        return render_template('docRecommend.html', recommendations=doctors_json)
    except exceptions.ServiceUnavailable as e:
        print(f"GenerativeAI service unavailable: {e}")
        return render_template('error') 


if __name__ == '__main__':
    app.run(debug=True)