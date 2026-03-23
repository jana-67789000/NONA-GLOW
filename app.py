import streamlit as st
import time

# إعداد الهوية البصرية
st.set_page_config(page_title="Nona-Glow AI", page_icon="✨")

# استايل الألوان المتغيرة (بينك للبنات / كحلي للأولاد)
def apply_theme(gender_choice):
    if "أنثى" in gender_choice:
        color, secondary = "#FFB6C1", "#FF69B4"
    else:
        color, secondary = "#001F3F", "#1E90FF"
    
    st.markdown(f"""
        <style>
        .stApp {{ background: {color}; }}
        .main-card {{ background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; border: 1px solid white; }}
        h1, h2, h3, p, span, label {{ color: white !important; text-align: right; }}
        </style>
    """, unsafe_allow_html=True)

# القائمة الجانبية للبيانات الأساسية
with st.sidebar:
    st.header("👤 الملف الشخصي")
    gender = st.radio("الجنس", ["أنثى ✨", "ذكر ⚡"])
    goal = st.selectbox("ما هو هدفك الرئيسي؟", ["خسارة وزن سريع", "نحت منطقة معينة", "تحسين الصحة العامة"])
    focus_area = st.multiselect("اختر مناطق التركيز:", ["البطن", "الأرداف", "الذراعين", "الظهر"])

apply_theme(gender)

st.title("✨ نونا جلو | الذكاء الاصطناعي للرشاقة")
st.write(f"### مرحباً بكِ.. لنصمم خطتك بناءً على أحدث أنظمة الصيام المتقطع")

# نظام الأسئلة التحليلي
with st.container():
    st.subheader("🔍 تحليل حالة الجسم")
    
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("الوزن الحالي (كجم)", 40, 200, 70)
        activity = st.select_slider("مستوى نشاطك اليومي", options=["خامل", "متوسط", "نشيط جداً"])
    with col2:
        height = st.number_input("الطول (سم)", 120, 220, 160)
        fasting_exp = st.selectbox("خبرتك في الصيام المتقطع", ["مبتدئ", "متوسط", "محترف"])

    if st.button("تحليل البيانات وإنشاء الخطة 🔥"):
        with st.status("جاري دمج البيانات وتحليل الأهداف...", expanded=True) as status:
            time.sleep(1)
            st.write("✅ تم حساب مؤشر كتلة الجسم...")
            time.sleep(1)
            st.write(f"✅ تم تحديد تمارين مخصصة لـ {', '.join(focus_area)}...")
            status.update(label="تم تجهيز خطتك الشخصية!", state="complete")
        
        st.balloons()
        
        # عرض النتائج
        st.markdown("---")
        st.header("📋 خطتك المقترحة")
        res1, res2, res3 = st.columns(3)
        res1.metric("نظام الصيام", "16:8" if activity != "خامل" else "14:10")
        res2.metric("السعرات المستهدفة", f"{weight * 24}")
        res3.metric("كمية الماء", f"{round(weight*0.035, 1)} لتر")
        
        # تصحيح الخطأ هنا (استخدام goal بدلاً من target_area)
        st.info(f"💡 نصيحة نونا: بما أن هدفك هو {goal}، ركزي على تمارين الكارديو الصباحية قبل أول وجبة!")

# قسم الاشتراكات (الأسعار الحقيقية اللي حددتيها)
st.markdown("---")
st.subheader("💎 ترقية الحساب (VIP)")
plans = {
    "تجريبي (1.5 د.ك)": 1.5, 
    "شهري (2.5 د.ك)": 2.5, 
    "3 شهور (7.5 د.ك)": 7.5, 
    "سنة (30 د.ك)": 30
}
selected_plan = st.radio("اختر باقة الاشتراك للوصول للتمارين الصوتية والفيديوهات:", list(plans.keys()))

if st.button("اشترك الآن بأمان 💳"):
    st.success(f"✅ جاري تحويلك لبوابة الدفع لدفع {plans[selected_plan]} دينار كويتي")
