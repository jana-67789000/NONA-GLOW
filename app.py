import streamlit as st
import time

# --- 1. إعدادات الهوية ---
st.set_page_config(page_title="Luna Glow AI", page_icon="🌙", layout="centered")

if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state: st.session_state.data = {}

# --- 2. التصميم (Copy-Paste من صورك) ---
def apply_style():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }
        .main-title { font-size: 28px; font-weight: 800; color: #111; text-align: center; margin-bottom: 10px; }
        .sub-title { font-size: 15px; color: #777; text-align: center; margin-bottom: 25px; }
        .stButton>button { 
            width: 100%; border-radius: 15px; border: 1px solid #F0F0F0; background: #FAFAFA; 
            color: #111; height: 60px; font-size: 17px; font-weight: 600; margin-bottom: 10px;
            text-align: left; padding-left: 20px; transition: 0.2s;
        }
        .stButton>button:hover { border-color: #FF1493; background: #FFF5FA; color: #FF1493; }
        .progress-bar { width: 100%; height: 8px; background: #F0F0F0; border-radius: 4px; margin-bottom: 40px; }
        .progress-fill { height: 100%; background: #FF1493; border-radius: 4px; transition: 0.4s; }
        .card { background: #F9F9F9; padding: 20px; border-radius: 20px; border: 1.5px solid #FF1493; text-align: center; }
        </style>
    """, unsafe_allow_html=True)

apply_style()

# شريط التقدم وزر الرجوع
if st.session_state.step < 12:
    progress = (st.session_state.step / 11) * 100
    st.markdown(f'<div class="progress-bar"><div class="progress-fill" style="width: {progress}%"></div></div>', unsafe_allow_html=True)
    if st.session_state.step > 1:
        if st.button("⬅️ Back", key="back"):
            st.session_state.step -= 1
            st.rerun()

# --- 3. الأسئلة بناءً على الـ 30 صورة ---

# 1. Gender
if st.session_state.step == 1:
    st.markdown('<p class="main-title">Choose your gender</p>', st.session_state.data.get('gender', ''))
    if st.button("Female 👩"): st.session_state.data['gender']='F'; st.session_state.step=2; st.rerun()
    if st.button("Male 👨"): st.session_state.data['gender']='M'; st.session_state.step=2; st.rerun()

# 2. Main Goal
elif st.session_state.step == 2:
    st.markdown('<p class="main-title">What is your main goal?</p>', unsafe_allow_html=True)
    if st.button("Lose Weight 📉"): st.session_state.data['goal']='lose'; st.session_state.step=3; st.rerun()
    if st.button("Maintain Weight ⚖️"): st.session_state.data['goal']='maintain'; st.session_state.step=3; st.rerun()
    if st.button("Gain Muscle 📈"): st.session_state.data['goal']='gain'; st.session_state.step=3; st.rerun()

# 3. Body Type (Current)
elif st.session_state.step == 3:
    st.markdown('<p class="main-title">Identify your body type</p>', unsafe_allow_html=True)
    if st.button("Ectomorph (Slim)"): st.session_state.step=4; st.rerun()
    if st.button("Mesomorph (Athletic)"): st.session_state.step=4; st.rerun()
    if st.button("Endomorph (Curvy)"): st.session_state.step=4; st.rerun()

# 4. Habits (Sweets & Fried Food)
elif st.session_state.step == 4:
    st.markdown('<p class="main-title">How often do you eat sweets? 🍭</p>', unsafe_allow_html=True)
    if st.button("Daily"): st.session_state.step=5; st.rerun()
    if st.button("Sometimes"): st.session_state.step=5; st.rerun()
    if st.button("Rarely"): st.session_state.step=5; st.rerun()

# 5. Activity Level
elif st.session_state.step == 5:
    st.markdown('<p class="main-title">What is your activity level?</p>', unsafe_allow_html=True)
    if st.button("Sedentary 🛋️"): st.session_state.data['act']=1.2; st.session_state.step=6; st.rerun()
    if st.button("Active 🏃"): st.session_state.data['act']=1.55; st.session_state.step=6; st.rerun()

# 6. Allergies
elif st.session_state.step == 6:
    st.markdown('<p class="main-title">Food Allergies ⚠️</p>', unsafe_allow_html=True)
    al = st.multiselect("", ["Lactose", "Gluten", "Nuts", "Seafood", "None"])
    if st.button("Next ➡️"): st.session_state.data['allergies']=al; st.session_state.step=7; st.rerun()

# 7. Age, Height, Weight (The core data)
elif st.session_state.step == 7:
    st.markdown('<p class="main-title">Body Measurements</p>', unsafe_allow_html=True)
    age = st.number_input("Age", 15, 80, 25)
    h = st.number_input("Height (cm)", 120, 220, 165)
    w = st.number_input("Weight (kg)", 30, 200, 70)
    if st.button("Calculate Plan 🔥"):
        st.session_state.data.update({'age':age, 'h':h, 'w':w})
        st.session_state.step = 8; st.rerun()

# 8. Analyzing Screen (The loading vibe)
elif st.session_state.step == 8:
    st.markdown('<p class="main-title">Creating your Luna Glow Plan...</p>', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/400x200?text=Analyzing+Data...")
    bar = st.progress(0)
    for i in range(100):
        time.sleep(0.03)
        bar.progress(i+1)
    st.session_state.step = 9; st.rerun()

# 9. FINAL RESULT: CALORIES & FASTING
elif st.session_state.step == 9:
    st.markdown('<p class="main-title">Your Personalized Plan ✨</p>', unsafe_allow_html=True)
    
    # Logic based on your request
    d = st.session_state.data
    # BMR calculation
    if d['gender'] == 'F':
        bmr = (10 * d['w']) + (6.25 * d['h']) - (5 * d['age']) - 161
    else:
        bmr = (10 * d['w']) + (6.25 * d['h']) - (5 * d['age']) + 5
    
    tdee = bmr * d['act']
    
    if d['goal'] == 'lose':
        target = tdee - 500 # Calorie Deficit
        fasting = "16:8 Fasting"
        msg = "Lose 0.5kg per week safely"
    elif d['goal'] == 'gain':
        target = tdee + 400 # Surplus
        fasting = "12:12 Fasting"
        msg = "Build muscle effectively"
    else:
        target = tdee
        fasting = "14:10 Fasting"
        msg = "Maintain your glow"

    st.markdown(f"""
    <div class="card">
        <h2 style="color:#FF1493;">Daily Calories: {int(target)} kcal</h2>
        <p style="font-size:18px;"><b>Method:</b> {fasting}</p>
        <p style="color:#666;">{msg}</p>
        <hr>
        <p>💧 Water: {round(d['w']*0.033, 1)}L | 🥩 Protein: {int(d['w']*1.6)}g</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Start New Journey 🔄"):
        st.session_state.step = 1; st.rerun()
