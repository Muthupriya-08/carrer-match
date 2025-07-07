💼 Career Match – Job Recommendation System

A simple, elegant, and responsive web application that recommends job roles based on user selection. Built using Streamlit, Python, and TF-IDF-based Cosine Similarity.


📌 Features
🎯 Personalized job role recommendations

🎨 Stylish and responsive UI with animations and hover effects

🔍 Intuitive dropdown-based job search

✨ Grid layout (4x5) with interactive job cards

🧠 How It Works
TF-IDF Vectorization is used to transform job titles.

Cosine Similarity finds the most similar job roles to the selected one.

The top 20 job matches are shown in a beautiful grid.

🛠️ Tech Stack
Technology	Usage
Python	Backend logic
Streamlit	Frontend + deployment
Pandas	Data manipulation
Sklearn	TF-IDF & similarity logic
HTML/CSS	Styling inside Streamlit
Pickle	To load pre-processed data

🚀 Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/career-match-app.git
cd career-match-app
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the app
bash
Copy
Edit
streamlit run app.py
📁 Project Structure
python
Copy
Edit
career-match-app/

│


├── app.py                   # Main Streamlit app


├── df.pkl                   # Job dataset


├── similarity.pkl           # Cosine similarity matrix


├── requirements.txt         # Python dependencies


└── README.md                # You are here 😊


🌐 Live Demo
If deployed (e.g. on Streamlit Cloud), add the link here:

🔗 Try it Live

✅ Future Improvements
Add search by keywords / skills

Integrate real-time job APIs (e.g., LinkedIn, Naukri)

Add job descriptions and company logos

Save favorite jobs to a local list or database

🙋‍♀️ Author
Made with 💙 by Priya

