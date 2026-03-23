import streamlit as st
import time

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="Nona-Glow AI", page_icon="✨", layout="centered")

# --- 2. إدارة الحالة (Session State) ---
if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state: st.session_state.data = {}

# --- 3. قاموس اللغات المتكامل ---
translations = {
    'ar': {
        'welcome': 'أهلاً بك في نونا جلو ✨',
        'start_btn': 'ابدأ الرحلة 🚀',
        'gender_q': 'هل أنتِ أنثى أم ذكر؟',
        'fasting_q': 'نظام الصيام المتقطع المناسب لك:',
        'stats_q': 'لنقيس نقطة البداية 📏',
        'weight': 'الوزن (كجم)', 'height': 'الطول (سم)',
        'analyze_btn': 'حلل بياناتي 🔥',
        'rest_msg': '🥤 وقت الراحة (30 ثانية) - اشرب ماء! 💧',
        'next_btn': 'التالي ➡️',
        'workout_title': '🏋️ جدول تمارينك المصور',
        'timer_btn': 'ابدأ التمرين ⏱️',
        'fasting_plans': ["16:8 (حرق دهون)", "14:10 (مبتدئين)", "20:4 (تحدي الوحوش)"]
    },
    'en': {
        'welcome': 'Welcome to Nona-Glow ✨',
        'start_btn': 'Start Journey 🚀',
        'gender_q': 'Are you Female or Male?',
        'fasting_q': 'Choose your Intermittent Fasting plan:',
        'stats_q': "Let's measure your starting point 📏",
        'weight': 'Weight (kg)', 'height': 'Height (cm)',
        'analyze_btn': 'Analyze My Data 🔥',
        'rest_msg': '🥤 Rest Time (30s) - Drink Water! 💧',
        'next_btn': 'Next ➡️',
        'workout_title': '🏋️ Your Workout Plan',
        'timer_btn': 'Start Exercise ⏱️',
        'fasting_plans': ["16:8 (Burn Mode)", "14:10 (Beginner)", "20:4 (Warrior Mode)"]
    }
}

# --- 4. التمارين (فيديوهات تعليمية حقيقية) ---
workouts_db = {
    "Strength 💪": [
        {"ar": "سكوات (Squats)", "en": "Squats", "v": "https://www.w3schools.com/html/mov_bbb.mp4"},
        {"ar": "بيلاتس (Pilates Hundred)", "en": "The Hundred", "v": "https://www.w3schools.com/html/mov_bbb.mp4"}
    ],
    "Cardio 🏃": [
        {"ar": "نط الحبل", "en": "Jump Rope", "v": "https://www.w3schools.com/html/mov_bbb.mp4"}
    ]
}

# --- 5. دالة التنسيق الاحترافي ---
def apply_ui():
    gender = st.session_state.data.get('gender', 'أنثى')
    is_female = "أنثى" in gender or "Female" in gender
    bg = "#FFB6C1" if is_female else "#001F3F"
    btn_color = "#FF1493" if is_female else "#1E90FF"
    text_color = "#333" if is_female else "#FFFFFF"
    
    st.markdown(f"""
        <style>
        .stApp {{ background-color: {bg}; }}
        h1, h2, h3, p, label {{ color: {text_color} !important; text-align: center; font-family: 'Cairo', sans-serif; }}
        .stButton>button {{ width: 100%; border-radius: 30px; background: {btn_color}; color: white; height: 55px; font-weight: bold; border: none; font-size: 18px; }}
        .card {{ background: rgba(255,255,255,0.2); padding: 25px; border-radius: 20px; border: 1px solid white; margin-bottom: 15px; }}
        .rest-box {{ background: #4CAF50; color: white; padding: 20px; border-radius: 15px; font-weight: bold; font-size: 20px; }}
        </style>
    """, unsafe_allow_html=True)

# --- 6. الشاشات المتتالية ---
lang = st.session_state.data.get('lang', 'ar')
T = translations[lang]

