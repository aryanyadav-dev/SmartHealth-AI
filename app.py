import streamlit as st
import tempfile
import os
import random
from config import primary_api_key, gmaps_api_key
from utils import encode_image, generate_image_description, chat_eli, chat_gpt35, translate_text

# Initialize session state
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None
if 'result' not in st.session_state:
    st.session_state.result = None

# Quotes
quotes = [
    "The greatest wealth is health. – Virgil",
    "Take care of your body. It’s the only place you have to live. – Jim Rohn",
    "Health is not valued till sickness comes. – Thomas Fuller",
    "A fit body, a calm mind, a house full of love. These things cannot be bought – they must be earned. – Naval Ravikant",
    "Health is the crown on the well person’s head that only the ill person can see. – Robin Sharma",
    "To keep the body in good health is a duty… otherwise we shall not be able to keep our mind strong and clear. – Buddha",
    "Early to bed and early to rise makes a man healthy, wealthy, and wise. – Benjamin Franklin",
    "The groundwork of all happiness is health. – Leigh Hunt",
    "It is health that is real wealth and not pieces of gold and silver. – Mahatma Gandhi",
    "Happiness is the highest form of health. – Dalai Lama",
    "He who has health has hope; and he who has hope has everything. – Arabian Proverb",
    "An apple a day keeps the doctor away. – Proverb",
    "Good health and good sense are two of life’s greatest blessings. – Publilius Syrus",
    "Health and intellect are the two blessings of life. – Menander",
    "Your body hears everything your mind says. – Naomi Judd",
    "A healthy outside starts from the inside. – Robert Urich",
    "Health is a state of complete harmony of the body, mind, and spirit. – B.K.S. Iyengar",
    "The first wealth is health. – Ralph Waldo Emerson",
    "A good laugh and a long sleep are the best cures in the doctor’s book. – Irish Proverb"
]
quote = random.choice(quotes)

st.title("Medical Help using Multimodal LLM")
st.markdown(f"<p style='font-size: 14px; color: gray;'>{quote}</p>", unsafe_allow_html=True)

with st.expander("About this App"):
    st.write("Upload an image to get an analysis or ask a medical-related question.")

st.subheader("Ask a Medical-Related Question")
user_question = st.text_input("Enter your question here:")

target_language = st.selectbox("Select Language for Translation", ["None", "Hindi", "Bengali", "Tamil", "Telugu", "Marathi"])

if st.button('Get Answer'):
    if user_question:
        response = chat_gpt35(user_question)
        
        if target_language != "None":
            response = translate_text(response, target_language)
        
        st.markdown(response, unsafe_allow_html=True)
        
        if 'location' in st.session_state:
            location = st.session_state.location
        else:
            location = st.text_input("Enter your location (latitude, longitude):")
            st.session_state.location = location
        
        if location:
            latitude, longitude = map(float, location.split(','))
            places_result = gmaps.places_nearby(location=(latitude, longitude), radius=5000, type='hospital')
            
            st.subheader("Nearby Clinics")
            for place in places_result['results']:
                st.markdown(f"**{place['name']}**")
                st.markdown(f"Address: {place['vicinity']}")
                if 'rating' in place:
                    st.markdown(f"Rating: {place['rating']}")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        st.session_state['filename'] = tmp_file.name

    st.image(uploaded_file, caption='Uploaded Image')

if st.button('Analyze Image'):
    if 'filename' in st.session_state and os.path.exists(st.session_state['filename']):
        st.session_state['result'] = generate_image_description(st.session_state['filename'])
        
        if target_language != "None":
            st.session_state['result'] = translate_text(st.session_state['result'], target_language)
        
        st.markdown(st.session_state['result'], unsafe_allow_html=True)
        os.unlink(st.session_state['filename'])

if 'result' in st.session_state and st.session_state['result']:
    st.info("Below you have an option for ELI5 to understand in simpler terms.")
    if st.radio("ELI5 - Explain Like I'm 5", ('No', 'Yes')) == 'Yes':
        simplified_explanation = chat_eli(st.session_state['result'])
        
        if target_language != "None":
            simplified_explanation = translate_text(simplified_explanation, target_language)
        
        st.markdown(simplified_explanation, unsafe_allow_html=True)
