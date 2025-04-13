
import streamlit as st
import openai

# Set DeepSeek API credentials
openai.api_key = "Sk-aa6408149c574b0eab3f169ec65e6ff6"
openai.api_base = "https://api.deepseek.com/v1"

st.set_page_config(page_title="Iraq AI", page_icon="🇮🇶")
st.title("🇮🇶 Iraq AI - دردش مع شخصية عراقية")

characters = {
    "الحجيّة": "إنت تتكلم ويه حجية من أهل الكرخ، تحب اللّف والدوران، بس طيبة!",
    "الحجي": "رجل كبير بالعمر من بغداد، دايمًا ينصح الشباب ويحب يحجي عن الماضي.",
    "ابن المنطقة": "شاب عراقي طيب ودايمًا يمون، يستخدم كلمات من الشارع العراقي.",
    "الفاشينيستا": "بنية تحب الماركات وتتكلم بطريقه فاشن، بس بعده بيها طيبة عراقية.",
    "الشاعر": "يتكلم بطريقة شعرية، يجاوب دومًا بكلمات موزونة.",
    "العسكري": "يتكلم بحزم وانضباط وكأنّه ضابط، بس عنده جانب فكاهي.",
    "السياسي": "يتكلم مثل السياسيين العراقيين، يحاول يلف ويدور وما ينطي جواب واضح 😂"
}

character = st.selectbox("👤 اختر شخصية:", list(characters.keys()))
st.markdown("✍️ اكتب سؤالك هنا 👇")
user_input = st.text_input("", placeholder="هلا")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("💬 أرسل"):
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        system_prompt = characters[character]
        try:
            response = openai.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": system_prompt},
                    *st.session_state.chat_history
                ]
            )
            reply = response.choices[0].message.content
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"خطأ: {str(e)}")

if st.session_state.chat_history:
    for msg in st.session_state.chat_history:
        st.write(f"**{'👤' if msg['role']=='user' else '🤖'}**: {msg['content']}")

if st.button("🗑️ مسح المحادثة"):
    st.session_state.chat_history = []
