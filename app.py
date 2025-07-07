import streamlit as st
import pandas as pd
import pickle

# Load data
df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommendation(title):
    idx = df[df['Title'] == title].index[0]
    idx = df.index.get_loc(idx)
    df['OriginalTitle'] = df['Title']  # Save a copy
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])[1:20]

    jobs = []
    for i in distances:
        jobs.append(df.iloc[i[0]]['OriginalTitle'])

    return jobs

# --------- ✨ STYLING SECTION START ---------
st.set_page_config(page_title="Career Match", page_icon="💼")

st.markdown("""
    <style>
        .main-title {
            font-size: 48px;
            font-weight: 800;
            color: #0d47a1;
            text-align: center;
            padding: 10px 0;
            background: linear-gradient(to right, #2196f3, #21cbf3);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: fadeIn 2s ease-in-out;
        }
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(-20px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        .main-container {
            max-width: 1000px;
            margin: auto;
            padding: 20px;
        }
        .sub-title {
            font-size: 24px;
            color: #1565c0;
            font-weight: bold;
            margin-top: 30px;
            margin-bottom: 10px;
            border-bottom: 2px dashed #90caf9;
            padding-bottom: 5px;
        }
        .divider {
            border-top: 4px solid #0d47a1;
            margin: 10px auto 30px auto;
            width: 20%;
            border-radius: 50px;
        }
        .search-box {
            font-size: 20px;
            font-weight: bold;
            color: #0077b6;
            padding: 10px 0;
        }
        .job-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        margin-top: 20px;
        }
        .job-box {
            background-color: #f0f8ff;
            color: #212121;
            border-left: 6px solid #0077b6;
            padding: 12px 20px;
            margin-bottom: 8px;
            border-radius: 8px;
            font-size: 17px;
            font-family: 'Courier New', monospace;
            transition: 0.3s ease;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        }
        .job-box:hover {
            transform: translateY(-3px);
            background: #e3f2fd;
            border-left: 6px solid #0d47a1;
        }
        .stApp {
            background: linear-gradient(to right, #e6f7ff, #ffffff);
            font-family: 'Segoe UI', sans-serif;
        }
        .apply-btn {
        display: inline-block;
        margin-top: 8px;
        font-size: 14px;
        color: white;
        background-color: #2196f3;
        padding: 6px 12px;
        border-radius: 5px;
        text-decoration: none;
        }
        .apply-btn:hover {
            background-color: #1976d2;
        }
    </style>
""", unsafe_allow_html=True)

# Re-add heading separately
st.markdown('<p class="main-title">🎯 CARRER MATCH - Job Recommendation System</p>', unsafe_allow_html=True)

# Job Search
st.markdown('<p class="search-box">🔍 SEARCH JOB</p>', unsafe_allow_html=True)
title = st.selectbox("", df['Title'])

# Recommendation output
jobs = recommendation(title)

if jobs:
    st.markdown("<h3 style='color:#1e88e5;'>✨ Recommended Jobs for You:</h3>", unsafe_allow_html=True)

    job_html = """
    <style>
        .job-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-top: 20px;
        }
        .job-box {
            background-color: #f0f8ff;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-weight: 500;
            color: #0d47a1;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, background-color 0.3s ease;
        }
        .job-box:hover {
            background-color: #e3f2fd;
            transform: scale(1.03);
        }
    </style>

    <div class="job-grid">
    """

    # Display up to 20 jobs in rows of 4
    job_html = "<div class='job-grid'>"
    for i in range(min(20, len(jobs))):
        job_html += f"<div class='job-box'>{jobs[i]}</div>"

    job_html += "</div>"

    st.markdown(job_html, unsafe_allow_html=True)