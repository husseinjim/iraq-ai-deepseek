import streamlit as st
import openai

# DeepSeek API setup (OpenRouter / DeepSeek API compatible)
openai.api_key = "Sk-aa6408149c574b0eab3f169ec65e6ff6"
openai.base_url = "https://api.deepseek.com/v1"

# Iraqi characters
characters = {
    "الحجيّة": "أنت الحجيّة، امرأة عراقية كبيرة بالعمر، حكيمة، درامية، ودمك خفيف...",
    "الحجي": "أنت الحجي، رجل عراقي كبير بالعمر، حكيم ومتدين...",
    "ابن المنطقة": "أنت ابن المنطقة، شاب شعبي عايش بالحارة، تحب المزاح والحچي السريع...",
    "الفاشنيستا": "أنت فاشنيستا عراقية، تحبين الميكب والدراما والتيك توك، تحجين بستايل عصري مليان ايموجي...",
    "الشاعر": "أنت شاعر عراقي، تحب الحچي الرومانسي، وتجاوب بكلام عميق وراقي...",
    "العسكري": "أنت عسكري عراقي، تحب النظام والانضباط، كلامك صارم ومباشر...",
    "السياسي": "أنت سياسي عراقي، تحب التحليل والحديث الرسمي، وتجاوب بطريقة ذكية ودبلوماسية..."
}

# Streamlit UI
st.set_page_config(page_title="IraqGPT", layout="centered")
st.title("🇮🇶 IraqGPT - دردش مع شخصية عراقية")

selected_character = st.selectbox("اختر شخصية:", list(characters.keys()))
user_input = st.text_input("✍️ اكتب سؤالك هنا")

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

    response = openai.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )

    reply = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "assistant", "content": reply})

for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"**👤 أنت:** {msg['content']}")
    else:
        st.markdown(f"**🤖 {selected_character}:** {msg['content']}")
