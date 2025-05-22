import streamlit as st
import random
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import io
import numpy as np
import time

# Initialize session state
if "users" not in st.session_state:
    st.session_state.users = {}

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
    * { font-family: 'Roboto', sans-serif; }
    .main { background-color: #ffffff; padding: 2rem; }
    .stButton>button { 
        background-color: #007bff; 
        color: white; 
        border-radius: 4px; 
        padding: 0.5rem 1rem; 
        font-weight: 500; 
        border: none;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .stButton>button:hover { 
        background-color: #0056b3; 
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transform: translateY(-2px);
    }
    .stTextInput>div>div>input { 
        border-radius: 4px; 
        border: 1px solid #ced4da;
        padding: 0.5rem;
        transition: all 0.3s ease;
    }
    .stTextInput>div>div>input:focus {
        border-color: #007bff;
        box-shadow: 0 0 0 0.2rem rgba(0,123,255,.25);
    }
    .stSelectbox>div>div>div { 
        border-radius: 4px; 
        border: 1px solid #ced4da;
        transition: all 0.3s ease;
    }
    .learning-hub-container {
        animation: fadeIn 1s ease-in;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 20px;
        border-radius: 10px;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_w98qte06.json")
lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_3rwasyjy.json")

st.title("Interactive Learning Hub: Code & Create 🚀")

st.subheader("📁 File Upload Center")
uploaded_file = st.file_uploader("Upload your project files", type=['py', 'txt', 'pdf', 'jpg', 'png'])
if uploaded_file is not None:
    try:
        if uploaded_file.type.startswith('image'):
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
        else:
            content = uploaded_file.read()
            try:
                st.write("File Contents:")
                st.code(content.decode('utf-8'))
            except UnicodeDecodeError:
                st.write("File Contents:")
                st.code(content.decode('latin-1'))
    except Exception as e:
        st.error(f"An error occurred while processing the file: {str(e)}")

# Inspirational Quotes
quotes = [
    "The only way to learn a new programming language is by writing programs in it. - Dennis Ritchie",
    "Code is like humor. When you have to explain it, it's bad. - Cory House",
    "Programming isn't about what you know; it's about what you can figure out. - Chris Pine",
    "The best error message is the one that never shows up. - Thomas Fuchs",
    "First, solve the problem. Then, write the code. - John Johnson",
    "Experience is the name everyone gives to their mistakes. - Oscar Wilde",
    "Programming is the art of telling another human what one wants the computer to do. - Donald Knuth",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Every great developer you know got there by solving problems they were unqualified to solve until they actually did it. - Patrick McKenzie",
    "The function of good software is to make the complex appear to be simple. - Grady Booch"
]

# Display random quote
st.info(random.choice(quotes))

# Main banner with dynamic content
# st.image("https://www.analyticsinsight.net/wp-content/uploads/2020/11/Artificial-Intelligence-5.jpg",         use_column_width=True)

col1, col2 = st.columns([1, 2])
with col1:
    st.sidebar.image("https://img.icons8.com/color/96/000000/programming.png")
    st.sidebar.header("Learning Center")
    name = st.sidebar.text_input("Your Name")
    goal = st.sidebar.text_input("Learning Goal")
    learning_path = st.sidebar.selectbox(
        "🛣️ Choose Your Path",
        ["Web Development", "Data Science", "Mobile App Development", "Cloud Computing", "Cybersecurity", "Game Development", "AI/ML", "DevOps", "Blockchain"]
    )
    experience_level = st.sidebar.select_slider(
        "⭐ Experience Level",
        options=["Beginner", "Intermediate", "Advanced", "Expert"]
    )
    preferred_language = st.sidebar.multiselect(
        "💻 Preferred Programming Languages",
        ["Python", "JavaScript", "Java", "C++", "Ruby", "Go", "Swift", "Kotlin"]
    )
    study_time = st.sidebar.slider("Daily Study Hours", 0, 12, 2)
    st_lottie(lottie_coding, height=200)

if name:
    if name not in st.session_state.users:
        st.session_state.users[name] = {
            "Skill Level": 1,
            "Projects Completed": 0,
            "XP Points": 0,
            "Achievements": ["Coding Explorer"],
            "Learning Streak": 1,
            "Badges": ["Newcomer"],
            "Daily Progress": [random.randint(1, 100) for _ in range(30)],
            "Study Hours": study_time,
            "Languages": preferred_language
        }
        st_lottie(lottie_hello, height=200)

    st.markdown(f"""
        <div class='learning-hub-container'>
            <h2>Welcome to Your Learning Journey, {name} 🌟</h2>
            <p>Current Path: {learning_path} | Level: {experience_level}</p>
            <p>Goal: {goal}</p>
            <p>Daily Study Commitment: {study_time} hours</p>
            <p>Languages: {', '.join(preferred_language)}</p>
        </div>
    """, unsafe_allow_html=True)

    # Additional Graphs and Visualizations
    st.subheader("📈 Learning Analytics Dashboard")
    
    # Daily Progress Line Chart
    fig_daily = px.line(
        x=list(range(1, 31)),
        y=st.session_state.users[name]["Daily Progress"],
        title="Daily Learning Progress",
        labels={"x": "Day", "y": "Progress Score"}
    )
    st.plotly_chart(fig_daily)

    # Learning Distribution Pie Chart
    learning_distribution = {
        "Coding Practice": 40,
        "Video Tutorials": 20,
        "Reading Docs": 15,
        "Projects": 25
    }
    fig_pie = px.pie(
        values=list(learning_distribution.values()),
        names=list(learning_distribution.keys()),
        title="Learning Activity Distribution"
    )
    st.plotly_chart(fig_pie)

    # Heat Map of Weekly Activity
    weekly_activity = np.random.randint(0, 10, size=(7, 24))
    fig_heat = px.imshow(
        weekly_activity,
        labels=dict(x="Hour of Day", y="Day of Week"),
        title="Weekly Learning Activity Heatmap"
    )
    st.plotly_chart(fig_heat)

    # Pomodoro Timer
    st.subheader("⏱️ Pomodoro Timer")
    pomodoro_duration = st.slider("Work Duration (minutes)", 1, 60, 25)
    if st.button("Start Pomodoro"):
        with st.empty():
            for secs in range(pomodoro_duration * 60, -1, -1):
                mm, ss = secs//60, secs%60
                st.metric("Time Remaining", f"{mm:02d}:{ss:02d}")
                time.sleep(1)
            st.success("Time's up! Take a break!")

    # Daily Motivation Quote
    if st.button("Get Daily Motivation"):
        st.success(random.choice(quotes))

    # Interactive Learning Features
    st.subheader("🎯 Today's Learning Challenges")
    challenges = [
        "Build a responsive website",
        "Create an API",
        "Develop a mobile app feature",
        "Implement authentication system",
        "Design a database schema",
        "Create a game level",
        "Build a machine learning model",
        "Implement a blockchain smart contract",
        "Create a CI/CD pipeline",
        "Design a microservice architecture"
    ]
    if st.button("Get New Challenge 🎲"):
        challenge = random.choice(challenges)
        st.info(f"Challenge Unlocked: {challenge}")
        st.session_state.users[name]["XP Points"] += 10

    # Real-time Code Editor with Syntax Highlighting
    st.subheader("💻 Code Playground")
    language = st.selectbox("Select Language", ["python", "javascript", "java", "cpp"])
    code = st.text_area("Write your code here:", height=200)
    if st.button("Run Code ▶️"):
        st.code(code, language=language)
        st.success("Code executed successfully!")

    # Progress Tracking
    st.subheader("📊 Learning Analytics")
    metrics = {
        "Skill Level": st.session_state.users[name]["Skill Level"],
        "Projects": st.session_state.users[name]["Projects Completed"],
        "XP": st.session_state.users[name]["XP Points"],
        "Streak": st.session_state.users[name]["Learning Streak"]
    }
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Skill Level", metrics["Skill Level"])
    with col2:
        st.metric("Projects", metrics["Projects"])
    with col3:
        st.metric("XP Points", metrics["XP"])
    with col4:
        st.metric("Day Streak", metrics["Streak"])

    # Interactive Learning Resources
    st.subheader("📚 Learning Resources")
    resource_tabs = st.tabs(["Tutorials", "Documentation", "Projects", "Community", "Practice"])
    
    with resource_tabs[0]:
        st.write("Interactive video tutorials and guides")
        if st.button("Access Tutorials"):
            st.video("https://youtu.be/example")
    
    with resource_tabs[1]:
        st.write("Comprehensive documentation and references")
        st.markdown("[View Documentation](https://docs.example.com)")
    
    with resource_tabs[2]:
        st.write("Hands-on project ideas and templates")
        project_ideas = ["E-commerce Site", "Weather App", "Task Manager", "Chat Application", "AI Image Generator", "Blockchain Wallet", "IoT Dashboard"]
        selected_project = st.selectbox("Select a project to start:", project_ideas)
        if st.button("Start Project"):
            st.success(f"Project '{selected_project}' initialized!")
    
    with resource_tabs[3]:
        st.write("Connect with fellow learners")
        st.text_input("Post a question to the community")
        if st.button("Post"):
            st.info("Question posted to community forum!")

    with resource_tabs[4]:
        st.write("Practice coding problems")
        difficulty = st.select_slider("Select difficulty", ["Easy", "Medium", "Hard"])
        if st.button("Generate Problem"):
            st.code("# Your coding problem appears here")

    # Achievement System
    st.subheader("🏆 Achievements & Badges")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Achievements:")
        for achievement in st.session_state.users[name]["Achievements"]:
            st.success(achievement)
    with col2:
        st.write("Badges:")
        for badge in st.session_state.users[name]["Badges"]:
            st.info(badge)

    # Skill Tree Visualization
    st.subheader("🌳 Skill Tree")
    skills = {
        "Programming": 85,
        "Problem Solving": 75,
        "Web Technologies": 70,
        "Database Management": 65,
        "System Architecture": 80,
        "UI/UX Design": 60,
        "Cloud Computing": 70,
        "DevOps": 65,
        "AI/ML": 55,
        "Cybersecurity": 50
    }
    fig = px.radar(
        r=[value for value in skills.values()],
        theta=[key for key in skills.keys()],
        title="Your Skill Progress"
    )
    st.plotly_chart(fig)

    # Learning Path Progress
    st.subheader("🎯 Path Progress")
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)

    # Community Leaderboard
    st.subheader("🏅 Global Leaderboard")
    df = pd.DataFrame.from_dict(st.session_state.users, orient="index")
    df['Total Score'] = df['Skill Level'] * 100 + df['XP Points']
    df = df.sort_values(by=['Total Score'], ascending=False)
    st.table(df[['Skill Level', 'Projects Completed', 'XP Points', 'Total Score']])

    # Peer Learning Network
    st.subheader("👥 Find Study Partners")
    st.write("Connect with learners on the same path")
    if st.button("Find Partners"):
        st.success("Study partner suggestions will appear here")