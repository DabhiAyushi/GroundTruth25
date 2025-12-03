import os
import requests
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def generate_caption(brand, product):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

    prompt = f"Write a short, catchy advertisement caption for the brand '{brand}' and its product '{product}'. Make it punchy, modern, and marketing-friendly."

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        print("❌ CAPTION ERROR:", response.text)
        try:
            error_message = response.json().get('error', {}).get('message', '')
            return f"Error generating caption: {error_message}"
        except:
            return f"{brand} {product}"

    try:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        print("❌ CAPTION ERROR: Unexpected response structure or missing data.")
        return f"{brand} {product}"