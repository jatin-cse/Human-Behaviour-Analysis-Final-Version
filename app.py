from flask import Flask, render_template, request, jsonify, send_file
import os
from collections import Counter

import joblib
import pandas as pd

from ollama import chat

# Flask Application

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024

# Upload Folder

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Store last prediction for download

app.config["LAST_PREDICTIONS"] = None

# Load Scaler

scaler = joblib.load("scaler.pkl")

# Load Machine Learning Models

models = {

    "Random Forest": joblib.load("random_forest_model.pkl"),
    "SVM": joblib.load("svm.pkl"),
    "Logistic Regression": joblib.load("logistic_regression.pkl"),
    "KNN": joblib.load("knn.pkl"),
    "Decision Tree": joblib.load("decision_tree.pkl")

}

# Model Accuracy

accuracies = {

    "Random Forest": "97.04%",
    "SVM": "94.71%",
    "Logistic Regression": "93.66%",
    "KNN": "89.64%",
    "Decision Tree": "87.53%"

}

# Label Mapping

label_map = {

    0: "Relaxed",
    1: "Neutral",
    2: "Concentrating"

}

# AI Report Generator

def generate_ai_interpretation(prediction, accuracy):

    prompt = f"""
You are an AI assistant for the project
Human Behaviour Analysis Using EEG Signal Analysis.

Predicted Behaviour:
{prediction}

Model Accuracy:
{accuracy}

Return ONLY HTML.
Format:
<h3>Interpretation</h3>
<p>
Explain the predicted mental state in
2-3 professional sentences.
</p>
<h3>Possible Observations</h3>
<p>
Describe behavioural characteristics.
</p>
<h3>Recommendations</h3>
<ul>
<li>Recommendation 1</li>
<li>Recommendation 2</li>
<li>Recommendation 3</li>
</ul>
<h3>Disclaimer</h3>
<p>
This interpretation is AI generated
for educational purposes only and is
not a medical diagnosis.
</p>
Rules:
- HTML only
- No Markdown
- No Emojis
- Maximum 150 words
"""
    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content":
                "You explain EEG behaviour professionally."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response["message"]["content"]

# Home Page

@app.route("/")
def home():

    return render_template("index.html")

# Prediction Route (AJAX)

@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:

        return jsonify({

            "success": False,
            "error": "Please upload a CSV file."

        })


    file = request.files["file"]

    if file.filename == "":

        return jsonify({

            "success": False,
            "error": "No file selected."

        })

    selected_model = request.form.get("model")

    if selected_model not in models:

        return jsonify({

            "success": False,
            "error": "Invalid Machine Learning Model."

        })


    try:

        # Save Uploaded File

        filepath = os.path.join(

            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(filepath)
      
        # Read CSV

        data = pd.read_csv(filepath)
    
        # Remove Label column if present

        if "Label" in data.columns:

            data = data.drop(columns=["Label"])

        # Scale Features

        data_scaled = scaler.transform(data)

        # Load Model

        ml_model = models[selected_model]

         # Prediction

        predictions = ml_model.predict(data_scaled)
        prediction_names = [
            label_map[int(x)]
            for x in predictions
            ]

# Prediction Confidence

        confidence = None

        if hasattr(ml_model, "predict_proba"):

            probabilities = ml_model.predict_proba(data_scaled)
            avg_probability = probabilities.mean(axis=0)
            confidence = {
                "Relaxed": round(avg_probability[0] * 100, 2),
                "Neutral": round(avg_probability[1] * 100, 2),
                "Concentrating": round(avg_probability[2] * 100, 2)
                }
        else:
            confidence = {
                "Relaxed": 0,
                "Neutral": 0,
                "Concentrating": 0
            }

        app.config["LAST_PREDICTIONS"] = prediction_names

        # Prediction Summary
        

        counts = Counter(prediction_names)

        dominant = counts.most_common(1)[0][0]

        # AI Report

        ai_report = generate_ai_interpretation(

            dominant,
            accuracies[selected_model]

        )

        # Chart Data

        chart_labels = list(counts.keys())
        chart_values = list(counts.values())

        # AJAX Response

        return jsonify({"success": True, "dominant": dominant, "model": selected_model, "accuracy": accuracies[selected_model], "filename": file.filename, "report": ai_report, "chart_labels": chart_labels, "chart_values": chart_values, "confidence": confidence})


    except Exception as e:

        return jsonify({

            "success": False,
            "error": str(e)

        })

# Download Prediction Report

@app.route("/download/<file_type>")
def download(file_type):

    predictions = app.config.get("LAST_PREDICTIONS")

    if predictions is None:

        return "No prediction report available."

    report = pd.DataFrame({

        "Sample No.": range(1, len(predictions) + 1),
        "Predicted Mental State": predictions

    })


    from datetime import datetime
    filename = f"EEG_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
    report_path = os.path.join(

        app.config["UPLOAD_FOLDER"],
        "Prediction_Report.csv"

    )

    report.to_csv(

        report_path,
        index=False

    )
    from datetime import datetime
    filename = f"EEG_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
    return send_file(
        report_path,
        as_attachment=True,
        download_name=filename

    )

# Run Flask

if __name__ == "__main__":

    app.run(

        debug=True,
        host="0.0.0.0",
        port=5000

    )
