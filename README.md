# 🤖 AI Lead Qualification System

A Streamlit app that analyzes leads using AI (Groq LLM) and generates a lead score along with insights like industry, business need, and recommended action.

---

## 🚀 Features
- Upload CSV file of leads  
- AI-based lead scoring (0–100)  
- Extracts:
  - Industry  
  - Business Need  
  - Recommended Action  
- Displays results in a table  
- Download results as Excel file  

---

## 📂 Input Format

Your CSV file should contain the following columns:

Name  
Email  
Company Name  
Job Title  
Message  

---

## ⚙️ Installation

1. Clone the repository:

git clone https://github.com/Majitha-p/AI_Lead_App.git
cd AI_Lead_App

2. Install dependencies:

pip install -r requirements.txt  

---

## 🔑 Environment Setup

Create a `.env` file in the project folder:

GROQ_API_KEY=your_api_key_here  

---

## ▶️ Run the App

streamlit run main.py  

---

## 📊 How to Use

1. Upload your CSV file  
2. Click "Analyze Leads"  
3. View AI-generated results  
4. Download the output as an Excel file  

---

## 🛠 Tech Stack
- Streamlit  
- Groq LLM  
- Pandas  
- Python  
- XlsxWriter  

---

## 📌 Notes
- Make sure your API key is valid  
- Large datasets may take some time to process  
- Internet connection is required  

---

## 👨‍💻 Author
Your Name
