import streamlit as st

# إعدادات الصفحة (الاسم والأيقونة)
st.set_page_config(page_title="Nona Glow ✨", page_icon="💖", layout="centered")

# حركة البالونات والنجوم أول ما يفتح الموقع
st.balloons()
st.snow()

# تنسيق العنوان والشعار
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>✨ نونا جلو - Nona Glow ✨</h1>", unsafe_allow_attribute=True)
st.markdown("<h3 style='text-align: center; color: #555;'>دليلكِ الكامل للعناية والجمال في الكويت 🇰🇼</h3>", unsafe_allow_attribute=True)

st.divider()

# الأقسام (روتين العناية والأسعار)
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌸 روتين نونا السحري")
    st.write("- ماسك النشا والترمس لتفتيح فوري.")
    st.write("- سكراب السكر وزيت الزيتون للنعومة.")
    st.write("- مرطب الشيا للبشرة الجافة.")

with col2:
    st.markdown("### 💰 عروض نونا جلو")
    st.info("الروتين الكامل: 15 د.ك")
    st.success("ماسك النضارة: 6 د.ك")

st.divider()

# زرار التواصل (أهم حتة للفلوس!)
st.markdown("### 📞 للحجز والاستفسار")
st.write("اضغطي على الزرار تحت عشان تطلبي الروتين بتاعك:")
# (غيري الـ X رقم تليفونك الكويتي)
st.link_button("اطلبي الآن عبر واتساب ✅", "https://wa.me/965XXXXXXXX")

st.info("💡 نصيحة نونا: الجمال يبدأ من اهتمامك بنفسك!")

# إضافة نجوم في آخر الصفحة
st.write("✨✨✨✨✨")
