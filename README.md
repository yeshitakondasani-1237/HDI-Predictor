# 🌍 Human Development Index (HDI) Predictor

A Machine Learning web application that predicts a country's **Human Development Index (HDI)** score based on key socio-economic indicators — Life Expectancy, Mean Years of Schooling, and Gross National Income (GNI) per Capita.

Built with **Python, Flask, Scikit-learn**, and a custom dark space-themed UI.

---

## 📌 About HDI

The Human Development Index (HDI) is a statistical composite index of life expectancy, education, and per capita income indicators, used to rank countries into four tiers — **Low, Medium, High, and Very High** human development. It was developed to emphasize that people and their capabilities should be the primary measure of a country's development, rather than economic growth alone.

---

## 🚀 Features

- 📊 Exploratory Data Analysis & Visualization (strip plots, correlation heatmap, scatter plots)
- 🧹 Data Preprocessing (null handling, label encoding)
- 🤖 Linear Regression model trained on real UNDP HDI dataset (**96.68% R² accuracy**)
- 💾 Model serialization using Pickle
- 🌐 Flask web application with input form and prediction result page
- 🎨 Custom dark, space-themed responsive UI

---

## 🗂️ Project Structure

```
HDI Project/
├── Dataset/
│   └── HDI.csv
│
├── Flask/
│   ├── templates/
│   │   ├── home.html
│   │   ├── indexnew.html
│   │   └── resultnew.html
│   ├── app.py
│   └── HDI.pkl
│
└── Training/
    └── HumDevIndex.ipynb
```

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.x |
| ML Library | Scikit-learn |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Web Framework | Flask |
| Model Serialization | Pickle |
| Frontend | HTML, CSS |

---

## ⚙️ System Requirements

**Hardware**
- Processor: Intel Core i3 or above
- RAM: Minimum 4 GB
- Storage: Minimum 10 GB free space

**Software**
- OS: Windows / Linux / macOS
- Python 3.x
- Anaconda Navigator
- Jupyter Notebook
- Flask Framework

---

## 📥 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yeshitakondasani-1237/HDI-Predictor.git
   cd HDI-Predictor
   ```

2. **Install dependencies**
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn flask
   ```

3. **Run the Flask app**
   ```bash
   cd Flask
   python app.py
   ```

4. **Open in browser**
   ```
   http://localhost:5000
   ```

---

## 🧠 Model Details

- **Algorithm:** Linear Regression
- **Features used:** Country (label encoded), Life Expectancy, Mean Years of Schooling, GNI per Capita
- **Target variable:** HDI Score
- **Train/Test split:** 90% / 10%
- **R² Score:** 0.9668 (96.68% accuracy)

---

## 🏷️ HDI Classification Tiers

| Tier | Score Range |
|---|---|
| 🔴 Low HDI | 0.30 – 0.54 |
| 🟠 Medium HDI | 0.55 – 0.69 |
| 🔵 High HDI | 0.70 – 0.79 |
| 🟢 Very High HDI | 0.80 – 0.94 |

---

## 📸 Pages

- **Home** — Project introduction and HDI tier overview
- **Predict** — Input form for country indicators
- **Result** — Displays predicted HDI score and development tier

---

## 📄 License

This project is open-source and available for educational purposes.

---

## 🙋‍♀️ Author

**Yeshita Kondasani**
[GitHub Profile](https://github.com/yeshitakondasani-1237)
**Polisetti Himesh Sai Hari Nagh**
[Github Profile]https://github.com/himeshsaiharinaghpolisetti-lab
**Mohammadkaif Shaik**
[Github Profile]https://github.com/mohammadkaif-shaik007
**Venkata Rishik Rapuru**
[Github Profile]https://github.com/rapururishik9-dev
