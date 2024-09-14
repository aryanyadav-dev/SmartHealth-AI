import base64
import time
import openai
from PIL import Image

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def generate_image_description(image_path: str):
    image = Image.open(image_path)
    image_description = f"Image size: {image.size}, Image mode: {image.mode}"
    description_prompt = f"Describe the following medical image details and provide a detailed analysis based on this information: {image_description}"
    
    response = api_call_with_retry(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI trained in analyzing and describing medical images."},
            {"role": "user", "content": description_prompt}
        ],
        max_tokens=1500
    )
    return response.choices[0].message["content"]

def chat_eli(query):
    eli5_prompt = "You have to explain the below piece of information to a five years old. \n" + query
    messages = [{"role": "user", "content": eli5_prompt}]
    
    response = api_call_with_retry(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1500
    )
    return response.choices[0].message["content"]

def chat_gpt35(query):
    messages = [{"role": "user", "content": query}]
    
    response = api_call_with_retry(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1500
    )
    return response.choices[0].message["content"]

def api_call_with_retry(model, messages, max_tokens, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens
            )
            return response
        except openai.error.RateLimitError:
            if alternative_api_key and openai.api_key == primary_api_key:
                openai.api_key = alternative_api_key
                st.warning("Switched to alternative API key due to rate limit.")
            if attempt < retries - 1:
                st.warning(f"Rate limit reached. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                st.error("Rate limit exceeded. Please check your API usage and try again later.")
                raise

def translate_text(text, target_language):
    translation_prompt = f"Translate the following text to {target_language}: {text}"
    messages = [{"role": "user", "content": translation_prompt}]
    
    response = api_call_with_retry(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1500
    )
    return response.choices[0].message["content"]
