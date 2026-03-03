import streamlit as st

st.title("🌾 AgriSmart AI - ระบบวิเคราะห์สุขภาพพืช")

st.write("กรอกข้อมูลจากโดรนหรือการสำรวจภาคสนาม")

ndvi = st.slider("ค่า NDVI", 0.0, 1.0, 0.5)
soil_moisture = st.slider("ค่าความชื้นในดิน (%)", 0, 100, 50)
fungi = st.selectbox("ระดับการพบเชื้อราในดิน", ["ต่ำ", "ปานกลาง", "สูง"])

st.subheader("📊 ผลการวิเคราะห์")

if ndvi < 0.3 and soil_moisture < 30:
    st.error("⚠️ พืชเสี่ยงขาดน้ำอย่างรุนแรง")
elif fungi == "สูง" and ndvi > 0.6:
    st.warning("🦠 พื้นที่อาจอยู่ในระยะปลายของ CDI")
elif ndvi < 0.5:
    st.warning("🌿 พืชเริ่มมีความเครียด")
else:
    st.success("✅ พืชอยู่ในสภาพปกติ")

st.info("หมายเหตุ: ควรใช้ข้อมูลร่วมกับการตรวจสอบภาคสนาม")
