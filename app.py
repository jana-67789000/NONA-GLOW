import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Nona Glow ✨", page_icon="💖")

# المفاجأة أول ما يفتح
st.balloons()
st.snow()

# العنوان بشكل بسيط وضمان إنه يشتغل
st.title("✨ نونا جلو - Nona Glow ✨")
st.subheader("دليلكِ الكامل للعناية والجمال في الكويت 🇰🇼")

st.divider()

# الأقسام
st.markdown("### 🌸 روتين نونا السحري")
st.write("- ماسك النشا والترمس لتفتيح فوري.")
st.write("- سكراب السكر وزيت الزيتون للنعومة.")

st.markdown("### 💰 عروض نونا جلو")
st.info("الروتين الكامل: 15 د.ك")
st.success("ماسك النضارة: 6 د.ك")

st.divider()

# زرار الواتساب (تأكدي من تغيير الرقم)
st.write("### 📞 للحجز والاستفسار")
st.link_button("اطلبي الآن عبر واتساب ✅", "https://wa.me/965XXXXXXXX")

st.write("✨✨✨✨✨")
