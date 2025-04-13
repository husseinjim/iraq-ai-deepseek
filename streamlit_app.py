import streamlit as st
import openai

# ✅ Correct DeepSeek API setup
openai.api_key = "Sk-aa6408149c574b0eab3f169ec65e6ff6"
openai.base_url = "https://api.deepseek.com/v1"

# Iraqi personality styles
characters = {
    "الحجيّة": "أنت الحجيّة، امرأة عراقية كبيرة بالعمر، حكيمة، درامية، ودمك خفيف...",
    "الحجي": "أنت الحجي، رجل عراقي كبير بالعمر، حكيم ومتدين...",
    "ابن المنطقة": "أنت ابن المنطقة، شاب شعبي يحب المزاح والسوالف باللهجة العراقية...",
    "الفاشنيستا": "أنت فاشنيستا عراقية تحبين الميكب، التيك توك، وتتكلمين بطريقة عصرية مليانة ايموجي...",
    "الشاعر": "أنت شاعر عراقي تحب الكلام العاطفي والرمزي، تجاوب بكل رقي...",
    "العسكري": "أنت عسكري عراقي، كلامك واضح، صارم ومباشر...",
    "السياسي": "أنت سياسي عراقي محترف، تتكلم بلغة رسمية ومليئة بالتحليل والمجاملات..."
}

# Streamlit UI setup
st.set_page_config(page_title="Iraq GPT", layout="centered")
st.title("🇮🇶 Iraq AI - دردش مع شخصية عراقية")

selected_character = st.selectbox("اختر شخصية:", list(characters.keys()))
user_input = st.text_input("✍️ اكتب سؤالك هنا")

# Initialize session state for chat history
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
    messages += st.session_state.chat_history
    messages.append({"role": "user", "content": user_input})

    response = openai.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )

    reply = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "assistant", "content": reply})

# Display chat messages
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"**👤 أنت:** {msg['content']}")
    else:
        st.markdown(f"**🤖 {selected_character}:** {msg['content']}")
