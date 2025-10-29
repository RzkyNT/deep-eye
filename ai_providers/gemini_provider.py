import requests
import json

def generate(prompt, config):
    """
    Gemini AI Provider for Deep-Eye
    """
    try:
        gemini_cfg = config["ai_providers"]["gemini"]
        api_key = gemini_cfg["api_key"]
        model = gemini_cfg.get("model", "gemini-1.5-flash")
        base_url = gemini_cfg.get("base_url", "https://generativelanguage.googleapis.com/v1beta")

        url = f"{base_url}/models/{model}:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        # Ambil teks hasil dari Gemini
        return data["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        return f"[Gemini Error] {e}"
