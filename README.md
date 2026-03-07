# 🚀 Cosmic Mission Control System  
### Interplanetary Mission Intelligence & Rocket Simulation Platform  

---

## 📌 Project Overview

Cosmic Mission Control is an advanced aerospace analytics and rocket simulation web application developed using Python and Streamlit.

This project integrates:

- Mathematical modeling (Newton’s Laws of Motion)
- Statistical data analysis
- Interactive visualization
- Real-time physics simulation
- Web deployment using Streamlit Cloud

The objective is to simulate interplanetary rocket missions while analyzing mission data to derive meaningful insights regarding performance, budget efficiency, and mission success.

---

## 🎯 Problem Understanding & Research

Space missions are influenced by multiple physical and operational factors:

- Thrust produced by rocket engines  
- Gravitational force of destination planets  
- Payload weight  
- Fuel consumption  
- Budget constraints  
- Mission objectives  

The simulation is based on Newton’s Second Law:

Acceleration = (Thrust − Mass × Gravity) / Mass

Key considerations:

- As fuel burns, rocket mass decreases  
- Lower mass increases acceleration  
- Higher gravity increases mission difficulty  
- Budget does not always guarantee mission success  

This model reflects real aerospace engineering principles and real-world mission planning logic.

---

## 📊 Dataset Description

File: `mission_data.csv`

The dataset includes:

- Mission_ID
- Agency
- Rocket_Type
- Destination
- Mission_Type
- Launch_Date
- Payload_kg
- Fuel_kg
- Thrust_N
- Gravity
- Estimated_Budget_Million
- Scientific_Yield_Score
- Mission_Success

Data preprocessing included:

- Column name standardization
- Datetime conversion for Launch_Date
- Validation of numeric columns
- Removal of inconsistencies

---

## 📈 Data Visualization & Analytics

The dashboard includes:

### 1️⃣ KPI Metrics
- Total Missions
- Mission Success Rate
- Average Budget
- Average Scientific Yield

### 2️⃣ Agency Performance Analysis
- Budget comparison by agency
- Mission success comparison
- Scientific yield analysis

### 3️⃣ Budget vs Scientific Yield
- Scatter plot visualization
- Return on Investment (ROI) insights
- Payload efficiency comparison

### 4️⃣ Timeline Analysis
- Budget trends over time
- Mission growth patterns

All visualizations are interactive and built using Plotly.

---

## 🚀 Rocket Simulation Model

The simulation calculates rocket motion over time using numerical integration.

### Mathematical Model

Acceleration:
a = (T − m × g) / m  

Velocity Update:
v = v + a × dt  

Altitude Update:
h = h + v × dt  

Where:

- T = Thrust  
- m = Mass  
- g = Planet Gravity  
- dt = Time step  

### Simulation Features

- Multi-planet gravity system  
- Adjustable thrust, payload, and fuel  
- 3D trajectory visualization  
- Real-time mission success detection  
- Interactive control system  

---

## 🌌 User Interface & Experience

- Animated cosmic gradient background  
- Moving star field animation  
- Interactive filters  
- KPI display panels  
- Responsive layout  
- Clean aerospace-inspired theme  

The UI simulates a realistic mission control environment.

---

## 🌍 Streamlit Cloud Deployment

1. Push project to GitHub  
2. Login to Streamlit Cloud  
3. Click "Deploy an App"  
4. Connect GitHub repository  
5. Select app.py  
6. Deploy  

Live App Link:  
(Add your deployed URL here)

---

## 📦 Requirements

streamlit>=1.30.0  
pandas>=2.0.0  
numpy>=1.24.0  
plotly>=5.18.0  

---

## 🧠 Key Insights Derived

- Higher gravity planets show lower success rates  
- Increased budget does not always guarantee success  
- Fuel-to-payload ratio impacts mission efficiency  
- Heavy rockets perform better for deep space missions  
- Scientific ROI varies across agencies  

---

## 🎓 Learning Outcomes Achieved

This project demonstrates:

- Application of calculus-based physics modeling  
- Data preprocessing using Pandas  
- Statistical reasoning and correlation analysis  
- Interactive visualization development  
- Full web application deployment lifecycle  
- Real-world aerospace simulation  

---

## 🚀 Future Improvements

- Machine learning-based mission success prediction  
- Risk probability modeling  
- Budget optimization engine  
- Orbital mechanics extension  
- PDF mission report export  
- Multi-user authentication system  

---

## 👨‍🚀 Author

Shivam Bhuva  
Artificial Intelligence  
Mathematics for AI Project  

---

## 📜 Academic Declaration

This project was developed for academic purposes as part of the Artificial Intelligence coursework and demonstrates applied mathematical modeling, data analytics, and interactive system development.

---

## 🚀 Live App

Click here to open the application:

🔗 https://space-exploration.streamlit.app/
