import streamlit as st
import pandas as pd
from groq import Groq
import json
import re
from dotenv import load_dotenv
import os
from io import BytesIO


# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# -----------------------------
# Helper: Extract JSON
# -----------------------------
def extract_json(text):
    text = text.replace("```json", "").replace("```", "")
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group() if match else None

# -----------------------------
# AI Function
# -----------------------------
def analyze_lead(row):
    prompt = f"""
You are an AI lead qualification system.

Return ONLY JSON:
{{
  "lead_score": number (0-100),
  "industry": string,
  "business_need": string,
  "recommended_action": string
}}

Lead:
Name: {row['Name']}
Email: {row['Email']}
Company: {row['Company Name']}
Job Title: {row['Job Title']}
Message: {row['Message']}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.choices[0].message.content
    json_text = extract_json(raw)

    try:
        return json.loads(json_text) if json_text else {}
    except:
        return {}

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🤖 AI Lead Qualification System")

uploaded_file = st.file_uploader("Upload your leads CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Uploaded Leads")
    st.dataframe(df)

    if st.button("🚀 Analyze Leads"):
        results = []

        for _, row in df.iterrows():
            with st.spinner(f"Processing {row['Name']}..."):
                ai_data = analyze_lead(row)

                results.append({
                    "Name": row["Name"],
                    "Email": row["Email"],
                    "Company": row["Company Name"],
                    "Job Title": row["Job Title"],
                    "Lead Score": ai_data.get("lead_score"),
                    "Industry": ai_data.get("industry"),
                    "Business Need": ai_data.get("business_need"),
                    "Recommended Action": ai_data.get("recommended_action")
                })

        result_df = pd.DataFrame(results)

        st.subheader("📊 AI Analysis Results")
        st.dataframe(result_df)

        # Download button
        output = BytesIO()

        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            result_df.to_excel(writer, index=False, sheet_name='Results')

            workbook = writer.book
            worksheet = writer.sheets['Results']

            # ✅ Wrap text format
            wrap_format = workbook.add_format({'text_wrap': True})

            # ✅ Set column width + apply wrap
            for i, col in enumerate(result_df.columns):
                worksheet.set_column(i, i, 30, wrap_format)

        st.download_button(
            label="⬇️ Download Excel",
            data=output.getvalue(),
            file_name="output.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )