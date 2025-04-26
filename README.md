# 🩺 Pneumonia Classification from Chest X-Ray Images

A deep learning project that classifies pediatric chest X-ray images as **Pneumonia** or **Normal** using a combination of **VGG16 (Transfer Learning)** and a **Custom CNN** model. The final model is deployed via a **Flask Web App** that allows users to upload X-ray images and receive predictions with confidence scores.

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Model Architecture](#model-architecture)
- [Evaluation Metrics](#evaluation-metrics)
- [Web App Features](#web-app-features)
- [How to Run](#how-to-run)
- [Future Enhancements](#future-enhancements)
- [Screenshots](#screenshots)
- [License](#license)

---

## 📖 Project Overview

- 🔍 Objective: Classify chest X-ray images as **Normal** or **Pneumonia-positive**.
- 🧠 Models Used: 
  - VGG16 (Pretrained on ImageNet)
  - Custom CNN (Built from scratch)
  - Ensemble Model (Average predictions of both)
- 🎯 Outcome: Achieved high accuracy and recall using ensemble learning and deployed an interactive web interface.

---

## 📁 Dataset

- **Name:** Chest X-Ray Images (Pneumonia)
- **Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
- **Images:** 5,863 JPEG files
- **Classes:** `NORMAL`, `PNEUMONIA`
- **Split:**
  - Training: 5,216 images
  - Validation: ~600 images
  - Test: 624 images

---

## 🧱 Project Structure

📦 chest_xray_classification/
├── chest_xray/                     # Dataset (train/val/test folders)
├── templates/
│   └── index.html                  # Flask frontend
├── static/uploads/                # Uploaded X-ray images
├── app.py                         # Flask app
├── vgg16_model.keras              # Saved VGG16 model
├── custom_cnn_model.keras         # Saved custom CNN model
├── requirements.txt               # Required Python packages
└── README.md                      # You’re reading it :)




---

## 🧱 Project Structure

```plaintext
📦 chest_xray_classification/
├── chest_xray/                   # Dataset (train/val/test folders)
├── templates/
│   └── index.html                 # Flask frontend
├── static/uploads/                # Uploaded X-ray images
├── app.py                         # Flask app
├── vgg16_model.keras              # Saved VGG16 model
├── custom_cnn_model.keras         # Saved Custom CNN model
├── requirements.txt               # Required Python packages
└── README.md                      # You’re reading it :)
```
---

## 📊 Evaluation Metrics

| Model        | Accuracy | Precision | Recall | F1 Score | ROC AUC |
|--------------|----------|-----------|--------|----------|---------|
| VGG16        | 92.8%    | 93.7%     | 91.2%  | 92.4%    | 97.3%   |
| Custom CNN   | 90.5%    | 91.4%     | 89.2%  | 90.3%    | 96.1%   |
| **Ensemble** | **94.7%**| **95.0%** | **93.8%**| **94.4%**| **98.3%** ✅

---

## 🌐 Web App Features

- 📁 Upload X-ray images (JPEG/PNG)
- 🧠 Model classifies as **Pneumonia** or **Normal**
- 📊 Displays confidence score
- 📄 Auto-generates PDF report (Future)
- 🧪 Grad-CAM heatmaps (Future)

---

## ▶️ How to Run

### 🔧 Step 1: Install Requirements
```bash
pip install -r requirements.txt

🖼 Step 2: Organize Dataset

Place the chest_xray dataset (from Kaggle) in your project root.

🚀 Step 3: Run Flask App
python app.py
Visit http://127.0.0.1:5000 in your browser.
```
### 🚀 Future Enhancements
	•	Grad-CAM heatmap integration for explainable AI
	•	Multi-class classification: Viral vs Bacterial Pneumonia
	•	Generative AI integration for auto medical reporting
	•	Model optimization for mobile/web deployment