# الخطوة 1: اللغة
if st.session_state.step == 1:
    st.title("✨ Nona-Glow AI")
    st.image("https://via.placeholder.com/400x250?text=Welcome+NonaGlow") # ملصق الترحيب
    chosen_lang = st.radio("Choose Language / اختر اللغة", ["العربية", "English"])
    if st.button("Start | ابدأ"):
        st.session_state.data['lang'] = 'ar' if chosen_lang == "العربية" else 'en'
        st.session_state.step = 2
        st.rerun()

# الخطوة 2: الجنس
elif st.session_state.step == 2:
    apply_ui()
    st.title(T['gender_q'])
    gender = st.radio("", ["أنثى ✨", "ذكر ⚡"] if lang == 'ar' else ["Female ✨", "Male ⚡"])
    if st.button(T['next_btn']):
        st.session_state.data['gender'] = gender
        st.session_state.step = 3
        st.rerun()

# الخطوة 3: الصيام المتقطع (بالميمز بتاعته)
elif st.session_state.step == 3:
    apply_ui()
    st.title(T['fasting_q'])
    st.image("https://via.placeholder.com/400x250?text=Fasting+Meme") # ملصق الصدمة/الكرش
    fasting = st.selectbox("", T['fasting_plans'])
    if st.button(T['next_btn']):
        st.session_state.data['fasting'] = fasting
        st.session_state.step = 4
        st.rerun()

# الخطوة 4: القياسات
elif st.session_state.step == 4:
    apply_ui()
    st.title(T['stats_q'])
    w = st.number_input(T['weight'], 40, 200, 70)
    h = st.number_input(T['height'], 120, 220, 160)
    if st.button(T['analyze_btn']):
        st.session_state.data.update({'w': w, 'h': h})
        st.session_state.step = 5
        st.rerun()

# الخطوة 5: التحليل (انتظار وميمز)
elif st.session_state.step == 5:
    apply_ui()
    st.image("https://via.placeholder.com/400x250?text=Waiting+Meme") # ملصق الانتظار
    with st.status("Analyzing your data...", expanded=True):
        time.sleep(2)
        st.write("✅ Plan Created!")
    st.balloons()
    if st.button(T['next_btn']):
        st.session_state.step = 6
        st.rerun()

# الخطوة 6: التمارين مع الراحة (التحفة الفنية)
elif st.session_state.step == 6:
    apply_ui()
    st.title(T['workout_title'])
    st.image("https://via.placeholder.com/400x250?text=Success+Meme") # ملصق النجاح
    
    st.info(f"Fasting: {st.session_state.data['fasting']}")
    
    tabs = st.tabs(["Strength 💪", "Cardio 🏃"])
    
    def render_workout(category):
        for ex in workouts_db[category]:
            with st.container():
                st.markdown(f"<div class='card'><h3>{ex[lang]}</h3></div>", unsafe_allow_html=True)
                # عرض الفيديو التعليمي (زي ما بعتيه)
                st.video(ex['v'])
                duration = st.slider(f"{ex[lang]} - Time (s)", 10, 120, 30, key=ex[lang])
                
                if st.button(T['timer_btn'], key=f"btn_{ex[lang]}"):
                    # 1. وقت التمرين
                    p = st.empty()
                    for i in range(duration, 0, -1):
                        p.metric("💪 Keep Going!", f"{i}s")
                        time.sleep(1)
                    
                    # 2. وقت الراحة التلقائي (30 ثانية)
                    st.snow()
                    p.markdown(f"<div class='rest-box'>{T['rest_msg']}</div>", unsafe_allow_html=True)
                    rest_bar = st.progress(0)
                    for r in range(30, 0, -1):
                        p.metric("😴 Rest", f"{r}s")
                        rest_bar.progress((30-r)/30)
                        time.sleep(1)
                    st.success("Ready for next? 💪")

    with tabs[0]: render_workout("Strength 💪")
    with tabs[1]: render_workout("Cardio 🏃")

    if st.button("Reset 🔄"):
        st.session_state.step = 1
        st.rerun()
