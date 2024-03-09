from flask import Flask, request, jsonify
import threading
import datetime

from model import findSkinDisease, findHairDisorder
from findDoc import findDoctors
from dietRec import getRecommendations
from descriptionGenerator import generateDescription

def random_filename():
    basename = "image"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([basename, suffix])

    return filename

app = Flask(__name__)


@app.route("/skin-disease", methods=["POST"])
def skinDisease():
    bytesOfImage = request.files["image"].read()
    fileName = random_filename()
    with open(f"./images/{fileName}.jpeg", "wb") as out:
        out.write(bytesOfImage)

    city = request.form.get("city")

    # Deep Learning Model Prediction
    diseaseName, accuracy = findSkinDisease(f"./images/{fileName}.jpeg")

    diseaseName = diseaseName.strip()

    # MultiThreading
    results = {}

    def run_in_thread(func, key, *args, **kwargs):
        result = func(*args, **kwargs)
        results[key] = result

    threads = [
        threading.Thread(target=run_in_thread, args=(findDoctors, "doctors", city)),
        threading.Thread(target=run_in_thread, args=(generateDescription, "description", diseaseName)),
        threading.Thread(target=run_in_thread, args=(getRecommendations, "recommendations", diseaseName)),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    recommendedDocs = results.get("doctors")
    description = results.get("description")
    tips, foods_to_take, foods_not_to_take, warning = results.get("recommendations")


    print({
      "DiseaseName": ""+diseaseName.title(),
        "Description": description[0],
        "Tips": tips,
        "FoodsToTake": foods_to_take,
        "FoodsNotToTake": foods_not_to_take,
        "Doctors": recommendedDocs,
        "Warning": warning,
    })

    return jsonify({
      "DiseaseName": ""+diseaseName.title(),
        "Description": description[0],
        "Tips": tips,
        "FoodsToTake": foods_to_take,
        "FoodsNotToTake": foods_not_to_take,
        "Doctors": recommendedDocs,
        "Warning": warning,
    })

   

@app.route("/hair-disorder", methods=["POST"])
def hairDisorder():
    bytesOfImage = request.files["image"].read()
    fileName = random_filename()
    with open(f"./images/{fileName}.jpeg", "wb") as out:
        out.write(bytesOfImage)

    city = request.form.get("city")

    # Deep Learning Model Prediction
    diseaseName, accuracy = findHairDisorder(f"./images/{fileName}.jpeg")
    diseaseName = diseaseName.strip()

    # MultiThreading
    results = {}

    def run_in_thread(func, key, *args, **kwargs):
        result = func(*args, **kwargs)
        results[key] = result

    threads = [
        threading.Thread(target=run_in_thread, args=(findDoctors, "doctors", city)),
        threading.Thread(target=run_in_thread, args=(generateDescription, "description", diseaseName)),
        threading.Thread(target=run_in_thread, args=(getRecommendations, "recommendations", diseaseName)),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    recommendedDocs = results.get("doctors")
    description = results.get("description")
    tips, foods_to_take, foods_not_to_take, warning = results.get("recommendations")

    print({
      "DiseaseName": ""+diseaseName.title(),
        "Description": description[0],
        "Tips": tips,
        "FoodsToTake": foods_to_take,
        "FoodsNotToTake": foods_not_to_take,
        "Doctors": recommendedDocs,
        "Warning": warning,
    })

    return jsonify({
      "DiseaseName": ""+diseaseName.title(),
        "Description": description[0],
        "Tips": tips,
        "FoodsToTake": foods_to_take,
        "FoodsNotToTake": foods_not_to_take,
        "Doctors": recommendedDocs,
        "Warning": warning,
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
