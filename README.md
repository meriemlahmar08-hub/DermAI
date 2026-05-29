#  DermAI 🔬

Flask web app for AI-powered skin lesion classification (Malignant/Benign) using a fine-tuned VGG16 model, with patient management dashboard and MySQL storage.
## Screenshots
<img width="1823" height="854" alt="image" src="https://github.com/user-attachments/assets/b6f8bf1b-81ab-4c03-89da-ca883d5f7c5f" />
<img width="1909" height="883" alt="image" src="https://github.com/user-attachments/assets/2bca694f-7416-405d-a80c-0809c1c30026" />
<img width="1801" height="756" alt="image" src="https://github.com/user-attachments/assets/7afe2aef-5c17-4966-868b-9f32a17d7b4a" />
<img width="1889" height="866" alt="image" src="https://github.com/user-attachments/assets/b0947eb9-00f5-444b-a5b7-49baf99d6b8d" />
<img width="1908" height="869" alt="image" src="https://github.com/user-attachments/assets/19b33dc8-82e9-4d12-8b13-232d18abf30e" />
<img width="1918" height="875" alt="image" src="https://github.com/user-attachments/assets/bf11ede2-88f9-442f-b6bb-161ce26be9c2" />
<img width="1750" height="771" alt="image" src="https://github.com/user-attachments/assets/a42f0e2a-ccfd-4875-bf5a-7be886a4411c" />


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





