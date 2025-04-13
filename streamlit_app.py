
import streamlit as st
import requests

st.set_page_config(page_title="🇮🇶 Iraq AI - دردش مع شخصية عراقية", layout="centered")
st.markdown("""<h1 style='text-align: center;'>🇮🇶 Iraq AI - دردش مع شخصية عراقية</h1>""", unsafe_allow_html=True)

st.markdown("### 👤 اختر شخصية:")
character = st.selectbox("", ["الحجية", "الحجي", "المعمم", "العسكري", "المراهق"])

st.markdown("### ✍️ اكتب سؤالك هنا 👇")
user_input = st.text_input("", "هلا")

if st.button("💬 أرسل"):
    if user_input:
        system_prompt = f"رد علي كأنك {character} عراقي باللهجة المحلية، وكن مرحاً وثقافياً بنفس الوقت."

        try:
            response = requests.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers={
                    "Authorization": "Bearer sk-aa6408149c574b0eab3f169ec65e6ff6",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "deepseek-chat",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_input}
                    ]
                }
            )

            result = response.json()
            if "choices" in result:
                reply = result["choices"][0]["message"]["content"]
                st.markdown(f"👤 **{character}**: {reply}")
            else:
                st.error("❌ خطأ: لم يتم العثور على رد من النموذج.")
        except Exception as e:
            st.error(f"❌ خطأ أثناء الاتصال بـ DeepSeek: {e}")
    else:
        st.warning("🟡 الرجاء كتابة رسالة أولاً.")
