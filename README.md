#  DermAI 🔬

Flask web app for AI-powered skin lesion classification (Malignant/Benign) using a fine-tuned VGG16 model, with patient management dashboard and MySQL storage.
## Demo
<img width="800" height="366" alt="Enregistrementdelcran2026-05-30001251-ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/ea34d46d-7cf0-4fe8-bef5-c4a024559e09" />


## Features

- 🔐 Secure login with session-based authentication
- 📊 Dashboard with real-time statistics (total cases, malignant/benign ratio, weekly trend)
- 🖼️ Image upload and VGG16-powered prediction with confidence score
- 🗃️ Patient records management with full history
- 📅 Daily/weekly analysis tracking
  
##  How It Works

1. The user logs in and navigates to the **Predict** page
2. They enter the patient's name, age, and upload a skin lesion image
3. The image is preprocessed (resized to 224×224, normalized) and fed into the VGG16 model
4. The model outputs a probability score — above 0.5 → **Malignant**, below → **Benign**
5. The result is saved to the database and displayed with the confidence percentage
6. The dashboard updates automatically to reflect the new case

##  Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Flask (Python) |
| AI Model | VGG16 via Keras / TensorFlow |
| Database | MySQL / MariaDB |
| Image Processing | NumPy + Keras utils |
## ⚠️ Disclaimer

This tool is intended for **research and educational purposes only**. It is not a substitute for professional medical diagnosis. Always consult a qualified dermatologist for medical advice.





