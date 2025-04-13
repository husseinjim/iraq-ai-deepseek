
import streamlit as st
import requests

st.set_page_config(page_title="Iraq AI - شات بشخصيات عراقية 🇮🇶", page_icon="🇮🇶")
st.markdown("<h1 style='text-align: center;'>🇮🇶 Iraq AI - دردش مع شخصية عراقية</h1>", unsafe_allow_html=True)

characters = {
    "الحجيّة": "ردّي كأنك حجيّة عراقية، حكيمة، تمزج بين المودّة والحدة، وتحچي باللهجة البغدادية الشعبية.",
    "الحجي": "رد كأنك حجّي من بغداد، خبير، حاد الذكاء، يحب ينصح ويعطي رأي مباشر باللهجة العراقية.",
    "العسكري": "رد كأنك عسكري عراقي، صارم، مختصر بالكلام، حاد، ينفّذ الأوامر ويتكلم بعسكريّة ولهجة عراقية.",
    "النسوانجي": "رد كأنك شب نسوانجي يحچي بعراقي سوقي، جريء ومغازل ويستعمل مصطلحات شوارع بغداد."
}

selected_character = st.selectbox("👤 اختر شخصية:", list(characters.keys()))
st.markdown("✍️ اكتب سؤالك هنا 👇")
user_input = st.text_input("", placeholder="مثلاً: شرايك بالوضع؟")

if st.button("💬 أرسل"):
    if user_input:
        system_prompt = characters[selected_character]
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer Sk-c73742bbdd1e4d7f9cf171c1a1ea20ab"
        }

        try:
            response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=payload)
            data = response.json()
            if "choices" in data and data["choices"]:
                reply = data["choices"][0]["message"]["content"]
                st.markdown(f"👤 {selected_character}:")
                st.write(reply)
            else:
                st.error("❌ خطأ: لم يتم العثور على رد من النموذج.")
        except Exception as e:
            st.error(f"⚠️ حدث خطأ: {str(e)}")
    else:
        st.warning("🟡 الرجاء كتابة رسالة قبل الإرسال.")
