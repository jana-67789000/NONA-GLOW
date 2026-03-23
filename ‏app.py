import streamlit as st
import time

# --- 1. إعدادات الصفحة والهوية ---
st.set_page_config(page_title="Nona-Glow Nutrition", page_icon="🥗", layout="centered")

if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state: st.session_state.data = {}

# --- 2. دالة التنسيق الشيك (نفس الروح اللي بتحبيها) ---
def apply_ui():
    gender = st.session_state.data.get('gender', 'أنثى ✨')
    is_female = "أنثى" in gender or "Female" in gender
    bg = "#FFB6C1" if is_female else "#001F3F"
    btn = "#FF1493" if is_female else "#1E90FF"
    txt = "#333" if is_female else "#FFFFFF"
    
    st.markdown(f"""
        <style>
        .stApp {{ background: {bg}; transition: 0.5s; }}
        h1, h2, h3, p, label {{ color: {txt} !important; text-align: center; font-family: 'Cairo', sans-serif; }}
        .stButton>button {{ width: 100%; border-radius: 30px; background: {btn}; color: white; height: 55px; font-weight: bold; border: none; font-size: 18px; }}
        .card {{ background: rgba(255,255,255,0.2); padding: 25px; border-radius: 20px; border: 1px solid white; margin-bottom: 15px; }}
        </style>
    """, unsafe_allow_html=True)

apply_ui()
lang = st.session_state.data.get('lang', 'ar')

# --- 3. رحلة المستخدم (الأسئلة المنظمة) ---

# الخطوة 1: اللغة
if st.session_state.step == 1:
    st.title("✨ Nona-Glow Nutrition")
    st.image("https://via.placeholder.com/400x250?text=Healthy+Lifestyle")
    l = st.radio("اختر اللغة / Choose Language", ["العربية", "English"])
    if st.button("استمرار | Continue"):
        st.session_state.data['lang'] = 'ar' if l == "العربية" else 'en'
        st.session_state.step = 2
        st.rerun()

# الخطوة 2: الهدف (تخسيس - تثبيت - زيادة)
elif st.session_state.step == 2:
    st.title("🎯 ما هو هدفكِ الغذائي؟" if lang == 'ar' else "What is your goal?")
    goal = st.radio("", ["خسارة وزن 📉", "تثبيت الوزن ⚖️", "زيادة كتلة عضلية/وزن 📈"] if lang == 'ar' else ["Lose Weight", "Maintain Weight", "Gain Weight"])
    if st.button("التالي ➡️"):
        st.session_state.data['goal'] = goal
        st.session_state.step = 3
        st.rerun()

# الخطوة 3: الحساسية (Allergies)
elif st.session_state.step == 3:
    st.title("⚠️ هل تعاني من أي حساسية؟" if lang == 'ar' else "Do you have any allergies?")
    allergies = st.multiselect("", ["ألبان (Lactose)", "جلوتين (Gluten)", "مكسرات (Nuts)", "بيض (Eggs)", "لا يوجد"] if lang == 'ar' else ["Lactose", "Gluten", "Nuts", "Eggs", "None"])
    if st.button("التالي ➡️"):
        st.session_state.data['allergies'] = allergies
        st.session_state.step = 4
        st.rerun()

# الخطوة 4: أنواع الأكل المفضلة (Protein, Carbs, etc.)
elif st.session_state.step == 4:
    st.title("🥦 ما هي مصادر الأكل المفضلة؟" if lang == 'ar' else "Preferred Food Types?")
    diet_pref = st.multiselect("", ["بروتين عالي (لحوم/بقوليات)", "كربوهيدرات صحية (شوفان/بطاطس)", "دهون صحية (أفوكادو/زيت زيتون)"] if lang == 'ar' else ["High Protein", "Healthy Carbs", "Healthy Fats"])
    if st.button("التالي ➡️"):
        st.session_state.data['diet_pref'] = diet_pref
        st.session_state.step = 5
        st.rerun()

# الخطوة 5: البيانات الجسدية (لحساب السعرات)
elif st.session_state.step == 5:
    st.title("📏 لندخل البيانات" if lang == 'ar' else "Enter Measurements")
    gender = st.radio("الجنس", ["أنثى ✨", "ذكر ⚡"] if lang == 'ar' else ["Female ✨", "Male ⚡"])
    col1, col2 = st.columns(2)
    with col1: w = st.number_input("الوزن (kg)", 40, 200, 70)
    with col2: h = st.number_input("الطول (cm)", 120, 220, 160)
    if st.button("إنشاء النظام الغذائي 🥣"):
        st.session_state.data.update({'gender': gender, 'w': w, 'h': h})
        st.session_state.step = 6
        st.rerun()

# الخطوة 6: النتيجة النهائية (صيام + سعرات + نصائح)
elif st.session_state.step == 6:
    st.title("🎉 نظامك الغذائي المخصص جاهز!" if lang == 'ar' else "Your Plan is Ready!")
    
    # منطق حساب الصيام والسعرات
    goal = st.session_state.data['goal']
    if "خسارة" in goal or "Lose" in goal:
        fasting = "16:8 (مثالي للحرق)"
        calories = (st.session_state.data['w'] * 22) - 500
    elif "تثبيت" in goal or "Maintain" in goal:
        fasting = "14:10 (للتوازن)"
        calories = st.session_state.data['w'] * 22
    else:
        fasting = "12:12 (للنمو)"
        calories = (st.session_state.data['w'] * 22) + 500

    st.markdown(f"""
    <div class='card'>
    <h3>⏳ نظام الصيام: {fasting}</h3>
    <h3>🔥 سعراتك اليومية: {int(calories)} سعرة</h3>
    <p>⚠️ الحساسية المكتشفة: {", ".join(st.session_state.data['allergies'])}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("نصيحة نونا: ابدأ بوجبة غنية بالبروتين لكسر الصيام! 🥗")
    
    if st.button("إعادة التحليل 🔄"):
        st.session_state.step = 1
        st.rerun()
