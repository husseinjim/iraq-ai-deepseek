import streamlit as st
import openai

# Correct DeepSeek API config
openai.api_key = "Sk-aa6408149c574b0eab3f169ec65e6ff6"
openai.base_url = "https://api.deepseek.com"

# Iraqi personalities
characters = {
    "الحجيّة": "أنت الحجيّة، امرأة عراقية كبيرة بالعمر، حكيمة، درامية، ودمك خفيف...",
    "الحجي": "أنت الحجي، رجل عراقي كبير بالعمر، حكيم ومتدين...",
    "ابن المنطقة": "أنت ابن المنطقة، شاب عراقي عايش بالحارة...",
    "الفاشنيستا": "أنت بنوتة عراقية مودرن، تحبين الميكب، التيك توك...",
    "الشاعر": "أنت شاعر عراقي، تحب الحكي العميق والرومانسي...",
    "العسكري": "أنت عسكري عراقي، تتكلم بنبرة صارمة، تحب الانضباط...",
    "السياسي": "أنت سياسي عراقي محترف، تتكلم بلغة رسمية جداً..."
}

# Streamlit layout
st.set_page_config(page_title="Iraq GPT", layout="centered")
st.title("🇮🇶 Iraq AI - دردش مع شخصية عراقية")

selected_character = st.selectbox("اختر شخصية: 🤖", list(characters.keys()))
user_input = st.text_input("👇 اكتب سؤالك هنا")

# Chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

col1, col2 = st.columns(2)
with col1:
    send = st.button("💬 أرسل")
with col2:
    clear = st.button("🗑️ مسح المحادثة")

if clear:
    st.session_state.chat_history = []
    st.experimental_rerun()

if send and user_input:
    messages = [{"role": "system", "content": characters[selected_character]}]
    for msg in st.session_state.chat_history:
        messages.append(msg)
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="deepseek-chat",
        messages=messages
    )

    reply = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "assistant", "content": reply})

# Display chat
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"**👤 أنت:** {msg['content']}")
    else:
        st.markdown(f"**🤖 {selected_character}:** {msg['content']}")
