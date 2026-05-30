from flask import Flask, render_template, request, redirect, session, flash
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret"

UPLOAD_FOLDER = "static/uploads/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = load_model("model/vgg16_malignant_benign.h5", compile=False)

# MYSQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="skin_cancer_db"
)
cursor = db.cursor(dictionary=True)

# LOGIN
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user, pwd))
        result = cursor.fetchone()
        if result:
            session["user"] = user
            flash("Login réussi ✓", "success")
            return redirect("/dashboard")
        else:
            flash("Erreur login ✗", "danger")
    return render_template("login.html")

# DASHBOARD 
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    # Total
    cursor.execute("SELECT COUNT(*) as total FROM patients")
    total = cursor.fetchone()['total']

    # Malignant
    cursor.execute("SELECT COUNT(*) as c FROM patients WHERE result='Malignant'")
    malignant = cursor.fetchone()['c']

    # Benign
    benign = total - malignant

    # Pourcentages
    mal_pct = round((malignant / total * 100), 1) if total > 0 else 0
    ben_pct = round((benign / total * 100), 1) if total > 0 else 0

    # Aujourd'hui
    cursor.execute("SELECT COUNT(*) as c FROM patients WHERE DATE(created_at) = CURDATE()")
    today = cursor.fetchone()['c']

    # 7 derniers jours
    weekly = []
    for i in range(6, -1, -1):
        cursor.execute("""
            SELECT COUNT(*) as c FROM patients
            WHERE DATE(created_at) = DATE_SUB(CURDATE(), INTERVAL %s DAY)
        """, (i,))
        weekly.append(cursor.fetchone()['c'])

    # 5 derniers patients
    cursor.execute("SELECT * FROM patients ORDER BY created_at DESC LIMIT 5")
    recent = cursor.fetchall()

    stats = {
        'total': total,
        'malignant': malignant,
        'benign': benign,
        'malignant_pct': mal_pct,
        'benign_pct': ben_pct,
        'today': today,
        'weekly': weekly,
        'recent': recent
    }

    return render_template("dashboard.html", stats=stats)

# PREDICT
@app.route("/predict", methods=["GET", "POST"])
def predict():
    if "user" not in session:
        return redirect("/")
    if request.method == "POST":
        try:
            name = request.form["name"]
            age = request.form["age"]
            file = request.files["image"]
            if file.filename == "":
                flash("Veuillez choisir une image", "warning")
                return redirect("/predict")
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)
            img = load_img(path, target_size=(224, 224))
            img = img_to_array(img) / 255.0
            img = np.expand_dims(img, axis=0)
            pred = model.predict(img)[0][0]
            result = "Malignant" if pred > 0.5 else "Benign"
            cursor.execute("""
                INSERT INTO patients (name, age, result, probability, image_path)
                VALUES (%s, %s, %s, %s, %s)
            """, (name, age, result, float(pred), path))
            db.commit()
            flash("Analyse réussie ✓", "success")
            return render_template("result.html",
                                   result=result,
                                   prob=round(pred * 100, 2),
                                   img=path)
        except Exception as e:
            print("ERROR DETAILS:", e)
            flash("Erreur lors de l'analyse ✗", "danger")
            return redirect("/predict")
    return render_template("predict.html")

# PATIENTS
@app.route("/patients", methods=["GET"])
def patients():
    cursor.execute("SELECT * FROM patients ORDER BY created_at DESC")
    data = cursor.fetchall()
    return render_template("patients.html", patients=data)

# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    flash("Déconnecté", "info")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)