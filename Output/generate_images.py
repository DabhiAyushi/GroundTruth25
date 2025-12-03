import base64
import requests
import os
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

def generate_ad_image(prompt, variation_id):
    url = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "num_inference_steps": 4,
            "guidance_scale": 3.5
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        print("❌ IMAGE ERROR:", response.text)
        return None

    # image bytes come directly in response.content
    filename = f"creative_{variation_id}.png"

    with open(filename, "wb") as f:
        f.write(response.content)

    return filename