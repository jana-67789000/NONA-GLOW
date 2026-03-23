import streamlit as st
import time

# --- 1. إعدادات الهوية ---
st.set_page_config(page_title="Nona-Glow AI", page_icon="✨", layout="centered")

if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state: st.session_state.data = {}

# --- 2. قاعدة بيانات التمارين ---
workouts = {
    "Strength 💪": [
        {"ar": "سكوات (Squats)", "en": "Squats", "v": "https://www.w3schools.com/html/mov_bbb.mp4"},
        {"ar": "ضغط (Push-ups)", "en": "Push-ups", "v": "https://www.w3schools.com/html/mov_bbb.mp4"}
    ],
    "Cardio 🏃": [
        {"ar": "نط الحبل", "en": "Jump Rope", "v": "https://www.w3schools.com/html/mov_bbb.mp4"}
    ],
    "Pilates 🧘": [
        {"ar": "بيلاتس (The Hundred)", "en": "The Hundred", "v": "https://www.w3schools.com/html/mov_bbb.mp4"}
    ]
}

# --- 3. دالة التنسيق الشيك ---
def apply_ui():
    gender = st.session_state.data.get('gender', 'أنثى ✨')
    is_female = "أنثى" in gender
    bg = "#FFB6C1" if is_female else "#001F3F"
    btn = "#FF1493" if is_female else "#1E90FF"
    txt = "#333" if is_female else "#FFFFFF"
    
    st.markdown(f"""
        <style>
        .stApp {{ background: {bg}; transition: 0.5s; }}
        h1, h2, h3, p, label {{ color: {txt} !important; text-align: center; }}
        .stButton>button {{ width: 100%; border-radius: 30px; background: {btn}; color: white; border: none; height: 55px; font-weight: bold; }}
        .card {{ background: rgba(255,255,255,0.15); padding: 25px; border-radius: 20px; border: 1px solid white; margin-bottom: 20px; }}
        .rest-box {{ background: #4CAF50; color: white; padding: 20px; border-radius: 15px; font-size: 20px; }}
        </style>
    """, unsafe_allow_html=True)

# --- 4. رحلة المستخدم خطوة بخطوة ---

apply_ui()

# الخطوة 1: اللغة والترحيب
if st.session_state.step == 1:
    st.title("✨ Nona-Glow AI")
    st.image("https://via.placeholder.com/400x250?text=Welcome+Meme") # ملصق الترحيب
    lang = st.radio("Choose Language / اختر اللغة", ["العربية", "English"])
    st.session_state.data['lang'] = 'ar' if lang == "العربية" else 'en'
    if st.button("ابدأ الرحلة 🚀"):
        st.session_state.step = 2
        st.rerun()

# الخطوة 2: تحديد الجنس
elif st.session_state.step == 2:
    st.title("👤 لنتعرف عليكِ/عليك")
    st.image("https://via.placeholder.com/200x200?text=Gender+Meme")
    gender = st.radio("الجنس", ["أنثى ✨", "ذكر ⚡"])
    if st.button("التالي ➡️"):
        st.session_state.data['gender'] = gender
        st.session_state.step = 3
        st.rerun()

# الخطوة 3: صيام متقطع
elif st.session_state.step == 3:
    st.title("⏳ نظام الصيام المتقطع")
    st.image("https://via.placeholder.com/300x200?text=Fasting+Meme") # ملصق الصيام (الصدمة مثلاً)
    fasting = st.selectbox("اختر نظام الصيام المناسب ليومك:", ["16:8 (حرق دهون مثالي)", "14:10 (للبداية الهادئة)", "20:4 (تحدي المحترفين)"])
    if st.button("تثبيت النظام ✅"):
        st.session_state.data['fasting'] = fasting
        st.session_state.step = 4
        st.rerun()

# الخطوة 4: البيانات الشخصية
elif st.session_state.step == 4:
    st.title("📏 القياسات")
    col1, col2 = st.columns(2)
    with col1: w = st.number_input("الوزن (كجم)", 40, 200, 70)
    with col2: h = st.number_input("الطول (سم)", 120, 220, 160)
    if st.button("حلل بياناتي 🔥"):
        st.session_state.data.update({'w': w, 'h': h})
        st.session_state.step = 5
        st.rerun()

# الخطوة 5: شاشة الانتظار
elif st.session_state.step == 5:
    st.image("https://via.placeholder.com/400x250?text=Waiting+Meme") # ملصق الانتظار
    with st.status("جاري دمج نظام الصيام والتمارين...", expanded=True):
        time.sleep(2)
        st.write("✅ تم حساب السعرات...")
        time.sleep(1)
        st.write("✅ تم تجهيز وقت الراحة والترطيب...")
    st.balloons()
    if st.button("رؤية برنامجي الكامل ✨"):
        st.session_state.step = 6
        st.rerun()

# الخطوة 6: البرنامج النهائي والتمارين
elif st.session_state.step == 6:
    lang = st.session_state.data['lang']
    st.title("🎉 خطتكِ الجاهزة")
    st.image("https://via.placeholder.com/400x250?text=Success+Meme") # ملصق النجاح
    
    st.markdown(f"""<div class='card'>
    <h3>📋 ملخص البرنامج</h3>
    <p>نظام الصيام: {st.session_state.data['fasting']}</p>
    <p>الهدف: خسارة وزن ونحت الجسم</p>
    </div>""", unsafe_allow_html=True)

    st.subheader("🏋️ ابدأ تمارينك الآن")
    t1, t2, t3 = st.tabs(["Strength", "Cardio", "Pilates"])

    def render_workout(cat):
        for ex in workouts[cat]:
            st.markdown(f"<div class='card'><h4>{ex[lang]}</h4></div>", unsafe_allow_html=True)
            duration = st.slider(f"وقت التمرين (ثانية) - {ex[lang]}", 10, 120, 30, key=ex[lang])
            st.video(ex['v'])
            
            if st.button(f"ابدأ {ex[lang]} ⏱️"):
                # مؤقت التمرين
                t_place = st.empty()
                for i in range(duration, 0, -1):
                    t_place.metric("🔥 تمرّن الآن!", f"{i} ثانية")
                    time.sleep(1)
                
                # وقت الراحة + نصيحة المايه
                st.snow()
                t_place.markdown("""<div class='rest-box'>🥤 وقت الراحة (30 ثانية)<br>💧 اشرب ماء الآن يا بطل! 💧</div>""", unsafe_allow_html=True)
                rest_progress = st.progress(0)
                for r in range(30, 0, -1):
                    t_place.metric("😴 استراحة وترطيب", f"{r} ثانية")
                    rest_progress.progress((30-r)/30)
                    time.sleep(1)
                st.success("انتهت الراحة! جاهز للي بعده؟ 💪")

    with t1: render_workout("Strength 💪")
    with t2: render_workout("Cardio 🏃")
    with t3: render_workout("Pilates 🧘")

    if st.button("العودة للرئيسية 🔄"):
        st.session_state.step = 1
        st.rerun()
