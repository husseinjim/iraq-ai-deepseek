
import streamlit as st
import requests

st.set_page_config(page_title="Iraq AI", page_icon="🇮🇶")
st.markdown("<h1 style='text-align: center;'>🇮🇶 Iraq AI - دردش مع شخصية عراقية 🇮🇶</h1>", unsafe_allow_html=True)

characters = {
    "الحجيّة": "إنتِ أم عراقية قديمة، شنو ردج؟",
    "الحجي": "إنت حجّي من الكبار.. شترد عليه؟",
    "ابن المنطقة": "رد كشباب منطقتك القح",
    "العسكري": "إنت ضابط قديم.. علمهم شلون",
    "السياسي": "رد سياسي ذكي ومحسوب",
    "الشاعر": "رد بصيغة بيت شعري عراقي",
}

st.markdown("### 👤 اختر شخصية:")
selected_character = st.selectbox("", list(characters.keys()))

st.markdown("### ✍️ اكتب سؤالك هنا 👇")
user_input = st.text_input("", placeholder="هلة")

if st.button("💬 أرسل"):
    with st.spinner("جاري توليد الرد..."):
        headers = {
            "Authorization": f"Bearer Sk-c73742bbdd1e4d7f9cf171c1a1ea20ab",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": characters[selected_character]},
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=payload)

        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            st.markdown(f"**{selected_character}:** {reply}")
        else:
            st.error(f"❌ Error {response.status_code}: {response.text}")
