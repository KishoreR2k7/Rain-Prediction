# Rain Prediction Web App 🌧️

A Machine Learning project to predict whether it will **rain tomorrow** based on weather features.  
This project uses **Random Forest Classifier** and provides a **web interface** using **Gradio**.

---

## 🚀 Live Demo
## 👉 https://huggingface.co/spaces/KishoreR123/Rain-Prediction

---

## 📸 Screenshot
<img width="1905" height="765" alt="image" src="https://github.com/user-attachments/assets/6128aa63-cc1a-4cad-bdf6-8ba15673aa41" />


---

## 📖 Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features Used](#features-used)
- [Model](#model)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Results](#results)
- [License](#license)

---

## 📌 Project Overview
This project predicts if it will rain the next day based on weather conditions like temperature, humidity, wind speed, and pressure.  
The app provides a simple and interactive **web interface** for predictions.

---

## 📊 Dataset
The dataset contains historical weather data, including features such as:

- Temperature
- Humidity
- Wind Speed
- Precipitation
- Cloud Cover
- Pressure
- Location (One-hot encoded)
- Rain Tomorrow (Target variable)

---

## Features Used
In the current model, we use:

- Temperature  
- Humidity  
- Wind Speed  
- Pressure  

> 📝 More features can be added to improve prediction accuracy.

---

##  Model
- **Algorithm:** Random Forest Classifier  
- **Train/Test Split:** 80% train, 20% test  
- **Accuracy:** ~76%  
- **Evaluation:** Confusion Matrix, Classification Report, ROC-AUC  

---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/YourUsername/DSA-Practice.git
cd DSA-Practice/Day 5
Install dependencies:

bash
Copy code
pip install -r requirements.txt
If you don’t have requirements.txt, install manually:

bash
Copy code
pip install numpy pandas scikit-learn matplotlib seaborn gradio
▶️ Usage
Run the Gradio app:

bash
Copy code
python app.py
A web interface will launch locally or in your browser.

Enter the following inputs:

Temperature

Humidity

Wind Speed

Pressure

Click Submit to get the prediction: Rain 🌧️ or No Rain ☀️.

To share the app publicly:

python
Copy code
iface.launch(share=True)
✅ Example
Temperature	Humidity	Wind Speed	Pressure	Prediction
80	70	15	1012	Rain 🌧️
35	50	5	1020	No Rain ☀️

📈 Results
Accuracy: 0.76

ROC-AUC: 0.82

Confusion Matrix:

lua
Copy code
[[10144 1292]
 [2153 1031]]
Model performs better at predicting No Rain due to class imbalance.

