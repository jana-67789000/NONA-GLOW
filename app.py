import streamlit as st
import time

# --- 1. SETTINGS & STYLING ---
st.set_page_config(page_title="Luna Glow AI", page_icon="🌙", layout="centered")

if 'step' not in st.session_state: st.session_state.step = 1
if 'user_data' not in st.session_state: st.session_state.user_data = {}

def apply_custom_ui():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }
        .main-title { font-size: 28px; font-weight: 800; color: #111; text-align: center; margin-bottom: 5px; }
        .sub-title { font-size: 15px; color: #777; text-align: center; margin-bottom: 25px; }
        .stButton>button { 
            width: 100%; border-radius: 15px; border: 1px solid #F0F0F0; background: #F9F9F9; 
            color: #111; height: 60px; font-size: 17px; font-weight: 600; margin-bottom: 10px;
            text-align: left; padding-left: 20px; transition: 0.3s;
        }
        .stButton>button:hover { border-color: #FF1493; background: #FFF5FA; color: #FF1493; }
        .progress-bar-bg { width: 100%; height: 6px; background: #F0F0F0; border-radius: 10px; margin-bottom: 35px; }
        .progress-bar-fill { height: 100%; background: #FF1493; border-radius: 10px; transition: 0.5s; }
        .result-box { background: #FDFDFD; padding: 25px; border-radius: 20px; border: 2px solid #FF1493; text-align: center; }
        </style>
    """, unsafe_allow_html=True)

apply_custom_ui()

# Navigation logic (Back button & Progress)
if 1 < st.session_state.step < 12:
    if st.button("⬅️ Back", key="back"):
        st.session_state.step -= 1
        st.rerun()

prog = (st.session_state.step / 11) * 100
st.markdown(f'<div class="progress-bar-bg"><div class="progress-bar-fill" style="width: {prog}%"></div></div>', unsafe_allow_html=True)

# --- 2. THE STEP-BY-STEP JOURNEY (From your 30 images) ---

# Step 1: Initial Welcome
if st.session_state.step == 1:
    st.markdown('<p class="main-title">Get your personalized fasting & nutrition plan</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Luna Glow helps you reach your goal efficiently</p>', unsafe_allow_html=True)
    if st.button("Start My Journey 🚀"): st.session_state.step = 2; st.rerun()

# Step 2: Gender
elif st.session_state.step == 2:
    st.markdown('<p class="main-title">What is your gender?</p>', unsafe_allow_html=True)
    if st.button("Female 👩"): st.session_state.user_data['gender']='F'; st.session_state.step=3; st.rerun()
    if st.button("Male 👨"): st.session_state.user_data['gender']='M'; st.session_state.step=3; st.rerun()

# Step 3: Primary Goal
elif st.session_state.step == 3:
    st.markdown('<p class="main-title">What is your primary goal?</p>', unsafe_allow_html=True)
    if st.button("Lose Weight (Fat Loss) 📉"): st.session_state.user_data['goal']='lose'; st.session_state.step=4; st.rerun()
    if st.button("Maintain Weight ⚖️"): st.session_state.user_data['goal']='maintain'; st.session_state.step=4; st.rerun()
    if st.button("Gain Muscle 📈"): st.session_state.user_data['goal']='gain'; st.session_state.step=4; st.rerun()

# Step 4: Target Areas (Based on your screenshots)
elif st.session_state.step == 4:
    st.markdown('<p class="main-title">Choose your target areas</p>', unsafe_allow_html=True)
    st.multiselect("", ["Belly & Waist", "Thighs", "Arms", "Back", "Full Body"])
    if st.button("Continue ➡️"): st.session_state.step=5; st.rerun()

# Step 5: Eating Habits (Sweets/Fried)
elif st.session_state.step == 5:
    st.markdown('<p class="main-title">How often do you consume sweets or fried food?</p>', unsafe_allow_html=True)
    if st.button("Multiple times a day 🍰"): st.session_state.step=6; st.rerun()
    if st.button("A few times a week 🍟"): st.session_state.step=6; st.rerun()
    if st.button("Rarely / Never 🥗"): st.session_state.step=6; st.rerun()

# Step 6: Activity Level
elif st.session_state.step == 6:
    st.markdown('<p class="main-title">What is your daily activity level?</p>', unsafe_allow_html=True)
    if st.button("Sedentary (Little exercise)"): st.session_state.user_data['act']=1.2; st.session_state.step=7; st.rerun()
    if st.button("Active (3-5 workouts/week)"): st.session_state.user_data['act']=1.55; st.session_state.step=7; st.rerun()
    if st.button("Elite (Intense daily exercise)"): st.session_state.user_data['act']=1.9; st.session_state.step=7; st.rerun()

# Step 7: Allergies (Important safety step)
elif st.session_state.step == 7:
    st.markdown('<p class="main-title">Do you have any food allergies?</p>', unsafe_allow_html=True)
    allergic = st.multiselect("", ["Lactose", "Gluten", "Nuts", "Seafood", "Eggs", "None"])
    if st.button("Confirm ➡️"): st.session_state.user_data['allergies']=allergic; st.session_state.step=8; st.rerun()

# Step 8: Sleep & Water
elif st.session_state.step == 8:
    st.markdown('<p class="main-title">Sleep & Hydration</p>', unsafe_allow_html=True)
    st.select_slider("Sleep Quality", ["Poor", "Average", "Excellent"])
    st.select_slider("Water Intake (liters)", ["< 1L", "1.5L", "2L", "3L+"])
    if st.button("Next ➡️"): st.session_state.step=9; st.rerun()

# Step 9: Measurements (The Engine)
elif st.session_state.step == 9:
    st.markdown('<p class="main-title">Final Measurements</p>', unsafe_allow_html=True)
    age = st.number_input("Your Age", 13, 100, 25)
    h = st.number_input("Your Height (cm)", 120, 230, 165)
    w = st.number_input("Your Weight (kg)", 35, 250, 70)
    if st.button("Generate Plan ✨"):
        st.session_state.user_data.update({'age':age, 'h':h, 'w':w})
        st.session_state.step = 10; st.rerun()

# Step 10: Analysis Screen
elif st.session_state.step == 10:
    st.markdown('<p class="main-title">Luna Glow is analyzing your data...</p>', unsafe_allow_html=True)
    bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        bar.progress(i + 1)
    st.session_state.step = 11; st.rerun()

# Step 11: FINAL RESULTS (FASTING + CALORIES + DEFICIT)
elif st.session_state.step == 11:
    st.markdown('<p class="main-title">Your Personalized Luna Glow Plan ✨</p>', unsafe_allow_html=True)
    
    # Core Logic
    u = st.session_state.user_data
    if u['gender'] == 'F':
        bmr = (10 * u['w']) + (6.25 * u['h']) - (5 * u['age']) - 161
    else:
        bmr = (10 * u['w']) + (6.25 * u['h']) - (5 * u['age']) + 5
    
    tdee = bmr * u.get('act', 1.2)
    
    # Apply Goal (Deficit/Surplus)
    if u['goal'] == 'lose':
        target = tdee - 500
        fasting_type = "16:8 (Power Fasting)"
        note = "Calorie Deficit Applied: -500 kcal/day"
    elif u['goal'] == 'gain':
        target = tdee + 400
        fasting_type = "12:12 (Steady Growth)"
        note = "Calorie Surplus Applied: +400 kcal/day"
    else:
        target = tdee
        fasting_type = "14:10 (Maintenance)"
        note = "Maintenance Calories Applied"

    st.markdown(f"""
    <div class="result-box">
        <h2 style="color:#FF1493; margin-top:0;">{int(target)} kcal/day</h2>
        <p style="font-size:18px;"><b>Fasting Plan:</b> {fasting_type}</p>
        <p style="color:#28A745; font-weight:bold;">{note}</p>
        <hr>
        <div style="display:flex; justify-content:space-around; font-size:14px;">
            <div><b>🥩 Protein</b><br>{int(u['w']*1.7)}g</div>
            <div><b>🍞 Carbs</b><br>{int(target*0.4/4)}g</div>
            <div><b>🥑 Fats</b><br>{int(target*0.25/9)}g</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.balloons()
    if st.button("Restart Analysis 🔄"): st.session_state.step = 1; st.rerun()
