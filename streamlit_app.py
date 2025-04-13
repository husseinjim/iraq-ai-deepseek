
import streamlit as st
import requests

st.set_page_config(page_title="Iraq AI", layout="centered")

st.markdown("""<h1 style='text-align: center;'>🇮🇶 Iraq AI - دردش مع شخصية عراقية</h1>""", unsafe_allow_html=True)

personality = st.selectbox("👤 اختر شخصية:", [
    "الحجّيّة", "الحجي", "ابن المنطقة", "الشاعر", "السياسي", "العسكري", "الفاشنيستا"
])

question = st.text_input("✍️ اكتب سؤالك هنا 👇", "")

if st.button("💬 أرسل"):
    if not question.strip():
        st.warning("الرجاء كتابة سؤال.")
    else:
        api_key = "Sk-c73742bbdd1e4d7f9cf171c1a1ea20ab"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        system_prompt = f"أجب على السؤال وكأنك {personality}، باللهجة العراقية، بأسلوب فكاهي وقريب للقلب."

        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ]
        }

        try:
            response = requests.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers=headers,
                json=data
            )
            result = response.json()

            if "choices" in result:
                answer = result["choices"][0]["message"]["content"]
                st.markdown(f"👤 **{personality}**: {answer}")
            else:
                st.error(f"❌ خطأ: {result.get('error', {}).get('message', 'استجابة غير معروفة')}")
        except Exception as e:
            st.error(f"⚠️ حدث خطأ أثناء الاتصال بـ DeepSeek: {e}")
