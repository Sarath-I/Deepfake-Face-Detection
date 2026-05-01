from flask import Flask, render_template, request
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model

app = Flask(__name__)

base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(128,128,3)
)

x = base_model.output
x = GlobalAveragePooling2D()(x)

x = Dense(128, activation='relu')(x)
x = Dropout(0.5)(x)

predictions = Dense(1, activation='sigmoid')(x)

model = Model(inputs=base_model.input, outputs=predictions)

model.load_weights("deepfake.weights.h5")

UPLOAD_FOLDER = "static"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def index():
    label = None
    confidence = None
    img_path = None

    if request.method == "POST":
        file = request.files["file"]

        if file:
            img_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(img_path)

            img = load_img(img_path, target_size=(128,128))
            img = img_to_array(img) / 255.0
            img = np.expand_dims(img, axis=0)

            prediction = model.predict(img)[0][0]

            if prediction > 0.5:
                label = "REAL"
            else:
                label = "FAKE"

            confidence = float(prediction)

    return render_template(
        "index.html",
        label=label,
        confidence=confidence,
        img_path=img_path
    )

if __name__ == "__main__":
    app.run(debug=True)